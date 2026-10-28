"""Shared helpers for merging two transcriptions with the checkers' and the editor's decisions.

A place (from prep_wf3/prep_wf4/prep_wf5) has reading_1, reading_2 and a list of differences; decisions.json (merge_adj.py)
gives for each difference a status ('decided' with a choice, or 'editor'). adopt() rebuilds the adopted reading:
the whole of one reading when every difference goes the same way, otherwise reading 1 with the differences that went
to reading 2 (or to an agreed 'other' text) spliced in."""
import difflib, json, re, unicodedata
from pathlib import Path

APOS = ("'", 'ʼ', '᾽', '᾿', '‘')

def nfc(s):
    s = unicodedata.normalize('NFC', s or '')
    for a in APOS:
        s = s.replace(a, '’')
    return s.replace('·', '·').replace(';', ';')

def norm_cmp(s, keep_red=False):
    """As cmp_wf2.norm: the form in which two transcriptions were compared."""
    s = nfc(s)
    if not keep_red:
        s = re.sub(r'⟦r\s*|⟧', '', s)
    s = s.replace('–', '-')
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'\s+([,.;:·])', r'\1', s)

STRIP = lambda s: re.sub(r'\s*[.·,:;]\s*', ' ', s).strip()

def char_ops(a, b):
    """prep_wf3.ops with positions: word-widened character differences, de-duplicated by label in order."""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out, seen = [], set()
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t == 'equal':
            continue
        while i1 > 0 and j1 > 0 and a[i1 - 1] != ' ' and b[j1 - 1] != ' ':
            i1 -= 1; j1 -= 1
        while i2 < len(a) and j2 < len(b) and a[i2] != ' ' and b[j2] != ' ':
            i2 += 1; j2 += 1
        lab = f'(1) «{a[i1:i2]}»  /  (2) «{b[j1:j2]}»'
        if lab not in seen:
            seen.add(lab)
            out.append((i1, i2, j1, j2, lab))
    return out

def word_ops(a, b):
    """prep_wf5.ops with positions (in characters of a and b)."""
    ta, tb = a.split(' '), b.split(' ')
    pa = [sum(len(t) + 1 for t in ta[:i]) for i in range(len(ta) + 1)]
    pb = [sum(len(t) + 1 for t in tb[:i]) for i in range(len(tb) + 1)]
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t == 'equal':
            continue
        lab = f'(1) «{" ".join(ta[i1:i2]) or "—"}»  /  (2) «{" ".join(tb[j1:j2]) or "—"}»'
        # character span; a pure insertion/deletion takes the separating space with it
        ca0, ca1 = pa[i1], max(pa[i1], pa[i2] - 1)
        cb0, cb1 = pb[j1], max(pb[j1], pb[j2] - 1)
        if i1 == i2:
            ca0 = ca1 = pa[i1]
            cb1 = pb[j2]
        if j1 == j2:
            cb0 = cb1 = pb[j1]
            ca1 = pa[i2]
        out.append((ca0, ca1, cb0, cb1, lab))
    return out

def splice(a, b, spans, picks):
    """picks[i] in {'1', '2', ('other', text)}; spans[i] = (i1, i2, j1, j2). Returns None if picked spans overlap."""
    chosen = sorted(((s, p) for s, p in zip(spans, picks) if p != '1'), key=lambda x: x[0][0])
    # overlapping differences decided the same way (e.g. two widened views of one word) are one span
    merged = []
    for s, p in chosen:
        if merged and s[0] < merged[-1][0][1] and p == merged[-1][1]:
            m = merged[-1][0]
            merged[-1] = ((m[0], max(m[1], s[1]), min(m[2], s[2]), max(m[3], s[3])), p)
        else:
            merged.append((s, p))
    chosen = merged
    out, pos = [], 0
    for (i1, i2, j1, j2), p in chosen:
        if i1 < pos:
            return None
        out.append(a[pos:i1])
        out.append(b[j1:j2] if p == '2' else p[1])
        pos = i2
    out.append(a[pos:])
    return ''.join(out)

def adopt(place, item, spans_fn, overrides=None, convention=None, pre=None, groups=None):
    """Return (text or None, picks, open_differences). overrides: {diff index (1-based): pick} from the editor;
    groups: [(diff indices, pick)] - one editor decision covering several (possibly overlapping) differences, applied to
    their joint span; convention: function(place, diff_index) -> pick for differences decided as 'convention'."""
    a, b = place['reading_1'], place['reading_2']
    if pre:
        a, b = pre(a), pre(b)
    spans = spans_fn(a, b)
    labels = [s[4] for s in spans]
    if labels != place['differences']:
        raise ValueError(f"{place['id']}: recomputed differences do not match\n{labels}\n{place['differences']}")
    units, covered = [], set()
    for diffs, pick in groups or []:
        ss = [spans[i - 1] for i in diffs]
        units.append(((min(s[0] for s in ss), max(s[1] for s in ss), min(s[2] for s in ss), max(s[3] for s in ss)), pick))
        covered |= set(diffs)
    picks, open_ = [], []
    for i, row in enumerate(item['rows'], 1):
        p = None
        if i in covered:
            picks.append(next(pk for d, pk in groups if i in d))
            continue
        if overrides and i in overrides:
            p = overrides[i]
        elif row['status'] == 'decided':
            if row['choice'] in ('1', '2'):
                p = row['choice']
            elif row['choice'] == 'convention':
                p = convention(place, i) if convention else None
            else:  # agreed 'other'
                p = ('other', row['A']['other'])
        if p is None:
            open_.append(i)
            p = '1'
        picks.append(p)
        units.append((spans[i - 1][:4], p))
    if open_:
        return None, picks, open_
    if all(p == '1' for p in picks):
        return a, picks, []
    if all(p == '2' for p in picks):
        return b, picks, []
    return splice(a, b, [u[0] for u in units], [u[1] for u in units]), picks, []

def load_json(p):
    return json.load(open(p, encoding='utf-8'))

def dump_json(obj, p):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    json.dump(obj, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def reason(row):
    parts = []
    for w in ('A', 'B'):
        x = row.get(w) or {}
        if x:
            o = f' «{x["other"]}»' if x.get('other') else ''
            parts.append(f'{w}: {x.get("choice")}{o} ({x.get("confidence")}) — {x.get("seen")}')
    return ' | '.join(parts)
