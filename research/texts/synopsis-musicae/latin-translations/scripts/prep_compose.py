"""Prepare the composition of the final RU/EN translations of the two Latin versions: one packet per group of segments
with everything a composer needs for each segment (the Latin, the four translations A–D, the three comparisons' findings,
the blind recheck, the decision cards and agreed points that touch it), plus a common file with the general cards and
the agreed points. The editor accepted every recommendation (decisions/editor-decisions.txt), so each card's
recommendation is the decision.
Usage: python -I prep_compose.py <latin-translations folder> <work folder>"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
L, W = sys.argv[1], sys.argv[2]
os.makedirs(W, exist_ok=True)
FILES = {'A': 'A-fable-5.2', 'B': 'B-gpt-6.2-sol', 'C': 'C-opus-5.5', 'D': 'D-gpt-6.2-astra'}
T = {k: json.load(open(f'{L}/translations/{v}.json', encoding='utf-8')) for k, v in FILES.items()}
SRC = json.load(open(f'{L}/independent/latin-texts.json', encoding='utf-8'))
MAP = {s['id']: s['units'] for s in json.load(open(f'{L}/segment-map.json', encoding='utf-8'))['segments']}
M = json.load(open(f'{L}/comparisons/merged.json', encoding='utf-8'))
RC = json.load(open(f'{L}/decisions/recheck.json', encoding='utf-8'))['items']
D = json.load(open(f'{L}/decisions/cards.json', encoding='utf-8'))
assert open(f'{L}/decisions/editor-decisions.txt', encoding='utf-8').read().count(': рекомендация') == len(D['cards'])
GROUPS = [('xylander', 'X01', 'X29'), ('xylander', 'X30', 'X58'), ('vinet', 'V01', 'V33'), ('vinet', 'V34', 'V66')]


def card_entry(c):
    return {'id': c['id'], 'kind': c['kind'], 'version': c['version'], 'segments': c['segments'], 'title_ru': c['title_ru'],
            'latin': c.get('latin'), 'question_ru': c['question_ru'], 'options': c['options'],
            'decision_ru': c['recommendation_ru'], 'evidence_ru': c['evidence_ru']}


common = {'note': 'The editor accepted every recommendation: decision_ru of each card is the decision. General cards apply wherever '
                  'their term or question occurs, not only in the segments listed.',
          'general_cards': [card_entry(c) for c in D['cards'] if c['kind'] == 'general'],
          'agreed': D['agreed']}
json.dump(common, open(f'{W}/common.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for gi, (w, a, b) in enumerate(GROUPS, 1):
    segs = SRC[w]['segments']
    ids = [s['id'] for s in segs]
    out = []
    for s in segs[ids.index(a):ids.index(b) + 1]:
        sid = s['id']
        out.append({
            'id': sid, 'version': w, 'units': MAP[sid], 'ref': s['ref'], 'latin': s['latin'], 'printed': s['printed'],
            **({'heading': True} if s.get('heading') else {}),
            **({'starts_paragraph': s['starts_paragraph']} if s.get('starts_paragraph') else {}),
            'translations': {k: {f: next(x for x in T[k]['versions'][w]['segments'] if x['id'] == sid).get(f)
                                 for f in ('ru', 'en', 'checks', 'notes', 'doubts')} for k in FILES},
            'text_issues': {k: [x for x in (T[k].get('text_issues') or []) if str(x.get('segment')) == sid] for k in FILES},
            'reviews': M['segments'][sid]['reviewers'],
            'recheck': [x for x in RC if x['segment'] == sid],
            'major_errors_corroborated': [x for x in M['major_corroborated'] if x['segment'] == sid],
            'place_cards': [card_entry(c) for c in D['cards'] if c['kind'] == 'place' and sid in c['segments']],
            'general_cards_listing_this_segment': [c['id'] for c in D['cards'] if c['kind'] == 'general' and sid in c['segments']],
            'agreed_points': [x for x in D['agreed'] if sid in (x.get('segments') or [])],
        })
    json.dump({'group': gi, 'version': w, 'segments': out}, open(f'{W}/packet-g{gi}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('packet', gi, w, a, '-', b, len(out), 'segments')
for f in ('about.md',):
    open(f'{W}/{f}', 'w', encoding='utf-8').write(open(f'{L}/independent/{f}', encoding='utf-8').read())
json.dump({k: T[k].get('terms') for k in FILES}, open(f'{W}/terms-by-translator.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('common:', len(common['general_cards']), 'general cards,', len(common['agreed']), 'agreed points')
