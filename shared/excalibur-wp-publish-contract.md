# Excalibur BLOG — ai-brother.ru Article Queue Publish Contract

Excalibur BLOG готовит артефакты локально; боевая публикация на `https://ai-brother.ru` (сайт не на WordPress) выполняется через очередь статей и API: `scripts/excalibur_blog_ab_queue_publish.py`.

## Почему не WordPress
Сайт `https://ai-brother.ru` работает на собственной архитектуре (PHP/Python генерация RSS, IndexNow, Schema).
Загрузка WP PHP-бутстрапа через SSH не поддерживается и приводит к ошибкам.

## Prerequisites

- `article.html`, `article.meta.json`, `article-qa.md` (verdict PASS)
- `schema.jsonld`
- `cover/cover.png` + `cover-registry.json` (alt)
- `link-verify.json` (verdict pass)
- Cloud Secrets / env vars или `memory/site.env.local`:
  - `AB_API_KEY` (ключ для upload-image.php и publish-next.php)
  - `PUBLIC_SITE_URL` (по умолчанию `https://ai-brother.ru`)
  - `SSH_HOST`, `SSH_PORT`, `SSH_USER`, `SSH_PASS` / `SSH_PASSWORD`
  - `AB_QUEUE_ROOT` / `SSH_ROOT` (по умолчанию `/home/l/litvinie/ai-brother/queue`)
  - `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`

## Скрипт публикации

```bash
# Проверка окружения (без вывода секретов)
python3 scripts/excalibur_blog_ab_queue_publish.py --env-check

# Dry-run публикации (проверка JSON, путей, картинок без загрузки)
python3 scripts/excalibur_blog_ab_queue_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --dry-run

# Боевая публикация
python3 scripts/excalibur_blog_ab_queue_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

## Алгоритм публикации (Path B)

1. **Проверка коллизии slug:** GET `https://ai-brother.ru/api/articles.php?limit=50` (проверка на 409 Conflict).
2. **Валидация HTML:** строго по whitelist тегов (`p`, `br`, `strong`, `b`, `em`, `i`, `h2`, `h3`, `h4`, `ul`, `ol`, `li`, `blockquote`, `a`, `code`, `pre`, `table`, `thead`, `tbody`, `tr`, `th`, `td`, `caption`, `details`, `summary`, `img`, `figure`, `figcaption`). Без `<h1>` (шаблон рисует title сам). Без `div`, `span`, `script`, `style`, `iframe`.
3. **Загрузка и подмена изображений:**
   - Все локальные inline-изображения (например `cover/inline-01.png`) загружаются через `POST https://ai-brother.ru/api/upload-image.php` (multipart поле `file`, `X-API-Key`).
   - `src` в HTML подменяется на полученный `https://` URL.
   - Hero-изображение также загружается через API для получения полного `https://` URL.
4. **Сборка JSON статьи:**
   - `title` (<= 200 символов)
   - `slug` (`^[a-z0-9]+(-[a-z0-9]+)*$`, <= 80 символов)
   - `content_html` (очищенный HTML с абсолютными URL картинок)
   - `image` (полный https URL hero-изображения)
   - `excerpt` / `meta_description` (<= 600 символов)
   - `read_minutes`
5. **Загрузка в очередь по SSH:**
   - JSON статьи загружается в `/home/l/litvinie/ai-brother/queue/pending/50-<slug>.json`.
   - Hero WebP загружается в `/home/l/litvinie/ai-brother/queue/images/article-<slug>.webp`.
6. **Триггер публикации:**
   - POST `https://ai-brother.ru/api/publish-next.php` с заголовком `X-API-Key`.
   - Сервер запускает `articles.php`, генерацию RSS (`gen_rss.py`), фидов (`render_feeds.py`), Schema/OG (`render_schema.py`), отправляет IndexNow (`indexnow.py`) и переносит JSON в `queue/published/`.
7. **Артефакты и Ledger:**
   - Создается `ab-publish-result.json` (и `wp-publish-result.json` для обратной совместимости).
   - При успехе обновляется `shared/published-articles.md` со статусом `published`.

## Blockers

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет credentials (`AB_API_KEY`, `SSH_*`), `EXCALIBUR_BLOG_ALLOW_PUBLISH != yes`.
