research_date: 2026-08-27
accessed_at: 2026-08-27
utility_verdict: PASS
year: 2026
prefer_sources_after: 2026-05-29
topic_id: B11
slug: sozdat-sajt-lending-v-cursor-ai-bez-koda
h1: Как создать лендинг в Cursor AI без кода: пошаговая инструкция для новичка
primary_query: cursor ai сайт
search_intent: how_to
article_mode: B

reader_outcome: За 1–2 часа без навыков программирования собрать адаптивный одностраничный лендинг в одном файле index.html с Tailwind CDN через Cursor Agent, подключить бесплатный приём заявок на почту через Formspree и опубликовать сайт с бесплатным HTTPS на Vercel Drop без терминала, npm и Git.
reader_pain: Новичок боится браться за Cursor AI из-за страха сложного кода и чёрного терминала, а при первой же попытке ИИ генерирует сложный проект на React/Next.js с десятками файлов и package.json, который ломается и не открывается без локального сервера.
success_criteria: Файл index.html открывается локально двойным кликом в любом браузере с работающими стилями Tailwind и адаптивной версткой под мобильные экраны; тестовая заявка из формы мгновенно приходит на email через Formspree; сайт доступен по публичной https-ссылке Vercel Drop.
voice_angle: Пошаговый практический проводник для предпринимателя и маркетолога: как зафиксировать правила проекта в .cursor/rules/landing.mdc, удержать ИИ в рамках чистого HTML/Tailwind без терминала и запустить тест коммерческой гипотезы за один вечер.
reader_story: Предпринимательница Анна захотела запустить лендинг для записи на мастер-класс. Открыла Cursor AI и написала: «Сделай мне красивый сайт». Агент создал 40 файлов, package.json, предложил запустить npm install в терминале и выдал ошибку порта. Анна испугалась, решила, что ИИ — только для сеньоров, и чуть не отдала 50 000 ₽ агентству. С правилом landing.mdc она пересоздала проект за 30 минут в одном index.html, привязала Formspree и уже к ночи получила первые 3 заявки.
surprising_fact: По умолчанию современные LLM в Cursor переобучены на веб-приложения и пытаются развернуть React и Next.js даже для простейшей страницы-визитки. Чтобы превратить Cursor в идеальный no-code инструмент для новичка, достаточно одного короткого файла проектного правила (.cursor/rules/landing.mdc), блокирующего любые терминальные команды и сборщики.

## research_questions
1. Как новичку без опыта в коде и без терминала запустить Cursor AI и создать свой первый лендинг?
2. Почему Cursor AI по умолчанию генерирует сложные проекты на React/Next.js и как проектное правило `.cursor/rules/landing.mdc` решает эту проблему?
3. Как правильно использовать Tailwind Play CDN (`<script src="https://cdn.tailwindcss.com"></script>` или `@tailwindcss/browser@4`) для адаптивной вёрстки в одном `index.html`?
4. Как настроить рабочий приём лидов и заявок через бесплатный backend Formspree без собственного сервера и серверного кода?
5. Как бесплатно опубликовать лендинг с SSL-сертификатом через Vercel Drop (`vercel.com/drop`) за 15 секунд методом drag-and-drop без Git и CLI?
6. Какие типичные ошибки допускают новички (забытый атрибут `name` у полей формы, отсутствие `<meta name="viewport">`, перегрузка скриптами) и как их избежать перед запуском трафика?
7. Какой реальный поисковый спрос в Яндексе на создание сайтов с нейросетями и Cursor AI по данным Wordstat на август 2026 года?

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Cursor Docs: Rules & MDC Format | https://cursor.com/docs/rules.md | accessed_at: 2026-08-27 | Официальная документация Cursor по системе проектных правил .cursor/rules/*.mdc, frontmatter-метаданным (alwaysApply, description, globs) и управлению поведением Agent |
| Cursor Docs: Agent & Composer Mode | https://cursor.com/docs/agent/overview | accessed_at: 2026-08-27 | Документация Cursor Agent: режим Composer (Ctrl+I), работа с контекстом файлов и автоматическое создание/редактирование кода по текстовому запросу |
| Tailwind CSS: Play CDN Guide | https://tailwindcss.com/docs/installation/play-cdn | accessed_at: 2026-08-27 | Официальное руководство Tailwind CSS по использованию Play CDN (`cdn.tailwindcss.com` и `@tailwindcss/browser@4`) для мгновенной стилизации без Node.js и сборки |
| Vercel Docs: Vercel Drop | https://vercel.com/docs/drop | accessed_at: 2026-08-27 | Официальная документация Vercel Drop: публикация статических сайтов и папок с index.html методом перетаскивания (drag-and-drop) без Git и CLI |
| Vercel Changelog: Introducing Drop | https://vercel.com/changelog/vercel-drop | accessed_at: 2026-08-27 | Анонс релиза Vercel Drop от 12 июня 2026 года для мгновенного развёртывания статических прототипов и AI-генераций |
| Formspree: Simple HTML Forms | https://formspree.io/html/ | accessed_at: 2026-08-27 | Документация Formspree по интеграции HTML-форм без бэкенда (`<form action="https://formspree.io/f/{form_id}" method="POST">`) с бесплатным лимитом 50 заявок в месяц |
| Cloudflare Pages: HTML Form with Formspree | https://developers.cloudflare.com/pages/tutorials/add-an-html-form-with-formspree/ | accessed_at: 2026-08-27 | Руководство Cloudflare по подключению Formspree к статическим HTML-страницам и обязательной проверке атрибутов name на полях ввода |
| AI Brother Fact Bank | https://ai-brother.ru | accessed_at: 2026-08-27 | Официальный сайт AI Brother (основатель Михаил Литвинов): стандарты сквозной автоматизации лидогенерации и внедрения ИИ-решений |

## wordstat
Статистика поискового спроса собрана через инструмент `wordstat_get_top_requests` MCP-сервера `user-mcp-kv` на 2026-08-27:

| phrase | impressions |
| --- | --- |
| cursor ai | 11852 |
| скачать cursor ai | 569 |
| cursor ai pro | 398 |
| cursor ai подписка | 356 |
| cursor ai бесплатно | 259 |
| cursor ai сайт | 110 |
| как пользоваться cursor ai | 107 |
| создать сайт нейросеть | 1585 |
| создать сайт с нейросетью | 659 |
| создать сайт с помощью нейросети | 477 |
| нейросеть онлайн создать сайт | 176 |
| создать сайт с нейросетью бесплатно | 170 |
| создать сайт нейросетью онлайн бесплатно | 164 |
| создать сайт с помощью нейросети бесплатно | 120 |
| создать сайт через нейросеть | 112 |
| создание лендинга | 1288 |
| создание сайтов лендингов | 302 |
| ии для создания лендинга | 88 |
| создание лендинга бесплатно | 58 |
| создание лендинг страницы | 57 |
| промт для создания лендинга | 41 |
| создание одностраничного сайта лендинг | 36 |

**LSI и сопутствующие запросы**:
- `сделать сайт` — 140 670 показов/мес
- `создать сайт` — 121 226 показов/мес
- `нейросеть для создания` — 96 403 показов/мес
- `разработка сайта` — 21 307 показов/мес
- `создать сайт бесплатно` — 18 351 показов/мес
- `как создать свой сайт` — 7 157 показов/мес
- `тильда конструктор сайтов` — 883 показов/мес

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| PatrickJS/awesome-cursorrules | https://github.com/PatrickJS/awesome-cursorrules | accessed_at: 2026-08-27. Популярная база правил Cursor rules, содержащая шаблон `rules/html-tailwind-css-javascript-cursorrules-prompt-fi.mdc` для генерации чистого vanilla HTML + Tailwind CSS без сложных фреймворков и сборщиков. |
| alwkala/Cinematic-Landing-Kit | https://github.com/alwkala/Cinematic-Landing-Kit | accessed_at: 2026-08-27. Репозиторий production-паттернов для AI coding agents (Cursor, Claude Code), генерирующий чистый single-file `index.html` с Tailwind CDN (`cdn.tailwindcss.com`) с нулевым build step. |
| dx-tooling/landingpages-ai-template | https://github.com/dx-tooling/landingpages-ai-template | accessed_at: 2026-08-27. Шаблон лендингов для работы с AI-ассистентами (Cursor / Windsurf) через `.cursorrules` с компонентным подходом и Tailwind CSS. |
| vpavlenko/web-2024-template | https://github.com/vpavlenko/web-2024-template | accessed_at: 2026-08-27. Практическое руководство по созданию простого веб-сайта в одном файле `index.html` через Cursor Composer Agent без необходимости локальной сборки и npm. |
| tailwindlabs/tailwindcss discussions #15855 | https://github.com/tailwindlabs/tailwindcss/discussions/15855 | accessed_at: 2026-08-27. Официальное обсуждение в репозитории Tailwind Labs по настройке и использованию Tailwind без окружения Node.js. |

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| Боль: страх программирования, терминала и сложных команд | Решение: работа исключительно через чат Cursor Agent (Ctrl+I) на обычном русском языке без открытия терминала и без выполнения консольных команд | https://cursor.com/docs/agent/overview (accessed_at: 2026-08-27) | Результат: новичок уверенно ставит задачи ИИ обычными словами и получает готовые блоки интерфейса |
| Боль: Cursor генерирует сложный проект на React/Next.js с 50 файлами и package.json, требующий сборки | Решение: добавление файла правила `.cursor/rules/landing.mdc` с флагом `alwaysApply: true`, жестко фиксирующего работу только в одном файле `index.html` со стилями Tailwind CDN | https://cursor.com/docs/rules.md (accessed_at: 2026-08-27) | Результат: вся структура сайта умещается в один файл `index.html`, который мгновенно открывается в браузере без npm и локальных серверов |
| Боль: сайт красивый, но кнопка "Оставить заявку" перезагружает страницу и не отправляет данные | Решение: подключение бесплатного эндпоинта Formspree в теге `<form action="https://formspree.io/f/{id}" method="POST">` с обязательными атрибутами `name` на каждом поле ввода | https://formspree.io/html/ (accessed_at: 2026-08-27) | Результат: все контактные данные клиентов мгновенно приходят на личную электронную почту и в Telegram без написания бэкенда |
| Боль: непонимание, как выложить сайт в интернет: страх покупки хостинга, настройки VPS, DNS и SSL | Решение: бесплатная публикация через Vercel Drop (`vercel.com/drop`) — простое перетаскивание папки с `index.html` в окно браузера | https://vercel.com/docs/drop (accessed_at: 2026-08-27) | Результат: рабочий сайт с бесплатным HTTPS-сертификатом и стабильной ссылкой доступен всему миру за 15 секунд |
| Боль: кривое отображение на смартфонах и "слипание" текста на экранах телефонов | Решение: включение в промпт обязательного мета-тега `<meta name="viewport" content="width=device-width, initial-scale=1.0">` и адаптивных классов Tailwind `md:` и `lg:` | https://tailwindcss.com/docs/installation/play-cdn (accessed_at: 2026-08-27) | Результат: идеально адаптированная мобильная версия сайта без ручной подгонки пикселей в CSS |

## competitor_gaps
| competitor | what_they_miss | how_we_write_better |
| --- | --- | --- |
| Обзоры на VC / DTF / Habr | Уходят в общие рассуждения о "вайбкодинге", показывают установку Node.js и терминала, пугая непрограммистов | Даём строгий no-code маршрут: замок landing.mdc, один index.html, Tailwind CDN и zero terminal |
| Статьи про конструкторы сайтов (Tilda AI, Framer) | Описывают платные платформы с ежемесячной подпиской от 1000–2500 ₽/мес и закрытой экосистемой | Показываем 100% бесплатный стек (Cursor Hobby + Tailwind CDN + Formspree Free + Vercel Drop Free) с полным контролем над кодом |
| YouTube-туториалы по Cursor | Создают сайты без форм и без хостинга (останавливаются на локальном просмотре) | Закрываем сквозной бизнес-контур: от создания оффера до приёма реальной заявки на почту и публикации в сети |

## action_outline
1. Скачать и установить Cursor с официального сайта `cursor.com`, войти в бесплатный аккаунт и создать пустую рабочую папку на компьютере (например, `my-landing`).
2. Создать файл правила `.cursor/rules/landing.mdc` с директивой `alwaysApply: true` и четким запретом npm, Node.js, React и внешних сборок, ограничив проект одним файлом `index.html` с Tailwind CDN.
3. Сформулировать четкий бриф для Cursor Agent (Ctrl+I): структура hero-экрана, 3 ключевых преимущества, блок тарифов/услуг, блок отзывов и форма захвата контактов.
4. Сгенерировать страницу в Cursor Agent, проконтролировать наличие скрипта Tailwind Play CDN в `<head>` и проверить результат локальным открытием `index.html` в браузере.
5. Зарегистрировать бесплатный аккаунт на `formspree.io`, создать форму и скопировать уникальный endpoint вида `https://formspree.io/f/ваш_id`.
6. Попросить Cursor Agent связать форму лендинга с полученным эндпоинтом Formspree (`method="POST"`, `action="..."`) и убедиться в наличии атрибута `name` у полей имени, телефона и email.
7. Протестировать отправку формы локально и подтвердить получение тестового письма во входящих сообщениях почты.
8. Перейти на `vercel.com/drop`, перетащить папку с готовым `index.html` в окно браузера, задать имя проекта и получить готовую публичную https-ссылку за 15 секунд без Git и консоли.
9. Провести финальный чек-лист: открыть сайт со смартфона, проверить кликабельность кнопок и корректность отображения всех блоков перед запуском рекламы.
