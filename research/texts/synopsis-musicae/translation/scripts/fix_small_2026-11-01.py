"""Small mechanical fixes after the fact-check pass (1.11.2026): commas between sigla in U043-U052 notes,
'LSJ s.v. διαμονή' in U066, Bacchius in the Jan bibliography entry.
Usage: python -I fix_small_2026-11-01.py <ws-cmp folder>"""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
F = sys.argv[1] + '/compose/final'
SIG = r'(?:Bas\.|Par\.|H|V|P)'
SEQ = re.compile(rf'(?<![\w.]){SIG}(?: {SIG})+(?!\w)')


def commas(s):
    return SEQ.sub(lambda m: ', '.join(m.group(0).split(' ')), s)


def save(uid, u):
    json.dump(u, open(f'{F}/{uid}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


for uid in ('U043', 'U045', 'U046', 'U049', 'U051', 'U052'):
    u = json.load(open(f'{F}/{uid}.json', encoding='utf-8'))
    n = 0
    for nt in u['notes']:
        for k in ('ru', 'en', 'source'):
            new = commas(nt[k])
            if new != nt[k]:
                n += len(SEQ.findall(nt[k]))
                nt[k] = new
    save(uid, u)
    print(uid, 'sigla sequences fixed:', n)

u = json.load(open(f'{F}/U066.json', encoding='utf-8'))
for nt in u['notes']:
    if '(LSJ: «продолжительность»)' in nt['ru']:
        nt['ru'] = nt['ru'].replace('(LSJ: «продолжительность»)', '(LSJ s.v. διαμονή: «продолжительность»)')
        print('U066 RU fixed')
    m = re.search(r'\(LSJ: “[^”]+”\)', nt['en'])
    if m and 'διαμον' in nt['en']:
        nt['en'] = nt['en'].replace('(LSJ: “', '(LSJ s.v. διαμονή: “', 1)
        print('U066 EN fixed:', m.group(0))
save('U066', u)

b = json.load(open(f'{F}/bibliography.json', encoding='utf-8'))
for e in b:
    if e['key_ru'] == 'Jan':
        e['ru'] = e['ru'].replace('Никомах, Гауденций,', 'Никомах, Вакхий, Гауденций,')
        e['en'] = e['en'].replace('Nicomachus, Gaudentius,', 'Nicomachus, Bacchius, Gaudentius,')
        print('Jan:', e['ru'][-90:])
json.dump(b, open(f'{F}/bibliography.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
