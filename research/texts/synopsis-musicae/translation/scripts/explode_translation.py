"""Unpack translation.json into the folder layout the composition scripts expect (inputs/group-1.json,
compose/final/Uxxx.json, compose/final/bibliography.json), so that check_composed.py, show_composed.py and
assemble_final.py can be run on the committed translation after the working folder is gone.
Usage: python -I explode_translation.py <translation.json> <work folder>"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
SRC, W = sys.argv[1], sys.argv[2]
d = json.load(open(SRC, encoding='utf-8'))
os.makedirs(f'{W}/inputs', exist_ok=True)
os.makedirs(f'{W}/compose/final', exist_ok=True)
units = [{k: u[k] for k in ('id', 'section', 'bas', 'p_only', 'paragraph_start', 'greek')} for u in d['units']]
json.dump({'units': units}, open(f'{W}/inputs/group-1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for n in (2, 3, 4):
    json.dump({'units': []}, open(f'{W}/inputs/group-{n}.json', 'w', encoding='utf-8'))
for u in d['units']:
    c = {'id': u['id'], 'ru': u['ru'], 'en': u['en'],
         'notes': [{k: v for k, v in nt.items() if k != 'n'} for nt in u['notes']],
         'basis': u['basis'], 'decisions': u['decisions'], 'open': u['open'], 'verify': u['verify']}
    json.dump(c, open(f'{W}/compose/final/{u["id"]}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(d['bibliography'], open(f'{W}/compose/final/bibliography.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(d['units']), 'units,', len(d['bibliography']), 'bibliography entries ->', W)
