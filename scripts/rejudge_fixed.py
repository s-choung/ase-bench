"""Surgical re-judge of the 37 truncation-fixed records.

build mode: writes judge_inputs/fix__<key>.json (ONLY the affected tids,
            with the re-captured full stdout).
merge mode: merges judge_out/fix__<key>.json verdicts INTO the canonical
            judge_out/<name>.json (replacing just those tids).

Old closed Claude models are keyed by display name in judge_out
(e.g. 'Haiku 4.5_skill_v3'), while the results json uses runner keys
('haiku-4-5-20251001_skill_v3') -> mapped here.

Usage: python rejudge_fixed.py build | merge
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")

# key -> [tids] (from fix_truncated_stdout.py run, 2026-06-10)
AFFECTED = {
    "gemma-3-27b_skill_v3": ["T44"],
    "grok-4.20_skill_v3": ["T34", "T35", "T37", "T40", "T44"],
    "grok-4.20_vanilla": ["T34", "T44"],
    "grok-4.3_skill_v3": ["T34", "T35"],
    "llama-4-maverick_vanilla": ["T44"],
    "llama-4-maverick_skill_v3": ["T35"],
    "mimo-v2.5_skill_v3": ["T34", "T35"],
    "minimax-m3_skill_v3": ["T35"],
    "mistral-large_vanilla": ["T34", "T44"],
    "mistral-medium-3.5_skill_v3": ["T34"],
    "qwen3-14b_skill_v3": ["T34"],
    "qwen3-235b-thinking_skill_v3": ["T34", "T35"],
    "qwen3-235b_skill_v3": ["T35"],
    "qwen3-max_skill_v3": ["T34", "T40"],
    "haiku-4-5-20251001_skill_v3": ["T37"],
    "sonnet-4-6_vanilla": ["T44"],
    "sonnet-4-6_skill_v3": ["T37"],
    "opus-4-7_skill_v3": ["T34", "T35"],
    "fable-5_skill_v3": ["T34"],
}

# runner key prefix -> judge_out display name (old closed models)
DISPLAY = {
    "haiku-4-5-20251001": "Haiku 4.5",
    "sonnet-4-6": "Sonnet 4.6",
    "opus-4-7": "Opus 4.7",
}
CLAUDE_KEYS = set(DISPLAY) | {"fable-5"}

PROMPTS = {t["id"]: t for t in json.load(open(os.path.join(BASE, "prompts_50_eng.json")))["tasks"]}
PROMPTS_KO = {t["id"]: t for t in json.load(open(os.path.join(BASE, "prompts_50.json")))["tasks"]}


def split_key(key):
    cond = "skill_v3" if key.endswith("_skill_v3") else "vanilla"
    alias = key[: -(len(cond) + 1)]
    return alias, cond


def records_for(key):
    alias, _ = split_key(key)
    if alias in CLAUDE_KEYS:
        j = json.load(open(os.path.join(RES, "benchmark_results_claude.json")))
        return j[key], os.path.join(BASE, "generated_v3", key), False
    j = json.load(open(os.path.join(RES, "openrouter", f"{alias}.json")))
    return j[key], os.path.join(BASE, "generated_v3", "eng", key), True


def judge_name(key):
    alias, cond = split_key(key)
    return f"{DISPLAY.get(alias, alias)}_{cond}"


def build():
    for key, tids in AFFECTED.items():
        records, gen_dir, eng = records_for(key)
        tasks = []
        for tid in tids:
            r = records[tid]
            cp = os.path.join(gen_dir, f"task_{tid[1:].zfill(2)}.py")
            ref = (PROMPTS if eng else PROMPTS_KO).get(tid, {})
            tasks.append({
                "tid": tid,
                "prompt": r.get("prompt", ref.get("prompt", "")),
                "category": r.get("category", ref.get("category", "")),
                "difficulty": r.get("difficulty", ref.get("difficulty", "")),
                "tests_api": ref.get("tests_api", ""),
                "code": open(cp).read() if os.path.exists(cp) else "",
                "stdout": (r.get("exec") or {}).get("stdout", ""),
            })
        out = os.path.join(RES, "judge_inputs", f"fix__{key}.json")
        json.dump({"model_cond": key, "tasks": tasks}, open(out, "w"),
                  ensure_ascii=False, indent=1)
        print(f"built {out} ({len(tasks)} tasks)")


def merge():
    for key, tids in AFFECTED.items():
        fix_path = os.path.join(RES, "judge_out", f"fix__{key}.json")
        if not os.path.exists(fix_path):
            print(f"!! missing {fix_path}")
            continue
        fix = {v["tid"]: v for v in json.load(open(fix_path))["verdicts"]}
        target_path = os.path.join(RES, "judge_out", f"{judge_name(key)}.json")
        tj = json.load(open(target_path))
        n = 0
        for v in tj["verdicts"]:
            if v["tid"] in fix:
                old = v["verdict"]
                v.update(fix[v["tid"]])
                print(f"{judge_name(key)}/{v['tid']}: {old} -> {v['verdict']} | {v['reason'][:80]}")
                n += 1
        missing = [t for t in tids if t not in {v['tid'] for v in tj['verdicts']}]
        for t in missing:
            tj["verdicts"].append(fix[t])
            print(f"{judge_name(key)}/{t}: (new) -> {fix[t]['verdict']} | {fix[t]['reason'][:80]}")
        json.dump(tj, open(target_path, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    {"build": build, "merge": merge}[sys.argv[1]]()
