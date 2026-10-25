# Precession of Draco-head stars to ancient epochs; grazing latitudes; long-day latitudes.
# Pure-python (no numpy). Run: python -I draco.py
import math
D2R = math.pi/180; AS2R = D2R/3600

# SIMBAD (Hipparcos 2007 / Gaia where given), J2000/ICRS, queried 2026-10-25
# name: (ra_deg, dec_deg, pmra_masyr (mu_a*cos d), pmdec_masyr, plx_mas, rv_kms)
STARS = {
 'gam Dra (Eltanin)':  (269.1515411786243, 51.48889561763423,  -8.48, -22.79, 21.14,  -27.91),
 'bet Dra (Rastaban)': (262.60817373291667,52.30138870861111, -15.89,  12.28,  8.58,  -20.825),
 'ksi Dra (Grumium)':  (268.38220642831584,56.87264192915222,  93.698, 78.914,29.0603,-26.09),
 'nu1 Dra':            (263.0440343771,    55.18424515288,   148.04,  54.194,33.2097,-15.2),
 'nu2 Dra':            (263.06684384646996,55.17291812915,   144.339, 59.585,33.4187,-16.0),
 'mu Dra (Alrakis)':   (256.33385013734693,54.47002762156135, -58.16,  67.87, 36.45,  -17.3),
}

def vec(ra, dec):
    a, d = ra*D2R, dec*D2R
    return [math.cos(d)*math.cos(a), math.cos(d)*math.sin(a), math.sin(d)]

def radec(v):
    x, y, z = v
    r = math.sqrt(x*x+y*y+z*z)
    return (math.atan2(y, x)/D2R) % 360, math.asin(z/r)/D2R

def propagate(ra, dec, pmra, pmdec, plx, rv, dt_yr):
    # Use position in AU-ish units: distance d = 1000/plx pc; velocity in pc/yr.
    a, dd = ra*D2R, dec*D2R
    p = [-math.sin(a), math.cos(a), 0.0]
    q = [-math.sin(dd)*math.cos(a), -math.sin(dd)*math.sin(a), math.cos(dd)]
    r = vec(ra, dec)
    dist_pc = 1000.0/plx
    k = 4.740470446  # km/s = 1 AU/yr
    vt_a = pmra/1000.0*dist_pc*k  # km/s
    vt_d = pmdec/1000.0*dist_pc*k
    kms_to_pcyr = 1.0/977792.2    # 1 km/s = 1.0227e-6 pc/yr
    V = [(vt_a*p[i] + vt_d*q[i] + rv*r[i])*kms_to_pcyr for i in range(3)]
    R = [r[i]*dist_pc + V[i]*dt_yr for i in range(3)]
    return R

def rot1(t, v):
    c, s = math.cos(t), math.sin(t); x, y, z = v
    return [x, c*y + s*z, -s*y + c*z]
def rot2(t, v):
    c, s = math.cos(t), math.sin(t); x, y, z = v
    return [c*x - s*z, y, s*x + c*z]
def rot3(t, v):
    c, s = math.cos(t), math.sin(t); x, y, z = v
    return [c*x + s*y, -s*x + c*y, z]

def prec_angles(T, model):
    if model == 'IAU1976':  # Lieske et al. 1977, from J2000
        zeta = 2306.2181*T + 0.30188*T**2 + 0.017998*T**3
        z    = 2306.2181*T + 1.09468*T**2 + 0.018203*T**3
        th   = 2004.3109*T - 0.42665*T**2 - 0.041833*T**3
    else:  # IAU 2006 / P03, Capitaine et al. 2003
        zeta = 2.650545 + 2306.083227*T + 0.2988499*T**2 + 0.01801828*T**3 - 0.000005971*T**4 - 0.0000003173*T**5
        z    = -2.650545 + 2306.077181*T + 1.0927348*T**2 + 0.01826837*T**3 - 0.000028596*T**4 - 0.0000002904*T**5
        th   = 2004.191903*T - 0.4294934*T**2 - 0.04182264*T**3 - 0.000007089*T**4 - 0.0000001274*T**5
    return zeta*AS2R, z*AS2R, th*AS2R

def precess(v, T, model='P03'):
    zeta, z, th = prec_angles(T, model)
    # P = R3(-z) R2(th) R3(-zeta)
    v = rot3(-zeta, v); v = rot2(th, v); v = rot3(-z, v)
    return v

def obliquity(T, model='Laskar'):
    if model == 'Laskar':  # Laskar 1986, U = T/100, valid +-10 kyr
        U = T/100.0
        c = [84381.448, -4680.93, -1.55, 1999.25, -51.38, -249.67, -39.05, 7.12, 27.87, 5.79, 2.45]
        return sum(c[i]*U**i for i in range(len(c)))/3600.0
    else:  # IAU 2006
        return (84381.406 - 46.836769*T - 0.0001831*T**2 + 0.00200340*T**3
                - 5.76e-7*T**4 - 4.34e-8*T**5)/3600.0

def dms(x):
    s = '-' if x < 0 else ''; x = abs(x)
    d = int(x); m = (x-d)*60; mm = int(m); sec = (m-mm)*60
    return f"{s}{d}°{mm:02d}'{sec:04.1f}\""

EPOCHS = [('800 BC (Homer)', -799), ('275 BC (Aratus)', -274), ('150 BC (Crates/Hipparchus)', -149), ('J2000', 2000)]

if __name__ == '__main__':
    stars = {k: v for k, v in STARS.items() if v}
    print('Obliquity:')
    for lab, y in EPOCHS:
        T = (y - 2000)/100.0
        print(f'  {lab:28s} T={T:7.3f}  Laskar86 {obliquity(T):.4f} ({dms(obliquity(T))})   IAU2006 {obliquity(T,"IAU"):.4f}')
    print()
    for name, (ra, dec, pa, pd, plx, rv) in stars.items():
        print(name)
        for lab, y in EPOCHS:
            T = (y - 2000)/100.0
            R = propagate(ra, dec, pa, pd, plx, rv, (y - 2000))
            res = {}
            for m in ('P03', 'IAU1976'):
                v = precess(R, T, m)
                res[m] = radec(v)
            ra_d, de_d = res['P03']
            print(f'  {lab:28s} RA {ra_d:8.3f}  Dec(P03) {de_d:8.4f} ({dms(de_d)})  Dec(IAU76) {res["IAU1976"][1]:8.4f}'
                  f'  polar dist {90-de_d:7.3f}  graze-lat geom {90-de_d:6.2f}  w/ refr(34\') {90-de_d-34/60:6.2f}')
        print()
