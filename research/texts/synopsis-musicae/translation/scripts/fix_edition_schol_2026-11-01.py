"""Bas. 33.15 corrected after the comparison with Mizler (1746), 1.11.2026. Bas. and Par. print σχολαιοτέραις with the
σχ-ligature, which resembles χ. Compared at enlargement with σχέσις (Bas. 24.16, Par. 21r) and with plain χ (ταχιναῖς on
the same line). Alard 1636 (p. 188) and Mizler 1746 (p. 200) print the same ligature. Both first transcriptions of Bas.
had σχολαιοτέραις; the collator of Par. and then the checkers took the ligature for χ. So there is no variant: the
apparatus entry and the departure at 33.15 are withdrawn, and the diplomatic lines of Bas. and Par. are corrected.
Usage: python -I fix_edition_schol_2026-11-01.py <synopsis-musicae folder>"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
R = sys.argv[1]
WHY = ('σχολαιοτέραις is printed with the σχ-ligature (a closed loop at the upper left of χ), the same sort as in σχέσις '
       '(Bas. 24.16, Par. 21r); plain χ, as in ταχιναῖς on the same line, has no loop. Re-examined 1.11.2026 at '
       'enlargement, prompted by the comparison with Mizler 1746; Alard 1636 (p. 188) and Mizler (p. 200) print the same '
       'ligature.')


def load(p):
    return json.load(open(f'{R}/{p}', encoding='utf-8'))


def save(p, d):
    json.dump(d, open(f'{R}/{p}', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def sub(s, old, new):
    assert s.count(old) == 1, ('not once', old[:70], s.count(old))
    return s.replace(old, new)


# 1. constituted/text.json
T = load('constituted/text.json')
s7 = [s for s in T['sections'] if int(s['section']) == 7][0]
n = len(s7['apparatus'])
s7['apparatus'] = [a for a in s7['apparatus'] if a['ref'] != 'Bas. 33.15']
assert len(s7['apparatus']) == n - 1
n = len(s7['departures'])
s7['departures'] = [d for d in s7['departures'] if d['ref'] != 'Bas. 33.15']
assert len(s7['departures']) == n - 1
d33 = [d for d in s7['departures'] if d['ref'] == 'Bas. 33.14'][0]
d33['reason'] = sub(d33['reason'],
                    'it shares χολαιοτέραις (33.15) with Par. against H V, and τὸ (32.23) with Par. V against H.',
                    'it shares τὸ (32.23) with Par. V against H, and five readings with Par. against H V (25.22 ἔχον, '
                    '25.24 οἷον, 29.14 without δίς, 29.21 τὸ, 31.5 διάτασιν).')
rd = [r for r in s7['resolved_doubts'] if r['ref'] == 'Bas. 33.15'][0]
rd['resolution'] = ('Revised 1.11.2026: option (b), and Par. agrees. ' + WHY + ' There is no variant; the apparatus entry '
                    'and the departure are withdrawn. The earlier resolution (Bas. without σ, "both checkers, high '
                    'confidence") mistook the ligature for χ.')
for wit in ('Bas', 'Par'):
    s7['orthographica'][wit] = s7['orthographica'][wit].rstrip() + (
        ' σχολαιοτέραις (33.15) is printed with the σχ-ligature, which resembles χ.' if wit == 'Bas' else
        ' σχολαιοτέραις (27r.20) is printed with the σχ-ligature, which resembles χ.')
T['status'] = T['status'].rstrip('.') + ('. Correction of 1.11.2026, from the comparison with Mizler (1746): Bas. and Par. '
                                         'print σχολαιοτέραις with a σχ-ligature at 33.15, so the apparatus entry there and '
                                         'the departure are withdrawn.')
assert not any('χολαιοτέραις Bas.' in a['entry'] for s in T['sections'] for a in s['apparatus'])
save('constituted/text.json', T)

# 2. constituted/text.md
p = f'{R}/constituted/text.md'
md = open(p, encoding='utf-8').read()
md = sub(md, '- Bas. 33.15: σχολαιοτέραις H V] χολαιοτέραις Bas. Par.\n', '')
md = sub(md, 'πεντεκαιδεκάχορδον — редкое слово, а не «обычное название»).*',
         'πεντεκαιδεκάχορδον — редкое слово, а не «обычное название»). Исправление 1.11.2026, по итогам сверки с Мицлером '
         '(1746): в Bas. и Par. при 33.15 напечатано σχολαιοτέραις с лигатурой σχ, похожей на χ, поэтому запись аппарата '
         'и отступление от Bas. в этом месте сняты.*')
open(p, 'w', encoding='utf-8').write(md)

# 3. transcriptions: the diplomatic lines of Bas. and Par.
B = load('transcriptions/basel1556-greek.json')


def walk(o, fix):
    global hits
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str) and v in fix:
                o[k] = fix[v]
                hits += 1
            else:
                walk(v, fix)
    elif isinstance(o, list):
        for v in o:
            walk(v, fix)


hits = 0
walk(B, {'καὶ ταῖς χολαιοτέραις καὶ ταχιναῖς μετα-': 'καὶ ταῖς σχολαιοτέραις καὶ ταχιναῖς μετα-'})
assert hits == 2, hits  # the line and the adjudication's adopted reading
found = 0  # the footnote on the lemma and the adjudication record


def fixnote(o):
    global found
    if isinstance(o, dict):
        if o.get('ref') == 'Bas. 33.15' and o.get('lemma') == 'χολαιοτέραις':
            o['lemma'] = 'σχολαιοτέραις'
            o['ru'] = ('«σχολαιοτέραις» — так напечатано и так в транскрипциях Claude и GPT-6: первая литера — лигатура σχ, '
                       'похожая на χ (замкнутая петля слева вверху, как в σχέσις, Bas. 24.16; у простого χ в ταχιναῖς той '
                       'же строки петли нет). Сверщик Парижского издания и затем оба проверяющих приняли её за χ; ошибка '
                       'исправлена 1.11.2026 при сверке с Мицлером (1746). В Par. 27r.20 та же лигатура.')
            o['en'] = ('«σχολαιοτέραις», as printed and as in the transcriptions of Claude and GPT-6: the first sort is the '
                       'σχ-ligature, which resembles χ (a closed loop at the upper left, as in σχέσις, Bas. 24.16; plain χ '
                       'in ταχιναῖς on the same line has none). The collator of the Paris edition and then both checkers '
                       'took it for χ; corrected 1.11.2026 in the comparison with Mizler (1746). Par. 27r.20 has the same '
                       'ligature.')
            found += 1
        if o.get('ref') == 'Bas. 33.15' and o.get('adopted') == 'καὶ ταῖς σχολαιοτέραις καὶ ταχιναῖς μετα-':
            o['correction_2026_11_01'] = 'The checkers\' pick (2) is withdrawn: the print has the σχ-ligature. ' + WHY
            found += 1
        for v in o.values():
            fixnote(v)
    elif isinstance(o, list):
        for v in o:
            fixnote(v)


fixnote(B)
assert found == 2, found
save('transcriptions/basel1556-greek.json', B)

P = load('transcriptions/par1545-greek.json')
hits = 0
walk(P, {'φορᾷ. ἀλλὰ καὶ ταῖς χολαιοτέραις·': 'φορᾷ. ἀλλὰ καὶ ταῖς σχολαιοτέραις·'})
assert hits == 1, hits
found = 0


def fixcoll(o):
    global found
    if isinstance(o, dict):
        if o.get('ref') == 'Bas. 33.15' and o.get('printed') == 'ταῖς χολαιοτέραις':
            o['printed'] = 'ταῖς σχολαιοτέραις'
            o['note'] = ('Withdrawn 1.11.2026: Bas. and Par. 27r.20 both print the σχ-ligature, which resembles χ, so our '
                         'text agrees with the print. ' + WHY)
            found += 1
        for v in o.values():
            fixcoll(v)
    elif isinstance(o, list):
        for v in o:
            fixcoll(v)


fixcoll(P)
assert found == 1, found
save('transcriptions/par1545-greek.json', P)

# 4. the two READMEs and the Xylander dossier
for path, old, new in [
    ('transcriptions/README.md',
     '- **Базель 33.15.** Напечатано «χολαιοτέραις», без σ. Ошибку обеих транскрипций заметил сверщик Парижа 1545, где слово тоже без σ.\n',
     '- **Базель 33.15.** Здесь были правы обе транскрипции: напечатано «σχολαιοτέραις» с лигатурой σχ, похожей на χ. Сверщик '
     'Парижа 1545 и оба проверяющих приняли её за χ; ошибка найдена 1.11.2026 при сверке с Мицлером (1746). В Париже та же '
     'лигатура.\n'),
    ('constituted/README.md',
     'Он разделяет с Par. опечатку «χολαιοτέραις» (33.15) и ещё пять чтений против H и V',
     'Он разделяет с Par. пять чтений против H и V'),
    ('../../studies/xylander/dossier.md',
     'проверить хотя бы общие места: 25.24 οἷον, 33.15 χολαιοτέραις.',
     'проверить хотя бы общие места: 25.24 οἷον (33.15 «χολαιοτέραις» снято: в Bas. и Par. напечатано σχολαιοτέραις с '
     'лигатурой σχ, 1.11.2026).'),
]:
    q = f'{R}/{path}'
    s = open(q, encoding='utf-8').read()
    open(q, 'w', encoding='utf-8').write(sub(s, old, new))
print('edition, transcriptions and READMEs corrected')
