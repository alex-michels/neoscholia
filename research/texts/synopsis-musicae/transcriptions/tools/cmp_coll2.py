"""Check every Par./V variant claimed by either side against the other side's evidence.
GPT's claims are checked against Claude's full line transcriptions of Par. and V (made by the collators);
Claude's claims that GPT does not list are checked against GPT's own Basel text (if GPT's Bas. already reads so, it is a Basel question).
Usage: python -I cmp_coll2.py <wf2 dir> <gpt greek json> <out json>"""
import ast, json, re, sys, unicodedata
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
wf2, gpt_path, out_path = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
G = json.load(open(gpt_path, encoding='utf-8'))

def core(s):
    s = unicodedata.normalize('NFD', s or '')
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'⟦r\s*|⟧|\[\?\]|\[|\]|[()\-\s.,·:;’\'᾽†+※*]', '', s).lower()
    return s.replace('ς', 'σ').replace('ϲ', 'σ')

# Claude's full witness transcriptions
wit = {'Par': {}, 'V': {}}
tree = ast.parse(open(wf2 / 'par' / 'build.py', encoding='utf-8').read())
pages = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'pages')
for f, txt in pages.items():
    for i, l in enumerate(txt.split('\n'), 1):
        wit['Par'][(f, i)] = l
for l in open(wf2 / 'v' / 'v-lines.txt', encoding='utf-8'):
    if '\t' in l:
        r, t = l.rstrip('\n').split('\t', 1)
        f, n = r.split('.')
        wit['V'][(f, int(n))] = t
order = {w: sorted(d) for w, d in wit.items()}
fol_key = lambda f: (int(f[:-1]), f[-1])
for w in order:
    order[w].sort(key=lambda k: (fol_key(k[0]), k[1]))

def window(w, refstr, pad=0):
    """Text of the witness lines named in e.g. '78v.6–7' or '79r.21–79v.1', joined with line-end hyphens removed."""
    m = re.findall(r'(\d+[rv])\.(\d+)', refstr)
    if not m:
        return None
    a = (m[0][0], int(m[0][1]))
    b = (m[-1][0], int(m[-1][1]))
    m2 = re.search(r'\d+[rv]\.\d+\s*[–-]\s*(\d+)(?![rv\d.])', refstr)
    if m2 and len(m) == 1:
        b = (a[0], int(m2[1]))
    keys = order[w]
    try:
        i, j = keys.index(a), keys.index(b)
    except ValueError:
        return None
    return ' '.join(wit[w][k] for k in keys[max(0, i - pad): j + 1 + pad])

gbas = {(p['page'], l['n']): l['text'] for p in G['bas']['pages'] for l in p['lines']}
def gbas_text(ref, pad=1):
    m = re.match(r'Bas\. (\d+)\.(\d+)', ref.replace('–', '-'))
    pg, ln = int(m[1]), int(m[2])
    return ' '.join(gbas.get((pg, x), '') for x in range(ln - pad, ln + pad + 2))

rows = []
for w, fn in (('Par', 'par/par-collation.json'), ('V', 'v/v-collation.json')):
    claude = json.load(open(wf2 / fn, encoding='utf-8'))['collation']
    gclaims = []
    for e in G['collation']:
        s = e.get(w)
        if not s or s.strip().startswith('= Bas'):
            continue
        m = re.match(r'(.*?)\s*\((?:Par\.|V) ([^)]*)\)\s*$', s)
        reading, wref = (m[1], m[2]) if m else (s, '')
        win = window(w, wref)
        win2 = window(w, wref, pad=1)
        r = re.sub(r'\[\?\]', '', reading).strip()
        if r.startswith('om.'):
            ok = win is not None and core(e['lemma']) not in core(win2)
        else:
            ok = win is not None and core(r) in core(win2)
        gclaims.append({'w': w, 'ref': e['ref'], 'lemma': e['lemma'], 'gpt': reading, 'wref': wref, 'claude_line': win,
                        'status': 'agree (Claude transcription has it)' if ok else 'DISPUTE: Claude transcription differs', 'gpt_id': e['id'], 'gpt_note': e.get('note')})
    rows += gclaims
    for e in claude:
        wl = window(w, e['witness_ref'], pad=0) or ''
        # does GPT list a claim for this witness here with the same reading?
        same = [g for g in gclaims if core(e['reading']).find(core(re.sub(r'\[\?\]', '', g['gpt']))) >= 0 and g['ref'].split('.')[1][:2] == e['ref'].split('.')[1][:2] and g['ref'].split()[1].split('.')[0] == e['ref'].split()[1].split('.')[0]]
        if same:
            continue
        gb = gbas_text(e['ref'])
        st = 'Basel question (GPT Bas. already reads so)' if core(e['reading']) in core(gb) or core(e['reading'].split('|')[0])[:12] in core(gb) else 'DISPUTE: GPT does not list it'
        rows.append({'w': w, 'ref': e['ref'], 'lemma': e['lemma'], 'claude': e['reading'], 'wref': e['witness_ref'], 'claude_line': wl, 'gpt_bas': gb,
                     'status': st, 'claude_note': e.get('note')})
json.dump(rows, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter((r['w'], r['status']) for r in rows))
for r in rows:
    if r['status'].startswith('DISPUTE') or r['status'].startswith('Basel'):
        print(f"{r['w']:3} {r['status'][:30]:30} | {r['ref']} | {r['lemma']} | G: {r.get('gpt')} | C: {r.get('claude')} | Cline({r['wref']}): {r['claude_line']}")
