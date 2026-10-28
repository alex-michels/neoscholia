"""Compare Claude's workflow-2 readings (H, Par./V collations, Vincent, Vinet) with GPT-6's.
Usage: python -I cmp_wf2.py <wf2 dir> <gpt greek json> <gpt latin json> <out dir> [h|coll|vincent|vinet ...]"""
import difflib, json, re, sys, unicodedata
from collections import Counter
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
wf2, gpt_gr, gpt_la, out = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4])
which = sys.argv[5:] or ['h', 'coll', 'vincent', 'vinet']
out.mkdir(exist_ok=True)
G = json.load(open(gpt_gr, encoding='utf-8'))
L = json.load(open(gpt_la, encoding='utf-8'))

def load(p):
    return json.load(open(p, encoding='utf-8')) if Path(p).exists() else None

def norm(s):
    s = unicodedata.normalize('NFC', s or '')
    s = re.sub(r'⟦r\s*|⟧', '', s)
    for a in ("'", 'ʼ', '᾽', '᾿', '‘'):
        s = s.replace(a, '’')
    s = s.replace('·', '·').replace(';', ';').replace('–', '-')
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\s+([,.;:·])', r'\1', s)
    return s

def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))

def kind(a, b):
    if strip_acc(a) == strip_acc(b):
        return 'diacritics'
    if strip_acc(a).replace(' ', '') == strip_acc(b).replace(' ', ''):
        return 'spacing'
    if re.sub(r'[^\w]', '', strip_acc(a)) == re.sub(r'[^\w]', '', strip_acc(b)):
        return 'punctuation/signs'
    if re.sub(r'[^\w]', '', strip_acc(a)).replace('(', '') == re.sub(r'[^\w]', '', strip_acc(b)):
        return 'expansion'
    return 'letters/words'

def linediff(claude, gpt, label, fname):
    keys = sorted(set(claude) | set(gpt))
    rows, same, kinds = [], 0, Counter()
    for k in keys:
        a, b = norm(claude.get(k)), norm(gpt.get(k))
        if a == b:
            same += 1
            continue
        kd = 'missing' if not a or not b else kind(a, b)
        kinds[kd] += 1
        sm = difflib.SequenceMatcher(None, a, b)
        ops = [f"«{a[i1:i2]}»→«{b[j1:j2]}»" for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
        rows.append({'ref': f'{label} {k[0]}.{k[1]}', 'kind': kd, 'claude': claude.get(k), 'gpt': gpt.get(k), 'ops': ops})
    json.dump({'same': same, 'total': len(keys), 'kinds': kinds, 'diffs': rows}, open(out / fname, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'== {label}: lines {len(keys)} (Claude {len(claude)}, GPT {len(gpt)}), identical {same}, different {len(rows)}', dict(kinds))
    for r in rows:
        if r['kind'] in ('letters/words', 'missing'):
            print(' ', r['ref'], '|', '; '.join(r['ops'])[:200])

if 'h' in which:
    claude = {}
    for a in ('h-a', 'h-b', 'h-c'):
        d = load(wf2 / a / f'{a}.json')
        if not d:
            print('!! missing', a)
            continue
        for f in d['folios']:
            for l in f['lines']:
                claude[(f['folio'], l['n'])] = l['text']
    gpt = {(f['folio'], l['n']): l['text'] for f in G['h']['folios'] for l in f['lines']}
    folios = {k[0] for k in claude}
    gpt = {k: v for k, v in gpt.items() if k[0] in folios}
    linediff(claude, gpt, 'H', 'cmp-h.json')

if 'vinet' in which:
    claude = {}
    for a in ('vinet-1', 'vinet-2'):
        d = load(wf2 / a / f'{a}.json')
        for p in d['pages']:
            for l in p['lines']:
                claude[(p['page'], l['n'])] = l['text']
    gpt = {(p['page'], l['n']): l['text'] for p in L['vinet']['pages'] for l in p['lines']}
    linediff(claude, gpt, 'Vinet', 'cmp-vinet.json')

if 'vincent' in which:
    d = load(wf2 / 'vincent' / 'vincent.json')
    claude = {(p['page'], l['n']): l['text'] for p in d['pages'] for l in p['lines']}
    gpt = {}
    for fr in G['p_fragments']:
        for l in fr['lines']:
            pg, n = l['ref'].split()[1].split('.')
            gpt[(int(pg), int(n))] = l['text']
    linediff(claude, gpt, 'Vinc.', 'cmp-vincent.json')
    cn = {n['ref']: n['text'] for p in d['pages'] for n in p['footnotes']}
    gn = {n['ref']: n['text'] for fr in G['p_fragments'] for n in fr['footnotes']}
    print('  footnotes:', len(cn), 'vs', len(gn))
    for r in sorted(set(cn) | set(gn)):
        if norm(cn.get(r)) != norm(gn.get(r)):
            print('  ', r, '| C:', cn.get(r), '| G:', gn.get(r))

def refkey(r):
    m = re.match(r'Bas\. (\d+)\.(\d+)', (r or '').replace('–', '-'))
    return (int(m[1]), int(m[2])) if m else None

def wit(s):
    return re.sub(r'\s*\((?:Par|V|H)\.? [^)]*\)\s*$', '', s or '').strip()

if 'coll' in which:
    for w, fn in (('Par', 'par/par-collation.json'), ('V', 'v/v-collation.json')):
        d = load(wf2 / fn)
        if not d:
            print('!! missing', fn)
            continue
        c = [(refkey(e['ref']), e) for e in d['collation']]
        g = [(refkey(e['ref']), e) for e in G['collation'] if e.get(w) and not wit(e[w]).startswith('= Bas')]
        used, rows = set(), []
        for k, e in c:
            m = [i for i, (gk, ge) in enumerate(g) if gk and k and abs(gk[0] * 100 + gk[1] - k[0] * 100 - k[1]) <= 1 and i not in used]
            if m:
                used.add(m[0])
                ge = g[m[0]][1]
                same = norm(strip_acc(re.sub(r'[()]', '', e['reading']))) == norm(strip_acc(re.sub(r'[()]', '', wit(ge[w]))))
                rows.append({'status': 'both, same' if same else 'both, differ', 'ref': e['ref'], 'lemma': e['lemma'], 'claude': e['reading'], 'gpt': ge[w], 'gpt_id': ge['id']})
            else:
                rows.append({'status': 'Claude only', 'ref': e['ref'], 'lemma': e['lemma'], 'claude': e['reading'], 'claude_note': e.get('note')})
        for i, (gk, ge) in enumerate(g):
            if i not in used:
                rows.append({'status': 'GPT only', 'ref': ge['ref'], 'lemma': ge['lemma'], 'gpt': ge[w], 'gpt_id': ge['id'], 'gpt_note': ge.get('note')})
        rows.sort(key=lambda r: refkey(r['ref']) or (0, 0))
        json.dump({'witness': w, 'rows': rows, 'claude_bas_corrections': d.get('bas_corrections'), 'claude_three_places': d.get('three_places')},
                  open(out / f'cmp-coll-{w.lower()}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'== {w} collation:', dict(Counter(r['status'] for r in rows)))
        for r in rows:
            if r['status'] != 'both, same':
                print(' ', r['status'], '|', r['ref'], '|', r['lemma'], '| C:', r.get('claude'), '| G:', r.get('gpt'))
