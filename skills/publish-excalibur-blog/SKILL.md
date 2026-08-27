---
name: publish-excalibur-blog
description: Excalibur BLOG Publish — публикация в очередь статей ai-brother.ru (Path B), загрузка hero/inline изображений, триггер publish-next, ledger.
---

# Excalibur BLOG — Publish (субагент ⑥)

**Роль:** `Task(excalibur-blog-publish)`  
**Когда:** сразу после Indexer (шаг ⑤), когда QA PASS, cover, schema и indexer готовы.

## Контракт

`shared/excalibur-wp-publish-contract.md` (ai-brother.ru article queue API)

## Preconditions (все обязательны)

| Проверка | Файл / env |
|----------|------------|
| QA PASS | `article-qa.md` → verdict PASS |
| Links | `link-verify.json` → pass |
| Cover | `cover/cover.png` + alt в `cover-registry.json` |
| Schema | `schema.jsonld` |
| Credentials | Cloud Secrets/env или `memory/site.env.local`: `AB_API_KEY`, `SSH_*`, `PUBLIC_SITE_URL` |
| Allow flag | `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` |

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** (не silent skip).

## Алгоритм

### 1. Preflight publish

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/link-verify.json \
  --site-base https://ai-brother.ru
```

Gate: `link-verify.json` → pass. Иначе FIX (writer/QA) или BLOCKER.

### 2. Env-check

```bash
python3 scripts/excalibur_blog_ab_queue_publish.py --env-check
```

Проверяет allow flag, `AB_API_KEY`, public URL и SSH-переменные без вывода секретов.

### 3. Dry-run

```bash
python3 scripts/excalibur_blog_ab_queue_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --dry-run
```

Проверь: slug, title, image URL, размер HTML payload и пути в очереди.

### 4. Publish

```bash
python3 scripts/excalibur_blog_ab_queue_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Скрипт:
- проверяет отсутствие коллизий по slug на live сайте (`GET /api/articles.php?limit=50`);
- проверяет HTML whitelist тегов (без `<h1>`, `<div>`, `<script>` и т.д.);
- загружает все локальные inline `<img>` через `POST /api/upload-image.php` и подменяет `src` на https URL;
- загружает hero-изображение через API;
- собирает JSON статьи и загружает его по SSH в `/home/l/litvinie/ai-brother/queue/pending/50-<slug>.json`;
- загружает WebP обложки в `/home/l/litvinie/ai-brother/queue/images/article-<slug>.webp`;
- отправляет POST-запрос на `https://ai-brother.ru/api/publish-next.php` с `X-API-Key`;
- создает артефакт `ab-publish-result.json`;
- обновляет `shared/published-articles.md`.

### 5. Post-publish артефакты

| Файл | Действие |
|------|----------|
| `ab-publish-result.json` | создаёт скрипт (verdict pass/fail) |
| `memory/blog/wp-publish-log.md` | допиши секцию с permalink, status |
| `shared/published-articles.md` | если есть строка topic_id со status=in_progress — обнови date/url/status=published; иначе добавь строку |
| `promotion-checklist.md` | Live URL = permalink |
| handoff | блок `=== EXCALIBUR BLOG PUBLISH ===` + permalink в `PIPELINE DONE` |

### 6. Post-publish (рекомендуется)

```bash
python3 scripts/excalibur_blog_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base https://ai-brother.ru
```

Inbound-ссылки из старых статей на новую.

## Handoff block (шаблон)

```text
=== EXCALIBUR BLOG PUBLISH ===
topic_id:
slug:
article_dir:
publish_date:
verdict: PASS|FAIL
permalink:
hero_image:
inline_images:
api_status: ok|fail
blockers:
```

## Blockers

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет cover/schema, credentials (`AB_API_KEY`, `SSH_*`), allow flag
- `❌ PUBLISH FAIL` — скрипт вернул fail (смотри `ab-publish-result.json`)

## Запрещено

- Писать или переписывать longread
- Генерировать cover/schema с нуля
- Пропускать dry-run
- Завершать пайплайн без записи или обновления `published-articles.md` при успешном publish
