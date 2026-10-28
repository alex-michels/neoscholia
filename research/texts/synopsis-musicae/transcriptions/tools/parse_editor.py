"""Turn the text copied from the review page into editor decisions for the merge scripts.
Usage: python -I parse_editor.py <pasted text file> <out json>
Lines look like: 'Bas. 23.7#1: 1 = οὐδέ' | '…: 2 = …' | '…: своё: TEXT' | '…: вариант проверяющего: TEXT' | '…: не разобрать' | '…: — (не решено)'
and 'REF — комментарий: TEXT'."""
import json, re, sys, unicodedata
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, str(Path(__file__).parent))
from review_spec import SPEC
Q = {f"{s['id']}#{i}": q for s in SPEC for i, q in enumerate(s['questions'], 1)}
out, comments, unresolved, unclear = {}, {}, [], []
for raw in open(sys.argv[1], encoding='utf-8'):
    line = unicodedata.normalize('NFC', raw.strip())
    m = re.match(r'(.+?#\d+):\s*(.*)$', line)
    if m and m[1] in Q:
        qid, ans, note = m[1], m[2].strip(), None
        q = Q[qid]
        if ans.startswith('1 ='):
            pick = '1'
        elif ans.startswith('2 ='):
            pick = '2'
        elif ans.startswith('своё:'):
            pick = ['other', ans.split(':', 1)[1].strip()]
        elif ans.startswith('вариант проверяющего:'):
            # a checker's option may carry his explanation after the reading: 'αὐλῶι (last letter …)'
            v = ans.split(':', 1)[1].strip()
            m2 = re.match(r'(\S+(?: \[\?\])?)\s+\((.+)\)$', v)
            pick = ['other', m2[1]] if m2 else ['other', v]
            if m2:
                note = m2[2]
        elif ans.startswith('не разобрать'):
            unclear.append(qid)  # stays open; settled separately (e.g. reading kept with [?])
            continue
        else:
            unresolved.append(qid)
            continue
        out[qid] = {'diffs': q['diffs'], 'pick': pick, 'l1': q['l1'], 'l2': q['l2'], **({'checker_note': note} if note else {})}
        continue
    m = re.match(r'(.+?) — комментарий:\s*(.*)$', line)
    if m:
        comments[m[1]] = m[2]
for qid, c in comments.items():
    for k in out:
        if k.split('#')[0] in qid:
            out[k]['comment'] = c
json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('decisions', len(out), '| unresolved', unresolved, '| unclear', unclear, '| comments', comments)
