"""Build anonymised places for the Greek adjudication workflow (wf3): Basel lines, H lines, Par./V collation disputes.
Each place has two readings in an order fixed by crc32 of its id; the key (which reading is whose) goes to a separate file.
Usage: python -I prep_wf3.py <scratchpad dir>"""
import difflib, json, re, sys, unicodedata, zlib
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
sp = Path(sys.argv[1])
SRC = str(Path(__file__).resolve().parents[2] / 'source')

def nfc(s):
    s = unicodedata.normalize('NFC', s or '')
    for a in ("'", 'ʼ', '᾽', '᾿', '‘'):
        s = s.replace(a, '’')
    return s.replace('·', '·').replace(';', ';')

def ops(a, b, strip_punct=False):
    if strip_punct:
        a, b = re.sub(r'\s*[.·,:;]\s*', ' ', a).strip(), re.sub(r'\s*[.·,:;]\s*', ' ', b).strip()
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t == 'equal':
            continue
        # widen to whole words for readability
        while i1 > 0 and j1 > 0 and a[i1 - 1] != ' ' and b[j1 - 1] != ' ':
            i1 -= 1; j1 -= 1
        while i2 < len(a) and j2 < len(b) and a[i2] != ' ' and b[j2] != ' ':
            i2 += 1; j2 += 1
        out.append(f'(1) «{a[i1:i2]}»  /  (2) «{b[j1:j2]}»')
    return list(dict.fromkeys(out))

def place(pid, group, src_file, ref, a, b, a_who, b_who, context='', question='', strip_punct=False):
    a, b = nfc(a), nfc(b)
    swap = zlib.crc32(pid.encode()) % 2 == 1
    r1, r2, w1, w2 = (b, a, b_who, a_who) if swap else (a, b, a_who, b_who)
    p = {'id': pid, 'ref': ref, 'image': src_file, 'reading_1': r1, 'reading_2': r2,
         'differences': ops(r1, r2, strip_punct)}
    if context:
        p['context'] = context
    if question:
        p['question'] = question
    groups.setdefault(group, []).append(p)
    key[pid] = {'1': w1, '2': w2}

groups, key = {}, {}
bas_img = lambda pg: f'{SRC}/basel1556/gr-seq{189 + pg - 23}-p{pg}.jpg'
H_FOL = ['64r', '64v', '65r', '65v', '66r', '66v', '67r', '67v', '68r', '68v', '69r', '69v', '70r']
h_img = lambda f: f'{SRC}/pal-gr-281/cpgraec281_{137 + H_FOL.index(f):04d}-f{f}.jpg'
def par_img(f):
    n, s = int(f[:-1]), f[-1]
    return f'{SRC}/paris1545/gr-scan{2 * n - 1 if s == "r" else 2 * n:04d}.jpg'
def v_img(f):
    n, s = int(f[:-1]), f[-1]
    sc = 155 + 2 * (n - 75) + (s == 'v')
    return f'{SRC}/vat-pal-gr-262/Pal.gr.262_0{sc}_fa_00{n}{s}_m.jpg'

# 1. Basel: 67 line differences
bas = json.load(open(Path(__file__).resolve().parents[1] / 'basel1556-greek-comparison.json', encoding='utf-8'))
for r in bas['diffs']:
    pg, ln = map(int, r['ref'].split()[1].split('.'))
    place(r['ref'], 'bas-a' if pg <= 27 else 'bas-b', bas_img(pg), r['ref'], r['claude'], r['gpt'], 'claude', 'gpt')
# Basel places raised by the collators (both transcriptions agree, a collator disagrees)
place('Bas. 33.15', 'bas-b', bas_img(33), 'Bas. 33.15', 'καὶ ταῖς σχολαιοτέραις καὶ ταχιναῖς μετα-', 'καὶ ταῖς χολαιοτέραις καὶ ταχιναῖς μετα-', 'both', 'collator')
place('Bas. 31.23 margin', 'bas-b', bas_img(31), 'Bas. 31.23, margin', 'no marginal note beside this line', '«* ἡ» in the margin (a correction of ἢ in the text)', 'both', 'collator',
      question='Is there a printed marginal note beside line 31.23, and if so what exactly does it read? (In the text the line begins «* ἢ ἁρμονία».)')
place('Bas. 32.23 margin', 'bas-b', bas_img(32), 'Bas. 32.23, margin', 'no marginal note beside this line', '«* τοῦ» in the margin (a correction of τὸ in the text)', 'both', 'collator',
      question='Is there a printed marginal note beside line 32.23, and if so what exactly does it read? (In the text the line has «* τὸ τετραχόρδου».)')

# 2. H: lines differing in letters, accents or breathings (punctuation-only differences are not judged)
cmp_h = json.load(open(sp / 'wf3' / 'cmp-h.json', encoding='utf-8'))
for r in cmp_h['diffs']:
    if r['kind'] in ('punctuation/signs', 'spacing'):
        continue
    f, n = r['ref'].split()[1].split('.')
    grp = 'h-a' if H_FOL.index(f) <= H_FOL.index(sys.argv[2] if len(sys.argv) > 2 else '66r') else 'h-b'
    # the manuscript has no hyphens: one side marks a line-end word break with '-', the other does not
    place(r['ref'], grp, h_img(f), r['ref'], r['claude'].rstrip().rstrip('-'), r['gpt'].rstrip().rstrip('-'), 'claude', 'gpt', strip_punct=True)

# 3. Par./V collation disputes (witness readings at one place)
COLL = [
    ('Par', '21r.19-20', 'Bas. 24.23', 'εἰ δ’ μὴ οὕτως ἐκφωνηθείη', 'εἰ γὰρ μὴ', 'εἰ δ’ μὴ', 'the word after εἰ (a compendium sort?)'),
    ('Par', '21v.18', 'Bas. 25.14', 'ὃν γὰρ λόγον ὁ πρῶτος', 'ὃν γὰρ λόγον', 'ὃν δὲ λόγον', ''),
    ('Par', '23r.16', 'Bas. 27.16', 'ταῦτα δὲ οὐκ ἄμεσα', 'οὐκ ἄμεσα', 'οὐκ ἀμερῆ', ''),
    ('Par', '23v.4-5', 'Bas. 27.24', 'ὡς διὰ πέντε χορδίων περαινόμενον', 'περαινόμενον', 'περαινούμενον', ''),
    ('Par', '23v.7', 'Bas. 28.1', 'ὡς δι’ ὀκτὼ τελούμενον', 'τελειούμενον', 'τελούμενον', ''),
    ('Par', '27r.16', 'Bas. 33.12', 'ὧν ἐφ’ ἑκάστῳ παιῶν, ὑμέναιος', 'παιήων', 'παιάν', ''),
    ('Par', '26r.12', 'Bas. 31.23', '* ἢ ἁρμονία συνέχεται', 'ἡ ἁρμονία (article)', 'ἢ ἁρμονία (particle)', 'breathing and accent on η'),
    ('V', '75r.19', 'Bas. 23.10', 'κἂν τεχνητὸν εἴη', 'τεχνητὸν', 'τεχνικὸν', ''),
    ('V', '75v.8', 'Bas. 24.5', 'τοῦ παντὸς ὀνομάζει/ὀνομάσοι', 'ὀνομάσοι', 'ὀνομάζοι', 'σ or ζ'),
    ('V', '76r.13', 'Bas. 24.25', 'οὐδ’ ἂν φθόγγος ὅλως καλοῖτο', 'ὅλως', 'ὅμως', ''),
    ('V', '76v.17', 'Bas. 25.20', 'διπλῆν ἔχον ἐπὶ τὸ ὀξὺ', 'διπλῆν', 'διπλῶν', ''),
    ('V', '79r.3', 'Bas. 28.15', 'ἠπίως πρῶτον καὶ εὐρύθμως', 'ἠπίως πῶς καὶ εὐρύθμως', 'ἠπίως πως καὶ ἐῤῥύθμως', ''),
    ('V', '79r.16', 'Bas. 29.1', 'καθ’ ἑαυτὰ θεωρούμενα', 'καθ’ ἑαυτὰ', 'καθ’ ἑαυτὸ', ''),
    ('V', '80r.9-10', 'Bas. 30.3', 'λόγον ἡμιόλιον ἔχον', 'ἔχων', 'ἔχον', ''),
    ('V', '80r.12', 'Bas. 30.5', 'ὧν ἔχει πρὸς τοὺς πρὸ αὐτοῦ', 'ἣν ἔχει πρὸς τοὺς αὐτοῦ', 'ὧν ἔχει πρὸς τοὺς αὐτοῦ', ''),
    ('V', '80v.10', 'Bas. 30.20', 'ἐπὶ δὲ τῶν ἐμπνευστῶν', 'πὶ δὲ (the initial ε, meant to be painted in red, missing)', 'τῇ δὲ', 'the first word of the line'),
    ('V', '81v.1', 'Bas. 31.23', '* ἢ ἁρμονία συνέχεται', 'ἡ ἁρμονία (article)', 'ἢ ἁρμονία (particle)', 'breathing and accent on η'),
    ('V', '81v.2', 'Bas. 31.24', 'ἀπερτίζεται μέλος', 'ἀπαρτίζεται', 'καταρτίζεται', ''),
    ('V', '81v.4', 'Bas. 31.25-32.1', 'τῆς ἁρμονίας προφέρεται', 'προφέρεται', 'περιφέρεται', ''),
    ('V', '81v.8', 'Bas. 32.4', 'ἀπήρτισται', 'ἀπήρτισται', 'ἀπήρτιται', ''),
    ('V', '81v.9', 'Bas. 32.5', 'ἡμιτονίῳ διείληπται', 'διείρηπται', 'διείληπται', 'λ or ρ'),
    ('V', '82r.11', 'Bas. 32.23', 'περὶ τὰ διαστήματα τοῦ', 'περὶ τὰ διαστήματα', 'περὶ τὸ διάστημα', ''),
]
for w, wref, bref, bas_words, c, g, note in COLL:
    f = wref.split('.')[0]
    img = par_img(f) if w == 'Par' else v_img(f)
    place(f'{w} {wref}', 'coll', img, f'{"Par." if w == "Par" else "V"} {wref} (= {bref})', c, g, 'claude', 'gpt',
          context=f'The Basel print reads here: «{bas_words}». Decide what THIS witness has.' + (f' Look at: {note}.' if note else ''))

for g, ps in groups.items():
    ps.sort(key=lambda p: p['id'])
json.dump({'groups': groups}, open(sp / 'wf3' / 'places.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(key, open(sp / 'wf3' / 'places-key.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({g: len(v) for g, v in groups.items()}, 'total', sum(len(v) for v in groups.values()))
missing = [p['image'] for v in groups.values() for p in v if not Path(p['image']).exists()]
print('missing images:', sorted(set(missing)))
