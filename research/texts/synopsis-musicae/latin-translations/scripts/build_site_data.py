"""Build the site's data for the page of the Latin versions of the Synopsis of music (src/_data/texts/synopsis-musicae-latin.json)
from translation-latin.json. Xylander and Vinet are two sections of one reading page; each segment shows the Latin, the
Russian and the English, with the margin notes numbered separately for each language (as on the Greek page) and the
units of the Greek text it answers to as a link to the Synopsis page.
Usage: python -I build_site_data.py <latin-translations folder> <out json>"""
import html, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
L, OUT = sys.argv[1], sys.argv[2]
d = json.load(open(f'{L}/translation-latin.json', encoding='utf-8'))
REPO = 'https://github.com/alex-michels/neoscholia/blob/main/research/texts/synopsis-musicae'
URL = 'https://alex-michels.github.io/neoscholia/synopsis-musicae-latin.html'
GREEK = 'synopsis-musicae.html'
SEG = re.compile(r'\b([XV])(\d{2})\b')
counter = {'ru': 0, 'en': 0}


def links(s):
    """Escape text and turn segment references (X14, V22) into links to the segments."""
    out, pos = [], 0
    for m in SEG.finditer(s):
        out.append(html.escape(s[pos:m.start()], quote=False))
        out.append(f'<a href="#c{m.group(0)}">{m.group(0)}</a>')
        pos = m.end()
    out.append(html.escape(s[pos:], quote=False))
    return ''.join(out)


def mark_text(text, notes, lang):
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
    pieces, last = [], len(text)
    for end, i in sorted(placed, reverse=True):
        pieces.append(html.escape(text[end:last], quote=False))
        suffix = '' if lang == 'ru' else '-en'
        pieces.append(f'<sup class="n"><a href="#n{nums[i]}{suffix}">{nums[i]}</a></sup>')
        last = end
    pieces.append(html.escape(text[:last], quote=False))
    return ''.join(reversed(pieces)), [{'n': nums[i], 'text': links(notes[i][lang])} for _, i in placed]


def greek_units(units):
    if not units:
        return []
    a, b = int(units[0][1:]), int(units[-1][1:])
    return [f'греч. § {a}' if a == b else f'греч. § {a}–{b}']


HEAD = {'xylander': {'n': 1, 'ru': 'Ксиландр (Базель, 1556)', 'en': 'Xylander (Basel, 1556)'},
        'vinet': {'n': 2, 'ru': 'Вине (Турнон, 1591)', 'en': 'Vinet (Tournon, 1591)'}}
chapters = []
stats = {'segments': 0, 'notes': 0}
for w, v in d['versions'].items():
    for k, s in enumerate(v['segments']):
        c = {'chapter': s['id'], 'parallels': [s['ref']] + greek_units(s['units']), 'orig': s['latin']}
        if k == 0:
            c['heading'] = HEAD[w]
        c['ru'], c['notes_ru'] = mark_text(s['ru'], s['notes'], 'ru')
        c['en'], c['notes_en'] = mark_text(s['en'], s['notes'], 'en')
        log = [{'role': 'Сводка', 'who': '', 'text': links(s['basis'])}] if s.get('basis') else []
        for f in s.get('fixes') or []:
            log.append({'role': 'Исправлено', 'who': '', 'text': links(f)})
        if s.get('decisions'):
            log.append({'role': 'Решения редактора', 'who': '', 'text': links(', '.join(s['decisions']))})
        c['log'] = log
        chapters.append(c)
        stats['segments'] += 1
        stats['notes'] += len(s['notes'])
NX = len(d['versions']['xylander']['segments'])
NV = len(d['versions']['vinet']['segments'])

intro_ru = f'''<p>«Точный Синопсис Музыки», музыкальный раздел анонимного «Четверокнижия» 1008 г., в XVI в. дважды перевели на латынь: Гвильельм Ксиландр (Базель, 1556) и Эли Вине (здесь — по изданию Турнона 1591 г.). Оба считали автором Михаила Пселла. Здесь их латинские тексты переведены на русский и английский. Цель — показать, как поняли сочинение сами учёные XVI в., поэтому переводы сделаны с латыни, а не с греческого: там, где латынь расходится с греческим оригиналом, перевод следует латыни. Греческий текст и наш перевод с него — на <a href="{GREEK}">странице «Синопсиса»</a>; у каждого отрезка указан параграф греческого текста, которому он соответствует.</p>
<p>Латинские тексты установлены дважды: две независимые построчные транскрипции сведены, каждое расхождение решено по сканам; текст для чтения сверен с ними слово в слово, исправленные опечатки перечислены в репозитории. Ксиландр печатает текст пятью длинными абзацами без номеров, Вине делит его на пять глав с заголовками и нумерованные параграфы. Отрезки ({NX} у Ксиландра, {NV} у Вине) проведены по границам параграфов греческого текста, чтобы версии можно было сравнивать. Отрывков рукописи Paris. gr. 2448 (греч. § 28–32, 42–44, 50) в латинских переводах нет: их не было в печатном греческом тексте, с которого переводили.</p>
<p>Термины даны так, как их принято передавать в науке: «кварта, квинта, октава»; названия отношений — по-русски кальками («полуторное [3:2]», «сверхтретное [4:3]»), по-английски боэциевскими формами («sesquialter», «sesquitertian»), с числовым отношением в квадратных скобках. Латинские слова, буквальные значения и объяснения — в примечаниях на полях.</p>'''
intro_en = f'''<p>A Precise Synopsis of Music, the music section of the anonymous Quadrivium of 1008, was twice translated into Latin in the sixteenth century: by Guilielmus Xylander (Basel, 1556) and by Élie Vinet (here in the Tournon printing of 1591). Both took Michael Psellus for the author. Their Latin is translated here into Russian and English. The aim is to show how these scholars understood the work, so the translations are made from the Latin, not from the Greek: where the Latin departs from the Greek original, the translation follows the Latin. The Greek text and our translation of it are on <a href="{GREEK}">the Synopsis page</a>; each segment gives the paragraph of the Greek it answers to.</p>
<p>The Latin texts were established twice: two independent line-by-line transcriptions were merged and every difference decided against the scans; the reading text was checked word by word against them, and the corrected misprints are listed in the repository. Xylander prints the text in five long unnumbered paragraphs; Vinet divides it into five chapters with headings and numbered paragraphs. The segments ({NX} in Xylander, {NV} in Vinet) follow the paragraphs of the Greek text so that the versions can be compared. The passages of the manuscript Paris. gr. 2448 (Greek § 28–32, 42–44, 50) are absent from both: they were not in the printed Greek the translators used.</p>
<p>Terms are rendered as is usual in scholarship: "the fourth, the fifth, the octave"; ratio names are given in Russian as calques and in English in Boethius' forms ("sesquialter", "sesquitertian"), with the numerical ratio in square brackets. Latin words, literal senses and explanations are in the margin notes.</p>'''

process = {
    'text': f'''<p>Четыре независимых перевода обоих латинских текстов на русский и английский сделали Claude Fable 5.2 и Claude Opus 5.5 (Anthropic) и GPT-6.2 Sol и GPT-6.2 Astra (OpenAI). Переводчики работали только с латынью и сканами, без греческого оригинала и без других переводов; словари, грамматики и теоретики были разрешены. Три рецензента — сводный процесс Claude и модели GPT-6.2 Sol и GPT-6.2 Astra — сравнили переводы вслепую, по меткам A–D, нашли ошибки каждого и вынесли спорные места. Серьёзные ошибки, найденные только одним рецензентом, перепроверены вслепую двумя моделями.</p>
<p>Из всех вопросов рецензентов составлена 71 карточка решений (термины, метод, трудные места); редактор принял рекомендации. Затем Claude Opus 5.5 с агентами свёл окончательный текст: четыре сборщика по частям, независимые проверяющие и сквозная сверка терминов; ссылки в примечаниях проверены по источникам.</p>
<p>Все четыре перевода, сравнения, карточки решений и журналы — <a href="{REPO}/latin-translations/README.md">в репозитории</a>. Под каждым отрезком — журнал: из каких переводов он сведён, что исправлено и какие решения применены.</p>''',
    'stats': [{'value': '4', 'label': 'независимых перевода, модели двух компаний'},
              {'value': '3', 'label': 'слепых сравнения переводов'},
              {'value': '71', 'label': 'решение редактора по спорным местам'},
              {'value': str(stats['notes']), 'label': 'примечаний на полях'}],
    'open': ['Сравнить латинские переводы с греческим оригиналом: где Ксиландр и Вине понимают текст иначе.',
             'Латинский перевод Л. Аларда (1636): расшифровать и перевести.',
             'Примечания Ксиландра (Annotationes) к этому тексту.'],
}
VERSION_TEXT = ('Первая публикация. Латинские переводы Ксиландра и Вине переведены на русский и английский: сведено из четырёх '
                'независимых переводов (Claude Fable 5.2, Claude Opus 5.5, GPT-6.2 Sol, GPT-6.2 Astra) после трёх слепых сравнений '
                'и 71 решения редактора; ссылки в примечаниях сверены с источниками.')
data = {
    'title': 'Латинские переводы «Синопсиса Музыки»',
    'subtitle': 'Ксиландр (Базель, 1556) и Вине (Турнон, 1591) на русском и английском',
    'crumbs': [{'label': 'Библиотека', 'href': 'library.html'}, {'label': 'Музыка', 'href': 'music.html'},
               {'label': 'Анонимный «Синопсис Музыки»', 'href': GREEK}, {'label': 'Латинские переводы'}],
    'source': 'латинские переводы: Г. Ксиландр, Базель 1556, с. 40–49; Э. Вине, Турнон 1591, с. 41–53',
    'editor': 'Александр Михельс, PhD',
    'refPrefix': '',
    'logPrefix': 'отрезку ',
    'pagesLabel': 'стр.',
    'origLang': 'la',
    'inlineNotes': True,
    'intro_ru': intro_ru,
    'intro_en': intro_en,
    'chapters': chapters,
    'process': process,
    'versions': [{'version': '0.1', 'date': '21.11.2026', 'at': '2026-11-21T12:00',
                  'short': 'первая публикация — латинские переводы Ксиландра и Вине на русском и английском',
                  'text': VERSION_TEXT}],
    'cite': 'Латинские переводы «Синопсиса Музыки»: Ксиландр (1556) и Вине (1591) / пер. с лат. и комм.: Александр Михельс. Версия {version}. Neoscholia, 2026. ' + URL,
    'licenses': f'<p>Латинские тексты — по изданиям Базеля (1556) и Турнона (1591), общественное достояние. Переводы и примечания — CC BY-NC-SA 4.0. Журналы сравнения и проверки — CC0. Все материалы — <a href="{REPO}/latin-translations/README.md">в репозитории</a>.</p>',
    'ai': '<p>Независимые переводы: Claude Fable 5.2 и Claude Opus 5.5 (Anthropic), GPT-6.2 Sol и GPT-6.2 Astra (OpenAI). Сравнения: сводный процесс Claude Opus 5.5, GPT-6.2 Sol и GPT-6.2 Astra. Сводку окончательного текста, проверку и сверку ссылок с источниками провела Claude Opus 5.5 с агентами. Латинские тексты установлены дважды независимо (Claude и GPT-6 Astra). Решения по спорным местам принял редактор, Александр Михельс.</p>',
}
json.dump(data, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('chapters', len(chapters), 'notes ru', counter['ru'], 'en', counter['en'], '->', OUT)
