"""ASE Skill Benchmark v3 — OpenRouter (open / Chinese models, English prompts).

Mirrors run_openai_50_eng.py EXACTLY for fairness: identical build_system_prompt
(base, +ase_skill_v3.md when cond==skill_v3), identical extract_python_code, and
identical scoring (run_script -> returncode==0 == success, 60s timeout).

Difference: one model per process so all 13 can run in parallel without clobbering
a shared file. Results -> results_v3/openrouter/<alias>.json, saved incrementally
after every task (so a killed/resumed run skips finished tasks).

Usage:
  python run_openrouter_50_eng.py <model_alias> [cond]
  cond in {vanilla, skill_v3}; omit to run both.
"""
import subprocess
import json
import os
import re
import time
import sys

from openai import OpenAI

BASE = os.path.dirname(os.path.abspath(__file__))
PROMPTS_FILE = os.path.join(BASE, "prompts_50_eng.json")
SKILL_V3_FILE = os.path.join(BASE, "tasks", "ase_skill_v3.md")
GEN_DIR = os.path.join(BASE, "generated_v3", "eng")
RESULTS_DIR = os.path.join(BASE, "results_v3", "openrouter")

# alias -> (openrouter api_model id, max_output_tokens)
MODELS = {
    "deepseek-v3.2":          ("deepseek/deepseek-v3.2", 24000),
    "deepseek-v4-pro":        ("deepseek/deepseek-v4-pro", 64000),
    "deepseek-r1-0528":       ("deepseek/deepseek-r1-0528", 40000),
    "qwen3-32b":              ("qwen/qwen3-32b", 24000),
    "qwen3-235b":             ("qwen/qwen3-235b-a22b-2507", 24000),
    "qwen3-235b-thinking":    ("qwen/qwen3-235b-a22b-thinking-2507", 40000),
    "minimax-m3":             ("minimax/minimax-m3", 64000),
    "kimi-k2.5":              ("moonshotai/kimi-k2.5", 24000),
    "mimo-v2.5":              ("xiaomi/mimo-v2.5", 96000),
    "gpt-oss-120b":           ("openai/gpt-oss-120b", 24000),
    "nemotron-3-super-120b":  ("nvidia/nemotron-3-super-120b-a12b", 24000),
    "solar-pro-3":            ("upstage/solar-pro-3", 24000),
    "grok-4.3":               ("x-ai/grok-4.3", 16000),
    # --- frontier-gap additions (2026-06-09) ---
    "gemini-3.1-pro":         ("google/gemini-3.1-pro-preview", 32000),
    "gpt-5.5-pro":            ("openai/gpt-5.5-pro", 64000),
    "claude-opus-4.8":        ("anthropic/claude-opus-4.8", 32000),
    "glm-4.6":                ("z-ai/glm-4.6", 24000),
    "glm-5":                  ("z-ai/glm-5", 32000),
    "qwen3-max":              ("qwen/qwen3-max", 24000),
    "mistral-large":          ("mistralai/mistral-large-2512", 24000),
    "llama-4-maverick":       ("meta-llama/llama-4-maverick", 16000),
    "command-a":              ("cohere/command-a", 16000),
    "nova-premier":           ("amazon/nova-premier-v1", 16000),
    "ernie-4.5":              ("baidu/ernie-4.5-vl-424b-a47b", 24000),
    "hunyuan-a13b":           ("tencent/hunyuan-a13b-instruct", 24000),
    # --- enrichment additions (2026-06-10): size ladder / missing vendors /
    #     open-weights counterparts / architecture diversity ---
    "qwen3-8b":               ("qwen/qwen3-8b", 24000),
    "qwen3-14b":              ("qwen/qwen3-14b", 24000),
    "glm-5.1":                ("z-ai/glm-5.1", 32000),
    "seed-1.6":               ("bytedance-seed/seed-1.6", 24000),
    "gemma-3-27b":            ("google/gemma-3-27b-it", 16000),
    "phi-4":                  ("microsoft/phi-4", 12000),
    "mercury-2":              ("inception/mercury-2", 16000),
    "olmo-3-32b-think":       ("allenai/olmo-3-32b-think", 40000),
    # --- round 3 (2026-06-10): gemma size ladder / Mistral frontier / vendor wrap-up ---
    "gemma-3-4b":             ("google/gemma-3-4b-it", 12000),
    "gemma-3-12b":            ("google/gemma-3-12b-it", 16000),
    "mistral-medium-3.5":     ("mistralai/mistral-medium-3-5", 24000),
    "step-3.7-flash":         ("stepfun/step-3.7-flash", 24000),
    "granite-4.1-8b":         ("ibm-granite/granite-4.1-8b", 16000),
    "deepseek-v4-flash":      ("deepseek/deepseek-v4-flash", 24000),
}
CONDITIONS = ["vanilla", "skill_v3"]


def get_api_key():
    r = subprocess.run(
        ["security", "find-generic-password", "-s", "openrouter-api-key", "-w"],
        capture_output=True, text=True,
    )
    return r.stdout.strip()


def load_prompts():
    with open(PROMPTS_FILE) as f:
        return json.load(f)["tasks"]


def load_skill():
    with open(SKILL_V3_FILE) as f:
        return f.read()


def extract_python_code(text):
    m = re.findall(r"```python\s*\n(.*?)```", text or "", re.DOTALL)
    if m:
        return m[0].strip()
    m2 = re.findall(r"```\s*\n(.*?)```", text or "", re.DOTALL)
    if m2:
        return m2[0].strip()
    return (text or "").strip()


def build_system_prompt(condition, skill_content):
    # IDENTICAL to run_openai_50_eng.py:build_system_prompt
    base = (
        "Write an ASE (Atomic Simulation Environment) Python script. "
        "Use only ASE built-in calculators (EMT, LJ, etc.). No GUI functions. "
        "Write concise code with minimal comments. "
        "Output a single ```python code block."
    )
    if condition == "skill_v3":
        return base + "\n\n" + skill_content
    return base


def call_openrouter(client, api_model, system_prompt, user_prompt, max_tokens):
    kwargs = dict(
        model=api_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_completion_tokens=max_tokens,
        extra_headers={"HTTP-Referer": "https://ase-bench.local",
                       "X-Title": "ASE-skill-bench"},
    )
    # retry transient failures (connection error / 429 rate limit) with backoff,
    # so parallel runs don't record false-negative FAILs.
    last = None
    for attempt in range(5):
        try:
            try:
                resp = client.chat.completions.create(**kwargs)
            except TypeError:
                kwargs.pop("max_completion_tokens", None)
                kwargs["max_tokens"] = max_tokens
                resp = client.chat.completions.create(**kwargs)
            break
        except Exception as e:
            last = e
            time.sleep(3 * (attempt + 1))
    else:
        raise last
    u = resp.usage
    usage = {
        "prompt_tokens": getattr(u, "prompt_tokens", 0) or 0,
        "completion_tokens": getattr(u, "completion_tokens", 0) or 0,
        "total_tokens": getattr(u, "total_tokens", 0) or 0,
    }
    cost = getattr(u, "cost", None)  # OpenRouter real billed USD
    return resp.choices[0].message.content, usage, cost


def run_script(filepath, timeout=60):
    # IDENTICAL scoring to run_openai_50_eng.py:run_script
    start = time.time()
    try:
        result = subprocess.run(
            ["conda", "run", "-n", "base", "python", filepath],
            capture_output=True, text=True, timeout=timeout,
            cwd=os.path.dirname(filepath),
        )
        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout[:2000],
            "stderr": result.stderr[:2000],
            "elapsed": round(time.time() - start, 3),
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": "TIMEOUT", "elapsed": timeout}
    except Exception as e:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": str(e),
                "elapsed": round(time.time() - start, 3)}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in MODELS:
        print("usage: run_openrouter_50_eng.py <model_alias> [cond]")
        print("models:", ", ".join(MODELS))
        sys.exit(1)
    alias = sys.argv[1]
    api_model, max_tokens = MODELS[alias]
    cond_filter = sys.argv[2] if len(sys.argv) > 2 else None

    # per-request timeout so a hung provider fails fast and our retry loop moves
    # on, instead of blocking indefinitely (glm/command/nova stalled without this)
    client = OpenAI(api_key=get_api_key(), base_url="https://openrouter.ai/api/v1",
                    timeout=90.0, max_retries=0)
    tasks = load_prompts()
    skill_content = load_skill()
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, f"{alias}.json")
    all_results = json.load(open(out_path)) if os.path.exists(out_path) else {}

    conds = [c for c in CONDITIONS if not cond_filter or c == cond_filter]
    for cond in conds:
        key = f"{alias}_{cond}"
        cond_dir = os.path.join(GEN_DIR, key)
        os.makedirs(cond_dir, exist_ok=True)
        system_prompt = build_system_prompt(cond, skill_content)
        results = all_results.get(key, {})
        print(f"\n{'='*60}\n  {alias} / {cond}  [{api_model}]\n{'='*60}")

        for task in tasks:
            tid = task["id"]
            if tid in results and results[tid].get("exec"):   # resume
                continue
            num = tid[1:].zfill(2)
            try:
                text, usage, cost = call_openrouter(
                    client, api_model, system_prompt, task["prompt"], max_tokens)
                code = extract_python_code(text)
                fp = os.path.join(cond_dir, f"task_{num}.py")
                with open(fp, "w") as f:
                    f.write(code + "\n")
                ex = run_script(fp)
                results[tid] = {
                    "success": ex["success"],
                    "category": task["category"],
                    "difficulty": task.get("difficulty", ""),
                    "prompt": task["prompt"],
                    "tokens": usage,
                    "cost": cost,
                    "exec": ex,
                    "code_length": len(code),
                }
                print(f"  {tid} {'PASS' if ex['success'] else 'FAIL'} "
                      f"({ex['elapsed']:.1f}s, {usage['total_tokens']}tok)")
                if not ex["success"]:
                    err = [l for l in ex["stderr"].split("\n") if l.strip()]
                    if err:
                        print(f"        -> {err[-1][:90]}")
            except Exception as e:
                results[tid] = {
                    "success": False, "category": task["category"],
                    "difficulty": task.get("difficulty", ""), "prompt": task["prompt"],
                    "error": str(e),
                }
                print(f"  {tid} ERROR: {str(e)[:80]}")
            all_results[key] = results
            with open(out_path, "w") as f:
                json.dump(all_results, f, ensure_ascii=False, indent=1)

        passed = sum(1 for r in results.values() if r.get("success"))
        print(f"  -> {alias}/{cond}: {passed}/{len(tasks)} passed")


if __name__ == "__main__":
    main()
