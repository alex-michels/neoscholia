"""Build the reading texts of the two Latin translations (Xylander 1556, Vinet 1591) for translation.

The base is the normalised reading text of the GPT-6 Astra transcription (orthography normalised: u/v, i/j, ae for æ
and e caudata, no printers' accents; abbreviations expanded; obvious misprints corrected). It is checked word by word
against the agreed diplomatic lines (transcriptions/xylander1556-latin.json, vinet1591-latin.json), after folding
both to lower case without accents, u/v, i/j and punctuation. Every difference must be one of the corrections listed
below (or a word division); anything else stops the script.
Usage: python -I build_reading.py <synopsis-musicae folder> <out json>"""
import difflib, json, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
R, OUT = sys.argv[1], sys.argv[2]
T = f'{R}/transcriptions'
G = json.load(open(f'{T}/gpt/transcription-gpt-6-astra-latin.json', encoding='utf-8'))

# Every difference between the folded diplomatic text and the folded reading text, with the reason.
CORRECTIONS = {
    'xylander': {
        'diatesseron': ('diatessaron', 'Xyl. 48.20', 'misprint: the interval is diatessaron everywhere else (48.11, 48.14, 48.24)', 'diatesseron', 'diatessaron'),
        'unamquanque': ('unamquamque', 'Xyl. 49.16', 'misprint: n before the -que sign; accusative unamquamque', 'unamquan- with the -que sign', 'unamquamque'),
        'meliodiarum': ('melodiarum', 'Xyl. 49.18', 'misprint: the word is melodia everywhere else', 'meliodiarum', 'melodiarum'),
    },
    'vinet': {
        'quedam': ('quaedam', 'Vinet 42.18', 'e caudata for ae', 'quędam', 'quaedam'),
        'hemitotonium': ('hemitonium', 'Vinet 44.7–8', 'misprint: the syllable to repeated across the line end', 'hemito-|tonium', 'hemitonium'),
        'que': ('quae', 'Vinet 44.17', 'e caudata for ae (relative pronoun)', 'quę', 'quae'),
        'hec': ('haec', 'Vinet 45.6', 'e caudata for ae', 'hęc', 'haec'),
        'nanque': ('namque', 'Vinet 45.9', 'spelling: nanque for namque', 'nanque', 'namque'),
        'nnncupata': ('nuncupata', 'Vinet 46.13', 'misprint: turned u', 'nnncupata', 'nuncupata'),
        'cnm': ('cum', 'Vinet 47.13', 'misprint: turned u', 'cnm', 'cum'),
        'iuterualli': ('interualli', 'Vinet 48.21', 'misprint: turned n', 'iuterualli', 'intervalli'),
        'sequitertia': ('sesquitertia', 'Vinet 48.22', 'misprint: s omitted; sesquialtera in the same line, sesquitertius 49.1', 'sequitertia', 'sesquitertia'),
        'diapasson': ('dia pason', 'Vinet 48.24–25', 'misprint: double s; Dia-pason everywhere else', 'Dià-|passon', 'Dia-pason'),
        'chordatum': ('chordarum', 'Vinet 50.4–5', 'misprint: the genitive plural is needed, cf. chor-|darum 49.8–9', 'chor-|datum', 'chordarum'),
        'quoqne': ('quoque', 'Vinet 53.17', 'misprint: turned u', 'quoqne', 'quoque'),
    },
}
HEADINGS = {'xylander': [], 'vinet': ['michaelis pselli musica caput 1 de musica in commune', 'caput 2 de soni natura et uariis appellationibus',
                                      'caput 3 de interuallis', 'cap 4 de systematis', 'caput 5 de harmonia', 'finis musicae']}


def fold(s):
    s = s.replace('æ', 'ae').replace('Æ', 'ae').replace('œ', 'oe').replace('Œ', 'oe').replace('ę', 'e')
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))
    return re.findall(r'[a-z0-9]+', s.lower().replace('v', 'u').replace('j', 'i'))


def diplomatic_words(lines):
    words, carry = [], ''
    for ln in lines:
        toks = ln['text'].split()
        for i, w in enumerate(toks):
            w, carry = carry + w, ''
            if i == len(toks) - 1 and w.endswith('-') and len(w) > 1:
                carry = w[:-1]
                continue
            words.append(w)
    return [f for w in words + ([carry] if carry else []) for f in fold(w)]


def capitals(t):
    """The decorative capitals after a large initial (UNiversum, MUsica) in normal case."""
    return re.sub(r'^([A-Z])([A-Z]+)([a-z])', lambda m: m.group(1) + m.group(2).lower() + m.group(3), t)


out = {'status': 'reading texts for translation, 2026-11-20: the normalised text of the GPT-6 Astra transcription, '
                 'checked word by word against the agreed diplomatic transcription (Claude and GPT-6 Astra, every '
                 'difference decided against the scans); each remaining difference is a correction listed here',
       'conventions': 'orthography normalised (u/v, i/j; ae and oe for æ, œ and e caudata; no printers\' accents); '
                      'abbreviations expanded; obvious misprints corrected (listed); decorative capitals after an '
                      "initial in normal case; Vinet's chapter numbers as Roman numerals (printed CAPVT 1. etc.)"}
for wit, src in (('xylander', 'xylander1556-latin.json'), ('vinet', 'vinet1591-latin.json')):
    D = json.load(open(f'{T}/{src}', encoding='utf-8'))
    g = G[wit]
    paras = [{'para': p['para'], 'ref': p['ref'], 'text': capitals(p['text'])} for p in g['reading_text']]
    extra = []
    if wit == 'vinet':
        for p in paras:
            if 'Dia pason cum' in p['text']:
                p['text'] = p['text'].replace('Dia pason cum', 'Dia-pason cum', 1)
                extra.append({'ref': 'Vinet 48.23', 'printed': 'Dià pason', 'reading': 'Dia-pason',
                              'reason': 'hyphen omitted; the name is hyphenated everywhere else'})
        assert len(extra) == 1
    entry = {'witness': D['witness'], 'paragraphs': paras}
    if wit == 'xylander':
        entry['title'] = g['reading_title']
        entry['closing'] = g['reading_closing_formula']
        rt = [g['reading_title']['text']] + [p['text'] for p in paras] + [g['reading_closing_formula']['text']]
    else:
        entry['chapters'] = [dict(c, title=c['title'].replace('interuallis', 'intervallis')) for c in g['chapters']]
        rt = [p['text'] for p in paras]
    a, b = diplomatic_words(D['lines']), [f for t in rt for f in fold(t)]
    used = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        da, db = ' '.join(a[i1:i2]), ' '.join(b[j1:j2])
        for h in HEADINGS[wit]:  # chapter headings and the closing formula stand apart from the paragraphs
            da = da.replace(h, ' ').strip()
        da = re.sub(r'\s+', ' ', da)
        if da.replace(' ', '') == db.replace(' ', ''):
            continue  # word division
        rest = da
        for wrong, (right, ref, why, *_) in CORRECTIONS[wit].items():
            if re.search(rf'\b{wrong}\b', rest) and right in db:
                rest = re.sub(rf'\b{wrong}\b', '', rest)
                used.append(wrong)
        for h in HEADINGS[wit]:
            rest = rest.replace(h, '')
        rest = re.sub(r'\b(dia|pason|diapason)\b', '', rest).strip()
        assert not rest, (wit, da, db)
    assert sorted(set(used)) == sorted(CORRECTIONS[wit]), (wit, sorted(set(used)), sorted(CORRECTIONS[wit]))
    entry['corrections'] = [{'ref': ref, 'printed': shown, 'reading': reading_form, 'reason': why}
                            for wrong, (right, ref, why, shown, reading_form) in CORRECTIONS[wit].items()] + extra
    out[wit] = entry
    print(wit, len(paras), 'paragraphs,', len(entry['corrections']), 'corrections, all differences explained')
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
