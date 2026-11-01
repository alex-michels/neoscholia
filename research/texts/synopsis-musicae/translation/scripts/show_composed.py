"""Print composed units compactly: Greek, RU, EN and (with --notes) the notes.
Usage: python -I show_composed.py <ws-cmp folder> <out|final> [--notes] [U001 U002 ... | U001-U014]"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
O, STAGE = sys.argv[1], sys.argv[2]
NOTES = '--notes' in sys.argv
want = set()
for a in sys.argv[3:]:
    m = re.fullmatch(r'U(\d{3})-U(\d{3})', a)
    if m:
        want.update(f'U{i:03d}' for i in range(int(m.group(1)), int(m.group(2)) + 1))
    elif re.fullmatch(r'U\d{3}', a):
        want.add(a)
G = {}
for n in (1, 2, 3, 4):
    for u in json.load(open(f'{O}/inputs/group-{n}.json', encoding='utf-8'))['units']:
        G.setdefault(u['id'], u['greek'])
d = f'{O}/compose/{STAGE}'
for f in sorted(os.listdir(d)):
    if not re.fullmatch(r'U\d{3}\.json', f) or (want and f[:4] not in want):
        continue
    u = json.load(open(f'{d}/{f}', encoding='utf-8'))
    print(f"=== {u['id']}\nGR: {G.get(u['id'])}\nRU: {u['ru']}\nEN: {u['en']}")
    if NOTES:
        for i, nt in enumerate(u.get('notes') or [], 1):
            print(f"  [{i}] ({nt.get('kind')}; at «{nt.get('anchor_ru')}» / '{nt.get('anchor_en')}')\n      RU: {nt.get('ru')}\n      EN: {nt.get('en')}\n      SRC: {nt.get('source')} [{nt.get('verified')}]")
    print()
