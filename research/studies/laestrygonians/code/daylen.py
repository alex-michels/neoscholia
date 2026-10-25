# Longest-day latitudes, grazing analysis by site, schematic sphere numbers.  python -I daylen.py
import math, sys
sys.stdout.reconfigure(encoding='utf-8')
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draco import STARS, propagate, precess, radec, obliquity, dms
D = math.pi/180

def decl(name, year):
    ra, dec, pa, pd, plx, rv = STARS[name]
    return radec(precess(propagate(ra, dec, pa, pd, plx, rv, year-2000), (year-2000)/100.0))[1]

def daylen(phi, dec, h0=0.0):
    """hours of sun above altitude h0 (deg) for declination dec at latitude phi"""
    c = (math.sin(h0*D) - math.sin(phi*D)*math.sin(dec*D)) / (math.cos(phi*D)*math.cos(dec*D))
    if c <= -1: return 24.0
    if c >= 1: return 0.0
    return 2*math.acos(c)/D/15.0

def lat_for(hours, eps, h0=0.0):
    lo, hi = 0.0, 89.9
    for _ in range(200):
        mid = (lo+hi)/2
        if daylen(mid, eps, h0) < hours: lo = mid
        else: hi = mid
    return (lo+hi)/2

def az_rise(phi, dec, h0=0.0):
    """azimuth of rising point measured from North toward East (deg)"""
    c = (math.sin(dec*D) - math.sin(h0*D)*math.sin(phi*D)) / (math.cos(h0*D)*math.cos(phi*D))
    c = max(-1, min(1, c)); return math.acos(c)/D

EPS = {'150 BC (Laskar)': obliquity(-21.49), '275 BC (Laskar)': obliquity(-22.74),
       '800 BC (Laskar)': obliquity(-27.99), 'Eratosthenes/Hipparchus/Ptolemy 11/83*180 = 23;51,20': 23 + 51/60 + 20/3600}
H0 = -50/60  # refraction 34' + solar semidiameter 16'
print('Latitude where longest day = N hours (geometric centre / with h0=-50\')')
for lab, e in EPS.items():
    row = []
    for N in (14.5, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24):
        row.append(f'{N}h:{lat_for(N-1e-9, e):.2f}/{lat_for(N-1e-9, e, H0):.2f}')
    print(f' eps={e:.4f} {lab}:\n   ' + '  '.join(row))
print()
e150 = obliquity(-21.49)
print('Arctic-circle latitude (24h, geometric) = 90 - eps:', round(90-e150, 3), dms(90-e150), ' (Ptolemy 66;8,40 =', round(90-(23+51/60+20/3600), 4), ')')
print()
SITES = [('Alexandria', 31.20), ('Rhodes', 36.44), ('Cnidus', 36.69), ('Soli (Cilicia)', 36.74), ('Mallos (Pleiades)', 36.756),
         ('Hipparchus "Athens" (tan phi = 3/4)', math.degrees(math.atan(0.75))), ('Syracuse', 37.08), ('Leontini', 37.28),
         ('Athens', 37.97), ('Pergamon', 39.13), ('Pella', 40.76), ('Byzantium', 41.01), ('Formiae', 41.26)]
for yr, lab in ((-799, '800 BC'), (-369, '370 BC (Eudoxus)'), (-274, '275 BC'), (-149, '150 BC')):
    g = decl('gam Dra (Eltanin)', yr); b = decl('bet Dra (Rastaban)', yr)
    eps = obliquity((yr-2000)/100)
    print(f'{lab}: dec gam={g:.3f} (graze lat {90-g:.2f}; apparent w/ 34\' refr {90-g-34/60:.2f}); dec bet={b:.3f} (graze lat {90-b:.2f}); eps={eps:.4f}')
    for s, phi in SITES:
        hg = phi + g - 90; hb = phi + b - 90
        print(f'   {s:38s} phi={phi:6.2f}  lower-culm alt gam {hg:+6.2f}  bet {hb:+6.2f}   longest day {daylen(phi, eps):5.2f} h (refr {daylen(phi, eps, H0):5.2f})')
    print()
print('Zenith reading: latitude = dec of head star (150 BC), longest day there')
for n in ('gam Dra (Eltanin)', 'bet Dra (Rastaban)', 'nu1 Dra', 'ksi Dra (Grumium)', 'mu Dra (Alrakis)'):
    d = decl(n, -149)
    print(f'  {n:20s} phi=dec={d:.2f}  longest day {daylen(d, e150):.2f} h (refr {daylen(d, e150, H0):.2f}); summer sunrise az {az_rise(d, e150):.1f} deg from N')
print()
for phi in (math.degrees(math.atan(0.75)), 37.97, 55.0, lat_for(23-1e-9, e150), 90-e150):
    print(f'phi={phi:.2f}: summer-solstice sunrise azimuth {az_rise(phi, e150):5.1f} deg E of N, sunset {360-az_rise(phi, e150):5.1f}; '
          f'set-to-rise gap through N = {2*az_rise(phi, e150):5.1f} deg; night {24-daylen(phi, e150):.2f} h; '
          f'arc of summer tropic below horizon {360-15*daylen(phi, e150):.1f} deg')
print()
# Schematic sphere for 150 BC, Hipparchus' Greece (phi = 36.87) and Athens
for phi in (math.degrees(math.atan(0.75)), 37.97):
    g = decl('gam Dra (Eltanin)', -149)
    print(f'SCHEMATIC 150 BC phi={phi:.2f}: pole altitude {phi:.2f}; always-visible circle radius (polar dist) {phi:.2f} -> dec >= {90-phi:.2f}; '
          f'gam Dra dec {g:.2f} (polar dist {90-g:.2f}), lower culmination alt {phi+g-90:+.2f}, upper culmination alt {90-phi+g if g<phi else 180-(90-phi+g):.2f} (zenith dist {abs(phi-g):.2f}); '
          f'sun summer solstice dec +{e150:.2f}, noon alt {90-phi+e150:.2f}, midnight depression {-(phi+e150-90):.2f}; '
          f'equator noon-alt {90-phi:.2f}; longest day {daylen(phi, e150):.2f} h')
