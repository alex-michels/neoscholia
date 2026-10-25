# Макеты сайта Neoscholia (архив)

> **Это архив.** Здесь лежат исходники первых макетов, опубликованных как приватные артефакты на claude.ai. Настоящий сайт теперь собирается из папки [`../src/`](../src/) генератором Eleventy; как править — в [`../EDITING.md`](../EDITING.md). Правки в этой папке на сайт не влияют.

| Страница | Файл | Ссылка |
|---|---|---|
| Главная библиотеки | [library-home.html](library-home.html) | https://claude.ai/artifact/Sxv32gV4SoYwPGMXD1UYHD |
| Раздел «Роман об Александре» | [alexander-section.html](alexander-section.html) | https://claude.ai/artifact/HTuCJke5U2X3XbBcPHJeWK |
| Раздел «Схолии» | [scholia-section.html](scholia-section.html) | https://claude.ai/artifact/HqyqE2tpQepFtVvpu58bdZ |
| Раздел «Музыка» | [music-section.html](music-section.html) | https://claude.ai/artifact/WZmCFMo4TVrZBDsoT5KGyu |
| Страница текста: схолии к «Одиссее» X | [scholia-odyssey-10.html](scholia-odyssey-10.html) | https://claude.ai/artifact/KBXAd7KtUgWioncxPUnJ77 |
| Метод (редакционная хартия) | [method.html](method.html) | https://claude.ai/artifact/LUNNJwceDXYWoepQJWmVVL |
| Исследования | [studies.html](studies.html) | https://claude.ai/artifact/FtriAuMyfVpLWqqMqZDQ8o |
| О проекте | [about.html](about.html) | https://claude.ai/artifact/WNygYEn7HeTq5PbrvPt2BF |
| Статья (макет страницы исследования): «Пергам против Александрии? Кратет, Аристарх и „короткие ночи“ лестригонов» | [study-laestrygonians.html](study-laestrygonians.html) | https://claude.ai/artifact/1cgGFnmeuFMRZKJK2XR8Nc |

## Общая система

**Фон.** Ровный тёплый фон без узора, текст лежит на светлом «листе». Есть тёмная тема «библиотеки при лампе».

**Шрифты:**
- Forum — заголовки;
- Gentium Book Plus — текст, политонический греческий и кириллица;
- Alegreya Sans SC — подписи.

**Цвета:**
- красный — леммы, отметки «нет перевода», акценты;
- синий — статусы и ссылки.

**Статусы текста:** машинный черновик → проверено моделями → проверено редактором → внешняя рецензия.

**Страница статьи** — образец для всех будущих исследований:
- оглавление слева, примечания на полях, на телефоне они открываются по нажатию;
- аннотация RU/EN;
- путь публикации: досье → препринт → проверка автором → рецензия → журнал;
- интерактивный рисунок с расчётом;
- приложение с переводом (тот же переключатель «перевод / параллельно / оригинал», что на странице текста);
- блок «Как сделана статья»: роль моделей и автора, итоги проверки;
- открытая рецензия и версии, литература с пометами о проверке, цитирование в трёх форматах.

Рядом со страницей публикуется досье источников (`laestrygonians-dossier.md`). Содержание статьи настоящее, рабочие материалы лежат в [`../research/studies/laestrygonians/`](../research/studies/laestrygonians/).

**Что пока заглушки:**
- переключатель языка интерфейса EN;
- указатели;
- «Весь раздел» у будущих разделов;
- DOI и ISSN;
- форма исправлений;
- [ФИО] редактора.
