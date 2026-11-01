"""Build greek-text.json for the independent translations of the Synopsis: the established text cut into translation units
(sentences within paragraphs; P-only passages flagged), with Bas. line references, and the apparatus entries (lemma] variants)
without the edition's notes. Usage: python -I build_tr_pkg.py <text.json> <out greek-text.json>"""
import json, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(sys.argv[1], encoding='utf-8'))
MARK = re.compile(r'\|(\d+\.\d+)\|')
units, cur_line, frag = [], '23.1', 0
VINC = {1: 'Vinc. 338.4–340.2', 2: 'Vinc. 340.7–342.4', 3: 'Vinc. 342.19–24'}

def clean(t):
    return re.sub(r'\s+', ' ', MARK.sub('', t)).strip()

def add(sec, chunk, p_only, para_start):
    global cur_line
    chunk = chunk.strip()
    if not chunk:
        return
    lines = MARK.findall(chunk)
    first = cur_line if not chunk.startswith('|') else lines[0]
    last = lines[-1] if lines else first
    if lines:
        cur_line = lines[-1]
    u = {'id': f'U{len(units) + 1:03d}', 'section': sec, 'bas': first if first == last else f'{first}–{last}',
         'p_only': p_only, 'paragraph_start': para_start, 'greek': clean(chunk), 'greek_with_lines': chunk}
    if p_only:
        u['p_fragment'] = f'P fragment {frag} ({VINC[frag]}), placed in Basel line {first}'
    units.append(u)

SENT = re.compile(r'(?<=[.;])\s+(?=\S)')                      # full stop or Greek question mark, then a space
for s in d['sections']:
    sec = int(s['section'])
    for k, para in enumerate(s['greek'].split('\n\n')):
        parts = re.split(r'(⟨⟨.*?⟩⟩)', para, flags=re.S)      # P-only passages as their own runs
        first_in_para = True
        for part in parts:
            if not part.strip():
                continue
            p_only = part.startswith('⟨⟨')
            if p_only:
                frag += 1
            for j, sent in enumerate(SENT.split(part)):
                add(sec, sent, p_only, first_in_para and (k > 0 or sec in (1, 2, 4, 6)) and j == 0)
                first_in_para = False
joined = ' '.join(u['greek_with_lines'] for u in units)
orig = ' '.join(s['greek'] for s in d['sections'])
assert re.sub(r'\s+', '', joined) == re.sub(r'\s+', '', orig), 'units do not cover the text exactly'
out = {
 'text': 'Anonymous, Quadrivium of 1008: the music section (Τῆς μουσικῆς σύνοψις ἠκριβωμένη), established critical text, Neoscholia 2026',
 'how_to_read': ('Translate the units in order; together they are the whole text. "greek" is the text to translate; "greek_with_lines" is the '
                 'same with the line markers |page.line| of the Basel print (1556), which give the reference grid and are not part of the '
                 'text. "p_only": true marks words found only in one manuscript, Paris. gr. 2448 (P), printed within ⟨⟨ ⟩⟩. '
                 '"paragraph_start": true where the edition begins a paragraph. Unit boundaries are mechanical (at full stops); if a '
                 'boundary splits a sentence badly, say so in your notes, but keep the units.'),
 'sigla': d['sigla'],
 'signs': {'|23.1|': 'line marker: Basel 1556, page 23, line 1 (also inside a word where Basel divides it)',
           '⟨ ⟩': 'words added by the edition where no witness has them',
           '⟨⟨ ⟩⟩': 'a passage found only in P (Paris. gr. 2448, known only from Vincent 1847); printed as P\'s text, not claimed for the text of 1008',
           '† †': 'a corrupt word that the edition cannot heal (obeli)',
           'coni.': 'in the apparatus: a conjecture of this edition',
           'Vinc.': 'in the apparatus: a correction printed by Vincent 1847 in his text of P'},
 'units': units,
 'apparatus': [{'section': int(s['section']), 'ref': a['ref'], 'entry': a['entry']} for s in d['sections'] for a in s['apparatus']],
}
for u in units:
    assert unicodedata.normalize('NFC', u['greek']) == u['greek']
json.dump(out, open(sys.argv[2], 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
L = [len(u['greek'].split()) for u in units]
print('units', len(units), '| P units', sum(u['p_only'] for u in units), '| words min/median/max', min(L), sorted(L)[len(L) // 2], max(L),
      '| apparatus', len(out['apparatus']))
for u in units:
    if len(u['greek'].split()) > 70 or len(u['greek'].split()) < 4:
        print(u['id'], u['bas'], len(u['greek'].split()), u['greek'][:120])
