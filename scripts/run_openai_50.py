"""ASE Skill Benchmark v3 — OpenAI API
50 prompts × 2 conditions (vanilla/skill_v3) × 3 models
Tracks tokens, limits output, saves generated code + results.
"""
import subprocess
import json
import os
import re
import time
import sys

from openai import OpenAI

BASE = os.path.dirname(os.path.abspath(__file__))
PROMPTS_FILE = os.path.join(BASE, "prompts_50.json")
SKILL_V3_FILE = os.path.join(BASE, "tasks", "ase_skill_v3.md")
GEN_DIR = os.path.join(BASE, "generated_v3")

MODELS = [
    "gpt-5.4-mini",
    "gpt-5.4",
    "gpt-5.5",
]
CONDITIONS = ["vanilla", "skill_v3"]
MAX_OUTPUT_TOKENS = 2048


def get_api_key():
    result = subprocess.run(
        ["security", "find-generic-password", "-s", "opencode-openai-api-key", "-w"],
        capture_output=True, text=True,
    )
    return result.stdout.strip()


def load_prompts():
    with open(PROMPTS_FILE) as f:
        return json.load(f)["tasks"]


def load_skill():
    with open(SKILL_V3_FILE) as f:
        return f.read()


def extract_python_code(text):
    matches = re.findall(r"```python\s*\n(.*?)```", text, re.DOTALL)
    if matches:
        return matches[0].strip()
    matches2 = re.findall(r"```\s*\n(.*?)```", text, re.DOTALL)
    if matches2:
        return matches2[0].strip()
    return text.strip()


def build_system_prompt(condition, skill_content):
    base = (
        "ASE (Atomic Simulation Environment) Python 스크립트를 작성하라. "
        "ASE 내장 calculator만 사용 (EMT, LJ 등). GUI 함수 금지. "
        "간결하게 코드만 작성하고 주석은 최소화. "
        "```python 코드블록 하나만 출력."
    )
    if condition == "skill_v3":
        return base + "\n\n" + skill_content
    return base


def call_openai(client, model_name, system_prompt, user_prompt):
    kwargs = dict(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_completion_tokens=MAX_OUTPUT_TOKENS,
    )
    if "5.5" not in model_name:
        kwargs["temperature"] = 0.0
    response = client.chat.completions.create(**kwargs)
    usage = {}
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens or 0,
            "completion_tokens": response.usage.completion_tokens or 0,
            "total_tokens": response.usage.total_tokens or 0,
        }
    return response.choices[0].message.content, usage


def run_script(filepath, timeout=60):
    start = time.time()
    try:
        result = subprocess.run(
            ["conda", "run", "-n", "base", "python", filepath],
            capture_output=True, text=True, timeout=timeout,
            cwd=os.path.dirname(filepath),
        )
        elapsed = time.time() - start
        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout[:2000],
            "stderr": result.stderr[:2000],
            "elapsed": round(elapsed, 3),
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": "TIMEOUT", "elapsed": timeout}
    except Exception as e:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": str(e), "elapsed": time.time() - start}


def main():
    api_key = get_api_key()
    client = OpenAI(api_key=api_key)

    tasks = load_prompts()
    skill_content = load_skill()
    all_results = {}
    token_summary = {}

    filter_model = sys.argv[1] if len(sys.argv) > 1 else None
    filter_cond = sys.argv[2] if len(sys.argv) > 2 else None

    target_models = [m for m in MODELS if not filter_model or filter_model in m]
    target_conds = [c for c in CONDITIONS if not filter_cond or c == filter_cond]

    for model_name in target_models:
        for cond in target_conds:
            key = f"{model_name}_{cond}"
            cond_dir = os.path.join(GEN_DIR, key)
            os.makedirs(cond_dir, exist_ok=True)

            system_prompt = build_system_prompt(cond, skill_content)

            print(f"\n{'='*70}")
            print(f"  {model_name} / {cond}")
            print(f"{'='*70}")

            results = {}
            total_tokens = {"prompt": 0, "completion": 0, "total": 0}

            for task in tasks:
                tid = task["id"]
                task_num = tid[1:].zfill(2)
                prompt = task["prompt"]

                print(f"  {tid:5s}", end=" ", flush=True)
                try:
                    text, usage = call_openai(client, model_name, system_prompt, prompt)
                    code = extract_python_code(text)
                    filepath = os.path.join(cond_dir, f"task_{task_num}.py")
                    with open(filepath, "w") as f:
                        f.write(code + "\n")

                    exec_result = run_script(filepath)
                    status = "PASS" if exec_result["success"] else "FAIL"
                    tok = usage.get("total_tokens", 0)
                    print(f"{status}  ({exec_result['elapsed']:.1f}s, {tok} tok)")

                    total_tokens["prompt"] += usage.get("prompt_tokens", 0)
                    total_tokens["completion"] += usage.get("completion_tokens", 0)
                    total_tokens["total"] += usage.get("total_tokens", 0)

                    results[tid] = {
                        "success": exec_result["success"],
                        "category": task["category"],
                        "difficulty": task.get("difficulty", ""),
                        "prompt": prompt,
                        "tokens": usage,
                        "exec": exec_result,
                        "code_length": len(code),
                    }

                    if not exec_result["success"]:
                        err = [l for l in exec_result["stderr"].split("\n") if l.strip()]
                        if err:
                            print(f"        → {err[-1][:100]}")

                except Exception as e:
                    print(f"ERROR: {e}")
                    results[tid] = {
                        "success": False,
                        "category": task["category"],
                        "difficulty": task.get("difficulty", ""),
                        "prompt": prompt,
                        "error": str(e),
                    }

            all_results[key] = results
            token_summary[key] = total_tokens

            passed = sum(1 for r in results.values() if r.get("success"))
            print(f"\n  → {passed}/{len(tasks)} passed | tokens: {total_tokens}")

    results_dir = os.path.join(BASE, "results_v3")
    os.makedirs(results_dir, exist_ok=True)

    results_path = os.path.join(results_dir, "benchmark_results_openai.json")
    token_path = os.path.join(results_dir, "token_summary_openai.json")

    existing_results = {}
    if os.path.exists(results_path):
        with open(results_path) as f:
            existing_results = json.load(f)
    existing_results.update(all_results)

    existing_tokens = {}
    if os.path.exists(token_path):
        with open(token_path) as f:
            existing_tokens = json.load(f)
    existing_tokens.update(token_summary)

    with open(results_path, "w") as f:
        json.dump(existing_results, f, indent=2, ensure_ascii=False)

    with open(token_path, "w") as f:
        json.dump(existing_tokens, f, indent=2)

    print(f"\n{'='*70}")
    print("  FINAL SUMMARY")
    print(f"{'='*70}")
    print(f"  {'Condition':<35s} {'Pass':>6} {'Tokens':>10}")
    print(f"  {'-'*35} {'-'*6} {'-'*10}")
    for key in sorted(all_results.keys()):
        passed = sum(1 for r in all_results[key].values() if r.get("success"))
        total = len(all_results[key])
        tok = token_summary[key]["total"]
        print(f"  {key:<35s} {passed:>3}/{total:<3} {tok:>10}")


if __name__ == "__main__":
    main()
