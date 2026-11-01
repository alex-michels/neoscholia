"""Dump the verified finals of the term research (workflow result) as markdown, one section per card.
Usage: python -I dump_term_finals.py <ws-cmp folder> <out.md> [card ids...]"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
O, OUT, ONLY = sys.argv[1], sys.argv[2], set(sys.argv[3:])
r = json.load(open(f'{O}/terms-research/workflow-output.txt', encoding='utf-8'))['result']
out = []
for g in r['groups']:
    for c in g['verify']['checks']:
        if ONLY and c['id'] not in ONLY:
            continue
        f = c['final']
        out.append(f"## {c['id']} [{c['verdict']}; {f.get('confidence')}]\n")
        for k in ('main_ru', 'main_en', 'note_ru', 'note_en', 'units', 'alternatives', 'conflict_with_editor', 'open_points'):
            v = f.get(k)
            if v:
                out.append(f"**{k}:** {v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)}\n")
        out.append(f"**verifier problems:** {c['problems']}\n")
open(OUT, 'w', encoding='utf-8').write('\n'.join(out))
print(len(out), 'lines written')
