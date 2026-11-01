"""Packets for the research on the editor's term decisions: for each card, the editor's decision, the Greek of the units,
the reviewers' analyses and the translators' renderings. Card definitions are read from build_decisions.py.
Usage: python -I prep_terms_research.py <ws-cmp folder>"""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
O = sys.argv[1]
src = open(f'{O}/scripts/build_decisions.py', encoding='utf-8').read()
src = src[:src.index('used_div, used_term = set(), set()')]
ns = {'__name__': 'cards'}
sys.argv = ['x', O, 'unused.html']
exec(compile(src, 'build_decisions.py', 'exec'), ns)
CARDS = {c['id']: c for c in ns['POLICIES'] + ns['PLACES']}
UNITS, TERMS, REV, G, tmatch, dmatch = ns['UNITS'], ns['TERMS'], ns['REV'], ns['G'], ns['tmatch'], ns['dmatch']
TT = json.load(open(f'{O}/inputs/terms.json', encoding='utf-8'))  # translators' own glossaries, by label

dec = {}
for line in open(f'{O}/editor-decisions-raw.txt', encoding='utf-8'):
    m = re.match(r'([PL]\d\d)( — комментарий)?: (.*)', line.strip())
    if m:
        d = dec.setdefault(m.group(1), {})
        d['comment' if m.group(2) else 'choice'] = m.group(3)

GROUPS = {
    1: ('Ratios, interval names, operations on ratios', ['P01', 'P02', 'P03', 'P11', 'L03', 'L09']),
    2: ('Note names, systems, interval classes, dynamis', ['P05', 'P06', 'P09', 'P10', 'P14']),
    3: ('Melody, tension, time, songs, melodic devices', ['P07', 'L08', 'P08', 'P13', 'L14', 'L15']),
    4: ('Wording and syntax', ['P12', 'L02', 'L10']),
}


def packet(cid):
    c = CARDS[cid]
    units, revs = set(), []
    for r, name in REV:
        pairs = [(c['unit'], k) for k in c.get('div', [])] if 'unit' in c else c.get('div', [])
        for uid, k in pairs:
            for d in (UNITS[r].get(uid) or {}).get('divergences') or []:
                if dmatch(d, k):
                    units.add(uid)
                    revs.append({'reviewer': name, 'unit': uid, **{x: d.get(x) for x in ('greek', 'issue', 'readings', 'verdict', 'recommended_ru',
                                                                                          'recommended_en', 'evidence', 'check_note', 'correction')}})
        if c.get('terms'):
            for t in TERMS[r]:
                if tmatch(t, c['terms'], c.get('xterms', ())):
                    units.update(re.findall(r'U\d{3}', str(t.get('units'))))
                    revs.append({'reviewer': name, 'glossary': True, **{x: t.get(x) for x in ('greek', 'units', 'renderings', 'recommended_ru',
                                                                                              'recommended_en', 'why', 'evidence')}})
    if 'unit' in c:
        units.add(c['unit'])
    tr = {}
    if c.get('terms'):
        for L, lst in TT.items():
            tr[L] = [t for t in lst if tmatch(t, c['terms'], c.get('xterms', ()))]
    return {'id': cid, 'title': c['title'], 'question': c['q'], 'options_offered': dict(c['opts']), 'note_on_page': c.get('note'),
            'editor': dec.get(cid, {}), 'units': {u: G[u]['greek'] for u in sorted(units) if u in G},
            'reviewers': revs, 'translators_glossaries': tr}


import os
os.makedirs(f'{O}/terms-research', exist_ok=True)
for gi, (title, ids) in GROUPS.items():
    p = {'group': gi, 'title': title, 'questions': [packet(i) for i in ids]}
    s = json.dumps(p, ensure_ascii=False, indent=1)
    open(f'{O}/terms-research/packet-{gi}.json', 'w', encoding='utf-8').write(s)
    print(gi, title, [(q['id'], len(q['units']), len(q['reviewers'])) for q in p['questions']], len(s), 'chars')
for k in (__import__('getpass').getuser(), 'Documents', 'ws-', 'C:\\'):
    for gi in GROUPS:
        if k in open(f'{O}/terms-research/packet-{gi}.json', encoding='utf-8').read():
            print('MENTION', k, 'in packet', gi)
