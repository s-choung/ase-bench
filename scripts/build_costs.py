"""Aggregate per-model benchmark cost (USD) across both conditions.

Sources:
  - OpenRouter models: per-task `cost` recorded from the API's usage.cost
    (actual billed dollars) in results_v3/openrouter/<alias>.json
  - Claude direct API: results_v3/token_summary_claude.json (tokens) x price
  - OpenAI direct API: results_v3/token_summary_openai_eng.json x price
  - Gemini direct API: results_v3/token_summary.json x price
    (completion + thinking both bill as output tokens)

Prices ($ / 1M tokens, input/output) from the model-pricing cheatsheet and the
claude-api reference (Fable 5 $10/$50) — NOT from memory at runtime; update
here when prices change.

Writes results_v3/model_costs.json:
  { "<display model name>": {"total_usd": x, "usd_per_task": x/100,
                              "estimated": bool} }
usd_per_task = total / 100 (50 tasks x 2 conditions).

Run: conda run -n base python build_costs.py
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
OUT = os.path.join(RES, "model_costs.json")

# $ per 1M tokens (input, output) for direct-API models
PRICES = {
    "Fable 5": (10.0, 50.0),
    "Opus 4.7": (5.0, 25.0),
    "Sonnet 4.6": (3.0, 15.0),
    "Haiku 4.5": (1.0, 5.0),
    "gpt-5.5": (5.0, 30.0),
    "gpt-5.4": (2.5, 15.0),
    "gpt-5.4-mini": (0.75, 4.5),
    "2.5 Pro": (1.25, 10.0),
    "2.5 Flash": (0.30, 2.50),
    "2.5 Flash-Lite": (0.10, 0.40),
}

# token-summary key prefix -> display name
KEY2DISPLAY = {
    "fable-5": "Fable 5",
    "opus-4-7": "Opus 4.7",
    "sonnet-4-6": "Sonnet 4.6",
    "haiku-4-5-20251001": "Haiku 4.5",
    "gpt-5.5": "gpt-5.5",
    "gpt-5.4": "gpt-5.4",
    "gpt-5.4-mini": "gpt-5.4-mini",
    "2.5-pro": "2.5 Pro",
    "2.5-flash": "2.5 Flash",
    "2.5-flash-lite": "2.5 Flash-Lite",
}


def split_key(key):
    cond = "skill_v3" if key.endswith("_skill_v3") else "vanilla"
    return key[: -(len(cond) + 1)], cond


def main():
    costs = {}

    # ---- OpenRouter: actual recorded cost --------------------------------
    for f in glob.glob(os.path.join(RES, "openrouter", "*.json")):
        alias = os.path.basename(f)[:-5]
        try:
            j = json.load(open(f))
        except json.JSONDecodeError:
            continue
        total = 0.0
        for key, recs in j.items():
            for rec in recs.values():
                total += float(rec.get("cost") or 0.0)
        if total > 0:
            costs[alias] = {"total_usd": round(total, 3),
                            "usd_per_task": round(total / 100, 5),
                            "estimated": False}

    # ---- direct-API models: tokens x price -------------------------------
    summaries = {}
    for fn in ["token_summary_claude.json", "token_summary_openai_eng.json",
               "token_summary.json"]:
        fp = os.path.join(RES, fn)
        if os.path.exists(fp):
            summaries.update(json.load(open(fp)))

    agg = {}
    for key, t in summaries.items():
        alias, _ = split_key(key)
        disp = KEY2DISPLAY.get(alias)
        if disp is None or disp not in PRICES:
            continue
        inp = t.get("prompt", 0)
        out = t.get("completion", 0) + t.get("thinking", 0)
        a = agg.setdefault(disp, [0, 0])
        a[0] += inp
        a[1] += out

    for disp, (inp, out) in agg.items():
        pi, po = PRICES[disp]
        usd = inp / 1e6 * pi + out / 1e6 * po
        costs[disp] = {"total_usd": round(usd, 3),
                       "usd_per_task": round(usd / 100, 5),
                       "estimated": True}

    json.dump(costs, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {OUT} ({len(costs)} models)")
    for k, v in sorted(costs.items(), key=lambda x: -x[1]["total_usd"])[:10]:
        print(f"  {k:24s} ${v['total_usd']:>7.2f} total  ${v['usd_per_task']*100:.2f}/100tasks"
              f"{' (est)' if v['estimated'] else ''}")


if __name__ == "__main__":
    main()
