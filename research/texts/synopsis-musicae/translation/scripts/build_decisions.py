"""Build the editor's decision page for the six translations of the Synopsis of music from the reviewers' comparisons.
Cards (general rules and single places) are defined below; each card pulls the matching divergences and terms of every
reviewer by unit and Greek words. Whatever no card takes goes to the lists of agreed points, errors and terms.
A third reviewer in the Codex format (comparison.json) is added with --astra <path>.
Usage: python -I build_decisions.py <ws-cmp folder> <out html> [--astra <comparison.json>]"""
import html, json, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
O, OUT = sys.argv[1], sys.argv[2]
ASTRA = sys.argv[sys.argv.index('--astra') + 1] if '--astra' in sys.argv else None
RUNS = O.replace('\\', '/').rsplit('/', 2)[0] + '/synopsis-musicae-translations-2026-10-31'
KEY = json.load(open(f'{O}/private/cmp-key.json', encoding='utf-8'))
MODEL = {'a1': 'GPT-6.1 Terra', 'b2': 'GPT-6.1 Sol', 'c3': 'GPT-6 Astra', 'd4': 'Claude Opus 5.5', 'e5': 'Claude Sonnet 5.5', 'f6': 'Kimi K3'}
LAB = {L: MODEL[f] for L, f in KEY.items()}
M = json.load(open(f'{O}/merged.json', encoding='utf-8'))
G = {u['id']: u for u in json.load(open(f'{O}/inputs/greek-units.json', encoding='utf-8'))['units']}
TR = {L: {u['id']: u for u in json.load(open(f'{RUNS}/ws-{f}/translation.json', encoding='utf-8'))['units']} for L, f in KEY.items()}
esc = html.escape

REV = [('claude', 'Claude (Opus 5.5, workflow с проверкой)'), ('sol', 'GPT-6.1 Sol (Codex)')]
UNITS = {'claude': {u: M[u]['claude'] for u in M}, 'sol': {u: M[u]['sol'] for u in M}}
TERMS = {'claude': json.load(open(f'{O}/claude-comparison/result.json', encoding='utf-8'))['result']['terms']['terms'],
         'sol': json.load(open(f'{O}/sol-comparison/comparison.json', encoding='utf-8'))['terms']}
if ASTRA:
    A = json.load(open(ASTRA, encoding='utf-8'))
    REV.append(('astra', 'GPT-6 Astra (Codex)'))
    UNITS['astra'] = {u['id']: u for u in A['units']}
    TERMS['astra'] = A.get('terms') or []


def norm(s):
    s = unicodedata.normalize('NFD', s or '').lower()
    s = ''.join(c for c in s if not unicodedata.combining(c)).replace('ς', 'σ')
    return ' '.join(re.findall(r'[α-ω]+', s))


# Cards. terms: Greek keys (accentless) one of which must occur in the term's Greek; xterms: keys that exclude it.
# div: (unit, key) pairs for divergences. opts: (code, Russian label). The reviewers' own recommendations are shown in full.
POLICIES = [
    dict(id='P01', title='Названия интервалов: διὰ τεσσάρων, διὰ πέντε, διὰ πασῶν',
         q='Общепринятые названия или буквальные «через четыре / через пять / через все»?',
         terms=['δια τεσσαρων', 'δια πεντε', 'δια πασων'], xterms=['δισ'], div=[('U033', 'δια τεσσαρων'), ('U035', 'δισ γαρ')],
         opts=[('a', 'кварта / квинта / октава (fourth / fifth / octave), при первом упоминании с греческим; там, где автор объясняет название '
                     '(U035: διὰ πασῶν — «через все»), буквально, с пояснением'),
               ('b', 'буквально везде: «через четыре», «через пять», «через все», как у C')],
         note='Оба рецензента за (a). У F в U035 стоит «октава» там, где автор объясняет само название; '
              'объяснение становится тавтологией (ошибка, её нашёл Claude).'),
    dict(id='P02', title='Авторские названия δὶς διὰ τεσσάρων / πέντε / πασῶν',
         q='Как передать «удвоенные» названия (по смыслу: октава с квартой 8:3, октава с квинтой 3:1, двойная октава 4:1)?',
         terms=['δισ δια'], div=[('U035', 'δισ γαρ'), ('U036', 'δισ δια'), ('U039', 'δισ δια')],
         opts=[('a', '«двойная кварта / квинта / октава» (double fourth / fifth / octave), с примечанием о смысле при U035 (D, E, F; оба рецензента в глоссарии)'),
               ('b', '«дважды кварта», «дважды квинта», «дважды октава» в кавычках (Claude, в разборе U035)'),
               ('c', '«двукратная кварта / квинта / октава» (A)')],
         note='Конъектуры Ксиландра (διὰ πασῶν καὶ διὰ τεσσάρων и т. д.) в тексте не печатаются; переводим напечатанное.'),
    dict(id='P03', title='Названия отношений по-русски: ἐπόγδοος, ἐπίτριτος, ἡμιόλιος и др.',
         q='Кальки или греческие формы?',
         terms=['επογδο', 'ημιεπογδο', 'επιτριτ', 'ημιολι', 'επιτεταρτ', 'επιδιμερ', 'διπλασιεπιμερ', 'διπλασιημιολι', 'πενταπλασ', 'τριπλασ', 'τετραπλασ'],
         div=[('U046', 'πενταπλασιων'), ('U020', 'υποτεμειν')],
         opts=[('a', 'кальки по Щетникову (Никомах): сверхвосьмерное, полусверхвосьмерное, сверхтретье, полуторное, сверхчетвертное, '
                     'сверхдвучастное, двукратно-сверхмногочастное, двукратное с половиной, пятикратное (Claude)'),
               ('b', 'эпогдоическое, полуэпогдоическое, эпитритное; остальные кальками: полуторное, сверхчетвертное, сверхдвучастное, '
                     'двукратно-сверхмногочастное, двукратное с половиной (Sol; так у A, C, E, F)')],
         note='Ошибка F в U040–U041: «двойное сверхчастное» для διπλασιεπιμερής (8:3). «Сверхчастное» — это ἐπιμόριος, другой класс. '
              'Нужно «сверхмногочастное» (это стоит в глоссариях обоих рецензентов).'),
    dict(id='P04', title='Названия отношений по-английски',
         q='Греческие формы (Barker) или латинские (Боэций)?',
         terms=['επογδο', 'επιτριτ', 'επιτεταρτ', 'επιδιμερ', 'διπλασιεπιμερ', 'διπλασιημιολι'],
         opts=[('a', 'Greek-based: epogdoic, half-epogdoic, epitritic, hemiolic, epitetartic, epidimeric, double-epimeric, double-hemiolic (Claude; A, C, D, E)'),
               ('b', 'Latin: sesquioctave, sesquitertian, sesquialter, sesquiquartan, superbipartient, duplex superpartient (B, F)')],
         note='У Sol в глоссарии смешанно: epogdoic, epitritic, но sesquiquartan, superbipartient.'),
    dict(id='P05', title='διάτονος в названиях ступеней (ὑπάτη διάτονος, διάτονος διεζευγμένη…)',
         q='«Диатоническая» или транслитерация «диатонос»?',
         terms=['διατονοσ'], xterms=['γενοσ', 'χρωματ'], div=[('U014', 'τριτη διεζευγμενη')],
         opts=[('a', '«диатоническая» (гипата диатоническая, диатоническая отделённая) (Claude)'),
               ('b', '«диатонос» (гипата диатонос, диатонос отделённая), как прочие транслитерированные имена ступеней (Sol)')],
         note='Оба рецензента согласны сохранять нестандартные формы рукописи (παράμεσος → «парамесос» с примечанием «= парамеса», '
              'именительный διεζευγμένη и т. п.).'),
    dict(id='P06', title='ὀκτάχορδον, πεντεκαιδεκάχορδον, ἑκκαιδεκάχορδον',
         q='«-хорд» или «-струнная система»?',
         terms=['καιδεκαχορδ', 'οκταχορδ', 'πενταχορδ', 'τετραχορδ'], div=[('U015', 'εκκαιδεκαχορδ')],
         opts=[('a', 'октахорд, пятнадцатихорд, шестнадцатихорд (как тетрахорд, пентахорд) (Claude)'),
               ('b', 'тетрахорд, пентахорд, октахорд, но «пятнадцатиструнная / шестнадцатиструнная система» (Sol)')]),
    dict(id='P07', title='μέλος и μελῳδία',
         q='Как переводить μέλος (и отличать ли его от μελῳδία)?',
         terms=['μελοσ', 'μελωδι'], xterms=['δυσμελ'],
         opts=[('a', '«мелодия» для обоих, греческое в скобках (Sol)'),
               ('b', '«напев» (μέλος) и «мелодия» (μελῳδία) (Claude)'),
               ('c', '«мелос» (μέλος) и «мелодия» (μελῳδία) (E)')]),
    dict(id='P08', title='ἐπίτασις / ἄνεσις',
         q='Одна пара слов везде или по контексту?',
         terms=['επιτασ', 'ανεσισ'],
         opts=[('a', '«напряжение / ослабление» везде (intensification / relaxation) (Claude)'),
               ('b', 'по контексту: «повышение / понижение» о высоте, «усиление натяжения / ослабление» о струнах (raising / lowering; tightening) (Sol)')]),
    dict(id='P09', title='ἄμεσος / ἔμμεσος (U042)',
         q='Как назвать интервалы без промежуточных звуков и с ними?',
         terms=['αμεσοσ', 'εμμεσοσ'], div=[('U042', 'τα μεν ουν εμμεσα')],
         opts=[('a', '«непосредственные / опосредованные» (immediate / mediate) (Claude)'),
               ('b', '«без промежуточных звуков / с промежуточными звуками» (without / with intermediate notes) (Sol)')]),
    dict(id='P10', title='δύναμις (и ἰσχύς)',
         q='Как переводить δύναμις интервала или системы?',
         terms=['δυναμισ'], div=[('U027', 'διαφορων τονων'), ('U051', 'δυναμεισ')],
         opts=[('a', '«возможность / возможности» (potential), ἰσχύς — «сила» (Claude)'),
               ('b', '«возможность»; где речь о величине — «интервальная величина» (capacity / interval magnitude) (Sol)'),
               ('c', '«сила» (power) везде, с примечанием')]),
    dict(id='P11', title='τριημιτόνιον', q='«Тригемитон» или описательно?', terms=['τριημιτον'],
         opts=[('a', '«тригемитон» (trihemitone) (Claude)'), ('b', '«трёхполутоновый интервал» (trihemitone) (Sol)')]),
    dict(id='P12', title='παρωνύμως / παρωνυμία (U053, U060)', q='Как передать «паронимическое» название?',
         terms=['παρωνυμ'], div=[('U060', 'εκ τησ κοινησ')],
         opts=[('a', '«отыменно; отыменное название» (paronymously; paronymous name) (Claude)'),
               ('b', '«по производному названию; производное название» (by a derivative name) (Sol)')]),
    dict(id='P13', title='ἰσοχρόνως / ἀνισοχρόνως (U037)', q='Что передаём: «время» или «время звучания»?',
         terms=['ισοχρον'], div=[('U037', 'ανισοχρονωσ')],
         opts=[('a', '«в равное / в неравное время» (at equal / unequal times) (Claude)'),
               ('b', '«при равном / неравном времени звучания» (with equal / unequal timing) (Sol)')]),
    dict(id='P14', title='περιοχή (U010)', q='«Охват» или «совокупность»?', terms=['περιοχ'], div=[('U010', 'περιοχ')],
         opts=[('a', '«охват» (compass) (Claude; Sol в разборе U010)'), ('b', '«совокупность» (collection) (Sol, глоссарий)')]),
    dict(id='P15', title='Заглавие: Μουσικῆς σύνοψις ἠκριβωμένη (U001)', q='Как назвать текст в переводе?',
         terms=['συνοψισ', 'ηκριβωμεν'], div=[('U001', 'συνοψισ')],
         opts=[('a', '«Точный обзор музыки» / «An Exact Synopsis of Music» (Claude)'),
               ('b', '«Тщательно выверенный обзор музыки» (Sol, по ἠκριβωμένη)'),
               ('c', 'оставить наше рабочее «Синопсис музыки», а точный перевод заглавия дать в примечании')]),
]
PLACES = [
    dict(id='L01', unit='U007', title='Родительный самостоятельный ἧς … θεωρουμένης', div=['ησ εν απασιν', 'ησ θεωρουμενησ'],
         q='Причина («поскольку») или уступка («хотя»)?',
         opts=[('a', '«Поскольку музыка так созерцается во всём…» (Claude)'), ('b', '«Хотя музыка…»'),
               ('c', 'без явной связи: «Музыка так усматривается во всём…, мы же…» (Sol)')]),
    dict(id='L02', unit='U013', title='ψόφος τις ἄλλως ἐκπεφωνημένος', div=['ψοφοσ', 'αλλωσ'], q='ἄλλως — «как попало», «иначе» или «просто так»?',
         opts=[('a', '«как попало» (at random) (Claude; C, E, F)'), ('b', '«иначе» (otherwise) (Sol; A, B)'), ('c', '«просто так» (D)')]),
    dict(id='L03', unit='U020', title='ὑποτεμεῖν … εἰς ἡμιεπόγδοον', div=['υποτεμειν', 'εισ ημιεπογδοον'],
         q='«Укоротить до…» или «подразделить на…»?',
         opts=[('a', '«укоротить до полуэпогдоического [отношения], то есть до полутона» (Claude)'),
               ('b', '«подразделить»')]),
    dict(id='L04', unit='U021', title='κατὰ τὸ δοκοῦν μῆκος', div=['κατα το δοκουν'], q='«До желаемой длины» или «на желаемую длину»?',
         opts=[('a', '«до желаемой длины» (A, B, C, F)'), ('b', '«на желаемую длину» (D, E)'), ('c', '«до желаемой величины» (Sol)')]),
    dict(id='L05', unit='U023', title='εἰς ἴσα … τετράγωνα', div=['εισ ισα', 'τετραγωνισθηναι'],
         q='Добавлять ли «[два]» в текст перевода?',
         opts=[('a', 'переводим напечатанное «на равные квадраты», в примечании: имеются в виду два (Claude)'),
               ('b', '«на [два] равных квадрата»')],
         note='Sol отдельно: τετραγωνισθῆναι — «представить квадратным числом», не «возвести в квадрат».'),
    dict(id='L06', unit='U039', title='καὶ μικρόν τι πρός, ὃ καὶ διέσεως ἧττον ὂν προσωνυμίας οὐκ ἔτυχε', div=['και μικρον'],
         q='Что сказать в примечании об «избытке» сверх 8½ / 9½ тонов?',
         opts=[('a', 'текст не исправлять; составитель, видимо, сложил 2½ тона Аристоксена с «безымянной» лиммой Платона '
                     '(Теон 66–67 Hiller: τὸ δὲ λεῖμμα τοῦτό φησιν ἀκατονόμαστον εἶναι; я сверил) (Claude)'),
               ('b', 'отметить арифметическую ошибку составителя: нужен недостаток, а не избыток (A, B, D, F)'),
               ('c', 'дать оба объяснения')]),
    dict(id='L07', unit='U040', title='Пропуск: ⟨τοῦ δὲ δὶς διὰ πασῶν τετραπλάσιος⟩', div=['του δια πασων'],
         q='Восполнять ли в переводе отношение двойной октавы 4:1?',
         opts=[('a', 'переводить напечатанное, восполнение дать в примечании (Claude; A, D, B, F)'),
               ('b', 'восполнить в переводе в угловых скобках ⟨…⟩ (C, E)')]),
    dict(id='L08', unit='U042', title='τὸ διὰ πέντε μέλος', div=['το δια πεντε μελοσ'], q='Как передать подозрительное μέλος (есть только в P)?',
         opts=[('a', '«мелос квинты (μέλος)» с примечанием (Claude; E)'), ('b', '«мелодия квинты» (B)'), ('c', '«квинтовый напев» (D)')],
         note='Связано с P07 (μέλος).'),
    dict(id='L09', unit='U042', title='λογοθετηθέντων', div=['λογοθετ'], terms=['λογοθετ'], q='Сохранять ли игру с λόγος?',
         opts=[('a', '«были исчислены» (reckoned), с примечанием об игре слов (Claude; E)'),
               ('b', '«были установлены отношения» (assigned ratios) (Sol; B, C, D, F)')]),
    dict(id='L10', unit='U044', title='οὕτως οὖν ἔχει περὶ τοὺς λόγους καὶ τὰ τῆς μουσικῆς διαστήματα', div=['ουτωσ ουν'],
         q='καί соединяет два дополнения или значит «и (интервалы) тоже»?',
         opts=[('a', '«Так обстоит дело с отношениями и с интервалами музыки» (A, B, C, E, F)'),
               ('b', '«Так обстоит дело и с интервалами музыки в том, что касается их отношений» (D; у Claude небольшое предпочтение)')]),
    dict(id='L11', unit='U046', title='οὐ πρὸς τὴν ὑπεροχὴν τῆς τῶν φθόγγων ποσότητος', div=['ου προσ την υπεροχην', 'τησ των φθογγων'],
         q='Раскрывать ли подразумеваемый «пятый звук»?',
         opts=[('a', 'буквально, множественное «звуков», без добавления (Claude)'), ('b', 'с пояснением в скобках «[пятый звук]» (Sol)')]),
    dict(id='L12', unit='U049', title='ἢ γνωριμώτερον ἀπὸ τῆς ἐξαρτήσεως τῶν βαρῶν', div=['η γνωριμωτερον'],
         q='«Что более известно» или «более наглядно»?',
         opts=[('a', '«или, что более известно (привычно)» (more familiarly) (Claude; A, E)'),
               ('b', '«или, более наглядно» (more intelligibly) (Sol; B, C, D, F)')]),
    dict(id='L13', unit='U050', title='†ἀμφότερον† … εἶδος', div=['αμφοτερον'], q='Как передать слово под крестами?',
         opts=[('a', '«†и то и другое†» / †both†, в примечании: по смыслу нужно «более низкий» (Claude; A, B, C, E)'),
               ('b', '«†двоякий† вид» / a †both† kind (Sol; D, F)')]),
    dict(id='L14', unit='U065', title='παιήων, ὑμέναιος, ἐξόδιος', div=['εξοδιοσ'], terms=['εξοδιοσ', 'υμεναιοσ'], q='Что сказать об ἐξόδιος?',
         opts=[('a', '«эксодий», в примечании: заключительная («выходная») песнь; в византийском словоупотреблении, возможно, погребальная (Claude)'),
               ('b', '«эксодий [песнь при выходе]» (Sol)')]),
    dict(id='L15', unit='U066', title='μεταφορᾷ … διαμοναῖς τε καὶ ῥοαῖς', div=['διαμοναισ'], terms=['διαμον', 'ροη', 'μεταφορ'],
         q='διαμοναί и ῥοαί?',
         opts=[('a', '«выдерживаниями и течениями» (sustainings and flows) (Claude)'),
               ('b', '«выдерживаниями и текучими движениями» (dwellings and flows) (Sol)')],
         note='Оба против «паузы/остановки»: διαμονή — длящийся звук, не молчание.'),
]
GENERAL_NOTE = {'U005': 'ἐν ᾧ относится к τὸ θεῖον: так считают оба рецензента и пять переводчиков из шести.'}


def tmatch(t, keys, xkeys=()):
    g = norm(t.get('greek'))
    return any(norm(k) in g for k in keys) and not any(norm(k) in g for k in xkeys)


def dmatch(d, key):
    return norm(key) in norm(d.get('greek'))


used_div, used_term = set(), set()


def collect(card):
    """Every reviewer's matching divergences and terms for a card."""
    out = []
    for r, _ in REV:
        divs, terms = [], []
        pairs = [(card['unit'], k) for k in card.get('div', [])] if 'unit' in card else card.get('div', [])
        for uid, k in pairs:
            for i, d in enumerate((UNITS[r].get(uid) or {}).get('divergences') or []):
                if dmatch(d, k) and (r, uid, i) not in {x[:3] for x in divs}:
                    divs.append((r, uid, i, d)); used_div.add((r, uid, i))
        for i, t in enumerate(TERMS[r]):
            if card.get('terms') and tmatch(t, card['terms'], card.get('xterms', ())):
                terms.append((r, i, t)); used_term.add((r, i))
        out.append((r, divs, terms))
    return out


def ev(lst):
    return ''.join(f'<li>{esc(str(e))}</li>' for e in (lst or []))


def rnd_readings(rs):
    rows = []
    for x in rs or []:
        tl = x.get('translators') or ([q.get('translator') for q in x.get('quotes') or []])
        ru = x.get('ru') or ' / '.join(q.get('ru', '')[:200] for q in x.get('quotes') or [])
        rows.append(f'<li><b>{esc(", ".join(tl or []))}</b> — {esc(x.get("construal") or "")}'
                    + (f'<br><span class="tr">{esc(ru[:400])}</span>' if ru else '') + '</li>')
    return '<ul class="rd">' + ''.join(rows) + '</ul>' if rows else ''


def rev_div(r, uid, d):
    chk = ''
    if r == 'claude':
        chk = f'<div class="chk">Проверка: {esc(d.get("check") or "")}. {esc(d.get("check_note") or "")}' + \
              (f' <b>Поправка:</b> {esc(str(d.get("correction")))}' if d.get('correction') else '') + '</div>'
    elif d.get('second_pass'):
        chk = f'<div class="chk">Второй проход: {esc(d["second_pass"])}</div>'
    return (f'<div class="rv"><div class="rh"><b>{esc(dict(REV)[r])}</b> · {uid} · <span class="gr">{esc(d.get("greek") or "")}</span>'
            f' · уверенность {esc(d.get("confidence") or "")}{" · к редактору" if d.get("to_editor") else ""}</div>'
            f'<div><i>{esc(d.get("issue") or "")}</i></div>{rnd_readings(d.get("readings"))}'
            f'<div>{esc(d.get("verdict") or "")}</div>'
            f'<div class="rec">Рекомендация: RU «{esc(str(d.get("recommended_ru")))}» · EN “{esc(str(d.get("recommended_en")))}”</div>'
            f'{chk}<details><summary>источники</summary><ul class="ev">{ev(d.get("evidence"))}</ul></details></div>')


def rev_term(r, t):
    rend = ''.join(f'<li><b>{esc(str(x.get("translator")))}</b>: {esc(str(x.get("ru")))} / {esc(str(x.get("en")))}</li>' for x in t.get('renderings') or [])
    return (f'<div class="rv"><div class="rh"><b>{esc(dict(REV)[r])}</b> · глоссарий · <span class="gr">{esc(t.get("greek") or "")}</span>'
            f'{" · к редактору" if t.get("to_editor") else ""}</div><ul class="rd">{rend}</ul>'
            f'<div class="rec">Рекомендация: RU «{esc(str(t.get("recommended_ru")))}» · EN “{esc(str(t.get("recommended_en")))}”</div>'
            f'<div>{esc(t.get("why") or "")}</div><details><summary>источники</summary><ul class="ev">{ev(t.get("evidence"))}</ul></details></div>')


def six(uid):
    rows = []
    for L in sorted(LAB):
        u = TR[L].get(uid) or {}
        notes = ''.join(f'<li>{esc(n.get("ru") or "")}</li>' for n in u.get('notes') or [])
        rows.append(f'<div class="six"><div class="lab">{L} · {esc(LAB[L])}</div><div>{esc(u.get("ru") or "")}</div>'
                    f'<div class="en">{esc(u.get("en") or "")}</div>'
                    + (f'<details><summary>примечания ({len(u.get("notes") or [])})</summary><ul>{notes}</ul></details>' if notes else '') + '</div>')
    return f'<details class="sixw"><summary>Греческий текст и шесть переводов {uid}</summary><p class="gr">{esc(G[uid]["greek"])}</p>{"".join(rows)}</details>'


def card_html(c, kind):
    got = collect(c)
    body = ''.join(rev_div(r, uid, d) for r, divs, _ in got for (_, uid, _, d) in divs)
    body += ''.join(rev_term(r, t) for r, _, terms in got for (_, _, t) in terms)
    n_found = sum(len(d) + len(t) for _, d, t in got)
    opts = ''.join(f'<label class="opt"><input type="radio" name="{c["id"]}" value="{k}"><span class="ch">{k}</span> {esc(lbl)}</label>'
                   for k, lbl in c['opts'])
    opts += f'<label class="opt"><input type="radio" name="{c["id"]}" value="own"><span class="ch">свой</span> <input class="own" data-q="{c["id"]}" placeholder="свой вариант"></label>'
    labels = json.dumps({k: lbl for k, lbl in c['opts']}, ensure_ascii=False)
    where = f'{c["unit"]} · ' if kind == 'L' else ''
    return (f'<section class="card q" data-q="{c["id"]}" data-labels="{esc(labels)}"><h2>{c["id"]}. {where}<span class="gr">{esc(c["title"])}</span></h2>'
            f'<p class="qq">{esc(c["q"])}</p>' + (f'<p class="nb">{esc(c["note"])}</p>' if c.get('note') else '')
            + f'<div class="opts">{opts}</div>'
            f'<label class="comment">Комментарий: <input type="text" class="cmt" data-p="{c["id"]}"></label>'
            f'<details><summary>Что говорят рецензенты ({n_found})</summary>{body}</details>'
            + (six(c['unit']) if kind == 'L' else '') + '</section>')


pol_html = ''.join(card_html(c, 'P') for c in POLICIES)
pl_html = ''.join(card_html(c, 'L') for c in PLACES)

# What no card took: agreed points, by unit
agreed = []
for uid in sorted(M):
    items = []
    for r, _ in REV:
        for i, d in enumerate((UNITS[r].get(uid) or {}).get('divergences') or []):
            if (r, uid, i) not in used_div:
                items.append(rev_div(r, uid, d))
    if items:
        oid = f'A-{uid}'
        gn = f'<p class="nb">{esc(GENERAL_NOTE[uid])}</p>' if uid in GENERAL_NOTE else ''
        agreed.append(f'<details class="ag"><summary>{uid} — пунктов: {len(items)}</summary>{gn}{"".join(items)}'
                      f'<label class="obj"><input type="checkbox" class="objc" data-o="{oid}"> возражаю</label>'
                      f'<input type="text" class="cmt" data-p="{oid}" placeholder="что не так"></details>')

# Errors
SEV = {'major': 0, 'minor': 1}
EM = json.load(open(f'{O}/merged3.json', encoding='utf-8')) if ASTRA else M  # merged3: errors matched across three reviewers
NAME = {'claude': 'Claude', 'sol': 'Sol', 'astra': 'Astra'}
err_by = {L: [] for L in sorted(LAB)}
for uid in sorted(EM):
    for e in EM[uid]['errors']:
        sev = e.get('severity_max') or (e.get('claude') or {}).get('severity') or (e.get('sol') or {}).get('severity')
        err_by[e['translator']].append((SEV.get(sev, 2), uid, e, sev))
err_html = []
for L, lst in err_by.items():
    lst.sort(key=lambda z: (z[0], z[1]))
    rows = []
    for _, uid, e, sev in lst:
        fb = e.get('found_by') or (['claude', 'sol'] if e['who'] == 'both' else [e['who']])
        who = ('все трое' if len(fb) == 3 else ('нашли: ' if len(fb) > 1 else 'только ') + ' и '.join(NAME[r] for r in fb))
        parts = []
        for r in ('claude', 'sol', 'astra'):
            x = e.get(r)
            if x:
                fix = x.get('fix') or x.get('correction_ru') or ''
                cn = f' <i>Проверка: {esc(x.get("check") or "")}. {esc(x.get("check_note") or "")}</i>' if r == 'claude' and x.get('check') else ''
                parts.append(f'<div><b>{r}</b> [{esc(str(x.get("severity")))}, {esc(str(x.get("lang", "")))}]: «{esc(str(x.get("quote") or ""))}» — '
                             f'{esc(str(x.get("problem") or ""))} <b>Исправить:</b> {esc(str(fix))}{cn}</div>')
        oid = f'E-{L}-{uid}-{len(rows)}'
        rows.append(f'<li class="e {esc(str(sev))}"><b>{uid}</b> · {esc(str(sev))} · {who}{"".join(parts)}'
                    f'<label class="obj"><input type="checkbox" class="objc" data-o="{oid}"> возражаю</label> '
                    f'<input type="text" class="cmt" data-p="{oid}" placeholder="почему"></li>')
    nmaj = sum(1 for z in lst if z[3] == 'major')
    err_html.append(f'<details class="ag"><summary>{L} · {esc(LAB[L])}: ошибок {len(lst)}, из них существенных {nmaj}</summary><ul class="errs">{"".join(rows)}</ul></details>')

# Terms that no card took
trow = []
for r, _ in REV:
    for i, t in enumerate(TERMS[r]):
        if (r, i) not in used_term:
            trow.append((norm(t.get('greek'))[:12], r, t))
trow.sort(key=lambda z: z[0])
term_html = ''.join(f'<tr><td class="gr">{esc(t.get("greek") or "")}</td><td>{r}</td><td>{esc(str(t.get("recommended_ru")))}</td>'
                    f'<td>{esc(str(t.get("recommended_en")))}</td><td>{"да" if t.get("to_editor") else ""}</td></tr>' for _, r, t in trow)

# Best picks by reviewer
from collections import Counter
best = {r: (Counter(), Counter()) for r, _ in REV}
for r, _ in REV:
    for uid, u in UNITS[r].items():
        for j, f in enumerate(('best_ru', 'best_en')):
            b = u.get(f)
            b = b.get('translator') if isinstance(b, dict) else b
            for x in re.findall('(?<![A-Za-z])[A-F](?![A-Za-z])', b if isinstance(b, str) else ''):  # ties are written 'A = E'
                best[r][j][x] += 1
best_rows = ''.join(f'<tr><td>{L}</td><td>{esc(LAB[L])}</td>' + ''.join(f'<td>{best[r][0][L]} / {best[r][1][L]}</td>' for r, _ in REV) + '</tr>'
                    for L in sorted(LAB))
best_head = ''.join(f'<th>{esc(n)}<br>ru / en</th>' for _, n in REV)

n_q = len(POLICIES) + len(PLACES)
page = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Решения по переводу</title>
<style>
:root {{ --bg:#f6f4ef; --card:#fff; --ink:#1d1c1a; --muted:#6b675f; --line:#ddd8cc; --accent:#9a3412; --mark:#ffe1b0; --btn-ink:#fff; --maj:#b91c1c; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#1b1a18; --card:#262421; --ink:#ece8df; --muted:#a8a294; --line:#3b3833; --accent:#f0a46b; --mark:#6b4a1c; --btn-ink:#1b1a18; --maj:#f87171; }} }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:16px/1.5 system-ui, "Segoe UI", sans-serif; }}
main {{ max-width:1080px; margin:0 auto; padding:16px 16px 160px; }}
h1 {{ font-size:1.5rem; margin:.5rem 0 }} h3 {{ margin-top:2rem }}
.intro {{ color:var(--muted); max-width:75ch }}
.gr {{ font-family:"Palatino Linotype","Gentium Plus","Noto Serif",serif; font-size:1.08em }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:16px; margin:18px 0; }}
.card h2 {{ margin:0 0 6px; font-size:1.15rem }}
.qq {{ margin:4px 0 8px; font-weight:600 }}
.nb {{ font-size:.92em; color:var(--muted); border-left:3px solid var(--accent); padding-left:8px }}
.opts {{ display:grid; gap:6px; margin:8px 0 }}
.opt {{ display:flex; align-items:flex-start; gap:8px; padding:6px 8px; border:1px solid var(--line); border-radius:6px; cursor:pointer }}
.opt:has(input:checked) {{ border-color:var(--accent); box-shadow:0 0 0 1px var(--accent) }}
.ch {{ font-weight:700; color:var(--accent); min-width:1.6em }}
input.own, input.cmt {{ font:inherit; padding:2px 6px; border:1px solid var(--line); border-radius:4px; background:var(--bg); color:var(--ink); min-width:14em; flex:1 }}
.comment {{ display:flex; gap:6px; align-items:center; color:var(--muted); margin:6px 0 }}
details {{ margin-top:8px }} summary {{ cursor:pointer; color:var(--muted) }}
.rv {{ border-top:1px dashed var(--line); padding:8px 0; font-size:.93em }}
.rh {{ margin-bottom:4px }} .rec {{ margin:4px 0; font-weight:600 }} .chk {{ color:var(--muted); font-size:.92em }}
.rd {{ margin:4px 0 4px 1em; padding:0 }} .tr {{ color:var(--muted) }} .ev {{ font-size:.9em; color:var(--muted) }}
.sixw .six {{ border-top:1px solid var(--line); padding:6px 0 }} .lab {{ font-weight:700; color:var(--accent) }} .en {{ color:var(--muted) }}
.ag {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:8px 12px; margin:8px 0 }}
.obj {{ display:inline-flex; gap:6px; align-items:center; margin:6px 12px 0 0; color:var(--muted) }}
.errs li {{ margin:8px 0 }} .errs li.major > b:first-child {{ color:var(--maj) }}
table {{ border-collapse:collapse; width:100%; font-size:.92em }} td, th {{ border:1px solid var(--line); padding:4px 6px; vertical-align:top; text-align:left }}
.wrap {{ overflow-x:auto }}
.bar {{ position:fixed; left:0; right:0; bottom:0; background:var(--card); border-top:1px solid var(--line); padding:10px 16px; }}
.bar .in {{ max-width:1080px; margin:0 auto; display:flex; gap:12px; align-items:center; flex-wrap:wrap }}
button {{ font:inherit; padding:8px 16px; border-radius:6px; border:0; background:var(--accent); color:var(--btn-ink); font-weight:600; cursor:pointer }}
#out {{ width:100%; height:8em; display:none; font:13px/1.4 ui-monospace,Consolas,monospace }}
</style></head><body><main>
<h1>Шесть переводов «Синопсиса музыки»: решения редактора</h1>
<p class="intro">Рецензентов {len(REV)}: {esc(", ".join(n for _, n in REV))}. Каждый сравнивал шесть переводов с греческим, не зная, чей перевод под какой буквой.
Ниже вопросы, по которым рецензенты расходятся или сами передают выбор вам: сначала общие правила (термины), потом отдельные места.
В каждой карточке разборы рецензентов с источниками (раскрываются), у мест есть также греческий текст и все шесть переводов.
Дальше то, о чём рецензенты договорились или что предложил один из них, а другой не оспорил; ошибки переводчиков и глоссарий.
Там ничего выбирать не нужно; если с чем-то не согласны, отметьте «возражаю». Выбор сохраняется в этом браузере.
Когда закончите, нажмите «Скопировать решения» и вставьте текст в чат.</p>
<p class="intro">Переводчики: {esc("; ".join(f"{L} — {LAB[L]}" for L in sorted(LAB)))}.</p>
<h3>Общие правила ({len(POLICIES)})</h3>{pol_html}
<h3>Отдельные места ({len(PLACES)})</h3>{pl_html}
<h3>Согласовано рецензентами или предложено одним из них</h3>
<p class="intro">Пункты по единицам текста. Если в единице есть что-то, с чем вы не согласны, отметьте «возражаю» и напишите, что именно.</p>
{"".join(agreed)}
<h3>Ошибки переводчиков</h3>
<p class="intro">Все ошибки будут исправлены при сведении. «Только …» означает, что ошибку нашёл один рецензент; такие существенные ошибки я пересмотрел.
В двух случаях оценку стоит понизить: U005 C (союзное слово, проверка Claude сочла ошибку незначительной) и U012 A
(примечание Sonnet к Фрасиллу: условие действительно перевёрнуто, но только в русском примечании, не в переводе).</p>
{"".join(err_html)}
<h3>Глоссарий (что не вошло в общие правила)</h3>
<p class="intro">Рекомендации рецензентов по остальным терминам. Если не согласны, напишите в общий комментарий внизу.</p>
<div class="wrap"><table><tr><th>греческий</th><th>рецензент</th><th>RU</th><th>EN</th><th>к редактору</th></tr>{term_html}</table></div>
<h3>Чьи переводы рецензенты считают лучшими</h3>
<p class="intro">Число единиц, где перевод назван лучшей основой (ru / en; при равенстве засчитаны оба). Каждый рецензент заметно предпочитает переводы своего «семейства»
(Claude: A и E; Sol и Astra: B, D и F). Поэтому «лучшую основу» я не считаю решающей: окончательный перевод будет сводным, а не одним из шести.
Надёжная часть сравнений — ошибки и расхождения с доказательствами.</p>
<div class="wrap"><table><tr><th></th><th>переводчик</th>{best_head}</tr>{best_rows}</table></div>
<label class="comment" style="margin-top:20px">Общий комментарий: <input type="text" class="cmt" data-p="general"></label>
</main>
<div class="bar"><div class="in"><span id="prog"></span><button id="copy">Скопировать решения</button><span id="msg"></span>
<textarea id="out" readonly></textarea></div></div>
<script>
const KEY = 'neoscholia-translation-decisions-synopsis';
const N = {n_q};
let st = {{}};
try {{ st = JSON.parse(localStorage.getItem(KEY) || '{{}}') }} catch (e) {{}}
const save = () => {{ try {{ localStorage.setItem(KEY, JSON.stringify(st)) }} catch (e) {{}} }};
document.querySelectorAll('input[type=radio]').forEach(r => {{
  if (st[r.name] && st[r.name].v === r.value) r.checked = true;
  r.addEventListener('change', () => {{ st[r.name] = Object.assign(st[r.name] || {{}}, {{ v: r.value }}); save(); prog() }});
}});
document.querySelectorAll('input.own').forEach(t => {{
  const q = t.dataset.q; if (st[q] && st[q].own) t.value = st[q].own;
  t.addEventListener('input', () => {{ st[q] = Object.assign(st[q] || {{}}, {{ own: t.value }});
    if (t.value) {{ document.querySelector(`input[type=radio][name="${{CSS.escape(q)}}"][value=own]`).checked = true; st[q].v = 'own' }}
    save(); prog() }});
}});
document.querySelectorAll('input.cmt').forEach(t => {{
  const k = 'cmt:' + t.dataset.p; if (st[k]) t.value = st[k].c || '';
  t.addEventListener('input', () => {{ st[k] = {{ c: t.value }}; save() }});
}});
document.querySelectorAll('input.objc').forEach(t => {{
  const k = 'obj:' + t.dataset.o; if (st[k]) t.checked = true;
  t.addEventListener('change', () => {{ if (t.checked) st[k] = 1; else delete st[k]; save() }});
}});
function prog() {{
  const done = [...document.querySelectorAll('.q')].filter(q => st[q.dataset.q] && st[q.dataset.q].v).length;
  document.getElementById('prog').textContent = `Решено ${{done}} из ${{N}}`;
}}
prog();
document.getElementById('copy').addEventListener('click', async () => {{
  const lines = ['Решения по переводу («Синопсис музыки»):'];
  document.querySelectorAll('.q').forEach(q => {{
    const id = q.dataset.q, s = st[id] || {{}}, L = JSON.parse(q.dataset.labels);
    let a = '— (не решено)';
    if (s.v === 'own') a = 'своё: ' + (s.own || '');
    else if (s.v) a = s.v + ' — ' + (L[s.v] || '');
    lines.push(`${{id}}: ${{a}}`);
    const c = st['cmt:' + id]; if (c && c.c) lines.push(`${{id}} — комментарий: ${{c.c}}`);
  }});
  Object.keys(st).filter(k => k.startsWith('obj:')).forEach(k => {{
    const id = k.slice(4), c = st['cmt:' + id];
    lines.push(`Возражение ${{id}}: ${{c && c.c ? c.c : '(без комментария)'}}`);
  }});
  Object.keys(st).filter(k => k.startsWith('cmt:') && !st['obj:' + k.slice(4)] && !document.querySelector(`.q[data-q="${{CSS.escape(k.slice(4))}}"]`))
    .forEach(k => {{ if (st[k].c) lines.push(`Комментарий ${{k.slice(4)}}: ${{st[k].c}}`) }});
  const text = lines.join('\\n');
  const out = document.getElementById('out'); out.value = text; out.style.display = 'block';
  try {{ await navigator.clipboard.writeText(text); document.getElementById('msg').textContent = 'Скопировано. Вставьте в чат.' }}
  catch (e) {{ out.select(); document.getElementById('msg').textContent = 'Выделите текст ниже и скопируйте (Ctrl+C).' }}
}});
</script></body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print('cards', n_q, '| divergences in cards', len(used_div), '| terms in cards', len(used_term),
      '| agreed units', len(agreed), '| errors', sum(len(v) for v in err_by.values()), '| other terms', len(trow), '->', OUT)
for c in POLICIES + PLACES:
    got = collect(c)
    n = [(r, len(d), len(t)) for r, d, t in got]
    if not any(d or t for _, d, t in got):
        print('EMPTY CARD', c['id'])
    else:
        print(c['id'], n)
