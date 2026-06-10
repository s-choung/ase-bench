# ASE-Bench

[![ASE-Bench](assets/readme_banner.png)](https://asebench.schoung.com)

45 models each write ASE Python scripts for 50 simulation tasks (crystals, slabs, MD, EOS, vibrations). Every script is executed and graded for physical correctness — with vs. without a one-page markdown skill.

**Live leaderboard:** [asebench.schoung.com](https://asebench.schoung.com) · [GitHub Pages mirror](https://s-choung.github.io/ase-bench/)

![Leaderboard](assets/readme_dashboard.png)

![Release timeline](assets/readme_timeline.png)

## Method in one paragraph

`returncode == 0` only proves the code *runs* — a large fraction of "passing" code solves the task wrong. Every passing run is therefore graded by a **rubric-based LLM judge (judge v2)**: each task has an explicit rubric (`judge_rubrics_50.json`) with verdict 2/1/0 boundaries and reference values *computed with ASE/EMT in the benchmark's own environment* (`reference_facts.py`). Verdicts are cross-checked against deterministic structural anchors, and a cross-model consistency audit (same task, same output → same verdict) shows **108 → 9** conflicting pairs versus a free-form judge. The only intervention between the two conditions is appending one markdown page (`tasks/ase_skill_v3.md`) to the system prompt.

## Repository

| Path | What |
|---|---|
| `index.html` | the leaderboard (latest report) |
| `prompts_50_eng.json` / `prompts_50.json` | the 50 tasks (EN / KO) |
| `tasks/ase_skill_v3.md` | the skill — the entire intervention |
| `judge_rubrics_50.json` | per-task grading rubrics (judge v2) |
| `generated_v3/` | every generated script, per model × condition |
| `results_v3/judge_out_v2/` | verdicts + reasons (leaderboard source) |
| `run_openrouter_50_eng.py` etc. | runners (resume-safe) |

## Add a model

Open a [model request](https://github.com/s-choung/ase-bench/issues/new?template=model-request.yml), or run it yourself:

```bash
python run_openrouter_50_eng.py <openrouter-alias>
```

## License

Code MIT · data & text CC-BY 4.0.
