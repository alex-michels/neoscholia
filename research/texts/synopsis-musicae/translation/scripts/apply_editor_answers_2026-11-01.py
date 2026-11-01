"""Apply the editor's answers of 1.11.2026 ("apply the recommendations") to the unpacked units
(explode_translation.py), and record each change in the unit's "verify" list.
Usage: python -I apply_editor_answers_2026-11-01.py <work folder>"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
F = sys.argv[1] + '/compose/final'
U = {}
STAMP = "Editor's answers, 1.11.2026: "


def unit(uid):
    if uid not in U:
        U[uid] = json.load(open(f'{F}/{uid}.json', encoding='utf-8'))
    return U[uid]


def rep(uid, where, old, new, count=1):
    """where: 'ru' | 'en' | (note number, field)"""
    u = unit(uid)
    if isinstance(where, str):
        obj, key = u, where
    else:
        obj, key = u['notes'][where[0] - 1], where[1]
    n = obj[key].count(old)
    assert n == count, f'{uid} {where}: expected {count} of «{old}», found {n}'
    obj[key] = obj[key].replace(old, new)


def append(uid, where, text):
    u = unit(uid)
    obj, key = u['notes'][where[0] - 1], where[1]
    obj[key] = obj[key] + text


def close(uid, starts, why):
    u = unit(uid)
    before = len(u['open'])
    u['open'] = [o for o in u['open'] if not o.startswith(starts)]
    assert len(u['open']) == before - 1, f'{uid}: open item «{starts}» not found'
    log(uid, why)


def log(uid, what):
    u = unit(uid)
    if not isinstance(u.get('verify'), list):
        u['verify'] = [u['verify']] if u.get('verify') else []
    u['verify'].append(STAMP + what)


# U004, U028, U031, U033: recommendations keep the text; the questions are closed
close('U004', 'τὸ πᾶν', 'τὸ πᾶν stays adverbial («всецело» / “wholly so”), as recommended.')
close('U028', 'ἐντεῦθεν', 'the possibility reading stays («оказывается возможным»), as recommended.')
close('U031', 'αὐτήν (P)', "P's αὐτήν is kept as a loose construction; note 1 states the lexical facts.")
close('U033', 'DECISIONS names no place', 'the main P01 note stays at the first mention.')
close('U037', 'DECISIONS names no place', 'the main P08 note stays at the first occurrence.')
# U012 and U054: one rule. Greek stands in the text only where the author's derivation is not visible in the translation
close('U012', 'DECISIONS § 2 allows Greek', 'no Greek in the text: the derivation is visible in the translation '
      '(«пригодный для гармонии … сочетаться в гармонии»). Rule: Greek stands in the text only where the derivation '
      'is not visible in the translation (U035, U054).')
close('U054', 'Greek (διὰ τόνων)', 'the Greek stays: the derivation of διάτονον from διὰ τόνων is not visible in the '
      'translation (rule as at U012).')

# U018: «двойной полутон» -> «полутон дважды»
rep('U018', 'ru', 'тон, который содержит двойной полутон', 'тон, который содержит полутон дважды')
close('U018', 'RU text «тон, который содержит двойной полутон»', 'RU «содержит полутон дважды», as the EN “contains the semitone twice”.')

# U029: ταύτῃ τοι as in U025
rep('U029', 'ru', 'Потому-то и геометрия', 'Именно так и геометрия')
rep('U029', 'en', 'That is why geometry too', 'In just this way geometry too')
rep('U029', (1, 'anchor_ru'), 'Потому-то и геометрия', 'Именно так и геометрия')
rep('U029', (1, 'anchor_en'), 'That is why geometry too', 'In just this way geometry too')
rep('U029', (1, 'ru'), 'ταύτῃ τοι («потому-то») вместо γάρ', 'ταύτῃ τοι («именно так») вместо γάρ')
rep('U029', (1, 'en'), 'ταύτῃ τοι (“that is why”) for γάρ', 'ταύτῃ τοι (“in just this way”) for γάρ')
append('U029', (1, 'ru'), ' Формула ταύτῃ τοι καί передана так же, как в U025: LSJ (s.v. οὗτος VIII.4) и Дворецкий дают '
       'для ταύτῃ только значения «здесь», «в этом», «так, этим способом»; причинное «потому-то» допускает лишь Bailly '
       '(«par conséquent»).')
append('U029', (1, 'en'), ' The formula ταύτῃ τοι καί is rendered as in U025: LSJ (s.v. οὗτος VIII.4) and Dvoretsky give '
       'ταύτῃ only as “here”, “herein”, “in this way, thus”; only Bailly allows the causal sense “that is why” '
       '(“par conséquent”).')
append('U029', (1, 'source'), '; LSJ s.v. οὗτος VIII.4; Dvoretsky; Bailly')
close('U029', 'ταύτῃ τοι is rendered causally', 'ταύτῃ τοι rendered «Именно так» / “In just this way”, as in U025; the causal reading in note 1.')

# U034: three roots for the three verbs
rep('U034', 'ru', 'кварта — как проходящая и завершающаяся через четыре звука', 'кварта — как проходящая и оканчивающаяся через четыре звука')
rep('U034', (3, 'ru'), '(«завершающаяся», «завершаемая»)', '(«оканчивающаяся», «завершаемая»)')
close('U034', 'DECISIONS (P01) gives', '«достигающая полноты» / “perfected” for τελειούμενον is confirmed.')
close('U034', 'Accuracy reader (1.11.2026)', 'περαινόμενον «оканчивающаяся»: three roots (конец / завершение / полнота), as in the EN.')

# U037: the coincidence of periods in [Aristotle], Problems XIX 39b
append('U037', (1, 'ru'), ' Ср., однако, там же (XIX 39b): в октаве у звуков «один и тот же конец периодов» (τὴν αὐτὴν '
       'τελευτὴν τῶν ἐν τοῖς φθόγγοις περιόδων), а в других созвучиях — нет; на такое совпадение периодов могут '
       'опираться и слова ἰσοχρόνως / ἀνισοχρόνως.')
append('U037', (1, 'en'), ' Cf., however, the same problem (XIX 39b): in the octave the notes share “the same end of their '
       'periods” (τὴν αὐτὴν τελευτὴν τῶν ἐν τοῖς φθόγγοις περιόδων), unlike the other consonances; ἰσοχρόνως / '
       'ἀνισοχρόνως may reflect such a coincidence of periods.')
rep('U037', (1, 'source'), '[Aristotle], Problems XIX 18, 39 (', '[Aristotle], Problems XIX 18, 39, 39b (')
close('U037', 'Fact-checker (1.11.2026)', 'the Problems XIX 39b sentence is added to note 1.')

# U042: «отношений к соседним звукам»
rep('U042', 'ru', 'своих отношений относительно соседних звуков перед ними', 'своих отношений к соседним звукам перед ними')
close('U042', 'DECISIONS P14 prescribes', 'RU «своих отношений к соседним звукам перед ними».')

# διάστασις: «расстояние» / “span” throughout
rep('U045', 'ru', 'отношения интервальных расстояний', 'отношения расстояний')
rep('U045', 'en', 'the ratios of the intervallic spans', 'the ratios of the spans')
rep('U045', (2, 'anchor_ru'), 'интервальных расстояний', 'расстояний')
rep('U045', (2, 'anchor_en'), 'intervallic spans', 'spans')
rep('U045', (2, 'ru'), 'передано здесь, в U049 и U056 как «интервальное расстояние», в U051 — как «расстояние», в U035–U036 — как «интервалы».',
    'передано здесь, в U049, U051 и U056 как «расстояние», в U035–U036 — как «интервалы».')
rep('U045', (2, 'en'), 'is rendered “intervallic span” here and at U049 and U056, “span” at U051 and “intervals” at U035–U036.',
    'is rendered “span” here and at U049, U051 and U056, and “intervals” at U035–U036.')
close('U045', 'διάστασις «интервальное расстояние»', 'διάστασις «расстояние» / “span” throughout (U045, U049, U051, U056).')
rep('U049', 'ru', 'отношения интервальных расстояний', 'отношения расстояний')
rep('U049', 'en', 'Such ratios of the intervallic spans', 'Such ratios of the spans')
rep('U049', (1, 'anchor_en'), 'Such ratios of the intervallic spans', 'Such ratios of the spans')
log('U049', 'διάστασις «расстояние» / “span”, as at U045.')
rep('U056', 'ru', 'из трёх интервальных расстояний', 'из трёх расстояний')
rep('U056', 'en', 'of three intervallic spans', 'of three spans')
rep('U056', (1, 'anchor_ru'), 'из трёх интервальных расстояний', 'из трёх расстояний')
rep('U056', (1, 'anchor_en'), 'of three intervallic spans', 'of three spans')
rep('U056', (1, 'ru'), '«тремя интервальными расстояниями»', '«тремя расстояниями»')
rep('U056', (1, 'en'), '“by three intervallic spans”', '“by three spans”')
log('U056', 'διάστασις «расстояние» / “span”, as at U045.')

# U050: διάτασις «расширение»
rep('U050', 'ru', 'или протяжённости отверстий', 'или расширении отверстий')
rep('U050', 'en', 'or the extension of the holes', 'or the widening of the holes')
rep('U050', (3, 'anchor_ru'), 'протяжённости отверстий', 'расширении отверстий')
rep('U050', (3, 'anchor_en'), 'extension of the holes', 'widening of the holes')
u = unit('U050')
u['notes'][2]['ru'] = ('διάτασις τῶν τρημάτων: LSJ даёт для διάτασις «натяжение, расширение, протяжение» (DGE и Bailly также '
                       'дают «расширение»); значения «расстояние между…» у этого слова нет (оно было бы у διάστασις). Переведено '
                       '«расширение»: абзац пересказывает Теона Смирнского, у которого духовые звучат ниже от длины и от ширины '
                       'отверстий (τὴν εὐρύτητα τῶν τρημάτων, «ширину отверстий», с. 66.7–8 Hiller); «длина авлосов» и '
                       '«расширение отверстий» в P отвечают этим двум причинам. Понимание «протяжённость [трубки] до отверстий» '
                       'лексически не подкреплено и повторяло бы длину.')
u['notes'][2]['en'] = ('διάτασις τῶν τρημάτων: LSJ gives διάτασις as “tension, dilatation, extension” (DGE and Bailly also give '
                       '“dilatation”); it has no sense “distance between”, which would be διάστασις. It is rendered “widening”: the '
                       'paragraph summarises Theon of Smyrna, for whom wind instruments sound lower by their length and by the '
                       'width of the holes (τὴν εὐρύτητα τῶν τρημάτων, p. 66.7–8 Hiller); P’s “length … of the auloi” and '
                       '“widening of the holes” answer these two causes. The reading “the extent [of the pipe] up to the holes” '
                       'has no lexical support and would repeat the length.')
close('U050', 'διάτασις τῶν τρημάτων', 'διάτασις «расширение» / “widening”, as recommended by both checkers; note 3 rewritten.')

# U051: ⟨квинты⟩
rep('U051', 'ru', 'охватывающий значения [интервала] ⟨через⟩ пять [то есть квинты]', 'охватывающий значения ⟨квинты⟩')
rep('U051', 'en', 'which comprises the values of the [interval] ⟨through⟩ five [i.e. the fifth]', 'which comprises the values of the ⟨fifth⟩')
rep('U051', (2, 'anchor_ru'), '⟨через⟩ пять', '⟨квинты⟩')
rep('U051', (2, 'anchor_en'), '⟨through⟩ five', '⟨fifth⟩')
rep('U051', (2, 'ru'), 'Чтобы угловые скобки охватывали только дополненное слово, здесь дан буквальный перевод «через пять»; в остальных местах διὰ πέντε — «квинта».',
    'Дополнено только διά; угловые скобки охватывают название «квинта», которым, как и везде, передано всё διὰ πέντε (букв. «через пять»).')
rep('U051', (2, 'en'), 'So that the angle brackets enclose only the supplied word, the literal “through five” is given here; elsewhere διὰ πέντε is “the fifth”.',
    'Only διά is supplied; the angle brackets enclose the name “fifth”, by which, as everywhere, the whole of διὰ πέντε (lit. “through five”) is rendered.')
close('U051', '⟨διὰ⟩ πέντε', '«значения ⟨квинты⟩» / “the values of the ⟨fifth⟩”; note 2 explains the brackets.')

# U052: H's reading, now in the edition's apparatus (Bas. 31.10)
rep('U052', (1, 'ru'), 'По указанию издания (аппарат к отрывку P, Vinc. 340.20), H читает здесь ἐμμέσω, Bas., Par., V — ἐν μέσῳ;',
    'В H здесь ἐμ̣μέσω (по скану чтение сомнительно: этот писец пишет ν почти как μ), в Bas., Par., V — ἐν μέσῳ;')
rep('U052', (1, 'en'), 'According to the edition (apparatus to the P passage, Vinc. 340.20), H reads ἐμμέσω here, Bas., Par., V ἐν μέσῳ;',
    'H has ἐμ̣μέσω here (doubtful on the scan: this scribe writes ν almost like μ), Bas., Par., V ἐν μέσῳ;')
rep('U052', (1, 'source'), 'Edition, apparatus and resolved doubts at P (Vinc. 340.20)', 'Edition, apparatus at Bas. 31.10; apparatus and resolved doubts at P (Vinc. 340.20)')
close('U052', 'The edition (section 4', "H's ἐμ̣μέσω checked in the H transcription and added to the section 6 apparatus (Bas. 31.10).")

# U061: the grounds for 'harmony in general'
rep('U061', (1, 'ru'), 'говорят скорее о гармонии вообще; перевод «гармония» допускает оба понимания.',
    'говорят скорее о гармонии вообще. Так же и словоупотребление автора: энармонический род он называет только ἁρμονικόν, '
    '«гармоническим» (U053, U054, U060, U063), и нигде не называет его ἡ ἁρμονία; ἡ ἁρμονία с артиклем у него производит '
    'все три рода (U054–U055), а в U060 сказано ἡ κοινὴ ἁρμονία, «общая гармония». Перевод «гармония» допускает оба понимания.')
rep('U061', (1, 'en'), 'rather favour harmony in general; the rendering “harmony” allows both readings.',
    'rather favour harmony in general. So does the author’s usage: he calls the enharmonic genus only ἁρμονικόν, “harmonic” '
    '(U053, U054, U060, U063), never ἡ ἁρμονία; ἡ ἁρμονία with the article produces all three genera (U054–U055), and U060 '
    'has ἡ κοινὴ ἁρμονία, “the general harmony”. The rendering “harmony” allows both readings.')
append('U061', (1, 'source'), '; U054, U055, U060, U063')
close('U061', 'The edition (section 7', 'ἡ ἁρμονία stays «гармония»; the grounds for “harmony in general” are added to note 1.')

# bibliography key in the order of the publication
for uid in ('U014', 'U018', 'U026'):
    u = unit(uid)
    for nt in u['notes']:
        for k in ('ru', 'en', 'source'):
            nt[k] = nt[k].replace('Александрова, Мякин 2009', 'Мякин, Александрова 2009').replace('Aleksandrova, Myakin 2009', 'Myakin, Aleksandrova 2009')
    log(uid, 'key «Мякин, Александрова 2009» / “Myakin, Aleksandrova 2009”, in the order of the publication.')
B = json.load(open(f'{F}/bibliography.json', encoding='utf-8'))
for e in B:
    if e['key_ru'] == 'Александрова, Мякин 2009':
        e['key_ru'], e['key_en'] = 'Мякин, Александрова 2009', 'Myakin, Aleksandrova 2009'
B.sort(key=lambda e: e['key_en'].lower())
json.dump(B, open(f'{F}/bibliography.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

for uid, u in U.items():
    json.dump(u, open(f'{F}/{uid}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('units changed:', ' '.join(sorted(U)))
print('open items left:', {uid: len(u['open']) for uid, u in U.items() if u['open']})
