"""Build v8 dashboard = v7 (9 closed models: Gemini/OpenAI/Claude) + our 13
open/Chinese models (OpenRouter). v7 HTML is the TEMPLATE; we splice 3 JS consts
and leave the renderer untouched, so 22 models render automatically:
  const DATA       -> add DATA[tid].models[<alias>_<cond>] = {provider,model,...}
  const SUMMARY    -> add <alias>_<cond>: {provider,model,condition,pass_count,total}
  const MODEL_KEYS -> append 13 { provider, model, van, skill }

Idempotent: re-reads v7 + current results each run, so just re-run after more
models finish (partial models render with whatever tasks are done so far).

Reads: results_v3/openrouter/<alias>.json (success, exec.stdout/stderr) +
       generated_v3/eng/<alias>_<cond>/task_NN.py (code).
Output: benchmark_report_v8.html
"""
import json
import re
import os
import glob

BASE = os.path.dirname(os.path.abspath(__file__))
V7 = "/Users/sean/Research-Skills/skills/ase/benchmark/benchmark_report_v7.html"
OUT = os.path.join(BASE, "benchmark_report_v8.html")
RES_DIR = os.path.join(BASE, "results_v3", "openrouter")
GEN_DIR = os.path.join(BASE, "generated_v3", "eng")
CONDS = ["vanilla", "skill_v3"]

# alias prefix -> vendor label (shown as provider in the dashboard)
_VENDOR = [
    ("deepseek", "DeepSeek"), ("qwen", "Qwen"), ("minimax", "MiniMax"),
    ("kimi", "Moonshot"), ("mimo", "Xiaomi"), ("gpt-oss", "OpenAI"),
    ("nemotron", "NVIDIA"), ("solar", "Upstage"), ("grok", "xAI"),
    # frontier-gap additions (2026-06-09)
    ("glm", "Zhipu"), ("mistral", "Mistral"), ("llama", "Meta"),
    ("command", "Cohere"), ("nova", "Amazon"), ("ernie", "Baidu"),
    ("hunyuan", "Tencent"),
    # enrichment additions (2026-06-10)
    ("seed", "ByteDance"), ("gemma", "Google"), ("phi", "Microsoft"),
    ("mercury", "Inception"), ("olmo", "AllenAI"),
    ("step", "StepFun"), ("granite", "IBM"),
    # round 4 (2026-06-11)
    ("hy3", "Tencent"), ("ring", "InclusionAI"), ("ling", "InclusionAI"),
    ("gpt-3.5", "OpenAI"), ("gpt-4", "OpenAI"),
]


def vendor(alias):
    for k, v in _VENDOR:
        if alias.startswith(k):
            return v
    return "OpenRouter"


# short column codes for the matrix header (v7 hardcodes these per model_cond)
SHORT_ALIAS = {
    "deepseek-v3.2": "d32", "deepseek-v4-pro": "d4p", "deepseek-r1-0528": "dr1",
    "qwen3-32b": "q32", "qwen3-235b": "q23", "qwen3-235b-thinking": "q23t",
    "minimax-m3": "mmx", "kimi-k2.5": "kmi", "mimo-v2.5": "mmo",
    "gpt-oss-120b": "oss", "nemotron-3-super-120b": "nem", "solar-pro-3": "sol",
    "grok-4.3": "gr4",
    "glm-4.6": "glm", "glm-5": "glm5", "qwen3-max": "qmx", "mistral-large": "mis",
    "llama-4-maverick": "l4m", "command-a": "cmd", "nova-premier": "nova",
    "ernie-4.5": "ern", "hunyuan-a13b": "hun",
    "qwen3-8b": "q8", "qwen3-14b": "q14", "glm-5.1": "g51", "seed-1.6": "sed",
    "gemma-3-27b": "gma", "phi-4": "phi", "mercury-2": "mrc",
    "olmo-3-32b-think": "olm", "fable-5": "fb5",
    "gemma-3-4b": "gm4", "gemma-3-12b": "gm12", "mistral-medium-3.5": "mm35",
    "step-3.7-flash": "stp", "granite-4.1-8b": "grn", "deepseek-v4-flash": "d4f",
    "qwen3.7-max": "q7mx", "qwen3.7-plus": "q7pl", "kimi-k2.6": "k26",
    "nemotron-3-ultra-550b": "nemu", "gemma-4-31b": "gm41", "gemma-4-26b-a4b": "gm42",
    "hy3-preview": "hy3", "ring-2.6-1t": "rng", "ling-2.6-flash": "lng",
    "gpt-3.5-turbo": "g35", "gpt-4o": "g4o", "gpt-4.1": "g41",
    "minimax-m2.7": "mm27", "seed-2.0-lite": "sd2", "qwen3-coder-next": "qcn",
}


def read_code(alias, cond, tid):
    fp = os.path.join(GEN_DIR, f"{alias}_{cond}", f"task_{tid[1:].zfill(2)}.py")
    return open(fp).read() if os.path.exists(fp) else ""


def main():
    h = open(V7).read()

    DATA = json.loads(re.search(r"const DATA = (\{.*?\});\s*\n", h, re.S).group(1))
    SUMMARY = json.loads(re.search(r"const SUMMARY = (\{.*?\});\s*\n", h, re.S).group(1))

    # olmo-3-32b-think: listed in the OpenRouter catalog but no live endpoints
    # (every call 404s) — provider unavailability, not model weakness. Exclude.
    SKIP = {"olmo-3-32b-think"}
    aliases = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(RES_DIR, "*.json"))
                     if os.path.basename(f)[:-5] not in SKIP)
    added = []
    for alias in aliases:
        try:
            r = json.load(open(os.path.join(RES_DIR, f"{alias}.json")))
        except json.JSONDecodeError:
            print(f"!! skipping mid-write file: {alias}.json")
            continue
        prov = vendor(alias)
        # v7's buildSummary() does SUMMARY[mk.van].pass_count with NO undefined
        # guard — if either condition is missing it throws and every later model
        # row stops rendering. So only add an alias once BOTH conditions have data.
        if not all(r.get(f"{alias}_{c}") for c in CONDS):
            continue
        for cond in CONDS:
            key = f"{alias}_{cond}"
            d = r.get(key)
            if not d:
                continue
            added.append((prov, alias))
            pc = 0
            for tid, v in d.items():
                if tid not in DATA:        # only the 50 known tasks
                    continue
                ex = v.get("exec", {}) or {}
                DATA[tid]["models"][key] = {
                    "provider": prov, "model": alias, "condition": cond,
                    "success": bool(v.get("success")), "quality": -1,
                    "code": read_code(alias, cond, tid),
                    "stdout": ex.get("stdout", ""), "stderr": ex.get("stderr", ""),
                }
                pc += bool(v.get("success"))
            SUMMARY[key] = {"provider": prov, "model": alias, "condition": cond,
                            "pass_count": pc, "total": len([t for t in d if t in DATA])}

    # --- fable-5 (Anthropic direct API; lives in benchmark_results_claude.json,
    # code in generated_v3/fable-5_<cond>/, Korean prompts run) ----------------
    claude_path = os.path.join(BASE, "results_v3", "benchmark_results_claude.json")
    cj = json.load(open(claude_path)) if os.path.exists(claude_path) else {}
    if all(cj.get(f"fable-5_{c}") for c in CONDS):
        for cond in CONDS:
            key = f"fable-5_{cond}"
            d = cj[key]
            added.append(("Claude", "fable-5"))
            pc = 0
            for tid, v in d.items():
                if tid not in DATA:
                    continue
                ex = v.get("exec", {}) or {}
                cp = os.path.join(BASE, "generated_v3", key, f"task_{tid[1:].zfill(2)}.py")
                DATA[tid]["models"][key] = {
                    "provider": "Claude", "model": "Fable 5", "condition": cond,
                    "success": bool(v.get("success")), "quality": -1,
                    "code": open(cp).read() if os.path.exists(cp) else "",
                    "stdout": ex.get("stdout", ""), "stderr": ex.get("stderr", ""),
                }
                pc += bool(v.get("success"))
            SUMMARY[key] = {"provider": "Claude", "model": "Fable 5", "condition": cond,
                            "pass_count": pc, "total": len([t for t in d if t in DATA])}

    # unique model groups we added (one per alias, both conds share van/skill keys)
    seen, extra_lines = set(), []
    for prov, alias in added:
        if alias in seen:
            continue
        seen.add(alias)
        disp = {"fable-5": "Fable 5"}.get(alias, alias)
        extra_lines.append(
            f'  {{ provider: "{prov}", model: "{disp}", '
            f'van: "{alias}_vanilla", skill: "{alias}_skill_v3" }},')
    extra = "\n".join(extra_lines)

    new_data = "const DATA = " + json.dumps(DATA, ensure_ascii=False) + ";\n"
    new_summary = "const SUMMARY = " + json.dumps(SUMMARY, ensure_ascii=False) + ";\n"
    h = re.sub(r"const DATA = \{.*?\};\s*\n", lambda m: new_data, h, count=1, flags=re.S)
    h = re.sub(r"const SUMMARY = \{.*?\};\s*\n", lambda m: new_summary, h, count=1, flags=re.S)
    # append 13 groups before the closing "];" of MODEL_KEYS
    h = re.sub(r"(const MODEL_KEYS = \[.*?)\n\];",
               lambda m: m.group(1) + "\n" + extra + "\n];", h, count=1, flags=re.S)

    # add short column codes for the 13 new models into COND_SHORT
    short_lines = []
    for alias in sorted(seen):
        sa = SHORT_ALIAS.get(alias, alias[:4])
        short_lines.append(f'  "{alias}_vanilla":"{sa}-v", "{alias}_skill_v3":"{sa}-s",')
    short_extra = "\n".join(short_lines)
    h = re.sub(r"(const COND_SHORT = \{.*?)\n\};",
               lambda m: m.group(1) + "\n" + short_extra + "\n};", h, count=1, flags=re.S)

    # retitle so it's clearly v8 / 22 models
    h = h.replace("Skill Benchmark v7", "Skill Benchmark v8")

    with open(OUT, "w") as f:
        f.write(h)
    print(f"wrote {OUT}")
    print(f"  added {len(seen)} open models, {len(added)} model_conds")
    print(f"  total SUMMARY entries: {len(SUMMARY)}")


if __name__ == "__main__":
    main()
