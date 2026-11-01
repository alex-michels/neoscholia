"""Corrections found by the adversarial check of the editor's answers (1.11.2026), in the unpacked units and in the
edition. Usage: python -I fix_after_verify_2026-11-01.py <work folder> <constituted folder>"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
F, C = sys.argv[1] + '/compose/final', sys.argv[2]


def sub(s, old, new, label):
    assert s.count(old) == 1, f'{label}: «{old[:60]}» found {s.count(old)} times'
    return s.replace(old, new)


def unit_fix(uid, n, field, old, new):
    p = f'{F}/{uid}.json'
    u = json.load(open(p, encoding='utf-8'))
    nt = u['notes'][n - 1]
    nt[field] = sub(nt[field], old, new, f'{uid} note {n} {field}')
    json.dump(u, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


# U050 note 3: Adrastus in Theon; the length and the width of the holes; "distance" is the missing sense
unit_fix('U050', 3, 'ru',
         'Переведено «расширение»: абзац пересказывает Теона Смирнского, у которого духовые звучат ниже от длины и от ширины '
         'отверстий (τὴν εὐρύτητα τῶν τρημάτων, «ширину отверстий», с. 66.7–8 Hiller); «длина авлосов» и «расширение '
         'отверстий» в P отвечают этим двум причинам. Понимание «протяжённость [трубки] до отверстий» лексически не '
         'подкреплено и повторяло бы длину.',
         'Переведено «расширение»: абзац пересказывает Адраста у Теона Смирнского, у которого более низкие звуки духовых '
         'объясняются длиной и шириной отверстий (διὰ τὸ μῆκος καὶ τὴν εὐρύτητα τῶν τρημάτων, с. 66.6–8 Hiller); длину P '
         'относит к самим авлосам (τοῦ μήκους … τῶν αὐλῶν), так что διάτασις отвечает ширине отверстий. Понимание '
         '«протяжённость [трубки] до отверстий» требует значения «расстояние», которого у слова нет, и повторяло бы длину.')
unit_fix('U050', 3, 'en',
         'It is rendered “widening”: the paragraph summarises Theon of Smyrna, for whom wind instruments sound lower by their '
         'length and by the width of the holes (τὴν εὐρύτητα τῶν τρημάτων, p. 66.7–8 Hiller); P’s “length … of the auloi” and '
         '“widening of the holes” answer these two causes. The reading “the extent [of the pipe] up to the holes” has no '
         'lexical support and would repeat the length.',
         'It is rendered “widening”: the paragraph summarises Adrastus in Theon of Smyrna, who explains the lower notes of '
         'wind instruments by the length and the width of the holes (διὰ τὸ μῆκος καὶ τὴν εὐρύτητα τῶν τρημάτων, p. 66.6–8 '
         'Hiller); P gives the length to the auloi themselves (τοῦ μήκους … τῶν αὐλῶν), so that διάτασις answers to the '
         'width of the holes. The reading “the extent [of the pipe] up to the holes” would need the sense “distance”, which '
         'the word does not have, and would repeat the length.')

# U037 note 1: the ends of the periods; Bekker's numbering, with Jan's 39b
unit_fix('U037', 1, 'ru',
         'Ср., однако, там же (XIX 39b): в октаве у звуков «один и тот же конец периодов» (τὴν αὐτὴν τελευτὴν τῶν ἐν τοῖς '
         'φθόγγοις περιόδων), а в других созвучиях — нет; на такое совпадение периодов могут опираться и слова ἰσοχρόνως / '
         'ἀνισοχρόνως.',
         'Ср., однако, там же, XIX 39 (921a21–22; у Яна — 39b): в октаве у звуков «один и тот же конец периодов» (τὴν αὐτὴν '
         'τελευτὴν τῶν ἐν τοῖς φθόγγοις περιόδων), а в других созвучиях — нет; на такое совпадение концов периодов могут '
         'опираться и слова ἰσοχρόνως / ἀνισοχρόνως.')
unit_fix('U037', 1, 'en',
         'Cf., however, the same problem (XIX 39b): in the octave the notes share “the same end of their periods” (τὴν αὐτὴν '
         'τελευτὴν τῶν ἐν τοῖς φθόγγοις περιόδων), unlike the other consonances; ἰσοχρόνως / ἀνισοχρόνως may reflect such a '
         'coincidence of periods.',
         'Cf., however, the same problem, XIX 39 (921a21–22; 39b in Jan): in the octave the notes share “the same end of their '
         'periods” (τὴν αὐτὴν τελευτὴν τῶν ἐν τοῖς φθόγγοις περιόδων), unlike the other consonances; ἰσοχρόνως / ἀνισοχρόνως '
         'may reflect such a coincidence of the ends of the periods.')
unit_fix('U037', 1, 'source', '[Aristotle], Problems XIX 18, 39, 39b (Jan pp. 88, 100–101)',
         '[Aristotle], Problems XIX 18, 39 (921a21–22; Jan pp. 88, 100–101, where 39 is divided into 39a and 39b)')

# U029 note 1: what each lexicon actually gives
unit_fix('U029', 1, 'ru',
         'LSJ (s.v. οὗτος VIII.4) и Дворецкий дают для ταύτῃ только значения «здесь», «в этом», «так, этим способом»; '
         'причинное «потому-то» допускает лишь Bailly («par conséquent»).',
         'LSJ (s.v. οὗτος VIII.4) даёт для ταύτῃ только значения «здесь», «в этом», «так, этим способом», Дворецкий — '
         'местные значения, «так» и «в этом отношении»; причинное «потому-то» допускает лишь Bailly («par conséquent»; '
         '«à cause de cela, pour cela» — со ссылкой на Лукиана, «Нигрин» 23).')
unit_fix('U029', 1, 'en',
         'LSJ (s.v. οὗτος VIII.4) and Dvoretsky give ταύτῃ only as “here”, “herein”, “in this way, thus”; only Bailly allows '
         'the causal sense “that is why” (“par conséquent”).',
         'LSJ (s.v. οὗτος VIII.4) gives ταύτῃ only as “here”, “herein”, “in this way, thus”, and Dvoretsky only local senses, '
         '“thus” and “in this respect”; only Bailly allows a causal sense (“par conséquent”; “à cause de cela, pour cela”, '
         'citing Lucian, Nigrinus 23).')

# U061 note 1: "nowhere else"; U060 has ἐκ τῆς κοινῆς ἁρμονίας
unit_fix('U061', 1, 'ru',
         'Так же и словоупотребление автора: энармонический род он называет только ἁρμονικόν, «гармоническим» (U053, U054, '
         'U060, U063), и нигде не называет его ἡ ἁρμονία; ἡ ἁρμονία с артиклем у него производит все три рода (U054–U055), '
         'а в U060 сказано ἡ κοινὴ ἁρμονία, «общая гармония».',
         'О том же говорит и словоупотребление автора: энармонический род он называет только ἁρμονικόν, «гармоническим» '
         '(U053, U054, U060, U063), и нигде больше не называет его ἡ ἁρμονία; ἡ ἁρμονία с артиклем у него производит все '
         'три рода (U054–U055), а в U060 род получает название от «общей гармонии» (ἐκ τῆς κοινῆς ἁρμονίας).')
unit_fix('U061', 1, 'en',
         'So does the author’s usage: he calls the enharmonic genus only ἁρμονικόν, “harmonic” (U053, U054, U060, U063), never '
         'ἡ ἁρμονία; ἡ ἁρμονία with the article produces all three genera (U054–U055), and U060 has ἡ κοινὴ ἁρμονία, “the '
         'general harmony”.',
         'So does the author’s usage: he calls the enharmonic genus only ἁρμονικόν, “harmonic” (U053, U054, U060, U063), and '
         'nowhere else ἡ ἁρμονία; ἡ ἁρμονία with the article produces all three genera (U054–U055), and in U060 the genus '
         'takes its name from “the general harmony” (ἐκ τῆς κοινῆς ἁρμονίας).')

# the edition
J = f'{C}/text.json'
d = json.load(open(J, encoding='utf-8'))
s6 = [s for s in d['sections'] if int(s['section']) == 6][0]
e = s6['apparatus'][0]
assert e['ref'] == 'Bas. 31.10'
e['entry'] = 'ἐν μέσῳ Bas. Par. V] ἐμμέσῳ H (reading doubtful)'
e['type'] = 'word (reading doubtful)'
e['note'] = sub(e['note'], 'H 68v.9: after ἐ two μ-shaped letters', 'H 68v.10: after ἐ two μ-shaped letters', 'apparatus 31.10')
e['note'] = sub(e['note'], 'gives ἐμ̣μέσω with a dot (adjudicated)', 'gives ἐμ̣μέσω with a dot under the first μ (adjudicated)', 'apparatus 31.10')
e['note'] = sub(e['note'], 'where the edition prints ἐμμέσων (section 5)', 'where the edition prints ἐμμέσων (section 4)', 'apparatus 31.10')
s6['orthographica']['H'] = sub(s6['orthographica']['H'],
                                'ἐμ̣μέσω (68v.10) is written as one word with assimilated ν for ἐν μέσῳ.',
                                'ἐμ̣μέσω (68v.10): one word ἐμμέσῳ, or ἐν μέσῳ written as one word with assimilated ν, which '
                                'the scan cannot decide; recorded in the apparatus at 31.10.', 'orthographica H')
for a in s6['apparatus']:
    if a['ref'] == 'Bas. 32.15':
        a['note'] = sub(a['note'], 'This section varies in substance at five places. Par. V Bas. agree against H at three of them:',
                        "This section varies in substance at five places; at a sixth, 31.10, H's reading is doubtful (ἐμ̣μέσω, "
                        'perhaps only ἐν μέσῳ written as one word). Par. V Bas. agree against H at three of the five:', '32.15')
d['principles'] = sub(d['principles'], 'οὐ γάρ at 32.1, ἐξάρηνται and γενομένης.',
                      'οὐ γάρ at 32.1, ἐξάρηνται and γενομένης, and ἐμ̣μέσω at 31.10 (if it is more than ἐν μέσῳ written as one word).',
                      'principles § 3')


def walk(o):
    items = o.items() if isinstance(o, dict) else enumerate(o) if isinstance(o, list) else []
    for k, v in list(items):
        if isinstance(v, (dict, list)):
            walk(v)
        elif isinstance(v, str) and "uses it of the moderns' fifteen-note scheme (p. 64.5-6 H.)" in v:
            o[k] = v.replace("uses it of the moderns' fifteen-note scheme (p. 64.5-6 H.)",
                             "uses it of the moderns' 'fifteen-string' scheme, which there spans three octaves and a tone, not "
                             "the double octave (p. 64.5-6 H.: τὸ πεντεκαιδεκάχορδον τρόπον μέγιστον ἐπὶ τὸ τρὶς διὰ πασῶν καὶ "
                             "τόνον διεστηκός; Bullialdus emended to ἐπὶ τὸ δὶς διὰ πασῶν διεστηκός)")
            walk.n += 1


walk.n = 0
walk(d)
assert walk.n == 1
json.dump(d, open(J, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

M = f'{C}/text.md'
md = open(M, encoding='utf-8').read()
md = sub(md, '- Bas. 31.10: ἐν μέσῳ Bas. Par. V] ἐμ̣μέσω H', '- Bas. 31.10: ἐν μέσῳ Bas. Par. V] ἐμμέσῳ H (чтение сомнительно)', 'text.md apparatus')
md = sub(md, 'Открытых сомнений нет.*',
         'Открытых сомнений нет. Исправления 1.11.2026, по итогам проверки перевода по источникам: в аппарат добавлено чтение H '
         'при Bas. 31.10 (раздел 6); исправлены два примечания (Теон, с. 56.9–57.6 Hiller, — изложение самого Теона, а не '
         'Адраста; πεντεκαιδεκάχορδον — редкое слово, а не «обычное название»).*', 'text.md status')
open(M, 'w', encoding='utf-8').write(md)
print('done')
