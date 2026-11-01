"""Build the site's data for the Synopsis of music page (src/_data/texts/synopsis-musicae.json) from the committed
translation (translation.json). Note markers go inline after their anchors and are numbered separately for each
language; references to units (U035, [U035]) become links to the paragraphs (§ 35).
Usage: python -I build_site_data.py <translation.json> <out json>"""
import html, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
SRC, OUT = sys.argv[1], sys.argv[2]
d = json.load(open(SRC, encoding='utf-8'))
REPO = 'https://github.com/alex-michels/neoscholia/blob/main/research/texts/synopsis-musicae'
URL = 'https://alex-michels.github.io/neoscholia/synopsis-musicae.html'

UREF = re.compile(r'\[?U(\d{3})\]?(?:–\[?U(\d{3})\]?)?')


def links(s):
    """Escape text and turn unit references into links to the paragraphs."""
    out, pos = [], 0
    for m in UREF.finditer(s):
        out.append(html.escape(s[pos:m.start()], quote=False))
        a = int(m.group(1))
        label = f'§ {a}–{int(m.group(2))}' if m.group(2) else f'§ {a}'
        out.append(f'<a href="#c{a}">{label}</a>')
        pos = m.end()
    out.append(html.escape(s[pos:], quote=False))
    return ''.join(out)


counter = {'ru': 0, 'en': 0}


def mark_text(text, notes, lang):
    """Insert note markers after the first occurrence of each anchor; number them in text order."""
    key = f'anchor_{lang}'
    placed = []
    for i, nt in enumerate(notes):
        a = nt.get(key) or ''
        p = text.find(a) if a else -1
        if p < 0:
            raise SystemExit(f'anchor not found: {lang} «{a}»')
        placed.append((p + len(a), i))
    placed.sort()
    nums = {}
    for end, i in placed:
        counter[lang] += 1
        nums[i] = counter[lang]
    # insert from the end; escape the text pieces between markers
    pieces, last = [], len(text)
    for end, i in sorted(placed, reverse=True):
        pieces.append(html.escape(text[end:last], quote=False))
        suffix = '' if lang == 'ru' else '-en'
        pieces.append(f'<sup class="n"><a href="#n{nums[i]}{suffix}">{nums[i]}</a></sup>')
        last = end
    pieces.append(html.escape(text[:last], quote=False))
    marked = ''.join(reversed(pieces))
    margin = [{'n': nums[i], 'text': links(notes[i][lang])} for _, i in placed]
    return marked, margin


SEC = {s['section']: s for s in d['sections']}
chapters, seen = [], set()
for u in d['units']:
    n = int(u['id'][1:])
    c = {'chapter': n, 'pages': u['bas'], 'parallels': ['только в P (Paris. gr. 2448)'] if u['p_only'] else [],
         'orig': u['greek']}
    if u['section'] not in seen:
        seen.add(u['section'])
        s = SEC[u['section']]
        c['heading'] = {'n': u['section'], 'ru': f"{u['section']}. {s['title_ru']}", 'en': f"{u['section']}. {s['title_en']}"}
    c['ru'], c['notes_ru'] = mark_text(u['ru'], u['notes'], 'ru')
    c['en'], c['notes_en'] = mark_text(u['en'], u['notes'], 'en')
    log = [{'role': 'Сводка', 'who': '', 'text': links(u['basis'])}] if u.get('basis') else []
    for v in u.get('verify') or []:
        if isinstance(v, str) and v.strip() and v.strip().lower() != 'no change':
            log.append({'role': 'Проверка', 'who': '', 'text': links(v)})
    c['log'] = log
    chapters.append(c)

intro_ru = f'''<p>«Точный Синопсис Музыки» (<span lang="grc">Τῆς μουσικῆς σύνοψις ἠκριβωμένη</span>) — музыкальный раздел анонимного «Четверокнижия»: краткого учебного свода логики и четырёх математических наук — арифметики, музыки, геометрии и астрономии. В астрономическом разделе автор дважды называет «нынешний» 6516 год от сотворения мира, то есть 1007/1008 г.; старейшая рукопись, Pal. gr. 281, переписана в 1040 г. В печатных изданиях XVI в. сочинение шло под именем Михаила Пселла, но Пселл родился около 1018 г. Поэтому автора называют Анонимом (в науке — Anonymus Heiberg, по критическому изданию Й. Л. Гейберга 1929 г.).</p>
<p>Это сжатый учебник гармоники в 67 параграфах: звук, интервал, система и гармония; названия ступеней; деление тона; несоставные и составные интервалы; консонансы и их отношения; как отношения находили по струнам, грузам и духовым инструментам; системы и три рода кварты; лады и виды мелодий. Учение об интервалах в основном пифагорейское, по Теону Смирнскому, изложение местами следует аристоксеновской традиции. Раздел цитировали Иоанн Зонара, Михаил Италик и Мануил Вриенний; целиком он вошёл в энциклопедию Иосифа Ракендита (XIV в.).</p>
<p>Греческий текст установлен заново: по рукописям Pal. gr. 281 (1040 г.) и Pal. gr. 262, по изданиям 1545 и 1556 гг. (Базельское — с латинским переводом и пометами Г. Ксиландра) и по отрывкам из рукописи Paris. gr. 2448, известным по публикации Венсана (1847). Эти отрывки (§ 28–32, 42–44, 50) есть только в этой рукописи и стоят в двойных угловых скобках ⟨⟨ ⟩⟩; одинарные ⟨ ⟩ отмечают слово, дополненное издателем, кресты † † — неисправленную порчу. Каждый параграф помечен страницей и строкой Базельского издания (Bas.). Издания Гейберга у нас нет. Текст, аппарат разночтений и все решения — <a href="{REPO}/constituted/text.md">в репозитории</a>.</p>
<p>Полного перевода на английский, насколько нам удалось установить, не было. Раздел переводили на латынь (Э. Вине, Г. Ксиландр, Л. Алард, XVI–XVII вв.) и на немецкий (Л. Мицлер, 1746). По-русски трактату посвящена глава 4 книги Е. В. Герцмана «Первый исторический этап европейского музыкального антиковедения» (2022); увидеть её нам пока не удалось, поэтому мы не называем наш русский перевод первым. С переводом Мицлера наш перевод сверен: его греческий столбец близок к изданию Аларда (1636), а немецкий перевод местами следует латыни Ксиландра (<a href="{REPO}/mizler-1746/README.md">сверка в репозитории</a>).</p>
<p>Термины даны так, как их принято передавать в русской и английской науке; буквальные значения, греческие формы и объяснения — в примечаниях на полях. Числовые отношения стоят в квадратных скобках: «сверхосминное [9:8]». В квадратных скобках даны и слова, добавленные для ясности. Примечания объясняют термины, учение и арифметику, приводят параллели у теоретиков и отмечают разночтения и ошибки составителя; ссылки в них сверены с источниками.</p>'''

intro_en = f'''<p>A Precise Synopsis of Music (<span lang="grc">Τῆς μουσικῆς σύνοψις ἠκριβωμένη</span>) is the music section of the anonymous Quadrivium, a short teaching compendium of logic and the four mathematical sciences: arithmetic, music, geometry and astronomy. In the astronomy section the author twice names the “present” year 6516 from the Creation, that is, 1007/1008; the oldest manuscript, Pal. gr. 281, was copied in 1040. The sixteenth-century printed editions put the work under the name of Michael Psellos, but Psellos was born around 1018. The author is therefore called the Anonymous (in scholarship, Anonymus Heiberg, after J. L. Heiberg’s critical edition of 1929).</p>
<p>It is a compact textbook of harmonics in 67 paragraphs: the note, the interval, the system and harmony; the names of the notes; the division of the tone; incomposite and composite intervals; the consonances and their ratios; how the ratios were found on strings, weights and wind instruments; the systems and the three genera of the fourth; modes and kinds of melody. Its doctrine of intervals is mostly Pythagorean, after Theon of Smyrna, while the exposition in places follows the Aristoxenian tradition. The section was quoted by John Zonaras, Michael Italikos and Manuel Bryennios, and was taken over whole into the encyclopaedia of Joseph Rhakendytes (fourteenth century).</p>
<p>The Greek text has been established afresh from the manuscripts Pal. gr. 281 (1040) and Pal. gr. 262, the editions of 1545 and 1556 (the Basel edition with Xylander’s Latin translation and marginal notes), and the passages of the manuscript Paris. gr. 2448 known from Vincent’s publication (1847). These passages (§ 28–32, 42–44, 50) occur only in that manuscript and stand in double angle brackets ⟨⟨ ⟩⟩; single ⟨ ⟩ mark a word supplied by the editor, and daggers † † an uncorrected corruption. Each paragraph carries the page and line of the Basel edition (Bas.). Heiberg’s edition has not been available to us. The text, the apparatus of variants and every decision are <a href="{REPO}/constituted/text.md">in the repository</a>.</p>
<p>As far as we have been able to establish, there has been no complete English translation. The section was translated into Latin (É. Vinet, W. Xylander, L. Alard, sixteenth–seventeenth centuries) and into German (L. Mizler, 1746). In Russian, chapter 4 of E. V. Gertsman’s book on the first stage of European musical classical scholarship (2022) is devoted to the treatise; we have not yet been able to see it, and so we do not call our Russian translation the first. Our translation has been compared with Mizler’s: his Greek column is close to Alard’s edition (1636), and his German in places follows Xylander’s Latin (<a href="{REPO}/mizler-1746/README.md">the comparison is in the repository</a>).</p>
<p>Terms are rendered as they are usually rendered in English and Russian scholarship; literal senses, Greek forms and explanations are in the notes in the margin. Numerical ratios stand in square brackets, “epogdoic [9:8]”; square brackets also enclose words added for clarity. The notes explain terms, doctrine and arithmetic, give parallels in the theorists and record variants and errors of the compiler; their references have been checked against the sources.</p>'''

VERSION_AT = '2026-11-01T21:30'
VERSION_TEXT = ('Сверка с немецким переводом Л. Мицлера (1746) и его греческим текстом (GPT-6.1 Sol с агентами; итоги '
                'проверила по сканам Claude Opus 5.5). В русском тексте исправлено согласование в § 50 («†и тот и другой† '
                'вид»); в § 66 ῥοαῖς — «текучим движением» вместо «плавным» («плавное движение» в теории музыки — '
                'поступенное, а этого текст не говорит). Уточнены примечания: определение ἄμεσος в § 34 и 43; толкования '
                'Мицлера в § 14, 18, 26 и 37. В аппарате снята запись «χολαιοτέραις Bas. Par.» при Bas. 33.15: оба издания '
                'печатают σχολαιοτέραις лигатурой σχ, похожей на χ; примечание к § 66 исправлено. Заглавие по-русски — '
                '«Точный Синопсис Музыки». '
                f'<a href="{REPO}/mizler-1746/README.md">Сверка и решения</a>.')

process = {
    'text': f'''<p>Перевод сделан по методу проекта, но в более широком составе. Шесть моделей трёх компаний независимо перевели весь текст на русский и английский: Claude Sonnet 5.5 и Claude Opus 5.5 (Anthropic), GPT-6.1 Terra, GPT-6.1 Sol и GPT-6 Astra (OpenAI), Kimi K3 (Moonshot AI). Три рецензента — сводный процесс Claude и модели GPT-6.1 Sol и GPT-6 Astra — сравнили переводы вслепую, по меткам A–F, нашли ошибки каждого и вынесли спорные места.</p>
<p>Редактор решил 15 общих вопросов перевода и 15 трудных мест. По спорным терминам проведено отдельное исследование словарей, теоретиков и русской и английской научной традиции; после него редактор пересмотрел шесть решений. Затем Claude Opus 5.5 с агентами свёл окончательный текст: шесть сборщиков по частям, три состязательных проверяющих и сквозная сверка терминов. Каждая ссылка в примечаниях проверена по самому источнику (Теон Смирнский по страницам Хиллера, теоретики по Яну, словари LSJ, DGE, Bailly); найденные ошибки исправлены. Последние 19 вопросов решил редактор.</p>
<p>После первой публикации перевод сверен с немецким переводом Л. Мицлера (1746) и его греческим текстом. Сверку независимо провела GPT-6.1 Sol с агентами: расшифровка Мицлера по сканам, пословная сверка двух греческих текстов, разбор по параграфам, по два скептика на каждую находку. Её итоги Claude Opus 5.5 проверила по сканам изданий. В русском тексте исправлены § 50 и 66, уточнены примечания. В аппарате снята ошибочная запись при Bas. 33.15: Базельское и Парижское издания печатают σχολαιοτέραις лигатурой σχ, похожей на χ.</p>
<p>Все шесть переводов, три сравнения, решения редактора, исследование терминов и журналы проверки — <a href="{REPO}/translation/README.md">в репозитории</a>. Под каждым параграфом — журнал: из каких переводов он сведён и что исправляли проверяющие (по-английски).</p>''',
    'stats': [{'value': '6', 'label': 'независимых переводов, модели трёх компаний'},
              {'value': '3', 'label': 'слепых сравнения переводов'},
              {'value': '49', 'label': 'решений редактора по спорным местам'},
              {'value': '142', 'label': 'примечания, ссылки сверены с источниками'}],
    'open': ['Сверить перевод с латинскими переводами Ксиландра, Вине и Аларда.',
             'Посмотреть главу о трактате в книге Е. В. Герцмана (2022).',
             'Сверить текст с критическим изданием Гейберга (1929), когда оно станет доступно.',
             'Ссылки, которые не удалось проверить в сети: страницы Баркера (Greek Musical Writings II), Лампе, формулировки Герцмана (2010) и Цыпина (2013).'],
}

data = {
    'title': 'Точный Синопсис Музыки',
    'subtitle': 'Музыкальный раздел анонимного «Четверокнижия» 1008 г., прежде приписывавшегося Михаилу Пселлу (67 параграфов)',
    'crumbs': [{'label': 'Библиотека', 'href': 'library.html'}, {'label': 'Музыка', 'href': 'music.html'},
               {'label': 'Анонимный «Синопсис Музыки»'}],
    'source': 'собственный критический текст: рукописи Pal. gr. 281 (1040) и Pal. gr. 262, издания 1545 и 1556 гг., отрывки Paris. gr. 2448 по Венсану (1847)',
    'editor': 'Александр Михельс, PhD',
    'first': 'Первый полный перевод на английский — насколько нам удалось установить',
    'refPrefix': '§ ',
    'logPrefix': '§ ',
    'pagesLabel': 'Bas.',
    'origLang': 'grc',
    'inlineNotes': True,
    'intro_ru': intro_ru,
    'intro_en': intro_en,
    'chapters': chapters,
    'process': process,
    'versions': [{'version': '0.2', 'date': '01.11.2026', 'at': VERSION_AT,
                  'short': 'сверка с немецким переводом Мицлера (1746): исправлены § 50 и 66, уточнены примечания, снята ошибочная запись аппарата при Bas. 33.15',
                  'text': VERSION_TEXT},
                 {'version': '0.1', 'date': '01.11.2026', 'at': '2026-11-01T04:30',
                  'short': 'первая публикация — перевод сведён из шести независимых, проверен моделями, ссылки сверены с источниками; спорные места решил редактор',
                  'text': 'Первая публикация. Перевод сведён из шести независимых переводов (Claude, GPT, Kimi) после трёх слепых сравнений и решений редактора по 49 спорным местам; ссылки в примечаниях сверены с источниками.'}],
    'cite': 'Аноним. Точный Синопсис Музыки (музыкальный раздел «Четверокнижия» 1008 г.) / пер. с греч. и комм.: Александр Михельс. Версия {version}. Neoscholia, 2026. ' + URL,
    'licenses': f'<p>Греческий текст установлен по изданиям 1545 и 1556 гг. (общественное достояние) и по цифровым копиям рукописей Pal. gr. 281 (Гейдельбергская университетская библиотека) и Pal. gr. 262 (Ватиканская библиотека); отрывки Paris. gr. 2448 — по изданию Венсана (1847, общественное достояние). Установленный текст, аппарат, перевод и примечания — CC BY-NC-SA 4.0. Журналы сравнения и проверки — CC0. Все материалы — <a href="{REPO}/translation/README.md">в репозитории</a>.</p>',
    'ai': '<p>Независимые переводы: Claude Sonnet 5.5 и Claude Opus 5.5 (Anthropic), GPT-6.1 Terra, GPT-6.1 Sol и GPT-6 Astra (OpenAI), Kimi K3 (Moonshot AI). Сравнения: сводный процесс Claude Opus 5.5, GPT-6.1 Sol и GPT-6 Astra. Исследование терминов, сводку окончательного текста, проверку и сверку ссылок с источниками провела Claude Opus 5.5 с агентами. Греческий текст установлен дважды независимо (Claude и GPT-6), спорные места решали судьи двух семейств моделей и редактор. Решения по спорным местам перевода принял редактор, Александр Михельс. Сверку с немецким переводом Мицлера (1746) провела GPT-6.1 Sol с агентами (Codex); её итоги проверила Claude Opus 5.5.</p>',
    'bibliography': [{'key_ru': b['key_ru'], 'key_en': b['key_en'], 'ru': html.escape(b['ru'], quote=False),
                      'en': html.escape(b['en'], quote=False)} for b in d['bibliography']],
}
json.dump(data, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('chapters', len(chapters), 'notes ru', counter['ru'], 'en', counter['en'], '->', OUT)
