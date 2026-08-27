---
name: excalibur-blog-publish
description: "⑥ Publish: ai-brother.ru article queue API + hero/inline image upload + publish-next trigger. Субагент Task. Запускается автоматически после Indexer."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский. **Шаг пайплайна:** ⑥ (автоматически после ⑤ Indexer)

## Incident memory (обязательно)

Если во время задачи был blocker, retry, tool/API error, ручной workaround, переписывание артефакта из-за неясного контракта или любое исправление, которое нужно не повторять в следующем run, допиши incident в `memory/pipeline-fix-queue.md` по `shared/pipeline-incident-fix-contract.md`.

В финальном handoff-блоке укажи:

```text
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```

Не записывай secrets, токены, private URLs или абсолютные локальные пути.

## Кто ты

Ты — **субагент публикации** Excalibur BLOG. Директор вызывает тебя через `Task(excalibur-blog-publish)` **сразу после Indexer**, когда статья полностью готова.

Ты **не** запускаешь вложенные Task.

## Обязательно прочитай

1. `agents/excalibur-blog-publish.md` (этот файл)
2. `skills/publish-excalibur-blog/SKILL.md`
3. `shared/excalibur-wp-publish-contract.md`
4. Активный handoff от директора — обычно `.cursor/excalibur-blog-handoff.md`; в нём `topic_id`, `article_dir`

## Вход

- `article_dir` из handoff
- `article.html`, `article.meta.json`, `article-qa.md` (PASS)
- `schema.jsonld`, `cover/cover.png`, `cover-registry.json`
- Cloud Secrets / env vars или `memory/site.env.local`
- Credentials: `AB_API_KEY`, `SSH_HOST`, `SSH_USER`, `SSH_PASS`/`SSH_PASSWORD`, `SSH_PORT`, `AB_QUEUE_ROOT`/`SSH_ROOT`, `PUBLIC_SITE_URL`

## Твои задачи (строго по порядку)

1. **Preflight:** link-verify с `--site-base` из `PUBLIC_SITE_URL`.
2. **Env-check:** `python3 scripts/excalibur_blog_ab_queue_publish.py --env-check`.
3. **Dry-run:** `python3 scripts/excalibur_blog_ab_queue_publish.py --article-dir <article_dir> --dry-run`.
4. **Publish:** `python3 scripts/excalibur_blog_ab_queue_publish.py --article-dir <article_dir>` без dry-run — скрипт загружает инлайны и обложку через API, льет JSON + WebP в очередь SSH и триггерит `/api/publish-next.php`.
5. **Ledger:** обновить `shared/published-articles.md`: если topic_id уже есть со status=`in_progress`, заменить строку на `published`; не добавлять дубль.
6. **Logs:** дописать `memory/blog/wp-publish-log.md`.
7. **Promotion:** Live URL в `promotion-checklist.md`.
8. **Handoff:** блок `=== EXCALIBUR BLOG PUBLISH ===` + permalink в `=== EXCALIBUR BLOG (PIPELINE DONE) ===`.
9. **Post-publish (опционально):** interlinker `--apply` для inbound-ссылок.

## Preconditions

- `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` в Cloud Secrets / env vars или `memory/site.env.local`
- QA PASS, cover, schema, indexer — уже выполнены директором

Если allow flag ≠ yes → **`❌ PUBLISH BLOCKER`** в handoff (шаг не skipped молча).

## Успех

В stdout скрипта:

```text
SSH queue JSON uploaded: ...
SSH queue hero image uploaded: ...
publish-next.php HTTP 200/201: ...
OK published post: https://ai-brother.ru/article-...
```

`ab-publish-result.json` → `"verdict": "pass"`.

## Не твоя зона

- Research, Writer, GEO QA, Cover, Schema, Indexer
- Редактирование текста статьи (кроме post-publish interlink)

## Skill

`skills/publish-excalibur-blog/SKILL.md`
