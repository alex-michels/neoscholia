"""Assemble the composed units (compose/final) into one translation: translation.json and translation.md, with the notes
numbered through the text and the bibliography at the end.
Usage: python -I assemble_final.py <ws-cmp folder> <constituted text.json> <out folder>"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
O, TEXT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
F = f'{O}/compose/final'
T = json.load(open(TEXT, encoding='utf-8'))
SEC = {int(s['section']): s for s in T['sections']}
G = {}
for n in (1, 2, 3, 4):
    for u in json.load(open(f'{O}/inputs/group-{n}.json', encoding='utf-8'))['units']:
        G.setdefault(u['id'], u)
BIB = json.load(open(f'{F}/bibliography.json', encoding='utf-8')) if os.path.exists(f'{F}/bibliography.json') else []

units, n = [], 0
for uid in sorted(G):
    c = json.load(open(f'{F}/{uid}.json', encoding='utf-8'))
    g = G[uid]
    notes = []
    for nt in c.get('notes') or []:
        n += 1
        notes.append({'n': n, **{k: nt.get(k) for k in ('anchor_ru', 'anchor_en', 'kind', 'ru', 'en', 'source', 'verified')}})
    units.append({'id': uid, 'section': g['section'], 'bas': g['bas'], 'p_only': g.get('p_only', False),
                  'paragraph_start': g.get('paragraph_start', False), 'greek': g['greek'], 'ru': c['ru'], 'en': c['en'],
                  'notes': notes, 'basis': c.get('basis'), 'decisions': c.get('decisions') or [], 'verify': c.get('verify'),
                  'open': c.get('open') or []})

os.makedirs(OUT, exist_ok=True)
doc = {'title_ru': 'Точный Синопсис Музыки', 'title_en': 'A Precise Synopsis of Music',
       'work': 'Anonymous, Quadrivium of 1008: the music section (Τῆς μουσικῆς σύνοψις ἠκριβωμένη)',
       'status': 'composed from six independent translations after three reviews and the editor\'s decisions, 31.10.2026; '
                 'verified and read for consistency; notes fact-checked against the sources, 1.11.2026; '
                 "the editor's answers to the open questions applied, 1.11.2026; compared with Mizler's German translation "
                 "(1746) and corrected, 1.11.2026; not yet signed by the editor",
       'sections': [{'section': k, 'title_ru': s['title_ru'], 'title_en': s['title_en'], 'ref_bas': s['ref_bas']} for k, s in sorted(SEC.items())],
       'units': units, 'bibliography': BIB}
json.dump(doc, open(f'{OUT}/translation.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def mark(text, notes, key):
    """Put note numbers after their anchors (the first occurrence of each anchor, left to right)."""
    for nt in sorted(notes, key=lambda x: -text.find(x[key]) if x.get(key) and x[key] in text else 0):
        a = nt.get(key)
        if a and a in text:
            i = text.find(a) + len(a)
            text = text[:i] + f'<sup>{nt["n"]}</sup>' + text[i:]
    return text


md = [f"# {doc['title_ru']} / {doc['title_en']}", '', f"*{doc['work']}.*", '', f"Status: {doc['status']}.", '']
cur = None
for u in units:
    if u['section'] != cur:
        cur = u['section']
        s = SEC[int(cur)]
        md += [f"## {cur}. {s['title_ru']} / {s['title_en']}", '', f"*{s['ref_bas']}*", '']
    md += [f"**{u['id']}** (Bas. {u['bas']}){' — P' if u['p_only'] else ''}", '', f"> {u['greek']}", '',
           mark(u['ru'], u['notes'], 'anchor_ru'), '', mark(u['en'], u['notes'], 'anchor_en'), '']
    for nt in u['notes']:
        md += [f"{nt['n']}. {nt['ru']}", f"   {nt['en']}", f"   *{nt['source']}*", '']
if BIB:
    md += ['## Литература / Bibliography', '']
    for b in BIB:
        md.append(f"- **{b.get('key_ru')}** — {b.get('ru')}" + (f" / **{b.get('key_en')}** — {b.get('en')}" if b.get('en') else ''))
open(f'{OUT}/translation.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('units', len(units), 'notes', n, 'bibliography', len(BIB), 'open', sum(len(u['open']) for u in units), '->', OUT)
