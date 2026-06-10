"""22-model ASE-bench bar chart (horizontal grouped bars, vanilla vs skill).

DYNAMIC data (no hardcoding): 9 closed models from v7's SUMMARY + our 13 open
models from results_v3/openrouter/*.json. Only COMPLETE models (both conditions
50/50) are plotted, for fair pass-rate bars; partial models are skipped + logged.

Run after the bench finishes: conda run -n base python build_barplot_v8.py
Output: ase_bench_barplot_v8.png (next to this script).
"""
import json
import os
import re
import glob

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Patch

BASE = os.path.dirname(os.path.abspath(__file__))
V7 = "/Users/sean/Research-Skills/skills/ase/benchmark/benchmark_report_v7.html"
RES_DIR = os.path.join(BASE, "results_v3", "openrouter")
OUT = os.path.join(BASE, "ase_bench_barplot_v8.png")
N_TASKS = 50

# provider display order (closed first, then open/Chinese)
ORDER = ["Gemini", "OpenAI", "Claude", "DeepSeek", "Qwen", "MiniMax",
         "Moonshot", "Xiaomi", "OpenAI-oss", "NVIDIA", "Upstage", "xAI"]

# (light = w/o skill, dark = w/ skill)
PALETTE = {
    "Gemini": ("#b3cde3", "#4682b4"), "OpenAI": ("#a8ddb5", "#2e8b57"),
    "Claude": ("#e5b8a0", "#c05a3c"), "DeepSeek": ("#c9c0e8", "#6c4fb0"),
    "Qwen": ("#f3c6a5", "#d97a34"), "MiniMax": ("#add8d6", "#2c8c88"),
    "Moonshot": ("#c7d3e8", "#3f5e9c"), "Xiaomi": ("#f4b8b8", "#d24a4a"),
    "OpenAI-oss": ("#b8e0c2", "#3fa15c"), "NVIDIA": ("#cbe6a6", "#6f9e2c"),
    "Upstage": ("#d5c3e8", "#8a52c0"), "xAI": ("#cccccc", "#444444"),
}

_VENDOR = [("deepseek", "DeepSeek"), ("qwen", "Qwen"), ("minimax", "MiniMax"),
           ("kimi", "Moonshot"), ("mimo", "Xiaomi"), ("gpt-oss", "OpenAI-oss"),
           ("nemotron", "NVIDIA"), ("solar", "Upstage"), ("grok", "xAI")]


def vendor(alias):
    for k, v in _VENDOR:
        if alias.startswith(k):
            return v
    return "OpenRouter"


def pct(pc, tot):
    return round(100 * pc / tot) if tot else 0


def collect():
    """-> {provider: [(model_label, van%, skill%), ...]}, plus skipped list."""
    groups = {p: [] for p in ORDER}
    skipped = []

    # 9 closed models from v7 SUMMARY
    h = open(V7).read()
    SUMMARY = json.loads(re.search(r"const SUMMARY = (\{.*?\});\s*\n", h, re.S).group(1))
    closed = {}  # (provider, model) -> {cond: (pc,total)}
    for key, s in SUMMARY.items():
        closed.setdefault((s["provider"], s["model"]), {})[s["condition"]] = (s["pass_count"], s["total"])
    for (prov, model), cc in closed.items():
        if "vanilla" in cc and "skill_v3" in cc:
            groups.setdefault(prov, []).append(
                (model, pct(*cc["vanilla"]), pct(*cc["skill_v3"])))

    # 13 open models from our results (complete only)
    for f in sorted(glob.glob(os.path.join(RES_DIR, "*.json"))):
        alias = os.path.basename(f)[:-5]
        r = json.load(open(f))
        v, s = r.get(f"{alias}_vanilla", {}), r.get(f"{alias}_skill_v3", {})
        vp = sum(1 for x in v.values() if x.get("success"))
        sp = sum(1 for x in s.values() if x.get("success"))
        if len(v) >= N_TASKS and len(s) >= N_TASKS:
            groups.setdefault(vendor(alias), []).append(
                (alias, pct(vp, len(v)), pct(sp, len(s))))
        else:
            skipped.append(f"{alias} (van {len(v)}/50, skill {len(s)}/50)")
    return groups, skipped


def main():
    groups, skipped = collect()
    data = [(p, groups[p]) for p in ORDER if groups.get(p)]
    n_models = sum(len(m) for _, m in data)
    if skipped:
        print("SKIPPED (incomplete):", "; ".join(skipped))
    print(f"plotting {n_models} models across {len(data)} providers")

    mpl.rcParams["font.family"] = "Arial"
    mpl.rcParams["font.size"] = 11
    bar_h = 0.32
    fig, ax = plt.subplots(figsize=(10.5, max(7.8, 0.62 * n_models + 1.5)))
    fig.patch.set_facecolor("#fafaf7")
    ax.set_facecolor("#fafaf7")

    all_entries, provider_ranges = [], []
    y = 0.0
    for pi, (prov, models) in enumerate(data):
        if pi > 0:
            y -= 1.8
        y_top = y
        for mi, (mname, van, sk) in enumerate(models):
            if mi > 0:
                y -= 1.0
            all_entries.append((prov, mname, van, sk, y))
        provider_ranges.append((prov, y_top, y))

    yticks, ylabels = [], []
    for prov, mname, van, sk, yc in all_entries:
        light, dark = PALETTE.get(prov, ("#cccccc", "#555555"))
        y_wo, y_w = yc + bar_h * 0.55, yc - bar_h * 0.55
        ax.barh(y_wo, van, height=bar_h, color=light, edgecolor="white", linewidth=0.5)
        ax.barh(y_w, sk, height=bar_h, color=dark, edgecolor="white", linewidth=0.5)
        ax.text(van + 1.2, y_wo, f"{van}%", va="center", ha="left", fontsize=8.5, color="#888")
        ax.text(sk + 1.2, y_w, f"{sk}%", va="center", ha="left", fontsize=8.5,
                color=dark, fontweight="bold")
        yticks.append(yc)
        ylabels.append(mname)

    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels, fontsize=11)
    for prov, y_top, y_bot in provider_ranges:
        ax.annotate(prov, xy=(0, y_top + 0.65), xycoords=("axes fraction", "data"),
                    xytext=(4, 0), textcoords="offset points", fontsize=12,
                    fontweight="bold", fontstyle="italic",
                    color=PALETTE.get(prov, ("", "#555"))[1], va="bottom", ha="left",
                    annotation_clip=False)

    ax.set_xlim(0, 113)
    ax.set_xlabel("Pass Rate (%)", fontsize=12, labelpad=8)
    ax.xaxis.set_major_locator(plt.MultipleLocator(20))
    ax.grid(axis="x", alpha=0.2, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=10)
    ax.set_ylim(min(e[4] for e in all_entries) - 0.9, max(e[4] for e in all_entries) + 1.4)

    ax.legend(handles=[Patch(facecolor="#b0b0b0", label="w/o Skill"),
                       Patch(facecolor="#555555", label="w/ Skill")],
              loc="upper right", fontsize=10, frameon=True, edgecolor="#ccc",
              facecolor="#fafaf7", ncol=1)
    plt.tight_layout()
    plt.subplots_adjust(left=0.28)
    fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="#fafaf7")
    print(f"saved {OUT}")
    plt.close()


if __name__ == "__main__":
    main()
