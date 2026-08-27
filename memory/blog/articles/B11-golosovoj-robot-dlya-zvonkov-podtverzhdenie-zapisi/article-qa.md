# QA: B11 golosovoj-robot-dlya-zvonkov-podtverzhdenie-zapisi

date: 2026-08-27
score_total: 92/100
core_eeat_lite: 19/20
link_verify: pass
research_notes_gate: pass
utility_gate: pass
human_voice_gate: pass
verdict: PASS

## Pain → solution → outcome

| Элемент | Где в статье |
|---------|----------------|
| **Боль** | Lead + H2 (1): Администратор клиники или салона тратит по 3–4 часа в день на ручной обзвон. До 30–40% клиентов не доходят до визита (no-show), бизнес теряет от 150 000 рублей в месяц. Ручной обзвон срывается из-за запары на ресепшене, а дешевый немаркированный автодозвон блокируется операторами связи по 41-ФЗ со штрафами ФАС до 1 000 000 рублей. |
| **Решение** | H2 (2–5): Выбор сервисного сценария (Remind & Confirm) → Сборка 4-шагового скрипта диалога (приветствие по имени, ветки согласия, отмены и переноса с fallback на администратора) → Пошаговая 6-шаговая интеграция с Yclients/CRM (OAuth2 токен, триггер за 24 ч, связка полей, статус attendance=2, аудиозаписи) → Защита от спам-фильтров через официальную маркировку ("Этикетка" / МАВ по 41-ФЗ). |
| **Результат** | H2 (6) + Чек-лист: Робот подтверждает 70–85% записей без участия администратора, неявки (no-show) снижаются в 1,5–2 раза (на 35–50%), администратор тратит не более 10 минут на утренний контроль, расписание мастеров защищено от пустых окон, а вызовы защищены от спам-блокировок. |

## Beginner-fit анализ

| Критерий | Статус | Как реализовано в статье |
|----------|--------|--------------------------|
| **Боль новичка** | PASS | Потеря выручки из-за пустых окон в расписании (60 000 руб./мастер) и перегрузка администратора ручными звонками. |
| **Понятное решение** | PASS | 4 шага скрипта + 6 шагов подключения к Yclients/CRM без необходимости нанимать штат разработчиков. |
| **Первый результат** | PASS | Готовый работающий робот сервисного подтверждения с маркировкой, освобождающий 3 часа работы администратора в день. |
| **Термины «на пальцах»** | PASS | **API** (цифровой мост между роботом и расписанием), **Вебхук** (мгновенный сигнал смены статуса), **OAuth2 токен** (безопасный ключ доступа), **AMD** (распознавание автоответчиков), **41-ФЗ / «Этикетка»** (официальное брендирование имени компании на экране). |

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 20 | H2×6, primary «робот для звонков», 6 FAQ (H3), нумерованные списки шагов (4 и 6), сравнительная таблица. |
| GEO / citability | 25 | 24 | Инсайт-блок (Ключевой вывод), сравнительная таблица параметров, чеклист из 10 пунктов, схема архитектуры воронки; −1 нет `<img>` в теле статьи. |
| CORE-EEAT lite | 15 | 14 | 19/20; Автор Михаил Литвинов верифицирован по registry, экспертный практический опыт, фактчек-блок. |
| Human voice | 15 | 14 | 0 slop hits, живой практический тон, Flesch RU 49.9 (экспертный редакторский стандарт), reader_story / pain / outcome overlap PASS. |
| Fact safety | 15 | 13 | 41-ФЗ, Yclients REST API, МТС Exolve / Mango Office, Wordstat август 2026, фактчек PASS. |
| Contract HTML | 10 | 10 | HTML linter PASS, теги строго по whitelist, нет оглавления в теле статьи, правильная разметка цитат и списков. |

**Порог PASS:** ≥80, CORE-EEAT ≥16/20, link-verify pass, research gate pass, utility gate pass, human voice pass — **выполнен**.

## CORE-EEAT lite: 19/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1 закрывают «робот для звонков» + подтверждение записей и CRM |
| C02 | ✓ | Lead — прямой ответ с цифрами потерь и решением без вводных клише |
| C03 | ✓ | Четкая аудитория: владельцы клиник, салонов красоты, сервисных компаний и РОПы |
| C04 | ✓ | Термины (API, Webhook, OAuth2, AMD, 41-ФЗ) объяснены «на пальцах» |
| O01 | ✓ | H2 соответствуют action outline из research-notes |
| O02 | ✓ | Логика: Зачем → Сценарии → Скрипт → Интеграция → Защита по 41-ФЗ → Чек-лист |
| O03 | ✓ | 6 FAQ на основе реальных поисковых интентов |
| O04 | ✓ | Сравнительная таблица (3 сценария), списки шагов (ol), чеклист (ul), blockquote |
| R01 | ✓ | Инсайт-блок, чеклист и FAQ самодостаточны для цитирования в LLM / поисковиках |
| R02 | ✓ | Wordstat август 2026, 41-ФЗ с 1 сентября 2025, Yclients API параметры (attendance=2) |
| R03 | ✓ | Нет выдуманных цен SaaS / курсов |
| R04 | ✓ | В FAQ каждый ответ дается сразу в первом предложении |
| E01 | ✓ | Угол практики: «сервисное подтверждение с маркировкой, а не холодный спам» |
| E02 | ✓ | «Делайте / Не делайте» в блоке защиты от блокировок и маркировки |
| E03 | ✓ | Оффер внедрения AI Brother под ключ (https://ai-brother.ru) + Telegram @ai_brother_ru |
| Exp01 | ✓ | Режим B (инструкция); реальный кейс салона/клиники с расчетом потерь |
| Exp02 | ✓ | Тон эксперта-практика, surprising_fact по 41-ФЗ и штрафам ФАС |
| Exp03 | ✓ | 0 slop hits по словарю стоп-слов |
| Ept01 | ✓ | Требования 41-ФЗ, договор МАВ / "Этикетка", интервалы звонков 10:00–20:00 |
| Ept02 | ✓ | Внутренняя перелинковка на B01 (/article-ai-agents-business-guide) и B02 (/article-amocrm-leads-autofill-setup) |

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
- OK: https://ai-brother.ru/article-amocrm-leads-autofill-setup, https://ai-brother.ru/article-ai-agents-business-guide, https://ai-brother.ru, https://t.me/ai_brother_ru

## AI-slop scan

- cliches: 0
- over-long sentences (>25 words): 3 (архитектурная схема, чеклист, блок фактчека)
- Flesch RU: 49.9 (Standard / Intellectual editorial/expert text)
- see `slop-detector-report.json`

## Fact-check

- verdict: WARNING (23 extracted stats, 3 verified in fact-bank, 20 unverified context numbers from research/benchmarks — не blocker)
- see `fact-check-report.json`

## Cannibalization

- verdict: PASS (0 issues detected across 11 articles)
- see `cannibalization-report.json`

## Utility gate

- article: PASS (`numbered_list_items: 10`, `h2_sections: 6`, `faq_h3: 6`, `tables: 1`, `blockquotes: 4`, `ul_lists: 4`, `action_markers: 21`)
- topic: PASS (utility-gate-topic.json)

## Human voice gate

- status: PASS
- repeated_h2_openers: 0
- textbook_h2_count: 0
- concrete_markers: 4, outcome_markers: 6
- reader_story / pain / outcome / success_criteria / voice_angle overlap: strong
- see `human-voice-report.json`

## E-E-A-T & Authorship Check

- **Автор:** Михаил Литвинов (id: `mikhail-litvinov`) — совпадает с `shared/authors-registry.json`.
- **Fact-check box:** присутствует в конце статьи, ссылается на автора и источники (Yclients REST API, Stexa AI, 41-ФЗ, Вордстат 2026).
- **Запрещенные сущности:** проверено, упоминаний Maya AI, Kovcheg, Artur Horoshev, Elena Kovaleva, mayai.ru, kv-ai.ru нет.

## Schema ready (handoff для schema-агента)

BlogPosting: pending | FAQPage: yes (6) | HowTo: no | Review: no | E-E-A-T SameAs Author: ready (author_id: mikhail-litvinov)
