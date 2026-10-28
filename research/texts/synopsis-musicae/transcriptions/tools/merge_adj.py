"""Merge the two checkers' verdicts per difference; decide where they agree, send the rest to the editor.
Usage: python -I merge_adj.py <wf dir (wf3|wf4)> <results json (list of {group, checker, result})>"""
import json, sys
from collections import Counter
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
wf, res_path = Path(sys.argv[1]), sys.argv[2]
key = json.load(open(wf / 'places-key.json', encoding='utf-8'))
res = json.load(open(res_path, encoding='utf-8'))
places = {}
for d in wf.glob('*-A'):
    for p in json.load(open(d / 'places.json', encoding='utf-8'))['places']:
        places[p['id']] = dict(p, group=d.name[:-2])
verd = {}
for r in res:
    if not r or not r.get('result'):
        continue
    for v in r['result']['verdicts']:
        verd[(v['id'], r['checker'])] = v

out, review, stats = [], [], Counter()
for pid, p in sorted(places.items(), key=lambda kv: (kv[1]['group'], kv[0])):
    a, b = verd.get((pid, 'A')), verd.get((pid, 'B'))
    rows = []
    for i, diff in enumerate(p['differences'], 1):
        da = next((x for x in (a or {}).get('decisions', []) if int(x['difference']) == i), None)
        db = next((x for x in (b or {}).get('decisions', []) if int(x['difference']) == i), None)
        ca, cb = (da or {}).get('choice'), (db or {}).get('choice')
        conf_ok = da and db and 'low' not in (da['confidence'], db['confidence'])
        if ca and ca == cb and ca in ('1', '2', 'convention') and conf_ok:
            status = 'decided'
        elif ca == cb == 'other' and conf_ok and (da.get('other') or '').strip() == (db.get('other') or '').strip():
            status = 'decided'
        else:
            status = 'editor'
        winner = key[pid].get(ca) if status == 'decided' and ca in ('1', '2') else None
        stats[(p['group'], status, winner)] += 1
        rows.append({'difference': diff, 'status': status, 'choice': ca if status == 'decided' else None, 'winner': winner,
                     'A': da, 'B': db})
    item = {'id': pid, 'group': p['group'], 'ref': p['ref'], 'image': p['image'], 'reading_1': p['reading_1'], 'reading_2': p['reading_2'],
            'context': p.get('context') or p.get('question'), 'rows': rows,
            'A_reading': (a or {}).get('my_reading'), 'B_reading': (b or {}).get('my_reading'),
            'A_note': (a or {}).get('note'), 'B_note': (b or {}).get('note')}
    out.append(item)
    if any(r['status'] == 'editor' for r in rows):
        review.append(item)
json.dump(out, open(wf / 'decisions.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(review, open(wf / 'for-editor.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [pid for pid in places if (pid, 'A') not in verd or (pid, 'B') not in verd]
print('places', len(places), '| missing verdicts:', missing)
for k, v in sorted(stats.items(), key=lambda kv: str(kv[0])):
    print(k, v)
print('places for the editor:', len(review))
