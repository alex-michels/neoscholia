"""Merge the two diplomatic transcriptions of H (Pal. gr. 281, ff. 64r-70r) with round 1 (wf3: letters, punctuation stripped),
round 2 (wf5: everything else) and the editor's decisions.
Usage: python -I merge_h.py <scratchpad> <out json> [editor decisions json]"""
import difflib, re, sys, unicodedata
from collections import Counter
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
SP = Path(sys.argv[1])
sys.path.insert(0, str(SP))
from merge_lib import nfc, char_ops, word_ops, adopt, load_json, dump_json, reason, STRIP
ED = load_json(sys.argv[3]) if len(sys.argv) > 3 else {}
G = load_json(str(Path(__file__).resolve().parents[6] / 'Neoscholia-runs' / 'synopsis-musicae-greek' / 'transcription-gpt-6-astra.json'))

def nfc5(s):
    """prep_wf5.nfc: rubric crosses '+', no line-end hyphen, single spaces."""
    s = nfc(s).replace('†', '+')
    s = re.sub(r'-\s*$', '', s.rstrip())
    return re.sub(r'\s+', ' ', s).strip()

def slots(s):
    toks = re.findall(r'[^\s.·,:;]+|[.·,:;]+', s)
    words, after = [], []
    for t in toks:
        if re.fullmatch(r'[.·,:;]+', t):
            if words:
                after[-1] += t
            else:
                words.append(''); after.append(t)
        else:
            words.append(t); after.append('')
    return words, after

def wkey(w):
    w = unicodedata.normalize('NFD', re.sub(r'\([^)]*\)|\[\?\]|[⟦⟧]|^r ', '', w))
    return ''.join(c for c in w if c.isalpha() and not unicodedata.combining(c)).lower()

def punct_slots(a, b):
    """prep_wf5.punct_diffs: [(slot index in a, punct a, punct b)] in the order of the differences."""
    wa, pa = slots(a); wb, pb = slots(b)
    sm = difflib.SequenceMatcher(None, [wkey(w) for w in wa], [wkey(w) for w in wb], autojunk=False)
    out = []
    for blk in sm.get_matching_blocks():
        for i in range(blk.size):
            if pa[blk.a + i] != pb[blk.b + i]:
                out.append((blk.a + i, pa[blk.a + i], pb[blk.b + i]))
    return out, (wa, pa)

def carry(aw, rw, rp):
    """Punctuation of reference words rw (rp) carried onto adopted words aw: identical words one to one; inside a changed
    stretch each reference mark goes to the adopted word whose end is nearest to the same share of the stretch's letters."""
    sm = difflib.SequenceMatcher(None, [wkey(w) for w in aw], [wkey(w) for w in rw], autojunk=False)
    punct = [''] * len(aw)
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t == 'equal' or (t == 'replace' and i2 - i1 == j2 - j1):
            for k in range(i2 - i1):
                punct[i1 + k] = rp[j1 + k]
        elif i2 > i1 and j2 > j1:
            la = [max(1, len(wkey(w))) for w in aw[i1:i2]]
            lr = [max(1, len(wkey(w))) for w in rw[j1:j2]]
            ca = [sum(la[:k + 1]) / sum(la) for k in range(len(la))]
            for k in range(len(lr)):
                if rp[j1 + k]:
                    share = sum(lr[:k + 1]) / sum(lr)
                    tgt = min(range(len(ca)), key=lambda i: abs(ca[i] - share))
                    punct[i1 + tgt] += rp[j1 + k]
        elif j2 > j1 and i1 > 0:  # reference words with no adopted counterpart: their mark goes to the preceding word
            punct[i1 - 1] += ''.join(rp[j1:j2])
    return punct

def with_punct(words_text, ref_words, ref_punct):
    """Put the punctuation of a reference line on the adopted words."""
    aw = words_text.split()
    lead = ref_punct[0] if ref_words and ref_words[0] == '' else ''
    rw, rp = (ref_words[1:], ref_punct[1:]) if lead else (ref_words, ref_punct)
    punct = carry(aw, rw, rp)
    lost = [] if sum(len(p) for p in punct) == sum(len(p) for p in rp) else ['count differs']
    return (lead + ' ' if lead else '') + ' '.join(w + p for w, p in zip(aw, punct)), lost

def h_convention(place, i):
    """Word division: a written accent on δια separates the words (both checkers saw a grave in every case);
    a word running on into the next line stays one word (ἐντι-|θεμένων)."""
    m = re.match(r'\(1\) «(.*)»\s+/\s+\(2\) «(.*)»', place['differences'][i - 1])
    s1, s2 = m[1], m[2]
    if 'διὰ' in s1 and 'διὰ' not in s2:
        return '1'
    if 'διὰ' in s2 and 'διὰ' not in s1:
        return '2'
    return '1' if ' ' not in s1 else '2'

# The editor could not decide 68v.10 from the scan (μ and ν have the same shape in this hand, no space is written):
# the first nasal is transcribed with an underdot as uncertain, ἐμμέσω and ἐν μέσω being equally possible.
ASSIST = {'H 68v.10': [([1], ('other', 'ἐμ̣μέσω'))],
          # both checkers saw a grave on δια (one called the difference a convention): separate words
          'H 66v.9': [([1], '2')]}

# Round-2 places the checkers left open, decided by the editor's assistant at the editor's request (2026-10-28): the editor
# delegated them and asked for the variants to be given in the notes. Picks refer to reading 1/2 of the wf5 place.
ASSIST5 = {
    'H 64v.8': {1: '2'},     # middle point: both checkers (one low)
    'H 64v.12': {2: '1'},    # high point; a lower blot may make it a double point
    'H 65r.12': {1: '2'},    # middle point: both checkers (one low)
    'H 66r.3': {1: '2'},     # comma: head with a tail down to the left (close-up)
    'H 66r.7': {1: '1'},     # point: no tail worth the name (close-up)
    'H 66v.8': {1: ('other', 'διαπασῶν,')},  # no accent on Δια (both); comma (close-up, as 66v.15)
    'H 66v.11': {1: '2'},    # κακεὶθεν: short straight stroke, not the scribe's arch (αὖθις in the same line)
    'H 66v.15': {1: '1'},    # comma (checker A high; close-up)
    'H 67r.14': {1: '2'},    # comma: both checkers (one low)
    'H 67r.17': {1: '2'},    # comma: both checkers (one low)
    'H 67v.20': {1: '2'},    # no comma after λόγον: the signs below the line are a separate mark
    'H 68r.16': {1: '2'},    # high point: both checkers (one low)
    'H 69r.22': {1: '2'},    # high point: both checkers (one low)
    'H 69v.4': {1: '1'},     # comma: both checkers (one low)
    'H 70r.1': {1: ('other', 'μεταφορᾶ·')},  # circumflex: as διαφορᾶ two lines below (dative, both checkers there)
}

# Punctuation differences in round-1 lines that round 2 did not list (the words around them differ in letters, so the
# slot comparison missed them); settled by the editor's assistant from close-ups (2026-10-28), at the editor's request.
# (word number in the adopted line, adopted mark, Claude's mark, GPT's mark, why)
POST = {
    'H 65r.21': [(4, ',', ',', '.', 'a point with a tail down to the left after μο̣ι̣ρὰν: comma')],
    'H 66r.12': [(5, '', '', '.', 'the stroke after τῶ is an iota adscript (round 1, both checkers), not a point')],
    'H 66r.22': [(5, '', '', '·', 'the stroke after λόγω is an iota adscript (round 1, both checkers), not a point')],
    'H 68r.10': [(4, '·', '.', '·', 'the point after νοήσομεν stands at the top of the letters (measured: centre at -0.07 of the letter body; agreed high point 68r.13 at 0.12, middle at 0.59); the mark above it is the breathing of ἐξ')],
    'H 69r.2': [(2, '.', '.', '·', 'the point after μέλος stands at mid-height (measured centre about 0.6 of the letter body); the mark above it is the breathing of οὐ')],
}

# Side corrections from the checkers' notes (errors shared by both transcriptions), round 2; (ref, old, new, who, why)
SIDE = [('H 68v.15', 'τοιόν δὲ', 'τοιόνδε', 'both checkers (side notes, round 2)',
         'no accent is written over δε (the next accent is the circumflex of τῆς), so by the word-division rule it is one word'),
        ('H 70r.2', 'διαφορᾶ·', 'διαφορᾶι·', 'one checker (side note, round 2), confirmed by the assistant on a close-up',
         'an iota adscript is written after the α, as in ταῖς in the same line')]

def set_punct(text, k, mark):
    """Set the punctuation after word k (1-based) of an adopted line."""
    toks = text.split(' ')
    words = [i for i, t in enumerate(toks) if re.sub(r'[.·,:;]+$', '', t)]
    i = words[k - 1]
    toks[i] = re.sub(r'[.·,:;]+$', '', toks[i]) + mark
    return ' '.join(toks)

def editor_groups(pid):
    return ASSIST.get(pid, []) + [(d['diffs'], tuple(d['pick']) if isinstance(d['pick'], list) else d['pick'])
                                  for qid, d in ED.items() if qid.split('#')[0] == pid]

cl, meta = {}, {}
for f in ('h-a/h-a.json', 'h-b/h-b.json', 'h-c/h-c.json'):
    d = load_json(SP / 'wf2' / f)
    for fo in d['folios']:
        for l in fo['lines']:
            cl[(fo['folio'], l['n'])] = l['text']
            meta[(fo['folio'], l['n'])] = {k: l[k] for k in ('rubric', 'note') if l.get(k)}
gp = {(fo['folio'], l['n']): l['text'] for fo in G['h']['folios'] for l in fo['lines']}
w3p = {p['id']: p for g in ('h-a', 'h-b') for p in load_json(SP / 'wf3/places.json')['groups'][g]}
w3i = {it['id']: it for it in load_json(SP / 'wf3/decisions.json')}
k3 = load_json(SP / 'wf3/places-key.json')
w5p = {p['id']: p for g in ('h1', 'h2', 'h3', 'h4') for p in load_json(SP / f'wf5/{g}-A/places.json')['places']}
w5i = {it['id']: it for it in load_json(SP / 'wf5/decisions.json')}
k5 = load_json(SP / 'wf5/places-key.json')

def record(pid, place, item, key, picks, round_, groups):
    gd = {i for d, _ in groups for i in d}
    return [{'round': round_, 'difference': d,
             'pick': (pk if isinstance(pk, str) else 'other: ' + pk[1]),
             'right': key.get(pk, 'other') if isinstance(pk, str) else 'other',
             'by': ('assistant (delegated by the editor)' if i in ASSIST5.get(pid, {}) else 'assistant' if any(i in d for d, _ in ASSIST.get(pid, [])) else 'editor') if i in gd
                   else 'checkers' if r['status'] == 'decided' else 'open', 'reason': reason(r)}
            for i, (d, pk, r) in enumerate(zip(place['differences'], picks, item['rows']), 1)]

lines, decisions, pending, problems, assisted = [], [], [], [], set()
order = sorted(set(cl) | set(gp), key=lambda k: (int(k[0][:-1]), k[0][-1], k[1]))
for k in order:
    pid = f'H {k[0]}.{k[1]}'
    a, b = nfc5(cl.get(k)), nfc5(gp.get(k))
    e = {'folio': k[0], 'line': k[1], 'text': a, **meta.get(k, {})}
    rec = {'ref': pid, 'claude': a, 'gpt': b, 'differences': []}
    open_all = []
    if a == b:
        lines.append(e)
        continue
    if pid in w3p:
        p3, i3 = w3p[pid], w3i[pid]
        # the editor's own reading replaces letters only: round 1 compared the lines without punctuation
        grp = [(d, ('other', STRIP(pk[1])) if not isinstance(pk, str) else pk) for d, pk in editor_groups(pid)]
        letters, picks, open3 = adopt(p3, i3, char_ops, groups=grp, convention=h_convention, pre=STRIP)
        rec['differences'] += record(pid, p3, i3, k3[pid], picks, 1, grp)
        open_all += [('round 1', p3['differences'][i - 1]) for i in open3]
        # punctuation: from round 2 where the two disagreed, otherwise the common punctuation
        if pid in w5p:
            p5, i5 = w5p[pid], w5i[pid]
            ps, (rw, rp) = punct_slots(p5['reading_1'], p5['reading_2'])
            if len(ps) != len(p5['differences']):
                problems.append((pid, 'punctuation slots do not match the differences'))
            rp = list(rp)
            picks5 = []
            for (slot, x, y), row in zip(ps, i5['rows']):
                if row['status'] == 'decided' and row['choice'] in ('1', '2'):
                    rp[slot] = x if row['choice'] == '1' else y
                    picks5.append(row['choice'])
                elif row['status'] == 'decided' and row['choice'] == 'other':
                    rp[slot] = ''.join(c for c in row['A']['other'] if c in '.·,:;')
                    picks5.append(('other', row['A']['other']))
                elif (i5n := len(picks5) + 1) in ASSIST5.get(pid, {}):
                    pk = ASSIST5[pid][i5n]
                    rp[slot] = x if pk == '1' else y if pk == '2' else ''.join(c for c in pk[1] if c in '.·,:;')
                    picks5.append(pk)
                    assisted.add((pid, i5n))
                else:
                    open_all.append(('round 2', row['difference']))
                    picks5.append('1')
            rec['differences'] += record(pid, p5, i5, k5[pid], picks5, 2, [([i], None) for (q, i) in assisted if q == pid])
        else:
            rw, rp = slots(a)
        if letters is not None:
            text, lost = with_punct(letters, rw, rp)
            if lost:
                problems.append((pid, f'punctuation not placed: {lost}'))
            for k_, mark, cm, gm, why in POST.get(pid, []):
                text = set_punct(text, k_, mark)
                rec['differences'].append({'round': 'assistant', 'difference': f'punctuation after word {k_}: Claude «{cm or "—"}» / GPT «{gm or "—"}»',
                                           'pick': mark or '—', 'right': 'claude' if mark == cm else 'gpt' if mark == gm else 'other',
                                           'by': 'assistant (delegated by the editor)', 'reason': why})
            e['text'] = text
    elif pid in w5p:
        p5, i5 = w5p[pid], w5i[pid]
        grp = editor_groups(pid) + [([i], pk) for i, pk in ASSIST5.get(pid, {}).items()]
        text, picks, open5 = adopt(p5, i5, word_ops, groups=grp, convention=h_convention)
        rec['differences'] += record(pid, p5, i5, k5[pid], picks, 2, grp)
        open_all += [('round 2', p5['differences'][i - 1]) for i in open5]
        if text is not None:
            e['text'] = text
    else:
        problems.append((pid, 'differs but was in neither round'))
    for r_, old_, new_, who, why in SIDE:
        if r_ == pid and not open_all:
            assert old_ in e['text'], (pid, e['text'])
            e['text'] = e['text'].replace(old_, new_, 1)
            rec['differences'].append({'round': 'side note', 'difference': f'{old_} (both transcriptions) -> {new_}', 'pick': new_,
                                       'right': 'other', 'by': who, 'reason': why})
    if open_all:
        e['pending'] = True
        e['text'] = a
        pending.append({'ref': pid, 'open': open_all, 'claude': a, 'gpt': b})
        rec['adopted'] = None
    else:
        rec['adopted'] = e['text']
    if text_none := (e['text'] is None):
        problems.append((pid, 'no text'))
    decisions.append(rec)
    lines.append(e)

out = {
    'witness': 'H = Heidelberg, Cod. Pal. graec. 281 (Constantinople, AD 1040), ff. 64r-70r.7 (music) and 70r.8-22',
    'status': 'agreed text of two independent diplomatic transcriptions (Claude, workflow 2026-10-27; GPT-6 Astra, Codex 2026-10-27); '
              'every difference decided against the scans by two anonymised checkers in two rounds (2026-10-27/28), places they left open by the editor',
    'conventions': 'diplomatic: letters, accents, breathings, iota adscript and diaeresis as written; modern word division, but an accent written on '
                   'the first element separates the words (διὰ πασῶν); supplied letters of abbreviations in round brackets; red ink ⟦r …⟧; '
                   'underdot for an uncertain letter, [?] after a doubtful word; points: high ·, low or middle ., comma ,, double point :; '
                   'rubric crosses +; no line-end hyphens (the manuscript has none)',
    'lines_total': len(lines),
    'identical_in_both': len(lines) - len(decisions),
    'decided': sum(1 for d in decisions if d['adopted'] is not None),
    'pending_editor': pending,
    'lines': lines,
    'decisions': decisions,
}
for k_ in ('abbreviations', 'corrections', 'orthography', 'doubts'):
    out[f'{k_}_claude'] = [x for f in ('h-a', 'h-b', 'h-c') for x in (load_json(SP / f'wf2/{f}/{f}.json').get(k_) or [])] \
        if k_ != 'orthography' else [load_json(SP / f'wf2/{f}/{f}.json').get(k_) for f in ('h-a', 'h-b', 'h-c')]
out['gpt'] = {k_: G['h'].get(k_) for k_ in ('abbreviations', 'corrections', 'orthography', 'limitations', 'insertions_P')}
dump_json(out, sys.argv[2])
print('lines', len(lines), 'decisions', len(decisions), 'pending', [p['ref'] for p in pending])
print(Counter('+'.join(sorted({d['right'] for d in r['differences']})) for r in decisions))
for pr in problems:
    print('  !', pr)
