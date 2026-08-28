# QA: B11 sozdat-sajt-v-cursor-ai-bez-koda

date: 2026-08-28
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
research_notes_gate: pass
utility_gate: pass
human_voice_gate: pass
beginner_fit: pass
verdict: PASS

## Pain → solution → outcome

| Элемент | Где в статье |
|---------|----------------|
| **Боль** | Lead: Новичок/предприниматель открывает Cursor AI, просит «сделай лендинг», нейросеть создает 15 файлов на Next.js, просит npm/Node.js, терминал выдает «npm not recognized», проект сломан |
| **Решение** | H2 «Зафиксируйте правило landing.mdc» → «Подготовьте бриф и соберите каркас в Agent Mode» → «Настройте ключевые блоки» → «Подключите форму через Formspree» → «Опубликуйте на Vercel Drop» |
| **Результат** | index.html открывается двойным кликом в браузере, адаптивный дизайн готов, тестовая заявка уходит на email/Telegram, сайт опубликован на Vercel Drop с бесплатным HTTPS за 60 секунд |

## Beginner-fit Checklist

- **Решенная боль новичка:** Полное избавление от необходимости работать в консоли/терминале, ставить Node.js, компилировать код или платить 1 500–3 000 руб/мес за облачные конструкторы.
- **Где показано решение:** В H2 #1 (файл правил `.cursor/rules/landing.mdc`), H2 #2 (режим Composer Ctrl+I для генерации single-file HTML с Tailwind CDN), H2 #4 (прием заявок через Formspree без бэкенда).
- **Первый результат читателя:** Через 30 минут читатель получает готовый рабочий адаптивный сайт в одном файле `index.html`, работающую форму заявок и публичный адрес сайта в сети.
- **Сложные термины объяснены «на пальцах»:**
  - *HTML* — единственный текстовый файл каркаса страницы, открывающийся в любом браузере.
  - *Tailwind CDN* — технология подключения готовых современных стилей через интернет одной строчкой без сборщиков.
  - *Composer / Agent Mode* — диалоговое окно по Ctrl+I, где нейросеть сама создает и редактирует файлы.
  - *Formspree* — бесплатный шлюз-переходник, который принимает контакты из формы и пересылает их на почту или в Telegram без программирования сервера.
  - *Vercel Drop* — сервис мгновенной публикации сайта в интернете простым перетаскиванием папки мышью из проводника.
  - *Сквозная воронка и Webhook* — автопередача лида из формы в CRM (amoCRM / Битрикс24) и голосовому роботу за 10 секунд.

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×6, primary «как создать сайт с помощью нейросети», secondary хвосты закрыты, FAQ×6, step-by-step списки |
| GEO / citability | 25 | 24 | Инсайт-блок без запрещенных ярлыков, 4 blockquote, 1 таблица сравнения с конструкторами, FAQ×6, схема сборки |
| CORE-EEAT lite | 15 | 14 | 19/20; глубокое раскрытие темы от лица практика Михаила Литвинова (AI Brother) |
| Human voice | 15 | 14 | 0 slop, Flesch RU 59.5 (Standard); сильный эмоциональный контраст боли и решения |
| Fact safety | 15 | 13 | fact-check PASS (2/15 в базовом fact-bank, остальные цифры строго из research-notes: Wordstat 11 852 и др.) |
| Contract HTML | 10 | 10 | HTML linter PASS, теги строго по whitelist, нет запрещенного TOC |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, research gate pass, utility gate pass, human voice pass, beginner-fit pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1 точно закрывают «создать сайт с помощью нейросети в Cursor AI без кода» |
| C02 | ✓ | Lead — прямой ответ с историей боли предпринимателя, без клише и пустых вводных |
| C03 | ✓ | Целевая аудитория: новички, предприниматели, маркетологи без навыков кодинга |
| C04 | ✓ | Термины (HTML, Tailwind CDN, Composer, Formspree, Vercel Drop, Webhook) объяснены доступным языком |
| O01 | ✓ | H2 строго соответствуют action outline из research-notes.md |
| O02 | ✓ | Логика: правило landing.mdc → бриф/Composer → блоки сайта → форма Formspree → хостинг Vercel Drop → чеклист и CRM |
| O03 | ✓ | FAQ 6 вопросов на основе поисковых запросов Яндекс Вордстат |
| O04 | ✓ | Нумерованные списки шагов (6, 6, 4), таблица сравнения с Tilda/студиями, списки, blockquotes |
| R01 | ✓ | Инсайт-блок + схема сборки + FAQ дают самодостаточный ответ для AI-движков |
| R02 | ✓ | Точные данные Wordstat (11 852, 3 000+) на 28 августа 2026 года из research-notes |
| R03 | ✓ | Реалистичные цены ($0 / 1500-3000 руб. Tilda / заказ в веб-студии) |
| R04 | ✓ | FAQ: конкретный ответ в первом предложении каждого пункта |
| E01 | ✓ | Уникальный практический угол: «Zero-Terminal» сборка в 1 файле index.html |
| E02 | ✓ | Блоки «Типичная ошибка», «В реальном проекте», чеклист аудита перед запуском |
| E03 | ✓ | Органичный CTA на сквозную воронку AI Brother и Telegram |
| Exp01 | ✓ | Режим статьи B; reader_story интегрирован в lead |
| Exp02 | ✓ | Авторский стиль Михаила Литвинова, surprising_fact о сборке без Node.js |
| Exp03 | ✓ | 0 AI-клише и шаблонных штампов |
| Ept01 | ✓ | Практическая безопасность: проверка name-атрибутов формы, SSL HTTPS, CRM-интеграция |
| Ept02 | ✓ | Рабочие внутренние ссылки на опубликованные статьи (/article-ai-agents-business-guide, /article-amocrm-leads-autofill-setup) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| research-notes gate | PASS | research-notes-gate.json |
| fact-check | WARNING (PASS) | fact-check-report.json |
| link-verify | PASS | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate (article) | PASS | utility-gate-report.json |
| human voice gate | PASS | human-voice-report.json |

## Link verify

- total: 4, failed: 0
- OK: `https://ai-brother.ru` (200), `/article-ai-agents-business-guide` (200), `/article-amocrm-leads-autofill-setup` (200), `https://t.me/ai_brother_ru` (200)

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 12 (допустимо для детальных инструкций и сравнительной таблицы)
- Flesch RU: 59.5 (Standard / Intellectual editorial text)
- see `slop-detector-report.json`

## Fact-check

- verdict: warning/pass (15 extracted, 2 verified in static fact-bank, 13 verified against research-notes.md and official documentation)
- see `fact-check-report.json`

## Cannibalization

- verdict: pass (0 issues detected across 11 article metadata files)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (h2_sections: 6, faq_h3: 6, tables: 1, blockquotes: 4, lists: 5)
- topic: PASS (utility-gate-topic.json)

## Human voice gate

- status: PASS
- reader_story / reader_pain / reader_outcome / success_criteria / voice_angle overlap: strong
- see `human-voice-report.json`

## Fix cycle

- cycle 1: обновлены относительные ссылки в `article.html` на опубликованные статьи (`/article-ai-agents-business-guide`, `/article-amocrm-leads-autofill-setup`). Все 8 скриптов успешно прошли валидацию с вердиктом PASS.

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: no | Review: no | E-E-A-T SameAs Author: pending (author_id: mikhail-litvinov)
