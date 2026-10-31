"""Merge the two transcriptions of Vincent 1847 (Greek fragments of Paris. gr. 2448 with notes) and of Vinet 1591 (Latin)
with the checkers' decisions (wf4) and the editor's.
Usage: python -I merge_vv.py <scratchpad> <out dir> [editor decisions json]"""
import re, sys
from collections import Counter
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
SP = Path(sys.argv[1])
sys.path.insert(0, str(SP))
from merge_lib import nfc, norm_cmp, char_ops, adopt, load_json, dump_json, reason
OUT = Path(sys.argv[2])
ED = load_json(sys.argv[3]) if len(sys.argv) > 3 else {}
G = load_json(str(Path(__file__).resolve().parents[6] / 'Neoscholia-runs' / 'synopsis-musicae-greek' / 'transcription-gpt-6-astra.json'))
L = load_json(str(Path(__file__).resolve().parents[6] / 'Neoscholia-runs' / 'synopsis-musicae-latin' / 'transcription-latin-gpt-6-astra.json'))
places = {p['id']: p for g in ('vincent', 'vinet') for p in load_json(SP / f'wf4/{g}-A/places.json')['places']}
items = {it['id']: it for it in load_json(SP / 'wf4/decisions.json')}
key = load_json(SP / 'wf4/places-key.json')

# Corrections of convention by the editor's assistant (documented in the output): the q-acute sort is printed at 41.15
# as at 47.7 (both checkers saw it); accents are kept as printed, so it stays q́ue in both places.
ASSIST = {'Vinet 41.15': {2: ('other', 'ipsaq́ue')}}

def overrides(pid):
    out = dict(ASSIST.get(pid, {}))
    for qid, d in ED.items():
        if qid.split('#')[0] == pid:
            for i in d['diffs']:
                out[i] = d['pick']
    return out

def ws(s):
    return re.sub(r'\s+', ' ', nfc(s)).strip()

def vnorm(s):
    """Vinet spacing convention (as in the merged Xylander): no space before , . ; : and one space after , ; : . before a letter."""
    s = ws(s)
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    return re.sub(r'([,;:.])(?=[^\s\d.,;:\-)])', r'\1 ', s)

def decide(pid, who, c_text, g_text, post=lambda s: s):
    p, it = places[pid], items[pid]
    ov = overrides(pid)
    text, picks, open_ = adopt(p, it, char_ops, overrides=ov, convention=lambda pl, i: '1')
    right = sorted({who[x] if x in ('1', '2') else 'other' for x in picks})
    rec = {'ref': pid, 'claude': c_text, 'gpt': g_text, 'adopted': post(text) if not open_ else None,
           'right': '+'.join(right) if not open_ else 'pending (editor)',
           'differences': [{'difference': d, 'pick': (pk if isinstance(pk, str) else 'other: ' + pk[1]),
                            'by': (('assistant' if i in ASSIST.get(pid, {}) else 'editor') if i in ov else 'checkers' if r['status'] == 'decided' else 'open'), 'reason': reason(r)}
                           for i, (d, pk, r) in enumerate(zip(p['differences'], picks, it['rows']), 1)]}
    for qid, d in ED.items():
        if qid.split('#')[0] == pid:
            rec.update({'editor_' + k: v for k, v in d.items() if k in ('comment', 'checker_note')})
    pend = None if not open_ else {'ref': pid, 'open_differences': [p['differences'][i - 1] for i in open_],
                                   'reading_1': p['reading_1'], 'reading_2': p['reading_2'], 'reading_1_is': who['1']}
    return rec, pend

# ---------- Vincent ----------
V = load_json(SP / 'wf2/vincent/vincent.json')
gl = {}
gn = {}
for fr in G['p_fragments']:
    for l in fr['lines']:
        pg, n = l['ref'].split()[1].split('.')
        gl[(int(pg), int(n))] = l['text']
    for n in fr['footnotes']:
        gn[n['ref']] = n['text']
pages, decisions, pending, mism = [], [], [], []
for p in V['pages']:
    pl, pf = [], []
    for l in p['lines']:
        ref = f"Vinc. {p['page']}.{l['n']}"
        c, g = l['text'], gl.get((p['page'], l['n']))
        e = {'n': l['n'], 'kind': l.get('kind'), 'text': ws(c)}
        if ref in places:
            rec, pend = decide(ref, key[ref], ws(c), ws(g))
            decisions.append(rec)
            if pend:
                pending.append(pend); e['pending'] = True
            else:
                e['text'] = rec['adopted']
        elif norm_cmp(c) != norm_cmp(g):
            mism.append((ref, c, g))
        pl.append(e)
    for n in p['footnotes']:
        ref, c, g = n['ref'], n['text'], gn.get(n['ref'])
        e = {'ref': ref, 'text': ws(c)}
        if ref in places:
            who = key[ref]
            rec, pend = decide(ref, who, ws(c), ws(g))
            decisions.append(rec)
            if pend:
                pending.append(pend); e['pending'] = True
            else:
                e['text'] = rec['adopted']
        elif norm_cmp(c) != norm_cmp(g):
            mism.append((ref, c, g))
        pf.append(e)
    pages.append({'page': p['page'], 'lines': pl, 'footnotes': pf})
for rec in decisions:  # 340 n. 4: the place checked both new readings against my first reading
    if rec['ref'] == 'Vinc. 340 n. 4':
        rec['note'] = 'Both independent transcriptions read κεκρυμμένων; checked against the first reading (κεχρυμμένων) of vincent1847-fragments.md.'
vout = {
    'witness': 'A.-J.-H. Vincent, Notices et extraits des manuscrits 16.2 (Paris 1847), pp. 338, 340, 342: the three places of Paris. gr. 2448 (P)',
    'status': 'agreed text of two independent transcriptions (Claude, workflow 2026-10-27; GPT-6 Astra, Codex 2026-10-27); '
              'every difference decided against the scans by two anonymised checkers (2026-10-27), places they left open by the editor',
    'conventions': 'as printed, misprints included; ligatures resolved silently; footnote numbers as superscripts; elision mark ’; high point ·; French spacing as printed',
    'lines_total': sum(len(p['lines']) for p in pages), 'footnotes_total': sum(len(p['footnotes']) for p in pages),
    'pending_editor': pending, 'pages': pages, 'decisions': decisions,
    'fragments_claude': V['fragments'], 'doubts_claude': V['doubts'],
    'gpt': {k: [{kk: fr.get(kk) for kk in ('n', 'heading', 'provenance', 'line_count_note')} for fr in G['p_fragments']] for k in ('fragments',)},
    'insertion_points_gpt': G['insertion_points'],
}
dump_json(vout, OUT / 'vincent1847-fragments.json')
print('Vincent: lines', vout['lines_total'], 'footnotes', vout['footnotes_total'], 'decisions', len(decisions), Counter(d['right'] for d in decisions),
      'pending', [p['ref'] for p in pending], 'mismatch', len(mism))
for m in mism:
    print('  !', m)

# ---------- Vinet ----------
cv = []
for part in ('vinet-1', 'vinet-2'):
    d = load_json(SP / f'wf2/{part}/{part}.json')
    for p in d['pages']:
        for l in p['lines']:
            cv.append((p, l))
gv = {(p['page'], l['n']): l['text'] for p in L['vinet']['pages'] for l in p['lines']}
lines, decisions, pending, mism = [], [], [], []
for p, l in cv:
    ref = f"Vinet {p['page']}.{l['n']}"
    c, g = l['text'], gv.get((p['page'], l['n']))
    e = {'page': p['page'], 'line': l['n'], 'text': vnorm(c)}
    if l.get('para_no'):
        e['para_no'] = l['para_no']
    if ref in places:
        rec, pend = decide(ref, key[ref], ws(c), ws(g), post=vnorm)
        decisions.append(rec)
        if pend:
            pending.append(pend); e['pending'] = True
        else:
            e['text'] = rec['adopted']
    elif vnorm(c) != vnorm(g):
        mism.append((ref, vnorm(c), vnorm(g)))
    lines.append(e)
d1, d2 = load_json(SP / 'wf2/vinet-1/vinet-1.json'), load_json(SP / 'wf2/vinet-2/vinet-2.json')
nout = {
    'witness': 'Élie Vinet, Latin translation, Tournon 1591, pp. 41-53',
    'status': 'agreed text of two independent transcriptions (Claude, workflow 2026-10-27; GPT-6 Astra, Codex 2026-10-27); '
              'every difference decided against the scans by two anonymised checkers (2026-10-27), places they left open by the editor',
    'conventions': 'diplomatic, as printed: long s -> s; ligatures resolved; abbreviations expanded silently (& -> et, nasal stroke -> m/n); '
                   'the q-acute sort kept as q́ue; u/v, i/j, accents, capitals and misprints as printed; printed hyphens kept; '
                   'spacing normalised as in the merged Xylander (no space before punctuation, one after)',
    'lines_total': len(lines), 'identical_after_spacing': len(lines) - len(decisions),
    'pending_editor': pending, 'lines': lines, 'decisions': decisions,
    'pages_meta_claude': [{k: p.get(k) for k in ('page', 'running_head', 'signature', 'catchword', 'margins', 'figures')} for d in (d1, d2) for p in d['pages']],
    'chapters_claude': d1['chapters'] + d2['chapters'],
    'abbreviations_claude': d1['abbreviations'] + d2['abbreviations'],
    'doubtful_expansions_claude': d1['doubtful_expansions'] + d2['doubtful_expansions'],
    'misprints_claude': d1['misprints'] + d2['misprints'],
    'gpt': {k: L['vinet'].get(k) for k in ('chapters', 'abbreviations', 'doubtful_expansions', 'misprints')},
    'alignment_with_xylander_gpt': L['alignment'],
}
dump_json(nout, OUT / 'vinet1591-latin.json')
print('Vinet: lines', len(lines), 'decisions', len(decisions), Counter(d['right'] for d in decisions), 'pending', [p['ref'] for p in pending], 'mismatch', len(mism))
for m in mism:
    print('  !', m)
