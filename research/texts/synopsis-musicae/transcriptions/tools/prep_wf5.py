"""Second round for H: every line difference the first round (wf3) did not judge.
- lines judged in wf3 (letters, with punctuation stripped): only their punctuation is still open -> one difference per punctuation slot;
- all other differing lines: every difference (accents, breathings, expansions, word division, punctuation).
Conventions applied before comparing (not judged): rubric crosses as '+', no line-end hyphen (the manuscript has none).
Usage: python -I prep_wf5.py <scratchpad dir>"""
import difflib, json, re, sys, unicodedata, zlib
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
sp = Path(sys.argv[1])
SRC = 'C:/Users/user/Documents/Projects/Neoscholia/research/texts/synopsis-musicae/source'
G = json.load(open('C:/Users/user/Documents/Projects/Neoscholia-runs/synopsis-musicae-greek/transcription-gpt-6-astra.json', encoding='utf-8'))
H_FOL = ['64r', '64v', '65r', '65v', '66r', '66v', '67r', '67v', '68r', '68v', '69r', '69v', '70r']
h_img = lambda f: f'{SRC}/pal-gr-281/cpgraec281_{137 + H_FOL.index(f):04d}-f{f}.jpg'
P = '.·,:;'

def nfc(s):
    s = unicodedata.normalize('NFC', s or '')
    for a in ("'", 'ʼ', '᾽', '᾿', '‘'):
        s = s.replace(a, '’')
    s = s.replace('·', '·').replace(';', ';').replace('†', '+')
    s = re.sub(r'-\s*$', '', s.rstrip())
    return re.sub(r'\s+', ' ', s).strip()

def ops(a, b):
    """Word-level differences: each run of differing words is one difference."""
    ta, tb = a.split(' '), b.split(' ')
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t != 'equal':
            out.append(f'(1) «{" ".join(ta[i1:i2]) or "—"}»  /  (2) «{" ".join(tb[j1:j2]) or "—"}»')
    return out

def slots(s):
    toks = re.findall(r'[^\s.·,:;]+|[.·,:;]+', s)
    words, after = [], []
    for t in toks:
        if re.fullmatch(r'[.·,:;]+', t):
            if words:
                after[-1] += t
            else:
                words.append(''); after.append(t)
        else:
            words.append(t); after.append('')
    return words, after

def wkey(w):
    w = unicodedata.normalize('NFD', re.sub(r'\([^)]*\)|\[\?\]|[⟦⟧]|^r ', '', w))
    return ''.join(c for c in w if c.isalpha() and not unicodedata.combining(c)).lower()

PNAME = {'.': 'low/middle point', '·': 'high point', ',': 'comma', ':': 'double point', ';': 'question mark', '': 'no punctuation'}
def punct_diffs(a, b):
    wa, pa = slots(a); wb, pb = slots(b)
    sm = difflib.SequenceMatcher(None, [wkey(w) for w in wa], [wkey(w) for w in wb], autojunk=False)
    out = []
    for blk in sm.get_matching_blocks():
        for i in range(blk.size):
            x, y = pa[blk.a + i], pb[blk.b + i]
            if x != y:
                w = wa[blk.a + i]
                out.append(f'punctuation after word {blk.a + i + 1} «{w}»: (1) «{x or "—"}» ({PNAME.get(x, x)})  /  (2) «{y or "—"}» ({PNAME.get(y, y)})')
    return out, (wa, pa), (wb, pb)

cl = {}
for f in ('h-a/h-a.json', 'h-b/h-b.json', 'h-c/h-c.json'):
    for fo in json.load(open(sp / 'wf2' / f, encoding='utf-8'))['folios']:
        for l in fo['lines']:
            cl[(fo['folio'], l['n'])] = l['text']
gp = {(fo['folio'], l['n']): l['text'] for fo in G['h']['folios'] for l in fo['lines']}
wf3 = json.load(open(sp / 'wf3' / 'places.json', encoding='utf-8'))['groups']
judged = {p['id'] for g in ('h-a', 'h-b') for p in wf3[g]}

groups, key, stats = {}, {}, {'punct-only': 0, 'all': 0}
for k in sorted(set(cl) | set(gp), key=lambda k: (int(k[0][:-1]), k[0][-1], k[1])):
    pid = f'H {k[0]}.{k[1]}'
    a, b = nfc(cl.get(k)), nfc(gp.get(k))
    if a == b:
        continue
    swap = zlib.crc32(pid.encode()) % 2 == 1
    if pid in judged:
        # letters were judged in round 1: ask only about punctuation; both readings shown with the same (reading-1) words
        if swap:
            a, b = b, a
        diffs, (wa, pa), (wb, pb) = punct_diffs(a, b)
        if not diffs:
            continue
        r1, r2 = a, b
        kind = 'punct-only'
        note = 'The letters of this line were already decided in an earlier round; judge ONLY the punctuation differences listed.'
    else:
        r1, r2 = (b, a) if swap else (a, b)
        diffs = ops(r1, r2)
        kind = 'all'
        note = ''
    stats[kind] += 1
    grp = 'h' + str(min(4, 1 + H_FOL.index(k[0]) * 4 // len(H_FOL)))  # four groups by folio
    p = {'id': pid, 'ref': pid, 'image': h_img(k[0]), 'reading_1': r1, 'reading_2': r2, 'differences': diffs}
    if note:
        p['context'] = note
    groups.setdefault(grp, []).append(p)
    key[pid] = {'1': 'gpt' if swap else 'claude', '2': 'claude' if swap else 'gpt'}

out = sp / 'wf5'
for g, ps in groups.items():
    for c in 'AB':
        d = out / f'{g}-{c}'
        d.mkdir(parents=True, exist_ok=True)
        json.dump({'group': g, 'places': ps}, open(d / 'places.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(key, open(out / 'places-key.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({g: (len(ps), sum(len(p['differences']) for p in ps)) for g, ps in groups.items()}, stats)
