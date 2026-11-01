"""Match the divergences and the terms of the two comparisons (Claude workflow, GPT-6.1 Sol) and sort them for the editor.
Divergences are matched within a unit by the overlap of their Greek words (accents removed, words cut to a stem);
terms by the same rule over the whole text. Writes reconcile.json next to merged.json.
Usage: python -I reconcile.py <ws-cmp folder>"""
import json, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
O = sys.argv[1]
M = json.load(open(f'{O}/merged.json', encoding='utf-8'))
CT = json.load(open(f'{O}/claude-comparison/result.json', encoding='utf-8'))['result']['terms']['terms']
ST = json.load(open(f'{O}/sol-comparison/comparison.json', encoding='utf-8'))['terms']


def gk(s, n=5):
    """Greek words of s without accents, cut to n letters."""
    s = unicodedata.normalize('NFD', s or '').lower()
    s = ''.join(c for c in s if not unicodedata.combining(c)).replace('ς', 'σ')
    return {w[:n] for w in re.findall(r'[α-ω]+', s) if len(w) > 2 or w in ('ου', 'μη')}


def ws(s, n=5):
    """Russian or English words of s, cut to n letters."""
    s = re.sub(r'\([^)]*\)', ' ', (s or '').lower())
    return {w[:n] for w in re.findall(r'[a-zа-яё]+', s) if len(w) > 2}


def ov(a, b):
    return len(a & b) / min(len(a), len(b)) if a and b else 0.0


def jac(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0


def readings(d):
    out = []
    for r in d.get('readings') or []:
        out.append({'translators': r.get('translators'), 'construal': r.get('construal'),
                    'ru': r.get('ru') or '; '.join(q.get('ru', '') for q in r.get('quotes') or [])[:400],
                    'en': r.get('en') or '; '.join(q.get('en', '') for q in r.get('quotes') or [])[:400]})
    return out


def side(d, who):
    x = {k: d.get(k) for k in ('issue', 'verdict', 'evidence', 'confidence', 'to_editor', 'recommended_ru', 'recommended_en')}
    x['greek'] = d.get('greek')
    x['readings'] = readings(d)
    if who == 'claude':
        x['check'] = d.get('check'); x['check_note'] = d.get('check_note'); x['correction'] = d.get('correction')
    else:
        x['second_pass'] = d.get('second_pass')
    return x


def status(c, s):
    if c and s:
        same = jac(ws(c.get('recommended_ru')), ws(s.get('recommended_ru'))) >= 0.5 or \
               jac(ws(c.get('recommended_en')), ws(s.get('recommended_en'))) >= 0.5
        if c.get('to_editor') or s.get('to_editor'):
            return 'both-editor' if same else 'both-differ-editor'
        return 'both-agree' if same else 'both-differ'
    one = c or s
    return ('claude' if c else 'sol') + ('-editor' if one.get('to_editor') else '')


div = {}
for uid, u in M.items():
    cl = [side(d, 'claude') for d in u['claude']['divergences']]
    so = [side(d, 'sol') for d in u['sol']['divergences']]
    pairs, used = [], set()
    for c in cl:
        best, bi = 0.0, None
        for i, s in enumerate(so):
            if i in used:
                continue
            o = ov(gk(c['greek']), gk(s['greek']))
            if o > best:
                best, bi = o, i
        if bi is not None and best >= 0.5:
            used.add(bi)
            pairs.append({'claude': c, 'sol': so[bi], 'overlap': round(best, 2)})
        else:
            pairs.append({'claude': c, 'sol': None})
    pairs += [{'claude': None, 'sol': s} for i, s in enumerate(so) if i not in used]
    for p in pairs:
        p['status'] = status(p['claude'], p['sol'])
    div[uid] = pairs


def tside(t):
    return {k: t.get(k) for k in ('greek', 'units', 'renderings', 'recommended_ru', 'recommended_en', 'why', 'evidence', 'to_editor')}


terms, used = [], set()
for c in CT:
    best, bi = 0.0, None
    for i, s in enumerate(ST):
        if i in used:
            continue
        o = jac(gk(c['greek'], 9), gk(s['greek'], 9))
        if o > best:
            best, bi = o, i
    if bi is not None and best >= 0.5:
        used.add(bi)
        terms.append({'claude': tside(c), 'sol': tside(ST[bi])})
    else:
        terms.append({'claude': tside(c), 'sol': None})
terms += [{'claude': None, 'sol': tside(s)} for i, s in enumerate(ST) if i not in used]
for t in terms:
    t['status'] = status(t['claude'], t['sol'])

json.dump({'divergences': div, 'terms': terms}, open(f'{O}/reconcile.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import collections
print('divergences:', collections.Counter(p['status'] for ps in div.values() for p in ps))
print('terms:', collections.Counter(t['status'] for t in terms))
