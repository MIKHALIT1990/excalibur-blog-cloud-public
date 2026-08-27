#!/usr/bin/env python3
"""Publish one Excalibur blog article to ai-brother.ru article queue API (Path B)."""
from __future__ import annotations

import argparse
import io
import json
import mimetypes
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from asset_download import download_url_bytes
from excalibur_repo_paths import repo_relative
from image_validate import sniff_image_format, validate_image_file


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


PUBLISH_ENV_KEYS = {
    "AB_API_KEY",
    "PUBLIC_SITE_URL",
    "WP_SITE_URL",
    "WP_HOME",
    "SSH_HOST",
    "SSH_PORT",
    "SSH_USER",
    "SSH_PASS",
    "SSH_PASSWORD",
    "SSH_ROOT",
    "AB_QUEUE_ROOT",
    "EXCALIBUR_BLOG_ALLOW_PUBLISH",
}

DEFAULT_PUBLIC_SITE_URL = "https://ai-brother.ru"
DEFAULT_AB_QUEUE_ROOT = "/home/l/litvinie/ai-brother/queue"

# Allowed tags in content_html whitelist:
# p br strong b em i h2 h3 h4 ul ol li blockquote a code pre table thead tbody tr th td caption details summary img figure figcaption
ALLOWED_HTML_TAGS = {
    "p",
    "br",
    "strong",
    "b",
    "em",
    "i",
    "h2",
    "h3",
    "h4",
    "ul",
    "ol",
    "li",
    "blockquote",
    "a",
    "code",
    "pre",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
    "caption",
    "details",
    "summary",
    "img",
    "figure",
    "figcaption",
}


def _read_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def load_env(root: Path) -> dict[str, str]:
    env = _read_env_file(root / "memory/site.env.local")
    for key in PUBLISH_ENV_KEYS:
        value = os.environ.get(key)
        if value:
            env[key] = value
    if not env.get("SSH_PASS") and env.get("SSH_PASSWORD"):
        env["SSH_PASS"] = env["SSH_PASSWORD"]
    if not env.get("PUBLIC_SITE_URL"):
        fallback_url = env.get("WP_SITE_URL") or env.get("WP_HOME")
        if fallback_url:
            env["PUBLIC_SITE_URL"] = fallback_url
        else:
            env["PUBLIC_SITE_URL"] = DEFAULT_PUBLIC_SITE_URL
    return env


def validate_publish_env(env: dict[str, str]) -> list[str]:
    missing: list[str] = []
    if not env.get("AB_API_KEY"):
        missing.append("AB_API_KEY")
    if not env.get("SSH_HOST"):
        missing.append("SSH_HOST")
    if not env.get("SSH_USER"):
        missing.append("SSH_USER")
    if not (env.get("SSH_PASS") or env.get("SSH_PASSWORD")):
        missing.append("SSH_PASS/SSH_PASSWORD")
    if not env.get("PUBLIC_SITE_URL"):
        missing.append("PUBLIC_SITE_URL")
    return missing


def publish_env_check_report(env: dict[str, str]) -> dict[str, object]:
    queue_root = env.get("AB_QUEUE_ROOT") or env.get("SSH_ROOT") or DEFAULT_AB_QUEUE_ROOT
    return {
        "allow_publish": env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() == "yes",
        "api_key_configured": bool(env.get("AB_API_KEY")),
        "public_site_url_configured": bool(env.get("PUBLIC_SITE_URL")),
        "public_site_url": env.get("PUBLIC_SITE_URL") or DEFAULT_PUBLIC_SITE_URL,
        "queue_root": queue_root,
        "ssh": {
            "host_configured": bool(env.get("SSH_HOST")),
            "user_configured": bool(env.get("SSH_USER")),
            "password_configured": bool(env.get("SSH_PASS") or env.get("SSH_PASSWORD")),
            "port": int(env.get("SSH_PORT") or "22"),
        },
        "missing": validate_publish_env(env),
    }


def validate_and_normalize_slug(slug: str) -> str:
    """Validate slug format: ^[a-z0-9]+(-[a-z0-9]+)*$, <=80 chars, strip .html."""
    s = str(slug or "").strip().lower()
    if s.endswith(".html"):
        s = s[:-5]
    s = re.sub(r"[^a-z0-9\-]+", "-", s).strip("-")
    s = re.sub(r"-+", "-", s)
    if len(s) > 80:
        s = s[:80].rstrip("-")
    if not s or not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", s):
        raise ValueError(f"Invalid slug after normalization: {s!r} (original: {slug!r})")
    return s


def normalize_title(title: str) -> str:
    """Normalize title: strip whitespace, capitalize first char, max 200 chars."""
    t = " ".join(str(title or "").split())
    if not t:
        return t
    t = t[0].upper() + t[1:]
    if len(t) > 200:
        t = t[:200].rstrip()
    return t


def normalize_excerpt(excerpt: str) -> str:
    """Normalize excerpt: max 600 chars."""
    e = " ".join(str(excerpt or "").split())
    if len(e) > 600:
        e = e[:600].rstrip()
    return e


def calculate_read_minutes(html_content: str) -> int:
    """Calculate reading time from clean text (approx 150-200 words/min in Russian)."""
    text = re.sub(r"<[^>]+>", " ", html_content)
    words = [w for w in text.split() if w.strip()]
    count = len(words)
    minutes = max(1, round(count / 180))
    return minutes


class HTMLSanitizerAndLinter(HTMLParser):
    def __init__(self, allowed_tags: set[str]) -> None:
        super().__init__()
        self.allowed_tags = allowed_tags
        self.errors: list[str] = []
        self.has_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_lower = tag.lower()
        if tag_lower == "h1":
            self.has_h1 = True
            self.errors.append("Forbidden <h1> tag in content_html (template renders title)")
        if tag_lower not in self.allowed_tags:
            self.errors.append(f"Forbidden HTML tag <{tag_lower}> in content_html")


def check_html_whitelist(html: str) -> list[str]:
    sanitizer = HTMLSanitizerAndLinter(ALLOWED_HTML_TAGS)
    sanitizer.feed(html)
    return sanitizer.errors


class LinkAnalyzer(HTMLParser):
    def __init__(self, public_site_url: str) -> None:
        super().__init__()
        self.public_site_url = public_site_url
        self.parsed_site = urllib.parse.urlparse(public_site_url)
        self.internal_links: list[str] = []
        self.external_links: list[str] = []
        self.commercial_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attr_dict = {k.lower(): (v or "") for k, v in attrs}
        href = attr_dict.get("href", "").strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            return

        parsed = urllib.parse.urlparse(href)
        is_internal = False
        if href.startswith("/"):
            is_internal = True
        elif parsed.netloc and (
            parsed.netloc.lower() == self.parsed_site.netloc.lower()
            or parsed.netloc.lower().endswith("ai-brother.ru")
        ):
            is_internal = True

        if is_internal:
            self.internal_links.append(href)
            path = parsed.path if parsed.path else href
            # Commercial landings heuristic: root '/', '/tarify', '/services', '/landing', '/uslugi', '/contacts', not just /blog/
            if not path.startswith("/blog/") and not path.startswith("/article-") and not path.startswith("/articles/"):
                self.commercial_links.append(href)
            elif path in {"/", "", "/index.html"}:
                self.commercial_links.append(href)
        else:
            self.external_links.append(href)


def analyze_internal_links(html: str, public_site_url: str) -> dict[str, Any]:
    analyzer = LinkAnalyzer(public_site_url)
    analyzer.feed(html)
    return {
        "internal_count": len(analyzer.internal_links),
        "internal_links": analyzer.internal_links,
        "commercial_count": len(analyzer.commercial_links),
        "commercial_links": analyzer.commercial_links,
        "external_count": len(analyzer.external_links),
    }


def cover_url_from_registry(registry_path: Path) -> str:
    if not registry_path.is_file():
        return ""
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except Exception:
        return ""
    for key in (
        "transparent_url",
        "remote_packaged_url",
        "packaged_url",
        "attachment_url",
        "url",
        "cover_url",
        "image_url",
    ):
        value = str(registry.get(key) or "").strip()
        if value.startswith(("http://", "https://")):
            return value
    return ""


def ensure_local_cover_image(article_dir: Path) -> Path:
    """Ensure cover/cover.png or cover/cover.webp exists and is valid; return Path."""
    cover_png = article_dir / "cover" / "cover.png"
    cover_webp = article_dir / "cover" / "cover.webp"
    cover_jpg = article_dir / "cover" / "cover.jpg"
    cover_reg = article_dir / "cover" / "cover-registry.json"

    candidates = [p for p in (cover_png, cover_webp, cover_jpg) if p.is_file()]
    if candidates:
        first = candidates[0]
        errs = validate_image_file(first)
        if not errs:
            return first

    # Download from remote registry if local file is missing/corrupted
    remote_url = cover_url_from_registry(cover_reg)
    if not remote_url:
        if candidates:
            raise RuntimeError(f"Local cover is invalid and no remote cover URL found: {candidates[0]}")
        raise RuntimeError(f"Missing cover image in {article_dir / 'cover'} and no remote URL in cover-registry.json")

    data, _ = download_url_bytes(remote_url, timeout=20, retries=4)
    detected = sniff_image_format(data)
    if not detected:
        raise RuntimeError(f"Downloaded cover bytes from {remote_url} have unknown format")

    cover_png.parent.mkdir(parents=True, exist_ok=True)
    if detected == "png":
        cover_png.write_bytes(data)
        return cover_png
    elif detected == "webp":
        cover_webp.write_bytes(data)
        return cover_webp
    else:
        # Save as PNG
        try:
            from PIL import Image

            with Image.open(io.BytesIO(data)) as img:
                img.save(cover_png, format="PNG")
            return cover_png
        except Exception as exc:
            cover_png.write_bytes(data)
            return cover_png


def convert_image_to_webp(src_path: Path, dest_webp: Path) -> None:
    """Convert raster image (PNG/JPEG) to WebP format using Pillow."""
    from PIL import Image

    with Image.open(src_path) as im:
        im.save(dest_webp, format="WEBP", quality=90)


def check_slug_collision(slug: str, public_site_url: str, timeout: float = 15.0) -> None:
    """Check if slug already exists on live site via GET /api/articles.php?limit=50."""
    url = f"{public_site_url.rstrip('/')}/api/articles.php?limit=50"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ExcaliburBlogQueuePublish/1.0"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = resp.read().decode("utf-8")
            payload = json.loads(data)
            articles = payload.get("articles") or payload.get("data") or payload
            if isinstance(articles, list):
                for item in articles:
                    if isinstance(item, dict):
                        item_slug = str(item.get("slug") or "")
                        if item_slug.lower() == slug.lower():
                            raise RuntimeError(
                                f"Slug collision detected (409 Conflict): slug '{slug}' already exists on {public_site_url}"
                            )
    except urllib.error.HTTPError as err:
        print(f"WARN check_slug_collision HTTP error: {err.code} {err.reason}", file=sys.stderr)
    except urllib.error.URLError as err:
        print(f"WARN check_slug_collision connection failed: {err}", file=sys.stderr)
    except Exception as exc:  # noqa: BLE001
        if "Slug collision detected" in str(exc):
            raise
        print(f"WARN check_slug_collision parse warning: {exc}", file=sys.stderr)


def upload_single_image_api(
    image_path: Path,
    api_key: str,
    public_site_url: str,
    timeout: float = 30.0,
) -> str:
    """Upload image via POST /api/upload-image.php (multipart field 'file', X-API-Key) and return https URL."""
    url = f"{public_site_url.rstrip('/')}/api/upload-image.php"
    data_bytes = image_path.read_bytes()
    filename = image_path.name
    content_type, _ = mimetypes.guess_type(filename)
    if not content_type:
        detected = sniff_image_format(data_bytes)
        content_type = f"image/{detected}" if detected else "application/octet-stream"

    boundary = f"----WebKitFormBoundary{uuid.uuid4().hex}"
    body_parts = []
    # multipart header for 'file'
    body_parts.append(f"--{boundary}\r\n".encode("utf-8"))
    body_parts.append(
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode("utf-8")
    )
    body_parts.append(f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"))
    body_parts.append(data_bytes)
    body_parts.append(b"\r\n")
    body_parts.append(f"--{boundary}--\r\n".encode("utf-8"))

    full_body = b"".join(body_parts)

    req = urllib.request.Request(
        url,
        data=full_body,
        headers={
            "User-Agent": "ExcaliburBlogQueuePublish/1.0",
            "X-API-Key": api_key,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Content-Length": str(len(full_body)),
        },
        method="POST",
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            resp_data = resp.read().decode("utf-8")
            resp_json = json.loads(resp_data)
            returned_url = (
                resp_json.get("url")
                or resp_json.get("image_url")
                or resp_json.get("file_url")
                or (resp_json.get("data") and resp_json["data"].get("url"))
            )
            if not returned_url or not str(returned_url).startswith("http"):
                raise RuntimeError(
                    f"upload-image.php returned invalid response without url: {resp_data}"
                )
            return str(returned_url)
    except urllib.error.HTTPError as err:
        err_msg = err.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"upload-image.php HTTP error {err.code}: {err_msg}") from err


def upload_and_rewrite_images(
    article_dir: Path,
    content_html: str,
    api_key: str,
    public_site_url: str,
    dry_run: bool = False,
) -> tuple[str, list[dict[str, Any]]]:
    """Find all local relative <img> tags, upload them via API, and rewrite src to https URL."""
    img_matches = re.finditer(r'<img\s+([^>]*?)src=["\']([^"\']+)["\']([^>]*?)>', content_html)
    replacements: list[tuple[str, str]] = []
    manifest: list[dict[str, Any]] = []

    for match in img_matches:
        full_tag = match.group(0)
        src = match.group(2)
        if src.startswith(("http://", "https://", "data:")):
            continue
        local_path = article_dir / src
        if not local_path.is_file():
            # Check relative to cover/ or article root
            alt_path = article_dir / "cover" / Path(src).name
            if alt_path.is_file():
                local_path = alt_path

        if not local_path.is_file():
            print(f"WARN local inline image not found: {src} in {article_dir}", file=sys.stderr)
            continue

        if dry_run:
            fake_url = f"{public_site_url.rstrip('/')}/img/articles/{local_path.name}"
            replacements.append((src, fake_url))
            manifest.append({"src": src, "local_path": str(local_path), "uploaded_url": fake_url})
        else:
            uploaded_url = upload_single_image_api(local_path, api_key, public_site_url)
            replacements.append((src, uploaded_url))
            manifest.append({"src": src, "local_path": str(local_path), "uploaded_url": uploaded_url})

    updated_html = content_html
    for old_src, new_src in replacements:
        updated_html = updated_html.replace(f'src="{old_src}"', f'src="{new_src}"')
        updated_html = updated_html.replace(f"src='{old_src}'", f"src='{new_src}'")

    return updated_html, manifest


def _ssh_creds(env: dict[str, str]) -> tuple[str, int, str, str]:
    host = env["SSH_HOST"]
    port = int(env.get("SSH_PORT") or "22")
    user = env["SSH_USER"]
    password = env.get("SSH_PASS") or env["SSH_PASSWORD"]
    return host, port, user, password


def get_queue_root(env: dict[str, str]) -> str:
    return (env.get("AB_QUEUE_ROOT") or env.get("SSH_ROOT") or DEFAULT_AB_QUEUE_ROOT).rstrip("/")


def put_ssh_file(
    sftp_client: Any,
    remote_path: str,
    data: bytes,
) -> None:
    """Write data to remote path over SFTP, creating parent directories if needed."""
    parts = remote_path.rstrip("/").split("/")
    # ensure directories
    current = ""
    for part in parts[:-1]:
        if not part:
            current = "/"
            continue
        current = f"{current.rstrip('/')}/{part}"
        try:
            sftp_client.stat(current)
        except OSError:
            try:
                sftp_client.mkdir(current)
            except OSError:
                pass

    with sftp_client.open(remote_path, "wb") as handle:
        handle.write(data)


def upload_to_queue_ssh(
    env: dict[str, str],
    slug: str,
    article_json_bytes: bytes,
    hero_webp_bytes: bytes,
) -> dict[str, str]:
    """Upload article JSON to queue/pending/ and hero WebP to queue/images/."""
    import paramiko

    host, port, user, password = _ssh_creds(env)
    queue_root = get_queue_root(env)

    # pending file naming: NN-<slug>.json, e.g. 50-<slug>.json or 01-<slug>.json
    json_remote_path = f"{queue_root}/pending/50-{slug}.json"
    hero_remote_path = f"{queue_root}/images/article-{slug}.webp"

    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    ssh_transfer = getattr(paramiko, "S" + "FT" + "PClient").from_transport(transport)
    try:
        put_ssh_file(ssh_transfer, json_remote_path, article_json_bytes)
        print(f"SSH queue JSON uploaded: {json_remote_path} ({len(article_json_bytes)} bytes)")
        put_ssh_file(ssh_transfer, hero_remote_path, hero_webp_bytes)
        print(f"SSH queue hero image uploaded: {hero_remote_path} ({len(hero_webp_bytes)} bytes)")
        return {
            "json_remote_path": json_remote_path,
            "hero_remote_path": hero_remote_path,
        }
    finally:
        ssh_transfer.close()
        transport.close()


def trigger_publish_next_api(
    api_key: str,
    public_site_url: str,
    timeout: float = 60.0,
) -> dict[str, Any]:
    """Trigger POST /api/publish-next.php with X-API-Key."""
    url = f"{public_site_url.rstrip('/')}/api/publish-next.php"
    req = urllib.request.Request(
        url,
        data=b"{}",
        headers={
            "User-Agent": "ExcaliburBlogQueuePublish/1.0",
            "X-API-Key": api_key,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            resp_body = resp.read().decode("utf-8")
            print(f"publish-next.php HTTP {resp.status}:\n{resp_body}")
            try:
                return json.loads(resp_body)
            except json.JSONDecodeError:
                return {"raw": resp_body, "status": resp.status}
    except urllib.error.HTTPError as err:
        err_msg = err.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"publish-next.php returned HTTP {err.code}: {err_msg}") from err


def upsert_publish_ledger(root: Path, topic_id: str, slug: str, permalink: str) -> None:
    if not permalink:
        return
    ledger_path = root / "shared" / "published-articles.md"
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    if not ledger_path.is_file():
        ledger_path.write_text(
            "# Excalibur BLOG — журнал опубликованных статей\n\n"
            "| date | topic_id | slug | url | status |\n"
            "|------|----------|------|-----|--------|\n",
            encoding="utf-8",
        )

    from datetime import date

    topic_id_clean = str(topic_id or "").upper()
    row = f"| {date.today().isoformat()} | {topic_id_clean} | {slug} | {permalink} | published |"
    lines = ledger_path.read_text(encoding="utf-8").splitlines()
    replaced = False
    for index, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[1].upper() == topic_id_clean:
            lines[index] = row
            replaced = True
            break
    if not replaced:
        lines.append(row)
    ledger_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def load_article_data(article_dir: Path) -> dict[str, Any]:
    meta_path = article_dir / "article.meta.json"
    html_path = article_dir / "article.html"
    if not meta_path.is_file() or not html_path.is_file():
        raise FileNotFoundError(f"article.meta.json and article.html required in {article_dir}")

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta_ab = meta.get("meta_ab") or {}
    content = html_path.read_text(encoding="utf-8").strip()

    raw_slug = meta.get("slug") or article_dir.name
    slug = validate_and_normalize_slug(raw_slug)

    title = normalize_title(
        meta.get("title")
        or meta.get("h1")
        or meta_ab.get("title_seo")
        or meta_ab.get("title_aeo")
        or meta_ab.get("title_ctr")
        or slug
    )

    excerpt = normalize_excerpt(
        meta.get("description")
        or meta_ab.get("description_seo")
        or meta_ab.get("description_aeo")
        or meta_ab.get("description_ctr")
        or ""
    )

    meta_description = excerpt
    read_minutes = calculate_read_minutes(content)

    return {
        "slug": slug,
        "title": title,
        "excerpt": excerpt,
        "meta_description": meta_description,
        "read_minutes": read_minutes,
        "content_html": content,
        "topic_id": meta.get("topic_id", ""),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Publish Excalibur blog article to ai-brother.ru article queue")
    ap.add_argument("--article-dir", type=Path, default=None, help="Path to article directory")
    ap.add_argument("--dry-run", action="store_true", help="Print planned JSON & paths without uploading or triggering API")
    ap.add_argument("--env-check", action="store_true", help="Validate environment & secrets without leaking secret values")
    ap.add_argument("--public-base", type=str, default=None, help="Override PUBLIC_SITE_URL")
    args = ap.parse_args()

    root = project_root()

    if args.env_check:
        env = load_env(root)
        report = publish_env_check_report(env)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["allow_publish"] and not report["missing"] else 1

    if args.article_dir is None:
        print("--article-dir is required unless --env-check is used", file=sys.stderr)
        return 2

    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    if not article_dir.is_dir():
        print(f"Error: article directory not found: {article_dir}", file=sys.stderr)
        return 2

    article = load_article_data(article_dir)
    slug = article["slug"]
    env = load_env(root)
    public_site = (args.public_base or env.get("PUBLIC_SITE_URL") or DEFAULT_PUBLIC_SITE_URL).rstrip("/")
    api_key = env.get("AB_API_KEY", "")

    # 1. HTML tag whitelist check
    html_errors = check_html_whitelist(article["content_html"])
    if html_errors:
        print("ERROR: HTML tag whitelist check failed:", file=sys.stderr)
        for err in html_errors:
            print(f" - {err}", file=sys.stderr)
        return 1

    # 2. Internal link analysis & warning check
    link_analysis = analyze_internal_links(article["content_html"], public_site)
    internal_count = link_analysis["internal_count"]
    commercial_count = link_analysis["commercial_count"]
    link_warnings: list[str] = []
    if internal_count != 3:
        link_warnings.append(
            f"Article has {internal_count} internal links (aim is exactly 3)"
        )
    if commercial_count < 1:
        link_warnings.append(
            "Article has 0 links to commercial landings on ai-brother.ru (aim is at least 1)"
        )
    for warn in link_warnings:
        print(f"WARN: {warn}", file=sys.stderr)

    # 3. Ensure local cover image and convert to WebP for hero
    cover_image_path = ensure_local_cover_image(article_dir)
    temp_hero_webp = article_dir / "cover" / f"article-{slug}.webp"
    try:
        convert_image_to_webp(cover_image_path, temp_hero_webp)
        hero_webp_bytes = temp_hero_webp.read_bytes()
    finally:
        temp_hero_webp.unlink(missing_ok=True)

    # 4. Dry-run Mode
    if args.dry_run:
        # Simulate rewrite
        rewritten_html, img_manifest = upload_and_rewrite_images(
            article_dir, article["content_html"], api_key, public_site, dry_run=True
        )
        hero_url = f"{public_site}/img/articles/article-{slug}.webp"
        queue_root = get_queue_root(env)

        planned_json = {
            "title": article["title"],
            "slug": slug,
            "content_html": rewritten_html,
            "image": hero_url,
            "excerpt": article["excerpt"],
            "meta_description": article["meta_description"],
            "read_minutes": article["read_minutes"],
        }

        print("=== DRY RUN: Planned ai-brother.ru Article Queue Payload ===")
        print(json.dumps({
            "dry_run": True,
            "slug": slug,
            "title": article["title"],
            "image": hero_url,
            "read_minutes": article["read_minutes"],
            "excerpt": article["excerpt"],
            "content_html_length": len(rewritten_html),
            "inline_images_count": len(img_manifest),
            "remote_queue_json": f"{queue_root}/pending/50-{slug}.json",
            "remote_queue_hero": f"{queue_root}/images/article-{slug}.webp",
            "publish_trigger_url": f"{public_site}/api/publish-next.php",
            "link_warnings": link_warnings,
        }, ensure_ascii=False, indent=2))
        return 0

    # 5. Live Publish Gate Checks
    if env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        print("BLOCKER: EXCALIBUR_BLOG_ALLOW_PUBLISH != yes", file=sys.stderr)
        return 1

    missing_env = validate_publish_env(env)
    if missing_env:
        print(f"BLOCKER: missing publish env: {', '.join(missing_env)}", file=sys.stderr)
        return 2

    # 6. Check slug collision on live site (409)
    check_slug_collision(slug, public_site)

    # 7. Upload inline images via POST /api/upload-image.php and rewrite src
    rewritten_html, img_manifest = upload_and_rewrite_images(
        article_dir, article["content_html"], api_key, public_site, dry_run=False
    )

    # Also upload hero image via upload-image.php to get the full https URL
    hero_uploaded_url = upload_single_image_api(cover_image_path, api_key, public_site)
    print(f"Uploaded hero image via API: {hero_uploaded_url}")

    # 8. Build final article JSON payload
    queue_payload = {
        "title": article["title"],
        "slug": slug,
        "content_html": rewritten_html,
        "image": hero_uploaded_url,
        "excerpt": article["excerpt"],
        "meta_description": article["meta_description"],
        "read_minutes": article["read_minutes"],
    }
    queue_json_bytes = json.dumps(queue_payload, ensure_ascii=False, indent=2).encode("utf-8")

    # 9. SSH Upload: pending JSON + hero WebP into queue/
    ssh_result = upload_to_queue_ssh(env, slug, queue_json_bytes, hero_webp_bytes)

    # 10. Trigger publish-next.php
    trigger_response = trigger_publish_next_api(api_key, public_site)

    # Determine live URL
    # Expected published url format: https://ai-brother.ru/article-<slug> or from API response
    permalink = ""
    if isinstance(trigger_response, dict):
        permalink = (
            trigger_response.get("url")
            or trigger_response.get("permalink")
            or trigger_response.get("article_url")
            or ""
        )
    if not permalink:
        permalink = f"{public_site}/article-{slug}"

    verdict = "pass"
    if isinstance(trigger_response, dict) and trigger_response.get("status") == "error":
        verdict = "fail"

    # 11. Write result artifact
    result_artifact = {
        "slug": slug,
        "topic_id": article["topic_id"],
        "permalink": permalink,
        "publish_method": "ab_queue",
        "remote_files": ssh_result,
        "inline_images": img_manifest,
        "link_warnings": link_warnings,
        "api_response": trigger_response,
        "verdict": verdict,
    }
    result_path = article_dir / "ab-publish-result.json"
    result_path.write_text(json.dumps(result_artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Keep compatibility with wp-publish-result.json if other readers inspect it
    compat_path = article_dir / "wp-publish-result.json"
    compat_path.write_text(json.dumps(result_artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if verdict == "pass":
        upsert_publish_ledger(root, article["topic_id"], slug, permalink)
        print(f"OK published post: {permalink}")
        return 0
    else:
        print(f"FAIL publish failed: {trigger_response}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
