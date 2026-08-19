"""Parallel finisher: fire ALL remaining (cond, task) requests for one alias at
once (thread pool), exec each returned script, and save into the canonical
results_v3/openrouter/<alias>.json. Single process owns the file (kill any
sequential runner for the alias first — two-process clobber).

usage: parallel_finish.py <alias> [workers=20]
"""
import json
import os
import sys
import threading
import importlib.util

BASE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "runner", os.path.join(BASE, "run_openrouter_50_eng.py"))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI


def main():
    alias = sys.argv[1]
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    api_model, max_tokens = runner.MODELS[alias]
    # long per-request timeout: reasoning models legitimately run several minutes
    client = OpenAI(api_key=runner.get_api_key(),
                    base_url="https://openrouter.ai/api/v1",
                    timeout=600.0, max_retries=0)
    tasks = runner.load_prompts()
    skill_content = runner.load_skill()
    out_path = os.path.join(runner.RESULTS_DIR, f"{alias}.json")
    all_results = json.load(open(out_path)) if os.path.exists(out_path) else {}
    lock = threading.Lock()

    todo = []
    for cond in runner.CONDITIONS:
        key = f"{alias}_{cond}"
        all_results.setdefault(key, {})
        for task in tasks:
            if task["id"] in all_results[key] and all_results[key][task["id"]].get("exec"):
                continue
            todo.append((cond, key, task))
    print(f"{alias}: {len(todo)} remaining, {workers} workers", flush=True)

    def work(item):
        cond, key, task = item
        tid = task["id"]
        cond_dir = os.path.join(runner.GEN_DIR, key)
        os.makedirs(cond_dir, exist_ok=True)
        system_prompt = runner.build_system_prompt(cond, skill_content)
        text, usage, cost = runner.call_openrouter(
            client, api_model, system_prompt, task["prompt"], max_tokens)
        code = runner.extract_python_code(text)
        fp = os.path.join(cond_dir, f"task_{tid[1:].zfill(2)}.py")
        with open(fp, "w") as f:
            f.write(code + "\n")
        ex = runner.run_script(fp)
        rec = {
            "success": ex["success"],
            "category": task["category"],
            "difficulty": task.get("difficulty", ""),
            "prompt": task["prompt"],
            "tokens": usage,
            "cost": cost,
            "exec": ex,
            "code_length": len(code),
        }
        with lock:
            all_results[key][tid] = rec
            tmp = out_path + ".tmp"
            with open(tmp, "w") as f:
                json.dump(all_results, f)
            os.replace(tmp, out_path)
        return key, tid, ex["returncode"] == 0

    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(work, it): it for it in todo}
        for fut in as_completed(futs):
            cond, key, task = futs[fut]
            done += 1
            try:
                _, tid, ok = fut.result()
                print(f"[{done}/{len(todo)}] {key} {tid} {'PASS' if ok else 'FAIL'}", flush=True)
            except Exception as e:
                print(f"[{done}/{len(todo)}] {key} {task['id']} ERROR {type(e).__name__}: {str(e)[:120]}", flush=True)
    print("DONE", alias, flush=True)


if __name__ == "__main__":
    main()
