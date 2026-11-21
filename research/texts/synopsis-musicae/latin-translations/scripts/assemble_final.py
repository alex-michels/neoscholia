"""Assemble the final RU/EN translations of the two Latin versions from the composed groups (work/composed-g1..4.json)
into translation-latin.json and translation-latin.md, with the Latin, the printed references, the units of the Greek
text each segment answers to (segment-map.json) and the notes numbered within each version.
Checks: every segment once, in order; ru and en present; every note anchor found verbatim.
Usage: python -I assemble_final.py <latin-translations folder> <work folder> [status]"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
L, W = sys.argv[1], sys.argv[2]
STATUS = sys.argv[3] if len(sys.argv) > 3 else ''
SRC = json.load(open(f'{L}/independent/latin-texts.json', encoding='utf-8'))
MAP = {s['id']: s['units'] for s in json.load(open(f'{L}/segment-map.json', encoding='utf-8'))['segments']}
comp = {}
for g in (1, 2, 3, 4):
    for s in json.load(open(f'{W}/work/composed-g{g}.json', encoding='utf-8'))['segments']:
        assert s['id'] not in comp, ('duplicate', s['id'])
        comp[s['id']] = s
TITLES = {'xylander': ('Ксиландр', 'Xylander', 'Basel: Oporinus, [1556], pp. 40–49'),
          'vinet': ('Вине', 'Vinet', 'Tournon, 1591, pp. 41–53')}
doc = {'title_ru': 'Латинские переводы «Синопсиса Музыки»: Ксиландр и Вине',
       'title_en': 'The Latin versions of the Synopsis of Music: Xylander and Vinet',
       'status': STATUS, 'versions': {}}
problems = []
for w in ('xylander', 'vinet'):
    segs, n = [], 0
    for s in SRC[w]['segments']:
        c = comp.get(s['id'])
        if not c:
            problems.append(f'missing {s["id"]}')
            continue
        for k in ('ru', 'en'):
            if not (c.get(k) or '').strip():
                problems.append(f'{s["id"]}: empty {k}')
        notes = []
        for nt in c.get('notes') or []:
            for k in ('ru', 'en'):
                a = nt.get(f'anchor_{k}') or ''
                if a and a not in c[k]:
                    problems.append(f'{s["id"]}: {k} anchor not found «{a}»')
            n += 1
            notes.append({'n': n, **{k: nt.get(k, '') for k in ('anchor_ru', 'anchor_en', 'ru', 'en', 'source')}})
        e = {'id': s['id'], 'units': MAP[s['id']], 'ref': s['ref'], 'latin': s['latin']}
        if s.get('heading'):
            e['heading'] = True
        if s.get('starts_paragraph'):
            e['starts_paragraph'] = s['starts_paragraph']
        e.update({'ru': c['ru'], 'en': c['en'], 'notes': notes, 'basis': c.get('basis', ''),
                  'decisions': c.get('decisions') or [], 'fixes': c.get('fixes') or [], 'open': c.get('open') or []})
        segs.append(e)
    ru, en, printing = TITLES[w]
    doc['versions'][w] = {'title_ru': ru, 'title_en': en, 'printing': printing, 'segments': segs}
if problems:
    raise SystemExit('PROBLEMS:\n' + '\n'.join(problems))
json.dump(doc, open(f'{L}/translation-latin.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

md = [f"# {doc['title_ru']} / {doc['title_en']}", '', f'Status: {STATUS}.' if STATUS else '', '']
for w, v in doc['versions'].items():
    md += [f"## {v['title_ru']} / {v['title_en']} ({v['printing']})", '']
    for s in v['segments']:
        md += [f"### {s['id']} · {s['ref']}" + (' (heading)' if s.get('heading') else ''), '', f"*{s['latin']}*", '',
               f"**RU.** {s['ru']}", '', f"**EN.** {s['en']}", '']
        for nt in s['notes']:
            md += [f"{nt['n']}. {nt['anchor_ru']} — {nt['ru']}", f"   {nt['anchor_en']}: {nt['en']}", f"   *{nt['source']}*", '']
open(f'{L}/translation-latin.md', 'w', encoding='utf-8').write('\n'.join(md))
print({w: (len(v['segments']), sum(len(s['notes']) for s in v['segments'])) for w, v in doc['versions'].items()}, '-> translation-latin.json / .md')
