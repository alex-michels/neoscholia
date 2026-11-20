"""Build latin-texts.json, the text file of the translation package for the two Latin versions (Xylander 1556,
Vinet 1591): the reading text cut into segments that follow the units of the Greek text (alignment.json), each with
its page.line range and the printed lines it covers (agreed diplomatic transcription), plus the corrections.
Checks that the segments reproduce the reading text exactly.
The labels that tie the segments to the Greek units stay out of the package (they would show where the Greek has
passages that the Latin lacks); they are written to a separate segment map.
Usage: python -I build_package.py <synopsis-musicae folder> <alignment.json> <out latin-texts.json> <out segment-map.json>"""
import difflib, json, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
R, ALIGN, OUT, MAP = sys.argv[1:5]
reading = json.load(open(f'{R}/latin-translations/reading-texts.json', encoding='utf-8'))
align = json.load(open(ALIGN, encoding='utf-8'))
SRC = {'xylander': ('Xyl.', 'xylander1556-latin.json', 'X'), 'vinet': ('Vinet', 'vinet1591-latin.json', 'V')}


def fold(s):
    s = s.replace('æ', 'ae').replace('Æ', 'ae').replace('œ', 'oe').replace('Œ', 'oe').replace('ę', 'e')
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))
    return re.findall(r'[a-z0-9]+', s.lower().replace('v', 'u').replace('j', 'i'))


def diplomatic_tokens(lines):
    """Folded tokens of the printed text, each with the lines where its word begins and ends."""
    out, carry = [], None
    for li, ln in enumerate(lines):
        toks = ln['text'].split()
        for i, w in enumerate(toks):
            if carry is not None and i == 0:
                w, start = carry[0] + w, carry[1]
                carry = None
            else:
                start = li
            if i == len(toks) - 1 and w.endswith('-') and len(w) > 1:
                carry = (w[:-1], start)
                continue
            out += [(f, (start, li)) for f in fold(w)]
    if carry:
        out += [(f, (carry[1], carry[1])) for f in fold(carry[0])]
    return out


def blocks_of(wit):
    w = reading[wit]
    if wit == 'xylander':
        b = [('title', w['title']['text'])] + [(f"para {p['para']}", p['text']) for p in w['paragraphs']] + [('closing', w['closing']['text'])]
    else:
        chap = {c['chapter']: c for c in w['chapters']}
        b, seen = [('title', 'Michaelis Pselli Musica.')], set()
        for p in w['paragraphs']:
            c = p['para'].split('.')[0]
            if c not in seen:
                seen.add(c)
                b.append((f'chapter {c}', f"Caput {c}. {chap[c]['title']}"))
            b.append((p['para'], p['text']))
        b.append(('closing', 'Finis Musicae.'))
    return b


norm = lambda s: re.sub(r'\s+', ' ', s).strip()
pkg = {'note': 'Two Latin versions of the music section, cut into segments; see about.md, section 3.'}
segmap = []
for wit, (sig, src, letter) in SRC.items():
    lines = json.load(open(f'{R}/transcriptions/{src}', encoding='utf-8'))['lines']
    dip = diplomatic_tokens(lines)
    segs = align[wit]['segments']
    blocks = blocks_of(wit)
    # 1. the segments reproduce every block exactly, in order
    order = [s['block'] for s in segs]
    assert [b for b, _ in blocks] == list(dict.fromkeys(order)), (wit, 'block order')
    for name, text in blocks:
        joined = norm(' '.join(s['text'] for s in segs if s['block'] == name))
        assert joined == norm(text), (wit, name)
    # 2. map reading tokens to printed lines
    red, owner = [], []
    for k, s in enumerate(segs):
        for f in fold(s['text']):
            red.append(f)
            owner.append(k)
    a = [t for t, _ in dip]
    pos = [None] * len(red)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=red, autojunk=False).get_opcodes():
        for j in range(j1, j2):
            if op == 'equal':
                pos[j] = dip[i1 + (j - j1)][1]
            elif i2 > i1:  # a word divided or corrected: the whole printed span
                pos[j] = (dip[i1][1][0], dip[i2 - 1][1][1])
            else:
                pos[j] = dip[min(i1, len(dip) - 1)][1]
    out = []
    for k, s in enumerate(segs):
        idx = [pos[j] for j in range(len(red)) if owner[j] == k and pos[j] is not None]
        first, last = (min(i[0] for i in idx), max(i[1] for i in idx)) if idx else (None, None)
        if first is None:  # headings and the like that are not in the diplomatic word stream
            m = [i for i, ln in enumerate(lines) if norm(ln['text']).lower().startswith(norm(s['text']).lower()[:12])]
            first = last = m[0] if m else 0
        L = lines[first:last + 1]
        ref = f"{sig} {L[0]['page']}.{L[0]['line']}" + ('' if len(L) == 1 else
              f"–{L[-1]['line']}" if L[-1]['page'] == L[0]['page'] else f"–{L[-1]['page']}.{L[-1]['line']}")
        seg = {'id': f'{letter}{k + 1:02d}'}
        if s['block'].startswith('chapter'):
            seg['heading'] = True
        elif k == 0 or segs[k - 1]['block'] != s['block']:
            b = s['block'].replace('para ', '')
            seg['starts_paragraph'] = {'title': 'title', 'closing': 'closing formula'}.get(b, b)
        seg.update({'ref': ref, 'latin': norm(s['text']),
                    'printed': [{'ref': f"{L_['page']}.{L_['line']}", 'text': L_['text']} for L_ in L]})
        out.append(seg)
        segmap.append({'id': seg['id'], 'units': s['units'], 'note': s.get('note', '')})
    entry = {'version': reading[wit]['witness'], 'segments': out, 'corrections': reading[wit]['corrections']}
    if wit == 'vinet':
        entry['chapters'] = reading[wit]['chapters']
    pkg[wit] = entry
    covered = {p['ref'] for s_ in out for p in s_['printed']}
    missing = [f"{l['page']}.{l['line']}" for l in lines if f"{l['page']}.{l['line']}" not in covered]
    assert not missing, (wit, 'printed lines in no segment', missing)
    print(wit, len(out), 'segments; every printed line in a segment')
json.dump(pkg, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'note': 'segment id -> units of the Greek text (alignment.json); not given to the translators', 'segments': segmap},
          open(MAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
