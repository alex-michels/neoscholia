"""Add the third reviewer (GPT-6 Astra, Codex format) to merged.json: its unit data, and its errors matched to the errors
already found by Claude and Sol (same unit and translator, overlapping wording, as in merge_comparisons.py).
Writes merged3.json (errors get 'found_by': sorted list of reviewers) and prints the statistics.
Usage: python -I merge_astra.py <ws-cmp folder> <astra comparison.json>"""
import collections, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
O, AF = sys.argv[1], sys.argv[2]
M = json.load(open(f'{O}/merged.json', encoding='utf-8'))
A = {u['id']: u for u in json.load(open(AF, encoding='utf-8'))['units']}
assert sorted(A) == sorted(M)


def words(s):
    return set(re.findall(r'\w{3,}', (s or '').lower()))


def label(x):
    m = re.findall(r'\b([A-F])\b', x or '')
    return m[0] if m else (x or '').strip()


def ws_of(e):
    return words(e.get('quote')) | words(e.get('problem'))


stats, per = collections.Counter(), collections.Counter()
for uid, u in M.items():
    a = A[uid]
    u['astra'] = {k: a.get(k) for k in ('sense', 'divergences', 'text_issues_review', 'notes_to_keep', 'editor_questions')}
    u['astra']['best_ru'] = (a.get('best_ru') or {}).get('translator')
    u['astra']['best_en'] = (a.get('best_en') or {}).get('translator')
    for e in u['errors']:
        e['found_by'] = sorted(['claude', 'sol'] if e['who'] == 'both' else [e['who']])
    used = set()
    for x in a.get('errors') or []:
        x = dict(x, translator=label(x.get('translator')))
        best, score = None, 0.0
        for j, e in enumerate(u['errors']):
            if e['translator'] != x['translator'] or j in used:
                continue
            for r in ('claude', 'sol'):
                if e.get(r):
                    b = ws_of(e[r])
                    s = len(ws_of(x) & b) / max(1, min(len(ws_of(x)), len(b)))
                    if s > score:
                        best, score = j, s
        if best is not None and score >= 0.34:
            used.add(best)
            u['errors'][best]['astra'] = x
            u['errors'][best]['found_by'] = sorted(u['errors'][best]['found_by'] + ['astra'])
        else:
            u['errors'].append({'who': 'astra', 'translator': x['translator'], 'astra': x, 'found_by': ['astra']})
    for e in u['errors']:
        sev = max((e[r].get('severity') for r in ('claude', 'sol', 'astra') if e.get(r)), key=lambda s: s == 'major')
        e['severity_max'] = sev
        stats[('+'.join(e['found_by']), sev)] += 1

json.dump(M, open(f'{O}/merged3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('errors by finders and the highest severity given:')
for k, v in sorted(stats.items(), key=lambda z: (-len(z[0][0]), z[0])):
    print(f'  {k[0]:20} {k[1]:6} {v}')

print('\nmajor errors found by one reviewer only, and whether the others saw them:')
for uid, u in M.items():
    for e in u['errors']:
        if len(e['found_by']) == 1 and e['severity_max'] == 'major':
            r = e['found_by'][0]
            x = e[r]
            print(f"  {uid} {e['translator']} [{r}] {(x.get('quote') or '')[:70]} — {(x.get('problem') or '')[:150]}")
print('\nmajor errors found by Astra and one other reviewer:')
for uid, u in M.items():
    for e in u['errors']:
        if len(e['found_by']) == 2 and 'astra' in e['found_by'] and e['severity_max'] == 'major':
            print(f"  {uid} {e['translator']} {e['found_by']} {(e['astra'].get('problem') or '')[:120]}")
