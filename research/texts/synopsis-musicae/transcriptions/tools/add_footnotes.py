"""Put the checked footnotes (wf6) into the merged files, with the footnotes for the corrections made after the records were
written (side notes of the checkers, the Basel hyphen convention).
Usage: python -I add_footnotes.py <scratchpad>"""
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
SP = Path(sys.argv[1])
F = {f['ref']: dict(f) for r in json.load(open(SP / 'wf6/footnotes.json', encoding='utf-8')) for f in r['footnotes']}

def add(ref, ru, en, lemma=None):
    f = F[ref]
    f['ru'] += ' ' + ru
    f['en'] += ' ' + en
    if lemma:
        f['lemma'] = lemma

F['Bas. 29.24'].update(
    lemma='οὒ',
    ru='«οὒ» — слово как в транскрипции Claude («οὐ»); в транскрипции GPT-6 «ἢ». Над последним знаком строки оба проверяющих видят '
       'тонкое придыхание и тяжёлое ударение, но сам знак один читает как Н-образное η (как ἢ в 28.22), другой — как лигатуру ου '
       '(как οὐ после ὡς в этой же строке). Слово выбрал редактор; придыхание и ударение даны, как напечатано.',
    en='«οὒ»: the word as in Claude\'s transcription («οὐ»); GPT-6\'s has «ἢ». Both checkers see a smooth breathing and a grave over the '
       'last sign of the line, but one reads the sign as an H-shaped η (as ἢ in 28.22), the other as the ου ligature (as the οὐ after ὡς '
       'in the same line). The word was chosen by the editor; the breathing and the accent are given as printed.')
add('Bas. 33.15', 'На ошибку обеих транскрипций указал сверщик Парижского издания 1545 г.: там тоже напечатано без σ (Par. 27r.20).',
    'The error of both transcriptions was pointed out by the collator of the Paris edition of 1545, which also prints the word without σ (Par. 27r.20).')
for ref in ('Bas. 25.8', 'Bas. 27.9', 'Bas. 28.14'):
    add(ref, 'Дефиса в конце строки в печати нет, и по общему правилу он не ставится.',
        'No hyphen is printed at the line end, and by the general rule none is added.', lemma=F[ref]['lemma'].rstrip('-'))
add('H 65r.19', 'Оба проверяющих считают, что надстрочная η написана и по правилу должна стоять вне скобок («βλεπομ(έν)η»); редактор принял «βλεπομ(ένη)».',
    'Both checkers hold that the superscript η is written and by the rule belongs outside the brackets («βλεπομ(έν)η»); the editor adopted «βλεπομ(ένη)».')
add('H 68v.15', 'Кроме того, над δε ударения нет (это отдельно отметили оба проверяющих во втором раунде), поэтому по правилу словоделения пишется '
                'одно слово «τοιόνδε»; в обеих транскрипциях «… δὲ».',
    'Moreover, no accent is written over δε (noted separately by both checkers in the second round), so by the word-division rule it is one '
    'word, «τοιόνδε»; both transcriptions have «… δὲ».', lemma='τοιόνδε')
add('H 70r.2', 'После α написана приписная йота, как в ταῖς той же строки (заметил один проверяющий, подтверждено на крупном плане), поэтому '
               '«διαφορᾶι·»; в обеих транскрипциях её нет.',
    'An iota adscript is written after the α, as in ταῖς in the same line (noted by one checker, confirmed on a close-up), hence «διαφορᾶι·»; '
    'both transcriptions lack it.', lemma='διαφορᾶι·')
# three settlements by the assistant that the records first labelled as the editor's
for ref, a_ru, b_ru, a_en, b_en in (
        ('H 66v.9', 'решил редактор.', 'решил ассистент редактора: раз ударение над δια написано, слова по правилу пишутся раздельно.',
         'decided by the editor.', "settled by the editor's assistant: since an accent is written over δια, by the rule the words are separate."),
        ('H 68v.10', 'Решил редактор.', 'Редактор тоже не смог решить по скану; ассистент редактора передал место с точкой под сомнительной буквой, «ἐν μέσω» столь же возможно.',
         'Decided by the editor.', "The editor could not decide from the scan either; the editor's assistant gave the place with a dot under the doubtful letter, «ἐν μέσω» being equally possible."),
        ('Vinet 41.15', 'редактор принял написание, как напечатано', 'ассистент редактора сохранил написание, как напечатано, как и в 47.7 «neturq́ue»',
         'the editor adopted the form as printed', "the editor's assistant kept the form as printed, as at 47.7 «neturq́ue»")):
    f = F[ref]
    assert a_ru in f['ru'] and a_en in f['en'], ref
    f['ru'] = f['ru'].replace(a_ru, b_ru)
    f['en'] = f['en'].replace(a_en, b_en)

F['Par. 27r.16'] = {'ref': 'Par. 27r.16', 'lemma': 'παιήων·',
                    'ru': '«παιήων·» — верхняя точка; в транскрипции Claude «παιήων.». Точка после παιήων стоит выше, чем после ὑμέναιος и ἐξόδιος '
                          '(заметил один проверяющий, подтверждено на крупном плане). Paris 1545 транскрибировал полностью только Claude.',
                    'en': '«παιήων·», a high point; Claude\'s transcription has «παιήων.». The point after παιήων stands higher than those after '
                          'ὑμέναιος and ἐξόδιος (noted by one checker, confirmed on a close-up). Only Claude transcribed Paris 1545 in full.'}

files = {'basel1556-greek': 'Bas. ', 'pal-gr-281-greek': 'H ', 'par1545-greek': 'Par. ', 'vat-pal-gr-262-greek': 'V ',
         'vincent1847-fragments': 'Vinc. ', 'vinet1591-latin': 'Vinet '}
used = set()
for fn, pre in files.items():
    p = SP / 'merged' / f'{fn}.json'
    d = json.load(open(p, encoding='utf-8'))
    refs = [r['ref'] for r in d.get('decisions', [])] or [r['place'] for r in d.get('disputes', [])]
    refs += [k for k in F if k.startswith(pre) and k not in refs]
    d['footnotes'] = [F[r] for r in refs if r in F]
    d['footnotes_note'] = ('One footnote, in Russian and English, at every place where the two transcriptions differed (and at the later '
                           'corrections): the adopted reading, the readings of Claude and GPT-6, what the scan shows, and who decided. Written '
                           'and checked against the decision records by two agents each (2026-10-28).')
    used |= {f['ref'] for f in d['footnotes']}
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(fn, len(d['footnotes']))
print('not placed:', [k for k in F if k not in used])
json.dump(list(F.values()), open(SP / 'wf6' / 'footnotes-final.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
