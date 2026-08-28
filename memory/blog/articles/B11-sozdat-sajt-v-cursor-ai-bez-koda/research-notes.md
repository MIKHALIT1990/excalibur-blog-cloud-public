research_date: 2026-08-28
accessed_at: 2026-08-28
prefer_sources_after: 2026-05-30
utility_verdict: PASS
reader_outcome: Новичок без навыков программирования создаст красивый адаптивный сайт-визитку или лендинг в редакторе Cursor AI за 30 минут, подключит форму сбора заявок без бэкенда и опубликует его в интернете бесплатно.
reader_pain: Страх перед кодом, консолью и сложными терминами: новичок открывает AI-редактор, просит «сделай сайт», а нейросеть начинает генерировать React/Node.js, требует установку npm/Docker в терминале, выдаёт ошибки сборки, и пользователь бросает затею.
success_criteria: Новичок открывает сгенерированный файл index.html двойным кликом в браузере, видит готовый современный адаптивный сайт с формой заявки, отправляет тестовый контакт и получает письмо на почту/в Telegram, а затем разворачивает сайт на бесплатном хостинге по постоянному URL.
voice_angle: Практический гайд от Михаила (AI Brother) без разработческого снобизма: показываем, как обуздать Cursor AI простым промптом и получить чистый HTML/Tailwind без терминала, поломок и платных конструкторов.
reader_story: Предприниматель или маркетолог решил сделать лендинг для услуги в Cursor AI. Написал в чат «Создай мне лендинг юридических услуг», нейросеть создала 15 файлов на Next.js и написала «запустите npm run dev». У пользователя нет Node.js, терминал выдаёт ошибку 'npm not recognized', в браузере ничего не открывается, вечер испорчен. Правильный путь — сразу ограничить Cursor правилом «Single-file HTML + Tailwind CDN».
surprising_fact: Cursor AI способен создавать полноценные интерактивные сайты в одном файле index.html с анимациями и адаптивным дизайном через CDN-библиотеки вообще без сборщиков кода и установки Node.js, а хостинг Vercel Drop или GitHub Pages позволяет выложить такой сайт в сеть за 60 секунд простым перетаскиванием мыши.

Окно свежести источников: prefer_sources_after=2026-05-30 (контекст research-context.json, 2026 год).

## research_questions
1. Какой реальный спрос в русскоязычном сегменте на создание сайтов с помощью нейросетей и Cursor AI в августе 2026 года?
2. Почему классические AI-конструкторы (Tilda AI, Framer AI, Wix) уступают связке Cursor AI + чистый HTML по гибкости и стоимости владения?
3. В чём главная ошибка новичков при первом запуске Cursor AI и как промптом запретить агенту плодить лишние файлы и сложные фреймворки (Next.js, Vite, npm)?
4. Какой минимальный и надёжный технологический стек подходит для no-code/low-code сборки в Cursor AI (HTML5, Tailwind CSS via CDN, Lucide Icons, Google Fonts)?
5. Как настроить прием заявок с формы без программирования серверной части (Web3Forms, Formspree, Telegram Webhook)?
6. Как бесплатно и без работы с консолью опубликовать готовый сайт в интернете (Vercel Drop, GitHub Pages, Netlify)?
7. Как связать форму на сайте со сквозной воронкой в CRM (amoCRM / Битрикс24) и Telegram для мгновенного первого ответа клиенту?

## source_table
| source | url | accessed_at | why_it_matters |
| --- | --- | --- | --- |
| Cursor Official Rules Docs | https://cursor.com/docs/rules | accessed_at: 2026-08-28 | Официальная спецификация правил Cursor (.cursor/rules/*.mdc, AGENTS.md), управление контекстом агента |
| Cursor Models & Pricing | https://cursor.com/docs/models-and-pricing | accessed_at: 2026-08-28 | Актуальные тарифы Cursor в 2026: бесплатный план, Pro ($20/мес), поддержка моделей Claude 3.7 / GPT-4o / Composer |
| GitHub Pages Official Guide | https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site | accessed_at: 2026-08-28 | Официальное руководство по бесплатному хостингу статических HTML-сайтов на GitHub |
| Vercel Drop Docs | https://vercel.com/docs/drop | accessed_at: 2026-08-28 | Документация мгновенной публикации статических HTML/CSS сайтов перетаскиванием без Git и CLI |
| Formspree HTML Forms Docs | https://help.formspree.io/articles/building-your-form/building-an-html-form | accessed_at: 2026-08-28 | Интеграция формы сбора лидов на статическом сайте без серверного кода и PHP |
| Web3Forms Official Docs | https://web3forms.com/ | accessed_at: 2026-08-28 | Бесплатный сервис отправки лидов с HTML-формы на Email без регистрации сервера |
| Awesome Cursorrules GitHub | https://github.com/PatrickJS/awesome-cursorrules | accessed_at: 2026-08-28 | Каталог проверенных правил .mdc для генерации HTML, Tailwind CSS и лендингов в Cursor AI |
| Cinematic Landing Kit GitHub | https://github.com/alwkala/Cinematic-Landing-Kit | accessed_at: 2026-08-28 | Шаблоны и архитектура сборки single-file HTML лендингов для AI-агентов без сборщиков и npm |
| Awesome Cursor Skills GitHub | https://github.com/spencerpauly/awesome-cursor-skills | accessed_at: 2026-08-28 | Репозиторий скиллов и правил для управления поведением AI-агента в Cursor |
| Open Agent Toolkit Docs | https://github.com/voxmedia/open-agent-toolkit/blob/main/.agents/docs/cursor-rules-files.md | accessed_at: 2026-08-28 | Архитектура инструкций для AI-агентов, спецификация .cursor/rules и AGENTS.md |
| Хабр: Актуальный гайд Cursor 2026 | https://habr.com/ru/companies/bothub/articles/1044774/ | accessed_at: 2026-08-28 | Опыт русскоязычного сообщества: агентный режим Composer, горячие клавиши, генерация интерфейсов |
| Журнал Код: Туториал Cursor 2026 | https://thecode.media/cursor-ai-tutorial-2026/ | accessed_at: 2026-08-28 | Практика пошагового контроля генерации кода и проверки результатов для новичков |
| AI Brother Fact Bank | https://ai-brother.ru | accessed_at: 2026-08-28 | Бизнес-логика: воронка «заявка → мгновенный ответ → CRM», интеграция лид-форм |

## wordstat
Данные: `wordstat_get_top_requests`, регион 225 (Россия), устройства: DEVICE_ALL, accessed_at: 2026-08-28.

| phrase | impressions |
| --- | --- |
| cursor ai | 11852 |
| создать сайт нейросеть | 1585 |
| создать сайт с нейросетью | 659 |
| скачать cursor ai | 569 |
| создать сайт с помощью нейросети | 477 |
| cursor ai pro | 398 |
| cursor ai подписка | 356 |
| cursor ai купить | 348 |
| создание сайта с помощью нейросети | 336 |
| cursor ai бесплатно | 259 |
| cursor ai code | 186 |
| нейросеть онлайн создать сайт | 176 |
| cursor ai в россии | 176 |
| создать сайт с нейросетью бесплатно | 170 |
| создать сайт нейросетью онлайн бесплатно | 164 |
| как создать сайт с помощью нейросети | 146 |
| cursor ai оплатить | 133 |
| cursor ai аналоги | 124 |
| создать сайт с помощью нейросети бесплатно | 120 |
| cursor ai claude | 123 |
| cursor ai купить подписку | 118 |
| cursor ai download | 118 |
| создать сайт через нейросеть | 112 |
| cursor ai установить | 112 |
| cursor ai сайт | 110 |
| cursor ai vs | 108 |
| как пользоваться cursor ai | 107 |
| cursor ai модели | 103 |
| как создать сайт с помощью нейросети бесплатно | 27 |
| как пользоваться cursor ai в россии | 15 |

LSI-ключи и поисковые хвосты для копирайтера:
- создание сайта с помощью нейросети пошагово
- как пользоваться cursor ai для новичка
- создать лендинг в cursor ai бесплатно
- одностраничный сайт html tailwind нейросеть
- форма сбора заявок без сервера для сайта
- как выложить сайт на github pages и vercel

## github_evidence
| repo/issue/doc | url | signal |
| --- | --- | --- |
| PatrickJS/awesome-cursorrules | https://github.com/PatrickJS/awesome-cursorrules | Правила .cursor/rules/*.mdc для HTML/Tailwind CSS/JS; запрет лишних фреймворков и генерация чистого семантического кода |
| alwkala/Cinematic-Landing-Kit | https://github.com/alwkala/Cinematic-Landing-Kit | Паттерн zero-build single-file index.html: Tailwind через CDN (cdn.tailwindcss.com), Lucide/FontAwesome и Google Fonts без npm |
| spencerpauly/awesome-cursor-skills | https://github.com/spencerpauly/awesome-cursor-skills | Каталог готовых правил и воркфлоу для Cursor Agent, техники удержания контекста |
| voxmedia/open-agent-toolkit | https://github.com/voxmedia/open-agent-toolkit/blob/main/.agents/docs/cursor-rules-files.md | Формат frontmatter для правил Cursor MDC (description, globs, alwaysApply) и поддержка AGENTS.md |
| justdoinc/justdo mdc format | https://github.com/justdoinc/justdo/blob/master/.cursor/rules/999-mdc-format.mdc | Спецификация структурирования инструкций в .cursor/rules для точной генерации файлов |

## pain_solution_map
| pain | solution | proof/source | reader_result |
| --- | --- | --- | --- |
| Боль: «Я не программист, не знаю HTML/CSS и боюсь сломать код при первой ошибке» | Решение: Работа в режиме Cursor Composer / Agent на человеческом русском языке. Ограничиваем задачу созданием одного файла index.html со стилями через CDN | https://cursor.com/docs/rules, https://thecode.media/cursor-ai-tutorial-2026/ | Читатель управляет сборкой сайта обычными текстовыми описаниями и видит результат сразу в браузере без правки кода вручную |
| Боль: Cursor генерирует React/Next.js и требует терминал, в котором сыплются ошибки npm | Решение: Использование простого стартового промпта или файла .cursor/rules/landing.mdc с прямым указанием: «Создавай только один файл index.html, используй Tailwind CSS CDN, не запускай npm и терминал» | https://github.com/PatrickJS/awesome-cursorrules, https://github.com/alwkala/Cinematic-Landing-Kit | Полное отсутствие ошибок сборки; проект состоит из 1 понятного файла, готового к запуску в любом браузере |
| Боль: Конструкторы (Tilda, Framer) требуют дорогую подписку (от 1500–2500 руб/мес) и привязывают сайт к платформе | Решение: Полная независимость — исходный код сайта остаётся у пользователя на компьютере, а хостинг на Vercel Drop или GitHub Pages полностью бесплатный | https://vercel.com/docs/drop, https://docs.github.com/en/pages | Нулевые затраты на содержание сайта ($0/месяц) и возможность перенести сайт на любой хостинг или домен |
| Боль: «Как получать заявки с сайта, если у меня нет базы данных, PHP и бэкенда?» | Решение: Бесплатное подключение Web3Forms или Formspree через атрибут action у формы — заявки с контактами мгновенно приходят на email или в Telegram | https://web3forms.com/, https://help.formspree.io/articles/building-your-form/building-an-html-form | Работающая форма обратной связи на сайте, отправляющая лиды прямо в телефон собственника без написания серверного кода |
| Боль: «Заявки приходят на почту, менеджеры долго отвечают и клиенты уходят к конкурентам» | Решение: Настройка webhook-передачи из формы в связку со звоноботом или ИИ-агентом (AI Brother) для мгновенного первого звонка/сообщения и фиксации в CRM | https://ai-brother.ru | Сквозная воронка продаж: сайт собирает лид → ИИ отвечает клиенту за 10 секунд → сделка создаётся в amoCRM/Битрикс24 |

## competitor_gaps
| competitor | what_they_miss | how_we_write_better |
| --- | --- | --- |
| VC.ru / Habr (общие статьи по Cursor) | Пишут для профессиональных разработчиков: сразу предлагают установить Node.js, настроить Git CLI, Docker и писать на React/TypeScript. Новичок пугается на первом же шаге | Предлагаем изолированный путь «Zero-Terminal»: 1 файл index.html, Tailwind через CDN, проверка простым двойным кликом в браузере |
| Land-maker / MashaGPT / TimeWeb (обзоры конструкторов) | Рекламируют платные облачные no-code платформы с абонентской платой, умалчивая, что AI-редакторы позволяют сделать сайт бесплатно и забрать исходный код себе | Честно сравниваем экономику: $0 за хостинг и код в вашей собственности против пожизненной подписки на конструктор |
| Блоги хостингов (Dzen, Scrile) | Дают поверхностные промпты вида «сделай лендинг», не объясняя, как настроить форму заявок, где брать бесплатные иконки/шрифты и как избежать галлюцинаций ИИ | Даём готовый шаблон промпта с блокировкой лишних файлов, инструкцию по иконкам Lucide/FontAwesome и интеграции формы через Web3Forms |

## action_outline
1. Подготовка и установка: Скачиваем Cursor AI с официального сайта cursor.com, авторизуемся под бесплатным тарифом и создаём пустую папку проекта на рабочем столе.
2. Закрепление правил для агента: Создаём в папке файл инструкции (простой промпт или правило), запрещающий установку Node.js/npm и требующий сборку сайта в одном файле index.html с подключением Tailwind CSS и Google Fonts через CDN.
3. Генерация структуры и контента: Открываем режим Composer / Agent (Ctrl+I / Cmd+I), вводим пошаговый промпт с описанием структуры страницы (Header, Hero с УТП, Преимущества, Тарифы/Услуги, Отзывы/Кейсы, Форма заявки, Footer).
4. Проверка и визуальная полировка: Открываем файл index.html в браузере (двойной клик), смотрим адаптивность на мобильных устройствах, просим Cursor исправить цвета, отступы или добавить раскрывающийся FAQ через интерактивный чат.
5. Подключение формы сбора заявок: Регистрируем бесплатный ключ в Web3Forms или Formspree за 1 минуту, вставляем его в форму и отправляем тестовую заявку для проверки доставки на Email/Telegram.
6. Бесплатная публикация сайта в интернете: Загружаем папку на Vercel Drop (drag-and-drop за 30 секунд) или настраиваем репозиторий GitHub Pages, получая рабочий HTTPS-адрес сайта.
7. Подключение собственного домена и связка с воронкой: Привязываем домен (по желанию) и настраиваем автопередачу контактов в CRM (amoCRM / Битрикс24) для мгновенного первого ответа клиентам.
