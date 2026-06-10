"""Tighten framing of the Blender task renders in renders/.

Slabs etc. were rendered with a generous x1.7 margin, so some structures
(T03/T16 ...) occupy <15% of the canvas. For every RGBA render: crop to the
alpha bounding box + 5% pad, then pad back to a centered square (transparent),
so the gallery shows every structure at a consistent, large scale.
RGB images (matplotlib composites) are left untouched.
Originals are archived at ~/.archive/2026-06-10/renders_pre_crop/.
"""
import glob
import os

from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))


def main():
    changed = 0
    for path in sorted(glob.glob(os.path.join(BASE, "renders", "T*.png"))):
        im = Image.open(path)
        if "A" not in im.mode:
            continue
        bbox = im.getchannel("A").getbbox()
        if not bbox:
            continue
        w, h = im.size
        bw, bh = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pad = int(max(bw, bh) * 0.05)
        x0, y0 = max(0, bbox[0] - pad), max(0, bbox[1] - pad)
        x1, y1 = min(w, bbox[2] + pad), min(h, bbox[3] + pad)
        crop = im.crop((x0, y0, x1, y1))
        cw, ch = crop.size
        side = max(cw, ch)
        sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        sq.paste(crop, ((side - cw) // 2, (side - ch) // 2))
        sq.save(path)
        frac = (bw * bh) / (w * h)
        print(f"{os.path.basename(path)}: content {frac:.2f} -> cropped {cw}x{ch} -> sq {side}")
        changed += 1
    print(f"cropped {changed} renders")


if __name__ == "__main__":
    main()
