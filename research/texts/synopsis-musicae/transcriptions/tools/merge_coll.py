"""Paris 1545 (Par.) and Vat. Pal. gr. 262 (V): Claude's full transcriptions, corrected by the decided collation disputes,
with both sides' variant lists. GPT-6 collated these witnesses against Bas. without transcribing them in full.
Usage: python -I merge_coll.py <scratchpad> <out dir> [editor decisions json]"""
import ast, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
SP = Path(sys.argv[1])
sys.path.insert(0, str(SP))
from merge_lib import nfc, load_json, dump_json, reason
OUT = Path(sys.argv[2])
ED = load_json(sys.argv[3]) if len(sys.argv) > 3 else {}
G = load_json(str(Path(__file__).resolve().parents[6] / 'Neoscholia-runs' / 'synopsis-musicae-greek' / 'transcription-gpt-6-astra.json'))
items = {it['id']: it for it in load_json(SP / 'wf3/decisions.json') if it['group'] == 'coll'}
key = load_json(SP / 'wf3/places-key.json')

# line corrections that follow from the decided disputes (witness line, old, new); checked by hand against the decisions
LINE_FIX = {'V': [('81v.1', 'ἡ ἁρμονία', 'ἢ ἁρμονία')],
            # a checker's side note, confirmed on a close-up: the point after παιήων is raised (those after ὑμέναιος, ἐξόδιος are low)
            'Par': [('27r.16', 'παιήων.', 'παιήων·', "a checker's side note, confirmed by the assistant on a close-up")]}
# collation entries of Claude's list refuted by the decisions: (witness, Bas. ref)
REFUTED = {('V', 'Bas. 31.23'): 'V has ἢ ἁρμονία as Bas. (both checkers, high confidence): no variant.'}

def disputes(w):
    out = []
    for pid, it in items.items():
        if not pid.startswith(w + ' '):
            continue
        who = key[pid]
        rows = it['rows']
        ed = {i: d['pick'] for qid, d in ED.items() if qid.split('#')[0] == pid for i in d['diffs']}
        res = []
        for i, r in enumerate(rows, 1):
            pick = ed.get(i) or (r['choice'] if r['status'] == 'decided' else None)
            res.append({'difference': r['difference'], 'pick': pick, 'right': who.get(pick, 'other') if pick else 'pending (editor)',
                        'by': 'editor' if i in ed else 'checkers' if r['status'] == 'decided' else 'open', 'reason': reason(r)})
        notes = {k: v for qid, d in ED.items() if qid.split('#')[0] == pid for k, v in d.items() if k in ('comment', 'checker_note')}
        out.append({'place': it['ref'], 'reading_1': it['reading_1'], 'reading_2': it['reading_2'], 'reading_1_is': who['1'],
                    'context': it['context'], 'differences': res, **({'editor_' + k: v for k, v in notes.items()})})
    return out

def fix_lines(w, lines):
    for ref, old, new, *why in LINE_FIX.get(w, []):
        e = next(l for l in lines if l['ref'] == ref)
        assert old in e['text'], (ref, e['text'])
        e['text'] = e['text'].replace(old, new, 1)
        e['corrected'] = f"{old} -> {new} ({why[0] if why else 'collation dispute decided against the scan'})"

def coll(w, d):
    out = []
    for e in d['collation']:
        e = dict(e)
        if (w, e['ref']) in REFUTED:
            e['refuted'] = REFUTED[(w, e['ref'])]
        out.append(e)
    return out

cmp_rows = {w: load_json(SP / f'wf3/cmp-coll-{w.lower()}.json')['rows'] for w in ('Par', 'V')}
gcoll = lambda w: [{k: e.get(k) for k in ('id', 'ref', 'lemma', 'Bas', w, 'type', 'note')} for e in G['collation'] if e.get(w)]

# ---------- Par. ----------
tree = ast.parse(open(SP / 'wf2/par/build.py', encoding='utf-8').read())
pages = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'pages')
pc = load_json(SP / 'wf2/par/par-collation.json')
lines = [{'ref': f, 'n': i, 'text': nfc(t)} for f, txt in pages.items() for i, t in enumerate(txt.split('\n'), 1)]
for l in lines:
    l['ref'] = f"{l['ref']}.{l['n']}"
fix_lines('Par', lines)
par = {
    'witness': 'Paris 1545 (Bogardus), Greek text of the music section, ff. 20v-27v',
    'status': 'full transcription by Claude (workflow 2026-10-27); GPT-6 Astra collated Par. against Bas. independently (Codex 2026-10-27) '
              'without a full transcription; 18 of its variant claims agree with this transcription, the 7 that did not were decided against '
              'the scans by two anonymised checkers (2026-10-27)',
    'conventions': 'as printed: ligatures and compendia expanded silently; accents, breathings, punctuation and misprints as printed; physical line numbers',
    'lines_total': len(lines), 'lines': [{'ref': f"Par. {l['ref']}", 'text': l['text'], **({'corrected': l['corrected']} if 'corrected' in l else {})} for l in lines],
    'disputes': disputes('Par'),
    'collation_claude': coll('Par', pc), 'collation_gpt': gcoll('Par'), 'collation_compared': cmp_rows['Par'],
    **{k: pc[k] for k in ('extent', 'three_places', 'page_map', 'margins', 'orthographica', 'doubts', 'xylander_supplements')},
    'basel_corrections_proposed_by_collator': pc['bas_corrections'],
}
dump_json(par, OUT / 'par1545-greek.json')

# ---------- V ----------
vc = load_json(SP / 'wf2/v/v-collation.json')
vl = []
for raw in open(SP / 'wf2/v/v-lines.txt', encoding='utf-8'):
    if '\t' in raw:
        r, t = raw.rstrip('\n').split('\t', 1)
        t = nfc(t)
        if '...' not in t:  # a stray space before a point (76v.18); lines with [...] are left as they are
            t = re.sub(r'\s+([,.·:;])', r'\1', t)
        vl.append({'ref': r, 'text': t})
fix_lines('V', vl)
pend = [d for d in disputes('V') if any(x['pick'] is None for x in d['differences'])]
v = {
    'witness': 'Vat. Pal. gr. 262 (15th c.), ff. 75r-82v (music from 75r.12)',
    'status': 'full transcription by Claude (workflow 2026-10-27); GPT-6 Astra collated V against Bas. independently (Codex 2026-10-27) '
              'without a full transcription; 28 of its variant claims agree with this transcription, the 15 that did not were decided against '
              'the scans by two anonymised checkers (2026-10-27), places they left open by the editor',
    'conventions': 'diplomatic: letters, accents, breathings as written; abbreviations expanded with supplied letters in round brackets; red ink ⟦r …⟧; '
                   'lines of the preceding arithmetic marked [arithmetic]; physical line numbers',
    'lines_total': len(vl), 'lines': [{'ref': f"V {l['ref']}", 'text': l['text'], **({'corrected': l['corrected']} if 'corrected' in l else {})} for l in vl],
    'pending_editor': pend,
    'disputes': disputes('V'),
    'collation_claude': coll('V', vc), 'collation_gpt': gcoll('V'), 'collation_compared': cmp_rows['V'],
    **{k: vc[k] for k in ('extent', 'three_places', 'page_map', 'margins', 'xylander_marginalia_check', 'orthographica', 'doubts')},
    'basel_corrections_proposed_by_collator': vc['bas_corrections'],
    'v_corrections_gpt': G['v_corrections_note'],
}
dump_json(v, OUT / 'vat-pal-gr-262-greek.json')
print('Par lines', len(lines), 'disputes', len(par['disputes']), '| V lines', len(vl), 'disputes', len(v['disputes']), 'pending', [p['place'] for p in pend])
for w, d in (('Par', par), ('V', v)):
    for x in d['disputes']:
        print(' ', x['place'], [(y['right'], y['by']) for y in x['differences']])
