"""Apply the results of the comparison with Mizler's German translation (1746; run by GPT-6.1 Sol, checked by Claude,
1.11.2026) to the unpacked units (explode_translation.py), and record each change in the unit's "verify" list.
Usage: python -I apply_mizler_comparison_2026-11-01.py <work folder> [--flowing]
--flowing: U066 ῥοαῖς «текучим движением» / “flowing motion” instead of «плавным» / “smooth” (the editor's call)."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
F = sys.argv[1] + '/compose/final'
FLOWING = '--flowing' in sys.argv[2:]
U = {}
STAMP = 'Mizler comparison, 1.11.2026: '


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


def log(uid, what):
    u = unit(uid)
    if not isinstance(u.get('verify'), list):
        u['verify'] = [u['verify']] if u.get('verify') else []
    u['verify'].append(STAMP + what)


# U050: the only correction to the Russian confirmed by both sceptics
rep('U050', 'ru', '†и то и другое† вид', '†и тот и другой† вид')
rep('U050', (4, 'anchor_ru'), '†и то и другое†', '†и тот и другой†')
log('U050', '«†и то и другое† вид» -> «†и тот и другой† вид»: «вид» is masculine; the obeli and the singular stay. '
            'EN “†both† kind” kept (it keeps the singular εἶδος of the crux).')

# U034, U043: ἄμεσος defined as in LSJ (propositions that cannot be proved syllogistically by means of a middle term)
rep('U034', (1, 'ru'), 'ἄμεσος — о посылках без среднего термина (Аристотель,',
    'ἄμεσος — о посылках, которые нельзя доказать силлогизмом через средний термин (Аристотель,')
rep('U034', (1, 'en'), 'ἄμεσος of premises without a middle term (Aristotle,',
    'ἄμεσος of premises that cannot be proved syllogistically through a middle term (Aristotle,')
log('U034', 'note 1: ἄμεσος worded as in LSJ («нельзя доказать силлогизмом через средний термин»), so that “without a '
            'middle term” is not read as “not containing the middle term”.')
rep('U043', (1, 'ru'), 'ἄμεσος говорится о посылке без среднего термина, ἔμμεσος — о посылке со средним термином.',
    'ἄμεσος говорится о посылке, которую нельзя доказать через средний термин, ἔμμεσος («опосредованный») — '
    'о том, что доказывается через средний термин.')
rep('U043', (1, 'en'), 'ἄμεσος is said of a premise without a middle term, ἔμμεσος of one with a middle term.',
    'ἄμεσος is said of a premise that cannot be proved through a middle term, ἔμμεσος (“mediate”) of what is proved '
    'through one.')
rep('U043', (1, 'source'), 'U034', 'U034; LSJ s.vv. ἄμεσος, ἔμμεσος')
log('U043', 'note 1: ἄμεσος / ἔμμεσος worded as in LSJ (“cannot be proved syllogistically by means of a middle term”; '
            '“mediate”).')

# Mizler as a witness to the interpretation (four places; the other proposed additions are left out, see the README)
append('U014', (3, 'ru'), ' Мицлер (1746, с. 176–177, прим. 4) вслед за Ксиландром вставляет это название в немецкий '
                          'перевод; в его греческом столбце, как и во всех источниках текста, названия нет.')
append('U014', (3, 'en'), ' Mizler (1746, pp. 176–177, n. 4), following Xylander, inserts the name in his German '
                          'translation; his Greek column, like all the witnesses, lacks it.')
append('U014', (3, 'source'), '; Mizler 1746, pp. 176–177')
log('U014', 'note 3: Mizler 1746 added (his German inserts διάτονος μέσων after Xylander).')
rep('U018', (3, 'ru'), 'все источники текста дают одно ὀκτώ.',
    'все источники текста дают одно ὀκτώ. Так же понимает место Мицлер: по-немецки у него «половина» и «четверть» '
    'сверхосминного отношения, как у Ксиландра по-латыни (dimidium, quadrans), а его примечание 5 — перевод рассуждения '
    'Ксиландра об этом месте (1746, с. 179–181).')
rep('U018', (3, 'en'), 'all witnesses have ὀκτώ alone.',
    'all witnesses have ὀκτώ alone. Mizler takes the passage the same way: his German has “half” and “a quarter” of the '
    'epogdoic ratio, as Xylander’s Latin has dimidium and quadrans, and his note 5 translates Xylander’s discussion of the '
    'passage (1746, pp. 179–181).')
append('U018', (3, 'source'), '; Mizler 1746, pp. 179–181')
log('U018', 'note 3: Mizler 1746 added (he follows Xylander’s “half / a quarter of 9:8”).')
append('U026', (3, 'ru'), ' Не во временном смысле понимал слово уже Мицлер: «das Maaß der Leiter», «мера звукоряда» '
                          '(1746, с. 184).')
append('U026', (3, 'en'), ' Mizler already took the word in a non-temporal sense: “das Maaß der Leiter”, “the measure of '
                          'the scale” (1746, p. 184).')
append('U026', (3, 'source'), '; Mizler 1746, p. 184')
log('U026', 'note 3: Mizler’s “das Maaß der Leiter” added as an early non-temporal reading of ῥυθμός.')
append('U037', (1, 'ru'), ' Так же понимал место Мицлер: парафонное созвучие — «консонанс в мелодии», антифонное — '
                          '«консонанс в гармонии» (1746, с. 188, прим. 10).')
append('U037', (1, 'en'), ' Mizler read the passage the same way: paraphonic is “a consonance in melody”, antiphonic “a '
                          'consonance in harmony” (1746, p. 188, n. 10).')
append('U037', (1, 'source'), '; Mizler 1746, p. 188')
log('U037', 'note 1: Mizler’s reading (melody / harmony) added.')

# U066: σχολαιοτέραις is printed with the σχ-ligature in Bas. and Par. (no variant; edition corrected the same day)
rep('U066', (1, 'ru'), 'σχολαιοτέραις («более медленными»; H, V) — в Bas. и Par. несуществующее χολαιοτέραις.',
    'σχολαιοτέραις («более медленными») — во всех источниках текста; в Bas. и Par. слово начинается лигатурой σχ, '
    'похожей на χ.')
rep('U066', (1, 'en'), 'σχολαιοτέραις (“slower”; H, V): Bas. and Par. have the non-word χολαιοτέραις.',
    'σχολαιοτέραις (“slower”) is in all the witnesses; in Bas. and Par. the word begins with the σχ-ligature, which '
    'resembles χ.')
rep('U066', (1, 'source'), 'at Bas. 33.13–15', 'at Bas. 33.13–14')
log('U066', 'note 1: «χολαιοτέραις Bas. Par.» withdrawn: both print σχολαιοτέραις with the σχ-ligature (checked at '
            'enlargement against σχέσις, Bas. 24.16, Par. 21r).')
if FLOWING:
    rep('U066', 'ru', 'выдержанными звуками и плавным движением', 'выдержанными звуками и текучим движением')
    rep('U066', 'en', 'by sustained notes and smooth motion', 'by sustained notes and flowing motion')
    rep('U066', (2, 'anchor_ru'), 'плавным движением', 'текучим движением')
    rep('U066', (2, 'anchor_en'), 'smooth motion', 'flowing motion')
    log('U066', '«плавным движением» -> «текучим движением», “smooth” -> “flowing” (the editor, 1.11.2026): in Russian '
                'music theory «плавное движение» is stepwise motion, which the text does not say (note 2 leaves it open).')

# The editor, 1.11.2026: the Russian title with a capital letter in every word
rep('U001', 'ru', 'Точный синопсис музыки', 'Точный Синопсис Музыки')
rep('U001', (1, 'anchor_ru'), 'синопсис', 'Синопсис')
rep('U001', (2, 'anchor_ru'), 'музыки', 'Музыки')
log('U001', '')
unit('U001')['verify'][-1] = "The editor, 1.11.2026: the Russian title is written «Точный Синопсис Музыки»."

B = json.load(open(f'{F}/bibliography.json', encoding='utf-8'))
assert not any(e['key_en'] == 'Mizler 1746' for e in B)
B.append({'key_ru': 'Мицлер 1746', 'key_en': 'Mizler 1746',
          'ru': 'Mizler L. Ch. Des Psellus vollständiger kurzer Inbegriff der Musik // Musikalische Bibliothek. Bd. III, '
                'Th. 2. Leipzig, 1746. S. 171–200. Греческий текст (близкий к изданию Л. Аларда, Шлойзинген, 1636) и '
                'немецкий перевод в два столбца, с примечаниями Ксиландра (X) и Мицлера; ссылки по страницам.',
          'en': 'Mizler, Lorenz Christoph. 1746. “Des Psellus vollständiger kurzer Inbegriff der Musik.” Musikalische '
                'Bibliothek, vol. 3, part 2, pp. 171–200. Leipzig. Greek text (close to L. Alard’s edition, Schleusingen '
                '1636) and German translation in two columns, with Xylander’s (X) and Mizler’s notes; cited by page.'})
B.sort(key=lambda e: e['key_en'].lower())
json.dump(B, open(f'{F}/bibliography.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

for uid, u in U.items():
    json.dump(u, open(f'{F}/{uid}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('units changed:', ' '.join(sorted(U)), '| flowing:', FLOWING)
