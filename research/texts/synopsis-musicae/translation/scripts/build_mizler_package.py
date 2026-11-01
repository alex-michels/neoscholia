"""Build the input files for the independent comparison of the translation with Mizler's German translation (1746):
units.json (Greek, Russian, English and notes of each unit) and edition.json (sigla, apparatus entries and departures
from the Basel text, without the edition's reasoning). Usage:
python -I build_mizler_package.py <translation.json> <constituted text.json> <package folder>"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
TR, TX, OUT = sys.argv[1:4]
tr = json.load(open(TR, encoding='utf-8'))
tx = json.load(open(TX, encoding='utf-8'))
# Neutral wording for the comparison (leak review, 1.11.2026): no traces of the working process, no names of parts of
# the edition that are not supplied, no statement on what the printed-edition translations have.
SCRUB = [('; checked against the scan, round 1', ''), (" (editor's decision, 31.10.2026)", ''),
         ('alternatives for translation', 'notes'), ('resolved doubts', 'notes'), ('resolved doubt', 'note'),
         ('treatment of the P passages', 'notes on the P passages'), ('description of the witnesses', 'description of the sources'),
         ('; так и во всех переводах, сделанных по печатным изданиям', ''), (', as do all translations made from the printed editions', '')]


def scrub(s):
    for a, b in SCRUB:
        s = s.replace(a, b)
    return s


tr = json.loads(scrub(json.dumps(tr, ensure_ascii=False)))
tx = json.loads(scrub(json.dumps(tx, ensure_ascii=False)))
os.makedirs(f'{OUT}/work', exist_ok=True)
sec_title = {s['section']: s['title_en'] for s in tr['sections']}
units = []
for u in tr['units']:
    units.append({
        'id': u['id'], 'section': u['section'], 'section_title': sec_title[u['section']], 'bas': u['bas'],
        'only_in_P': u['p_only'], 'greek': u['greek'], 'ru': u['ru'], 'en': u['en'],
        'notes': [{'n': i, 'anchor_ru': n['anchor_ru'], 'anchor_en': n['anchor_en'], 'ru': n['ru'], 'en': n['en'],
                   'source': n['source']} for i, n in enumerate(u['notes'], 1)]})
json.dump({'title': 'Τῆς μουσικῆς σύνοψις ἠκριβωμένη', 'units': units},
          open(f'{OUT}/units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
edition = {'sigla': tx['sigla'], 'sections': []}
for s in tx['sections']:
    edition['sections'].append({
        'section': s['section'], 'ref_bas': s['ref_bas'],
        'apparatus': [{'ref': a['ref'], 'entry': a['entry']} for a in s.get('apparatus') or []],
        'departures_from_Bas': [{'ref': d['ref'], 'Bas': d['Bas'], 'adopted': d['adopted'], 'source': d['source']}
                                for d in s.get('departures') or []]})
json.dump(edition, open(f'{OUT}/edition.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
EDITION = ('The edition of the Greek text from which the translation was made: the established text (in units.json), the '
           'apparatus and the departures from Bas. (in edition.json). Its notes and its description of the sources are not '
           'supplied. Cited by page and line of Bas. and by page and line of Vinc.')
json.dump([{'key': b['key_en'], 'entry': EDITION if b['key_en'] == 'Edition' else b['en']} for b in tr['bibliography']],
          open(f'{OUT}/bibliography.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(units), 'units;', sum(len(s['apparatus']) for s in edition['sections']), 'apparatus entries;',
      sum(len(s['departures_from_Bas']) for s in edition['sections']), 'departures ->', OUT)
