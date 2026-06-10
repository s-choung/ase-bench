"""For computational tasks (EOS / vibration / MD), compose the STRUCTURE render
(top) and the PROPERTY plot (bottom) into one square cell image, so the gallery
shows both what the system is AND what was computed.

Reads renders/<tid>.png (Blender structure) + renders_plot/<tid>.png (matplotlib
plot) -> writes renders/<tid>.png (composite). Pure-structure tasks are left
untouched. Run after render_gallery + viz_special + viz_md."""
import os
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
RENDERS = os.path.join(BASE, "renders")
PLOTS = os.path.join(BASE, "renders_plot")

PLOT_TIDS = ["T05", "T36", "T50", "T08", "T32", "T33",
             "T06", "T07", "T27", "T28", "T29", "T30", "T31"]

W = 1000          # square cell
TOP_H = 470       # structure region
GAP = 14


def fit(img, box_w, box_h):
    img = img.convert("RGBA")
    r = min(box_w / img.width, box_h / img.height)
    return img.resize((max(1, int(img.width * r)), max(1, int(img.height * r))), Image.LANCZOS)


def main():
    done = 0
    for tid in PLOT_TIDS:
        sp = os.path.join(RENDERS, f"{tid}.png")
        pp = os.path.join(PLOTS, f"{tid}.png")
        if not (os.path.exists(sp) and os.path.exists(pp)):
            print(f"{tid}: missing ({'struct' if not os.path.exists(sp) else 'plot'})")
            continue
        canvas = Image.new("RGBA", (W, W), (255, 255, 255, 255))
        # structure on top (on a soft light panel)
        struct = fit(Image.open(sp), W - 40, TOP_H - 30)
        sx = (W - struct.width) // 2
        sy = (TOP_H - struct.height) // 2 + 10
        canvas.alpha_composite(struct, (sx, sy))
        # plot on bottom
        plot = fit(Image.open(pp), W - 20, W - TOP_H - GAP)
        px = (W - plot.width) // 2
        py = TOP_H + GAP + (W - TOP_H - GAP - plot.height) // 2
        canvas.alpha_composite(plot, (px, py))
        # thin divider
        from PIL import ImageDraw
        d = ImageDraw.Draw(canvas)
        d.line([(30, TOP_H + GAP // 2), (W - 30, TOP_H + GAP // 2)], fill=(226, 229, 234, 255), width=2)
        canvas.convert("RGB").save(sp)
        done += 1
        print(f"{tid}: composited")
    print(f"composited {done}/{len(PLOT_TIDS)}")


if __name__ == "__main__":
    main()
