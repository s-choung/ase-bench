"""Thinking-token sweep: run the 50 ASE tasks (skill condition) at several reasoning
budgets/efforts. Captures ACTUAL reasoning_tokens per task so the x-axis is measured,
not the requested cap. Resume-safe. ccel key (openrouter2) via OPENROUTER_ACCT.

Output: results_v3/thinking_sweep/<alias>__<level>.json   (keyed by tid)
Usage:  python run_thinking_sweep.py <alias> [level]        # omit level to run all
"""
import subprocess, json, os, re, time, sys
from openai import OpenAI

BASE = os.path.dirname(os.path.abspath(__file__))
PROMPTS_FILE = os.path.join(BASE, "prompts_50_eng.json")
SKILL_V3_FILE = os.path.join(BASE, "tasks", "ase_skill_v3.md")
GEN_DIR = os.path.join(BASE, "generated_v3", "sweep")
RESULTS_DIR = os.path.join(BASE, "results_v3", "thinking_sweep")

# alias -> (api_model, max_output_tokens, control, levels)
#   control="effort": levels are effort strings ; "budget": levels are ints (0 = reasoning off)
SWEEP = {
    "gpt-oss-120b":        ("openai/gpt-oss-120b", 16000, "effort", ["minimal", "low", "medium", "high"]),
    # sonnet-5 DROPPED: thinking-independent on ASE — effort:high yields only ~24-71 reasoning
    # tokens (vs gpt-oss 2248); flat curve, not worth sweeping.
    # "sonnet-5":          ("anthropic/claude-sonnet-5", 16000, "budget", [0, 1024, 2048, 4096, 8192]),
    "deepseek-v3.2":       ("deepseek/deepseek-v3.2", 16000, "effort", ["minimal", "low", "medium", "high"]),
    "minimax-m3":          ("minimax/minimax-m3", 16000, "budget", [128, 512, 1024, 2048, 4096]),
    "kimi-k2-thinking":    ("moonshotai/kimi-k2-thinking", 16000, "budget", [512, 1024, 2048, 4096, 8192]),
    # DROPPED — thinking not controllable on ASE:
    #   qwen3-235b-thinking ignores the budget cap (512 -> 3000+ reasoning tokens);
    #   glm-5.2 barely thinks either lever (effort high->0; budget 512/4096 -> 89/28);
    #   sonnet-5 is thinking-independent (~0 reasoning even at effort:high).
    # "qwen3-235b-thinking": ("qwen/qwen3-235b-a22b-thinking-2507", 16000, "budget", [512, 1024, 2048, 4096]),
    # "glm-5.2":            ("z-ai/glm-5.2", 16000, "effort", ["minimal", "low", "medium", "high"]),
}


def get_api_key():
    acct = os.environ.get("OPENROUTER_ACCT", "openrouter2")
    return subprocess.run(["security", "find-generic-password", "-a", acct, "-s", "openrouter-api-key", "-w"],
                          capture_output=True, text=True).stdout.strip()


def extract_python_code(text):
    m = re.findall(r"```python\s*\n(.*?)```", text or "", re.DOTALL)
    if m:
        return m[0].strip()
    m2 = re.findall(r"```\s*\n(.*?)```", text or "", re.DOTALL)
    if m2:
        return m2[0].strip()
    return (text or "").strip()


def system_prompt(skill):
    base = ("Write an ASE (Atomic Simulation Environment) Python script. Use only ASE built-in "
            "calculators (EMT, LJ, etc.). No GUI functions. Write concise code with minimal comments. "
            "Output a single ```python code block.")
    return base + "\n\n" + skill


def reasoning_arg(control, level):
    if control == "effort":
        return {"effort": level}
    if level == 0:
        return {"enabled": False}
    return {"max_tokens": level}


def call(client, api_model, sysp, userp, max_tokens, reasoning):
    kwargs = dict(
        model=api_model,
        messages=[{"role": "system", "content": sysp}, {"role": "user", "content": userp}],
        max_completion_tokens=max_tokens,
        extra_body={"reasoning": reasoning, "usage": {"include": True}},
        extra_headers={"HTTP-Referer": "https://ase-bench.local", "X-Title": "ASE-thinking-sweep"},
    )
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
    ud = resp.usage.model_dump() if hasattr(resp.usage, "model_dump") else dict(resp.usage)
    det = ud.get("completion_tokens_details") or {}
    rt = det.get("reasoning_tokens") if isinstance(det, dict) else None
    if rt is None:
        rt = ud.get("reasoning_tokens")
    usage = {
        "prompt_tokens": ud.get("prompt_tokens", 0) or 0,
        "completion_tokens": ud.get("completion_tokens", 0) or 0,
        "reasoning_tokens": rt or 0,
        "total_tokens": ud.get("total_tokens", 0) or 0,
    }
    return resp.choices[0].message.content, usage, ud.get("cost")


def run_script(filepath, timeout=60):
    start = time.time()
    try:
        r = subprocess.run(["conda", "run", "-n", "base", "python", filepath],
                           capture_output=True, text=True, timeout=timeout, cwd=os.path.dirname(filepath))
        out = r.stdout if len(r.stdout) <= 3500 else (r.stdout[:2000] + "\n...[middle truncated]...\n" + r.stdout[-1500:])
        return {"success": r.returncode == 0, "returncode": r.returncode, "stdout": out,
                "stderr": r.stderr[:2000], "elapsed": round(time.time() - start, 3)}
    except subprocess.TimeoutExpired:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": "TIMEOUT", "elapsed": timeout}
    except Exception as e:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": str(e), "elapsed": round(time.time() - start, 3)}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in SWEEP:
        print("usage: run_thinking_sweep.py <alias> [level]")
        print("aliases:", ", ".join(SWEEP))
        sys.exit(1)
    alias = sys.argv[1]
    api_model, max_tokens, control, levels = SWEEP[alias]
    if len(sys.argv) > 2:
        only = sys.argv[2]
        levels = [only if control == "effort" else int(only)]

    client = OpenAI(api_key=get_api_key(), base_url="https://openrouter.ai/api/v1", timeout=120.0, max_retries=0)
    tasks = json.load(open(PROMPTS_FILE))["tasks"]
    sysp = system_prompt(open(SKILL_V3_FILE).read())
    os.makedirs(RESULTS_DIR, exist_ok=True)

    for level in levels:
        lk = str(level)
        out_path = os.path.join(RESULTS_DIR, f"{alias}__{lk}.json")
        results = json.load(open(out_path)) if os.path.exists(out_path) else {}
        cond_dir = os.path.join(GEN_DIR, f"{alias}__{lk}")
        os.makedirs(cond_dir, exist_ok=True)
        reasoning = reasoning_arg(control, level)
        print(f"\n=== {alias} / level={lk} / reasoning={reasoning} ===")
        for task in tasks:
            tid = task["id"]
            if tid in results and results[tid].get("exec"):
                continue
            num = tid[1:].zfill(2)
            try:
                text, usage, cost = call(client, api_model, sysp, task["prompt"], max_tokens, reasoning)
                code = extract_python_code(text)
                fp = os.path.join(cond_dir, f"task_{num}.py")
                open(fp, "w").write(code + "\n")
                ex = run_script(fp)
                results[tid] = {"success": ex["success"], "category": task["category"],
                                "difficulty": task.get("difficulty", ""), "prompt": task["prompt"],
                                "tokens": usage, "cost": cost, "exec": ex, "code_length": len(code)}
                print(f"  {tid} {'PASS' if ex['success'] else 'FAIL'} rtok={usage['reasoning_tokens']} tot={usage['total_tokens']}")
            except Exception as e:
                results[tid] = {"success": False, "category": task["category"],
                                "difficulty": task.get("difficulty", ""), "prompt": task["prompt"], "error": str(e)}
                print(f"  {tid} ERROR: {str(e)[:80]}")
            open(out_path, "w").write(json.dumps(results, ensure_ascii=False, indent=1))
        passed = sum(1 for r in results.values() if r.get("success"))
        rts = [(r.get("tokens", {}) or {}).get("reasoning_tokens", 0) for r in results.values() if r.get("tokens")]
        mean_rt = sum(rts) / len(rts) if rts else 0
        print(f"  -> {alias}/{lk}: {passed}/{len(tasks)} pass, mean reasoning_tokens={mean_rt:.0f}")


if __name__ == "__main__":
    main()
