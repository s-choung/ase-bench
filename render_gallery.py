"""Render the extracted task structures with Blender (sequential, 1 process per
file per the blender-atom-render skill) and build a 5x10 Task Visualizer gallery
so the 50 abstract ASE tasks become a visual grid of what each one builds.

  python render_gallery.py            # render missing + build gallery
  python render_gallery.py --html     # only rebuild gallery HTML

Structures come from structure_extract.py (GPT-5.5 skill_v3 code). Renders ->
renders/<tid>.png (perspective). Gallery -> task_gallery.html.
"""
import glob
import json
import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
V8 = os.path.join(BASE, "benchmark_report_v8.html")
STRUCT = os.path.join(BASE, "structures")
RENDERS = os.path.join(BASE, "renders")
GALLERY = os.path.join(BASE, "task_gallery.html")
BLENDER = "/Applications/Blender.app/Contents/MacOS/Blender"
SCRIPT = os.path.join(BASE, "render_autoframe_v2.py")


def task_meta():
    h = open(V8).read()
    DATA = json.loads(re.search(r"const DATA = (\{.*?\});\s*\n", h, re.S).group(1))
    return {tid: {"prompt": t.get("prompt_en") or t.get("prompt", ""),
                  "category": t.get("category", ""), "difficulty": t.get("difficulty", "")}
            for tid, t in DATA.items()}


def render_all():
    os.makedirs(RENDERS, exist_ok=True)
    import re
    xyzs = [p for p in glob.glob(os.path.join(STRUCT, "*.xyz"))
            if re.fullmatch(r"T\d+\.xyz", os.path.basename(p))]
    xyzs.sort(key=lambda p: int(os.path.basename(p)[1:-4]))
    print(f"rendering {len(xyzs)} structures (sequential Blender)")
    for xyz in xyzs:
        tid = os.path.basename(xyz)[:-4]
        out = os.path.join(RENDERS, f"{tid}.png")
        if os.path.exists(out) and os.path.getsize(out) > 1000:
            print(f"  {tid} skip (exists)")
            continue
        try:
            r = subprocess.run([BLENDER, "--background", "--python", SCRIPT,
                                "--", xyz, out, "perspective"],
                               capture_output=True, text=True, timeout=180)
            ok = os.path.exists(out)
            print(f"  {tid} {'OK' if ok else 'FAIL'}")
        except subprocess.TimeoutExpired:
            print(f"  {tid} TIMEOUT")


def build_gallery():
    meta = task_meta()
    tids = sorted(meta, key=lambda t: int(t[1:]))
    cells = []
    for tid in tids:
        m = meta[tid]
        png = f"renders/{tid}.png"
        has = os.path.exists(os.path.join(BASE, "renders", f"{tid}.png"))
        img = (f'<img src="{png}" loading="lazy" alt="{tid}">' if has
               else '<div class="noimg">no structure</div>')
        title = m["prompt"]
        short = title if len(title) < 90 else title[:88] + "…"
        cells.append(f'''<figure class="cell">
  <div class="thumb">{img}</div>
  <figcaption><span class="tid">{tid}</span><span class="cat">{m["category"]} · {m["difficulty"]}</span>
    <span class="desc">{short}</span></figcaption>
</figure>''')
    html = f'''<!doctype html><meta charset="utf-8"><title>ASE Task Visualizer — 50 structures</title>
<style>
body{{font:14px/1.5 -apple-system,system-ui,sans-serif;background:#0f1115;color:#e5e7eb;margin:0;padding:24px}}
h1{{font-size:20px;font-weight:700;margin:0 0 4px}}
p.sub{{color:#9ca3af;margin:0 0 20px;font-size:13px}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}}
.cell{{margin:0;background:#1a1d24;border:1px solid #262a33;border-radius:10px;overflow:hidden;display:flex;flex-direction:column}}
.thumb{{aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;
  background:radial-gradient(circle at 50% 40%,#2a2f3a,#15171d)}}
.thumb img{{width:100%;height:100%;object-fit:contain}}
.noimg{{color:#6b7280;font-size:12px}}
figcaption{{padding:8px 10px;display:flex;flex-direction:column;gap:2px;border-top:1px solid #262a33}}
.tid{{font-weight:800;font-size:13px;color:#a5b4fc}}
.cat{{font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.4px}}
.desc{{font-size:11px;color:#cbd5e1;line-height:1.35}}
@media(max-width:1100px){{.grid{{grid-template-columns:repeat(3,1fr)}}}}
@media(max-width:680px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
</style>
<h1>ASE Task Visualizer</h1>
<p class="sub">50 benchmark tasks &mdash; the structure GPT-5.5 (skill) builds for each, rendered in Blender. A visual key to what each abstract task is actually about.</p>
<div class="grid">
{''.join(cells)}
</div>'''
    with open(GALLERY, "w") as f:
        f.write(html)
    n = sum(1 for tid in tids if os.path.exists(os.path.join(RENDERS, f"{tid}.png")))
    print(f"wrote {GALLERY}  ({n}/{len(tids)} rendered)")


def main():
    if "--html" not in sys.argv:
        render_all()
    build_gallery()


if __name__ == "__main__":
    main()
