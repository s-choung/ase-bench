"""Build the ASE-Bench hero collage: a 12x4 mosaic of the Blender task renders
-> assets/hero_collage.jpg. Text ("ASE-Bench") is overlaid in HTML/CSS, not
baked in, so it stays crisp and i18n-able. Deterministic tile order (T01..),
slight dimming so white text reads on top.
"""
import glob
import os

from PIL import Image, ImageEnhance

BASE = os.path.dirname(os.path.abspath(__file__))
RENDERS = sorted(glob.glob(os.path.join(BASE, "renders", "T*.png")),
                 key=lambda p: int(os.path.basename(p)[1:-4]))
OUT = os.path.join(BASE, "assets", "hero_collage.jpg")

COLS, ROWS, TILE = 12, 4, 220


def center_square(img):
    w, h = img.size
    s = min(w, h)
    return img.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))


def main():
    canvas = Image.new("RGB", (COLS * TILE, ROWS * TILE), "#0e1118")
    n = COLS * ROWS
    # interleave so adjacent tiles are not consecutive task IDs (visual variety)
    order = [RENDERS[(i * 7) % len(RENDERS)] for i in range(n)]
    for i, path in enumerate(order):
        tile = Image.open(path).convert("RGB")
        tile = center_square(tile).resize((TILE, TILE), Image.LANCZOS)
        tile = ImageEnhance.Brightness(tile).enhance(0.82)
        canvas.paste(tile, ((i % COLS) * TILE, (i // COLS) * TILE))
    canvas.save(OUT, quality=80, optimize=True)
    print(f"wrote {OUT} ({os.path.getsize(OUT)//1024} KB, {COLS*TILE}x{ROWS*TILE})")


if __name__ == "__main__":
    main()
