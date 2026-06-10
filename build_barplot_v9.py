"""22-model ASE-bench bar chart — CORRECT% (Opus-judged), vanilla vs skill.

Unlike v8 (pass/runs rate), this plots the CORRECT rate: Opus verdict == 2 over
50 tasks. Reads SUMMARY + MODEL_KEYS straight from benchmark_report_v9.html
(which already carries correct/pass_count/total for all 44 model_conds).
Output: ase_bench_barplot_v9.png
"""
import json
import os
import re

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Patch

BASE = os.path.dirname(os.path.abspath(__file__))
V9 = os.path.join(BASE, "benchmark_report_v9.html")
OUT = os.path.join(BASE, "ase_bench_barplot_v9.png")

ORDER = ["Gemini", "OpenAI", "Claude", "DeepSeek", "Qwen", "MiniMax",
         "Moonshot", "Xiaomi", "OpenAI-oss", "NVIDIA", "Upstage", "xAI"]
PALETTE = {
    "Gemini": ("#b3cde3", "#4682b4"), "OpenAI": ("#a8ddb5", "#2e8b57"),
    "Claude": ("#e5b8a0", "#c05a3c"), "DeepSeek": ("#c9c0e8", "#6c4fb0"),
    "Qwen": ("#f3c6a5", "#d97a34"), "MiniMax": ("#add8d6", "#2c8c88"),
    "Moonshot": ("#c7d3e8", "#3f5e9c"), "Xiaomi": ("#f4b8b8", "#d24a4a"),
    "OpenAI-oss": ("#b8e0c2", "#3fa15c"), "NVIDIA": ("#cbe6a6", "#6f9e2c"),
    "Upstage": ("#d5c3e8", "#8a52c0"), "xAI": ("#cccccc", "#444444"),
}


def pct(a, b):
    return round(100 * a / b) if b else 0


def main():
    h = open(V9).read()
    SUMMARY = json.loads(re.search(r"const SUMMARY = (\{.*?\});\s*\n", h, re.S).group(1))

    # pair vanilla / skill_v3 per (provider, model) straight from SUMMARY
    pair = {}  # (provider, model) -> {cond: summary}
    for s in SUMMARY.values():
        pair.setdefault((s["provider"], s["model"]), {})[s["condition"]] = s
    groups = {p: [] for p in ORDER}
    for (prov, model), cc in pair.items():
        vs, ss = cc.get("vanilla"), cc.get("skill_v3")
        if not vs or not ss:
            continue
        vC, sC = pct(vs.get("correct", 0), vs["total"]), pct(ss.get("correct", 0), ss["total"])
        groups.setdefault(prov, []).append((model, vC, sC))

    data = [(p, groups[p]) for p in ORDER if groups.get(p)]
    n_models = sum(len(m) for _, m in data)
    print(f"plotting {n_models} models (correct%)")

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
        models = sorted(models, key=lambda m: -m[2])
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

    ax.set_xlim(0, 108)
    ax.set_xlabel("Correct Rate (%) — Opus-judged, of 50 tasks", fontsize=12, labelpad=8)
    ax.xaxis.set_major_locator(plt.MultipleLocator(20))
    ax.grid(axis="x", alpha=0.2, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=10)
    ax.set_ylim(min(e[4] for e in all_entries) - 0.9, max(e[4] for e in all_entries) + 1.4)
    ax.set_title("ASE-bench — Correct Rate (not just runs)", fontsize=13, fontweight="bold", pad=12)
    ax.legend(handles=[Patch(facecolor="#b0b0b0", label="w/o Skill"),
                       Patch(facecolor="#555555", label="w/ Skill")],
              loc="lower right", fontsize=10, frameon=True, edgecolor="#ccc",
              facecolor="#fafaf7")
    plt.tight_layout()
    plt.subplots_adjust(left=0.28)
    fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="#fafaf7")
    print(f"saved {OUT}")
    plt.close()


if __name__ == "__main__":
    main()
