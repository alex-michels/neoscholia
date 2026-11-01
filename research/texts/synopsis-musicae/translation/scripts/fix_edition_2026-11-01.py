"""Corrections to the edition (constituted/text.json and text.md) found by the translation's fact-check (1.11.2026):
the missing apparatus entry for H at Bas. 31.10; Theon pp. 56.9-57.6 Hiller is not Adrastus; the overstated
'usual term' for a fifteen-note system. Usage: python -I fix_edition_2026-11-01.py <constituted folder>"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
C = sys.argv[1]
J = f'{C}/text.json'
d = json.load(open(J, encoding='utf-8'))
sec = {int(s['section']): s for s in d['sections']}

# 1. section 6 apparatus: H at Bas. 31.10 (first entry, text order)
app = sec[6]['apparatus']
assert app[0]['ref'] == 'Bas. 31.23' and not any(a['ref'] == 'Bas. 31.10' for a in app)
app.insert(0, {
    'ref': 'Bas. 31.10',
    'entry': 'ἐν μέσῳ Bas. Par. V] ἐμ̣μέσω H',
    'type': 'substitution (word division)',
    'note': "H 68v.9: after ἐ two μ-shaped letters without a space, but this scribe writes ν with a μ-like shape "
            "(ἐν later in the line; ἁρμονικὸν 69r.1), so the scan cannot separate ἐμμέσω from ἐν μέσω; the H "
            "transcription gives ἐμ̣μέσω with a dot (adjudicated). The text follows Bas. Par. V: τῶν ἐν μέσῳ διαστημάτων, "
            "'the intervals lying between', against which ἐμμέσω does not construe. The same confusion in P at Vinc. "
            "340.20, where the edition prints ἐμμέσων (section 5). Entry added 1.11.2026: the section 4 materials cited "
            "H's reading, but the apparatus lacked it (found in the fact-check of the translation)."})

# 2. and 3. wording in the apparatus notes and resolved doubts
n = 0


def walk(o):
    global n
    items = o.items() if isinstance(o, dict) else enumerate(o) if isinstance(o, list) else []
    for f, v in list(items):
        if isinstance(v, (dict, list)):
            walk(v)
            continue
        if not isinstance(v, str):
            continue
        new = v.replace(
                    'the usual term for a fifteen-note system is πεντεκαιδεκάχορδον (LSJ s.v. cites Adrastus in Theon of '
                    'Smyrna p. 64 H. and Ptolemy, Harmonics 3.1).',
                    'the word πεντεκαιδεκάχορδον is rare (LSJ s.v.: three attestations, "with fifteen strings"): Adrastus in '
                    'Theon of Smyrna uses it of the moderns\' fifteen-note scheme (p. 64.5-6 H.), Ptolemy of the '
                    'fifteen-string kanon on which the whole double-octave system can be set out (Harmonics 3.1, title and '
                    'opening). [Wording corrected 1.11.2026; it had called πεντεκαιδεκάχορδον "the usual term".]')
        new = new.replace(
            'Theon of Smyrna p. 56.9-57.6 Hiller (Adrastus)',
            'Theon of Smyrna p. 56.9-57.6 Hiller (Theon\'s own account, not Adrastus: Theon turns back to Adrastus '
            'only at 61.18-19, ἐπανέλθωμεν δὲ ἐπὶ τὰ ὑπὸ τοῦ Ἀδράστου παραδεδομένα; corrected 1.11.2026)')
        if new != v:
            o[f] = new
            n += 1


walk(d)
assert n == 2, n
json.dump(d, open(J, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

M = f'{C}/text.md'
md = open(M, encoding='utf-8').read()
old = '- Bas. 31.23: ἡ H Xyl.] ἢ Bas. Par. V'
assert md.count(old) == 1
md = md.replace(old, '- Bas. 31.10: ἐν μέσῳ Bas. Par. V] ἐμ̣μέσω H\n' + old)
open(M, 'w', encoding='utf-8').write(md)
print('apparatus entry added; wording corrected in', n, 'places')
