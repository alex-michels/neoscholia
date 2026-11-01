"""Merge the two critical comparisons of the six translations (Claude workflow with verification; GPT-6.1 Sol in Codex) into one
per-unit file, and count agreement between them. Labels stay anonymous here (A-F); the key is applied only in the summary.
Usage: python -I merge_comparisons.py <ws-cmp folder>"""
import collections, json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
O = Path(sys.argv[1])
C = json.load(open(O / 'claude-comparison' / 'result.json', encoding='utf-8'))
C = C.get('result', C)
S = json.load(open(O / 'sol-comparison' / 'comparison.json', encoding='utf-8'))
KEY = json.load(open(O / 'private' / 'cmp-key.json', encoding='utf-8'))
RUNS = json.load(open(O / 'private' / 'runs-key.json', encoding='utf-8'))
MODEL = {L: RUNS['ws-' + f].split(' (')[0] for L, f in KEY.items()}
IDS = [f'U{i:03d}' for i in range(1, 68)]


def words(s):
    return set(w for w in re.findall(r'\w{3,}', (s or '').lower()))


def label(x):
    """'translator A', '[A]', 'A' -> 'A'."""
    m = re.findall(r'\b([A-F])\b', x or '')
    return m[0] if m else (x or '').strip()


# ---- Claude: findings with the verifier's verdicts applied
claude = {}
for g in C['groups']:
    found, ver = g['found'], g['verify'] or {}
    checks = collections.defaultdict(dict)
    for c in ver.get('checks', []):
        checks[c['unit']][c['item'].strip().lower()] = c
    for u in found['units']:
        cu = checks.get(u['id'], {})
        divs = []
        for i, d in enumerate(u['divergences'], 1):
            v = cu.get(f'divergence {i}', {})
            if v.get('verdict') == 'rejected':
                continue
            divs.append(dict(d, check=v.get('verdict', 'unchecked'), check_note=v.get('note'), correction=v.get('correction')))
        errs = []
        for i, e in enumerate(u['errors'], 1):
            v = cu.get(f'error {i}', {})
            if v.get('verdict') == 'rejected':
                continue
            errs.append(dict(e, translator=label(e['translator']), check=v.get('verdict', 'unchecked'), check_note=v.get('note'),
                             correction=v.get('correction')))
        for m in ver.get('missed', []):
            if m['unit'] == u['id']:
                errs.append({'translator': label(m['translator']), 'lang': '?', 'type': 'missed', 'severity': m['severity'],
                             'quote': '', 'problem': m['problem'], 'fix': m['fix'], 'check': 'added by verifier'})
        best = {}
        for k in ('best_ru', 'best_en'):
            v = cu.get(k)
            best[k] = (v.get('correction') or u[k]['translator']) if v and v.get('verdict') in ('modified', 'rejected') else u[k]['translator']
        claude[u['id']] = {'sense': u['sense'], 'divergences': divs, 'errors': errs, 'best_ru': best['best_ru'], 'best_en': best['best_en'],
                           'notes_to_keep': u['notes_to_keep'], 'editor_questions': u['editor_questions']}

# ---- Sol
sol = {}
for u in S['units']:
    sol[u['id']] = {'sense': u.get('sense'), 'divergences': u.get('divergences') or [],
                    'errors': [dict(e, translator=label(e.get('translator'))) for e in (u.get('errors') or [])],
                    'text_issues_review': u.get('text_issues_review') or [],
                    'best_ru': (u.get('best_ru') or {}).get('translator'), 'best_en': (u.get('best_en') or {}).get('translator'),
                    'notes_to_keep': u.get('notes_to_keep') or [], 'editor_questions': u.get('editor_questions') or []}
assert sorted(claude) == IDS and sorted(sol) == IDS


# ---- match errors between the two reviewers (same unit, same translator, overlapping wording)
def match(e, pool):
    best, score = None, 0.0
    a = words(e.get('quote')) | words(e.get('problem'))
    for j, f in enumerate(pool):
        if f['translator'] != e['translator'] or f.get('_used'):
            continue
        b = words(f.get('quote')) | words(f.get('problem'))
        s = len(a & b) / max(1, min(len(a), len(b)))
        if s > score:
            best, score = j, s
    return (best, score) if score >= 0.34 else (None, score)


merged, stats = {}, collections.Counter()
per_label = {L: collections.Counter() for L in 'ABCDEF'}
for uid in IDS:
    cu, su = claude[uid], sol[uid]
    pool = [dict(e) for e in su['errors']]
    errs = []
    for e in cu['errors']:
        j, s = match(e, pool)
        if j is not None:
            pool[j]['_used'] = True
            errs.append({'who': 'both', 'translator': e['translator'], 'claude': e, 'sol': pool[j]})
        else:
            errs.append({'who': 'claude', 'translator': e['translator'], 'claude': e})
    for f in pool:
        if not f.get('_used'):
            errs.append({'who': 'sol', 'translator': f['translator'], 'sol': f})
    for x in errs:
        sev = {(x.get('claude') or {}).get('severity'), (x.get('sol') or {}).get('severity')}
        major = 'major' in sev
        stats[(x['who'], 'major' if major else 'minor')] += 1
        per_label[x['translator']][(x['who'], 'major' if major else 'minor')] += 1
    merged[uid] = {'claude': cu, 'sol': su, 'errors': errs}

json.dump(merged, open(O / 'merged.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('errors: both / only Claude / only Sol (major, minor):')
for who in ('both', 'claude', 'sol'):
    print(f'  {who:7s} major {stats[(who, "major")]:3d}  minor {stats[(who, "minor")]:3d}')
print('\nper translator (label = model): both-major, Claude-only-major, Sol-only-major | all both/Claude-only/Sol-only')
for L in 'ABCDEF':
    p = per_label[L]
    tot = lambda w: p[(w, 'major')] + p[(w, 'minor')]
    print(f'  {L} = {MODEL[L]:18s} major {p[("both","major")]:2d} / {p[("claude","major")]:2d} / {p[("sol","major")]:2d}   all {tot("both"):3d} / {tot("claude"):3d} / {tot("sol"):3d}')


def labels_in(best):
    return set(re.findall(r'\b[A-F]\b', best or ''))


print('\nbest base, number of units where the label is (one of) the best: Claude ru / Sol ru | Claude en / Sol en')
for L in 'ABCDEF':
    cr = sum(L in labels_in(merged[u]['claude']['best_ru']) for u in IDS); sr = sum(L in labels_in(merged[u]['sol']['best_ru']) for u in IDS)
    ce = sum(L in labels_in(merged[u]['claude']['best_en']) for u in IDS); se = sum(L in labels_in(merged[u]['sol']['best_en']) for u in IDS)
    print(f'  {L} = {MODEL[L]:18s} {cr:2d} / {sr:2d} | {ce:2d} / {se:2d}')
agree_ru = sum(bool(labels_in(merged[u]['claude']['best_ru']) & labels_in(merged[u]['sol']['best_ru'])) for u in IDS)
agree_en = sum(bool(labels_in(merged[u]['claude']['best_en']) & labels_in(merged[u]['sol']['best_en'])) for u in IDS)
print(f'units where the two reviewers share a best label: ru {agree_ru}/67, en {agree_en}/67')
ed_c = sum(1 for u in IDS for d in merged[u]['claude']['divergences'] if d.get('to_editor'))
ed_s = sum(1 for u in IDS for d in merged[u]['sol']['divergences'] if str(d.get('to_editor')).lower() == 'true')
print(f'divergences to the editor: Claude {ed_c}, Sol {ed_s}; Claude divergences {sum(len(merged[u]["claude"]["divergences"]) for u in IDS)}, Sol {sum(len(merged[u]["sol"]["divergences"]) for u in IDS)}')
