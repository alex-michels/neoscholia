"""Find text-line bands on a page image by horizontal projection; print them, optionally draw them for checking.
Usage: python -I locate_lines.py <image> [out_png_with_bands]"""
import sys
from PIL import Image, ImageDraw, ImageStat

def bands(path, x0f=0.12, x1f=0.88, min_h=0.004):
    with Image.open(path) as im:
        g = im.convert('L')
        W, H = g.size
        s = 1400 / W
        g = g.resize((1400, int(H * s)))
    st = ImageStat.Stat(g)
    thr = st.mean[0] - 1.2 * st.stddev[0]
    w = g.size[0]
    dark = g.crop((int(w * x0f), 0, int(w * x1f), g.size[1])).point(lambda v: 255 if v < thr else 0)
    col = dark.resize((1, dark.size[1]), Image.BOX)
    prof = [v / 255 * dark.size[0] for v in col.getdata()]
    prof = [sum(prof[max(0, i - 1):i + 2]) / len(prof[max(0, i - 1):i + 2]) for i in range(len(prof))]
    mx = max(prof)
    on = [v > max(2.0, 0.08 * mx) for v in prof]
    out, y = [], 0
    while y < len(on):
        if on[y]:
            y0 = y
            while y < len(on) and on[y]:
                y += 1
            if (y - y0) / len(on) >= min_h:
                out.append((int(y0 / s), int(y / s)))
        y += 1
    return out, (W, H)

if __name__ == '__main__':
    b, (W, H) = bands(sys.argv[1])
    for i, (y0, y1) in enumerate(b, 1):
        print(i, y0, y1, y1 - y0)
    if len(sys.argv) > 2:
        with Image.open(sys.argv[1]) as im:
            im = im.convert('RGB')
            d = ImageDraw.Draw(im)
            for i, (y0, y1) in enumerate(b, 1):
                d.rectangle([0, y0, W - 1, y1], outline=(255, 0, 0), width=3)
                d.text((10, y0), str(i), fill=(255, 0, 0))
            im.thumbnail((1000, 1400))
            im.save(sys.argv[2])
