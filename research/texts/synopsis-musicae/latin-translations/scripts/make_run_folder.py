"""Make one translator's folder for the Latin translations: PROMPT.md (with {FOLDER} replaced by the folder's own
path), about.md, latin-texts.json and scans/ (the printed Latin pages). The folder must be outside the repository and
must not exist yet.
Usage: python -I make_run_folder.py <synopsis-musicae folder> <new run folder>"""
import os, re, shutil, sys
R, RUN = sys.argv[1], os.path.abspath(sys.argv[2])
assert not os.path.exists(RUN), f'{RUN} exists'
assert 'neoscholia' not in RUN.lower(), 'the run folder must be outside the repository'
PKG = f'{R}/latin-translations/independent'
os.makedirs(f'{RUN}/scans')
os.makedirs(f'{RUN}/work')
prompt = open(f'{PKG}/PROMPT.md', encoding='utf-8').read()
assert prompt.count('{FOLDER}') == 1
open(f'{RUN}/PROMPT.md', 'w', encoding='utf-8').write(prompt.replace('{FOLDER}', RUN))
about = open(f'{PKG}/about.md', encoding='utf-8').read()
assert not re.search(r'\{EN_[A-Z_]+\}', about), 'about.md still has placeholders'
open(f'{RUN}/about.md', 'w', encoding='utf-8').write(about)
shutil.copyfile(f'{PKG}/latin-texts.json', f'{RUN}/latin-texts.json')
n = 0
for d, pat, name in ((f'{R}/source/basel1556', r'^la-seq\d+-p(\d+)\.jpg$', 'xylander-p{}.jpg'),
                     (f'{R}/source/tournon1591', r'^la-vinet-seq\d+-p(\d+)\.jpg$', 'vinet-p{}.jpg')):
    for f in sorted(os.listdir(d)):
        m = re.match(pat, f)
        if m:
            shutil.copyfile(f'{d}/{f}', f'{RUN}/scans/{name.format(m.group(1))}')
            n += 1
print(f'{RUN}: PROMPT.md, about.md, latin-texts.json, {n} scans')
