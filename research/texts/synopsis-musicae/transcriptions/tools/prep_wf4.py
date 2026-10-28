"""Build anonymised places for the Vincent and Vinet adjudication workflow (wf4); same design as prep_wf3.py.
Usage: python -I prep_wf4.py <scratchpad dir> <gpt greek json>"""
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
sys.argv = [sys.argv[0], sys.argv[1]] + sys.argv[2:]
sp, gpt_gr = Path(sys.argv[1]), sys.argv[2]
src = open(sp / 'prep_wf3.py', encoding='utf-8').read()
ns = {'__name__': 'prep_wf3_lib', 'sys': sys}
exec(src.split('groups, key = {}, {}')[0], ns)          # reuse nfc(), ops(), place() and SRC
groups, key = {}, {}
ns['groups'], ns['key'] = groups, key
place, SRC = ns['place'], ns['SRC']
G = json.load(open(gpt_gr, encoding='utf-8'))

vinc_img = {338: 'p338-leaf0361.jpg', 340: 'p340-leaf0363.jpg', 342: 'p342-leaf0365.jpg'}
for r in json.load(open(sp / 'wf3' / 'cmp-vincent.json', encoding='utf-8'))['diffs']:
    pg = int(r['ref'].split()[1].split('.')[0])
    place(r['ref'], 'vincent', f"{SRC}/vincent1847/{vinc_img[pg]}", r['ref'], r['claude'], r['gpt'], 'claude', 'gpt')
cn = {n['ref']: n['text'] for p in json.load(open(sp / 'wf2' / 'vincent' / 'vincent.json', encoding='utf-8'))['pages'] for n in p['footnotes']}
gn = {n['ref']: n['text'] for f in G['p_fragments'] for n in f['footnotes']}
for ref in ('Vinc. 338 n. 1', 'Vinc. 338 n. 6', 'Vinc. 340 n. 1', 'Vinc. 342 n. 5'):
    pg = int(ref.split()[1])
    place(ref, 'vincent', f"{SRC}/vincent1847/{vinc_img[pg]}", ref + ' (footnote, small type at the foot of the page)', cn[ref], gn[ref], 'claude', 'gpt')
# my first reading against both later ones
place('Vinc. 340 n. 4', 'vincent', f"{SRC}/vincent1847/{vinc_img[340]}", 'Vinc. 340 n. 4 (footnote)', 'Ms. κεκρυμμένων.', 'Ms. κεχρυμμένων.', 'claude-wf+gpt', 'claude-1')

vinet_img = lambda pg: f"{SRC}/tournon1591/la-vinet-seq{47 + pg - 41}-p{pg}.jpg"
for r in json.load(open(sp / 'wf3' / 'cmp-vinet.json', encoding='utf-8'))['diffs']:
    if r['kind'] == 'spacing' and all(o == '«»→« »' for o in r['ops']):
        continue
    pg = int(r['ref'].split()[1].split('.')[0])
    place(r['ref'], 'vinet', vinet_img(pg), r['ref'], r['claude'], r['gpt'], 'claude', 'gpt')

for g, ps in groups.items():
    ps.sort(key=lambda p: p['id'])
    for c in ('A', 'B'):
        f = sp / 'wf4' / f'{g}-{c}'
        f.mkdir(parents=True, exist_ok=True)
        json.dump({'group': g, 'places': ps}, open(f / 'places.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(key, open(sp / 'wf4' / 'places-key.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({g: len(v) for g, v in groups.items()})
print('missing images:', sorted({p['image'] for v in groups.values() for p in v if not Path(p['image']).exists()}))
