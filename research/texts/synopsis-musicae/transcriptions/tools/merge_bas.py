"""Merge the two Basel 1556 Greek transcriptions (Claude, GPT-6) with the decisions of round 1 (wf3) and the editor.
Usage: python -I merge_bas.py <scratchpad> <out json> [editor decisions json]"""
import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
SP = Path(sys.argv[1])
sys.path.insert(0, str(SP))
from merge_lib import nfc, norm_cmp, char_ops, adopt, load_json, dump_json, reason
REPO = Path(__file__).resolve().parents[2]
G = load_json(str(Path(__file__).resolve().parents[6] / 'Neoscholia-runs' / 'synopsis-musicae-greek' / 'transcription-gpt-6-astra.json'))
ED = load_json(sys.argv[3]) if len(sys.argv) > 3 else {}

C = [load_json(REPO / f'transcriptions/claude/basel1556-greek-{p}.json') for p in ('p23-26', 'p27-30', 'p31-33')]
cl = [l for c in C for l in c['lines']]
gp = {(p['page'], l['n']): l['text'] for p in G['bas']['pages'] for l in p['lines']}
places = {p['id']: p for g in ('bas-a', 'bas-b') for p in load_json(SP / 'wf3/places.json')['groups'][g]}
items = {it['id']: it for it in load_json(SP / 'wf3/decisions.json')}
key = load_json(SP / 'wf3/places-key.json')

def editor_overrides(pid):
    """Editor decisions for this place, as {difference index: pick}; from 'qid' entries {'diffs': [...], 'pick': ...}."""
    out = {}
    for qid, d in ED.items():
        if qid.split('#')[0] == pid:
            for i in d['diffs']:
                out[i] = d['pick']
    return out

# Line-end hyphens only where printed (as in the merged Xylander): Claude's notes list the breaks where it added one by rule;
# at 25.8 both checkers saw none (side notes, round 1).
NO_HYPHEN = {(n['page'], n['line']) for c in C for n in c['notes'] if n['what'] == 'hyphen not printed'} | {(25, 8)}
# Side corrections from the checkers' notes, confirmed by the editor's assistant on a close-up (2026-10-28):
# (ref, old, new, why)
SIDE = [('Bas. 29.24', 'φθόγγων οὐ', 'φθόγγων οὒ',
         'over the ου-ligature both checkers saw a smooth breathing and a grave; the editor chose the word (οὐ, not ἢ), the diacritics are as printed')]
hyphens_removed = []
lines, decisions, pending, mismatch = [], [], [], []
for l in cl:
    ref = f"Bas. {l['page']}.{l['line']}"
    c_text, g_text = l['text'], gp.get((l['page'], l['line']))
    entry = {'page': l['page'], 'line': l['line'], 'text': None}
    for k in ('heading', 'para_start'):
        if l.get(k):
            entry[k] = True
    if ref in places:
        p, it = places[ref], items[ref]
        text, picks, open_ = adopt(p, it, char_ops, overrides=editor_overrides(ref))
        who = key[ref]
        if open_:
            entry['text'] = norm_cmp(c_text, keep_red=True)
            entry['pending'] = True
            pending.append({'ref': ref, 'open_differences': [p['differences'][i - 1] for i in open_],
                            'reading_1': p['reading_1'], 'reading_2': p['reading_2'], 'reading_1_is': who['1']})
        else:
            entry['text'] = text
        right = sorted({who[x] if x in ('1', '2') else 'other' for x in picks})
        decisions.append({'ref': ref, 'claude': norm_cmp(c_text), 'gpt': norm_cmp(g_text), 'adopted': entry['text'] if not open_ else None,
                          'right': '+'.join(right) if not open_ else 'pending (editor)',
                          'differences': [{'difference': d, 'pick': (pk if isinstance(pk, str) else 'other: ' + pk[1]),
                                           'by': ('editor' if i in editor_overrides(ref) else 'checkers' if r['status'] == 'decided' else 'open'),
                                           'reason': reason(r)}
                                          for i, (d, pk, r) in enumerate(zip(p['differences'], picks, it['rows']), 1)]})
        for qid, d in ED.items():
            if qid.split('#')[0] == ref:
                decisions[-1].update({'editor_' + k: v for k, v in d.items() if k in ('comment', 'checker_note')})
    else:
        if norm_cmp(c_text) != norm_cmp(g_text):
            mismatch.append((ref, c_text, g_text))
        entry['text'] = norm_cmp(c_text, keep_red=True)
    if (l['page'], l['line']) in NO_HYPHEN and entry['text'].endswith('-'):
        entry['text'] = entry['text'][:-1]
        hyphens_removed.append(ref)
        if decisions and decisions[-1]['ref'] == ref and decisions[-1]['adopted']:
            decisions[-1]['adopted'] = entry['text']
    for r_, old_, new_, why in SIDE:
        if r_ == ref:
            assert old_ in entry['text'], (ref, entry['text'])
            entry['text'] = entry['text'].replace(old_, new_, 1)
            d_ = next(d for d in decisions if d['ref'] == ref)
            d_['adopted'] = entry['text']
            d_['differences'].append({'difference': f'{old_} -> {new_}', 'pick': new_, 'right': 'other', 'by': 'assistant (from both checkers notes)', 'reason': why})
    lines.append(entry)

# the margin questions (both transcriptions record the notes; the checkers confirm them)
margin_checks = []
for pid in ('Bas. 31.23 margin', 'Bas. 32.23 margin'):
    it = items[pid]
    margin_checks.append({'ref': pid, 'confirmed': all(r['status'] == 'decided' and key[pid][r['choice']] == 'collator' for r in it['rows']),
                          'seen': reason(it['rows'][0])})

out = {
    'witness': 'Basel 1556 (Oporinus), Greek text of the music section, pp. 23-33',
    'status': 'agreed text of two independent transcriptions (Claude, workflow 2026-10-26/27; GPT-6 Astra, Codex 2026-10-27); '
              'every difference decided against the scans by two anonymised checkers (2026-10-27), places they left open by the editor',
    'conventions': 'as printed: ligatures and contractions expanded silently; accents, breathings, punctuation and misprints as printed; '
                   "Xylander's asterisks and daggers kept in the line; line-end hyphens only where printed (as in the merged Xylander); elision mark ’; high point ·",
    'hyphens_not_printed_removed': hyphens_removed,
    'lines_total': len(lines),
    'identical_in_both': len(lines) - len(decisions),
    'decided': sum(1 for d in decisions if d['adopted'] is not None),
    'pending_editor': pending,
    'lines': lines,
    'decisions': decisions,
    'marginal_notes_confirmed': margin_checks,
    'notes_claude': [n for c in C for n in c['notes']],
    # GPT's proposed corrections ('reading', 'why') are kept out until Claude has constituted its own text independently
    'notes_gpt': {'misprints_printed': [{k: m.get(k) for k in ('ref', 'printed', 'category')} for m in G['bas']['misprints']],
                  **{k: G['bas'][k] for k in ('marginalia', 'expansions', 'diagrams')}},
}
dump_json(out, sys.argv[2])
print('lines', len(lines), 'decisions', len(decisions), 'pending', [p['ref'] for p in pending], 'mismatch outside places', len(mismatch))
for m in mismatch:
    print('  !', m)
from collections import Counter
print(Counter(d['right'] for d in decisions))
