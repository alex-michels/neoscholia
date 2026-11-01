"""Mechanical checks of the composed units against DECISIONS.md: format, forbidden renderings, ratio brackets,
Greek in the running text, signs of the edition, note style and anchors. Prints one line per problem.
Usage: python -I check_composed.py <ws-cmp folder> <out|final>"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
O, STAGE = sys.argv[1], sys.argv[2]
d = f'{O}/compose/{STAGE}'
G = {}
for n in (1, 2, 3, 4):
    for u in json.load(open(f'{O}/inputs/group-{n}.json', encoding='utf-8'))['units']:
        G.setdefault(u['id'], u['greek'])

GREEK_OK = {'U033', 'U035', 'U054'}              # Greek allowed in the running text (both languages); U054: the author
                                                 # derives διάτονον from διὰ τόνων (DECISIONS § 2, listed in its basis)
MELOS_EN = {'U027', 'U028', 'U054', 'U065'}       # EN '(μέλος)'
RU_BAD = [(r'пятнадцатихорд|шестнадцатихорд', 'P06 b: «пятнадцатизвуковая / шестнадцатизвуковая система»'),
          (r'трёхполутонов|трехполутонов|тригемитон|трихемитон', 'P11 a: «трёхполутон»'),
          (r'эпогдо|эпитрит|гемиол|эпитетарт|эпидимер|эпимер', 'P03 a: calques in the text'),
          (r'опосредованн|непосредственн', 'P09 b: «между смежными / несмежными звуками»'),
          (r'функци', 'P10 a: «значение»'),
          (r'двойн\w* \[|пятерн|тройн\w* \[|четверн\w* \[', 'P03 a: двукратное / трёхкратное / четырёхкратное'),
          (r'просламбаноменос|парамесос|парамеса\b', 'note names: «просламбаномен», «парамес»'),
          (r'свидетел', 'no «свидетель» for a witness'),
          (r'шестнадцатихорд|совокупност\w* \(', 'P14: no Greek in the text')]
EN_BAD = [(r'fifteen-chord|sixteen-chord', 'P06 b: fifteen-note / sixteen-note system'),
          (r'\b(im)?mediate\b', 'P09 b: between adjacent / non-adjacent notes'),
          (r'\baggregate\b', 'P14: collection'),
          (r'\bfunctions?\b', 'P10 a: value'),
          (r'\bduple\b|sesqui', 'P04 a: Greek-based English')]
RATIO_RU = r'(?<!полу)(двукратн|трёхкратн|четырёхкратн|пятикратн|полуторн|сверхтретн|сверхосминн|сверхчетвертн|сверхдвухчастн|двукратн\w* сверхчастн|двукратн\w* с половиной)\w*'
RATIO_EN = r'\b(double|triple|quadruple|quintuple|hemiolic|epitritic|epogdoic|epitetartic|epidimeric|double-epimeric|double-hemiolic)\b'
GREEK = re.compile(r'[Ͱ-Ͽἀ-῿]')

probs = []
files = sorted(f for f in os.listdir(d) if re.fullmatch(r'U\d{3}\.json', f))
have = {f[:4] for f in files}
missing = sorted(set(G) - have)
if missing:
    probs.append(f'missing units: {missing}')
for f in files:
    uid = f[:4]
    try:
        u = json.load(open(f'{d}/{f}', encoding='utf-8'))
    except Exception as e:
        probs.append(f'{uid}: invalid JSON: {e}')
        continue
    for k in ('id', 'ru', 'en', 'notes', 'basis'):
        if k not in u:
            probs.append(f'{uid}: no field {k}')
    ru, en = u.get('ru') or '', u.get('en') or ''
    for pat, why in RU_BAD:
        for m in re.finditer(pat, ru, re.I):
            probs.append(f'{uid} RU text «{m.group(0)}»: {why}')
    if re.search(r'двойн\w* (кварт|квинт)', ru) and uid != 'U035':
        probs.append(f'{uid} RU text: «двойная кварта / квинта» only at U035 (P02 b)')
    for pat, why in EN_BAD:
        for m in re.finditer(pat, en, re.I):
            probs.append(f'{uid} EN text "{m.group(0)}": {why}')
    if re.search(r'double (fourth|fifth)', en, re.I) and uid != 'U035':
        probs.append(f'{uid} EN text: "double fourth / fifth" only at U035 (P02 b)')
    # ratio names followed by [n:m] (the adjective, then optionally «отношение» and words, then the bracket)
    for m in re.finditer(RATIO_RU, ru):
        tail = ru[m.end():m.end() + 40]
        if uid in ('U018', 'U020', 'U025', 'U040', 'U041', 'U046', 'U047') and not re.match(r'[^.;\[]{0,25}\[\d+:\d+\]', tail) \
                and 'половин' not in m.group(0)[-9:] and not m.group(0).startswith('полусверх'):
            probs.append(f'{uid} RU ratio «{m.group(0)}» without [n:m] right after it')
    for m in re.finditer(RATIO_EN, en):
        tail = en[m.end():m.end() + 30]
        if uid in ('U040', 'U041', 'U046', 'U047') and not re.match(r'[^.;\[]{0,25}\[\d+:\d+\]', tail):
            probs.append(f'{uid} EN ratio "{m.group(0)}" without [n:m] right after it')
    # Greek in the running text
    if uid not in GREEK_OK:
        g_ru = GREEK.findall(ru)
        en_wo = en.replace('(μέλος)', '') if uid in MELOS_EN else en
        if g_ru:
            probs.append(f'{uid} RU text has Greek: {"".join(g_ru)[:30]}')
        if GREEK.search(en_wo):
            probs.append(f'{uid} EN text has Greek: {"".join(GREEK.findall(en_wo))[:30]}')
    if uid in MELOS_EN and '(μέλος)' not in en:
        probs.append(f'{uid} EN: "(μέλος)" expected after "melody" (P07)')
    # signs of the edition
    for sign in ('⟨⟨', '⟩⟩', '†'):
        if G[uid].count(sign) != ru.count(sign) or G[uid].count(sign) != en.count(sign):
            probs.append(f'{uid}: sign {sign} count Greek {G[uid].count(sign)} / RU {ru.count(sign)} / EN {en.count(sign)}')
    single_g = G[uid].replace('⟨⟨', '').replace('⟩⟩', '').count('⟨')
    for lang, t in (('RU', ru), ('EN', en)):
        if t.replace('⟨⟨', '').replace('⟩⟩', '').count('⟨') != single_g:
            probs.append(f'{uid} {lang}: ⟨ ⟩ count differs from the Greek ({single_g})')
    # notes
    for i, nt in enumerate(u.get('notes') or [], 1):
        for k in ('ru', 'en', 'source', 'verified', 'kind', 'anchor_ru', 'anchor_en'):
            if not nt.get(k):
                probs.append(f'{uid} note {i}: empty {k}')
        if nt.get('anchor_ru') and nt['anchor_ru'] not in ru:
            probs.append(f'{uid} note {i}: anchor_ru not in the RU text: «{nt["anchor_ru"]}»')
        if nt.get('anchor_en') and nt['anchor_en'] not in en:
            probs.append(f'{uid} note {i}: anchor_en not in the EN text: "{nt["anchor_en"]}"')
        nr, ne = nt.get('ru') or '', nt.get('en') or ''
        if re.match(r'\s*Греч\.', nr) or re.match(r'\s*Greek\b', ne):
            probs.append(f'{uid} note {i}: opens with «Греч.» / "Greek"')
        if re.search(r'\bliterally\b', ne):
            probs.append(f'{uid} note {i}: "literally" -> "lit."')
        if re.search(r'\d\s+:\s*\d|\d\s*:\s+\d', nr + ' ' + ne):
            probs.append(f'{uid} note {i}: ratio with spaces')
        if re.search(r"(?<![A-Za-z])'[A-Za-z][^']{2,}'", nr):
            probs.append(f'{uid} note {i}: English in single quotes inside the RU note')
        if re.search(r'свидетел', nr):
            probs.append(f'{uid} note {i}: «свидетель»')
        if re.search(r'\[(checked|from memory)\]', nr + ne + (nt.get('source') or '')):
            probs.append(f'{uid} note {i}: [checked]/[from memory] marks belong in "verified", not in the text or source')
        if re.search(r'(?<!\w)(Hiller|Хиллер)', nr) and not re.search(r'с\. \d', nr):
            probs.append(f'{uid} note {i}: Theon citation should read «с. N Hiller»')
        if re.search(r'Папе|по Папе', nr):
            probs.append(f'{uid} note {i}: write Pape in Latin letters')
print('\n'.join(probs) if probs else 'no problems found')
print(f'-- {len(files)} units checked, {len(probs)} problems')
