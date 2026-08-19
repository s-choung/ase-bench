"""Build v10 = ASE-Bench public leaderboard page, spliced from benchmark_report_v9.html.

v10 goals (public-facing landing page, not an internal report):
  1. Rebrand: title/h1/footer -> "ASE-Bench" (+ tagline, version badge).
  2. Bar chart simplified: ONE sort toggle, Correct% only, 2-tone colors
     (vanilla light slate / skill indigo), provider LOGOS next to model names.
  3. NEW release-timeline chart: X=release month, Y=Correct%, per model two
     markers (w/o = hollow, w/ = filled) joined by a dashed connector.
  4. Task Explorer: default condition filter = w/ Skill; mini-dot badges wrap
     instead of overflowing (44+ conditions).
  5. "How to Use" section moved to the bottom of the page.

Input : benchmark_report_v9.html   (rebuild v8 -> v9 first when new models join)
Output: benchmark_report_v10.html  (idempotent: always re-derives from v9)
"""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
V9 = os.path.join(BASE, "benchmark_report_v9.html")
VER = sys.argv[1] if len(sys.argv) > 1 else "10"   # e.g. `build_v10.py 11` -> v11
OUT = os.path.join(BASE, f"benchmark_report_v{VER}.html")

TH_PROV = {"gpt-oss-120b": "OpenAI-oss", "deepseek-v3.2": "DeepSeek", "minimax-m3": "MiniMax",
           "kimi-k2-thinking": "Moonshot", "qwen3-235b-thinking": "Qwen", "glm-5.2": "Zhipu",
           "gemini-2.5-flash-lite": "Gemini"}


def build_thsweep():
    """Aggregate results_v3/thinking_sweep/<model>__<level>.json (complete levels only)
    into {model: {prov, pts:[{lvl, rt, acc}]}} for the interactive thinking chart."""
    import glob
    base = os.path.join(BASE, "results_v3", "thinking_sweep")
    if not os.path.isdir(base):
        return {}
    agg = {}
    for f in sorted(glob.glob(os.path.join(base, "*.json"))):
        name = os.path.basename(f)[:-5]
        if "__" not in name:
            continue
        model, lvl = name.split("__", 1)
        try:
            j = json.load(open(f))
        except json.JSONDecodeError:
            continue
        if len(j) < 50:
            continue
        rts = [(t.get("tokens", {}) or {}).get("reasoning_tokens", 0) for t in j.values() if t.get("tokens")]
        if not rts:
            continue
        mrt = round(sum(rts) / len(rts))
        if mrt <= 0:
            continue  # reasoning-off / zero-reasoning level can't sit on the log x-axis (log(0)=-inf)
        acc = round(sum(1 for t in j.values() if t.get("success")) / len(j) * 100, 1)
        agg.setdefault(model, {"prov": TH_PROV.get(model, "OpenRouter"), "pts": []})["pts"].append(
            {"lvl": lvl, "rt": mrt, "acc": acc})
    for m in agg:
        agg[m]["pts"].sort(key=lambda p: p["rt"])
    return {m: v for m, v in agg.items() if len(v["pts"]) >= 2}


# ---------- canonical score definition (one number per model) ----------------
# Every ranked view (bar chart / timeline / Pareto / table) already reads the
# same SUMMARY object, but nothing on the page said WHICH of the four numbers
# per model is "the score" -> readers compared w/o-Skill 100% against
# w/-Skill 96% and saw a contradiction. This caption pins the definition.
_SCORE_EN = (
    "<b>ASE-Bench score = Correct % with the ASE skill.</b> Every ranking on this page uses that one "
    "number &mdash; the bar chart, the release timeline, the cost-vs-accuracy plot and the "
    "<b>w/ Skill Correct%</b> column of the table below all show the same value for a given model. "
    "The other figures are context, not the score: <b>Runs%</b> counts scripts that merely executed "
    "without crashing, and the <b>w/o Skill</b> figures are the same model run without the skill, shown "
    "only to make the skill's effect visible. So a model reading 100% under w/o Skill and 96% under "
    "w/ Skill has an ASE-Bench score of 96%.")
_SCORE_KO = (
    "<b>ASE-Bench 점수 = ASE 스킬을 준 조건의 Correct %.</b> 이 페이지의 모든 순위는 이 한 값을 쓴다. "
    "막대 그래프, 릴리스 타임라인, 비용 대비 정확도 그래프, 아래 표의 <b>w/ Skill Correct%</b> 열이 "
    "같은 모델에 대해 모두 같은 값을 보여준다. 나머지 숫자는 점수가 아니라 참고값이다. "
    "<b>Runs%</b>는 스크립트가 죽지 않고 실행되기만 한 비율이고, <b>w/o Skill</b> 값은 같은 모델을 "
    "스킬 없이 돌린 결과로 스킬 효과를 드러내기 위해 함께 표시한다. 따라서 w/o Skill이 100%, "
    "w/ Skill이 96%인 모델의 ASE-Bench 점수는 96%다.")
SCORE_DEF_BLOCK = (
    '<p class="i18n-html score-def" style="font-size:12.5px;color:#4b5563;max-width:980px;'
    'margin:10px auto 18px;line-height:1.7;padding:11px 15px;border-left:3px solid #c7d2fe;'
    'background:#f7f8ff;border-radius:0 8px 8px 0" '
    f'data-en="{_SCORE_EN}" data-ko="{_SCORE_KO}">{_SCORE_EN}</p>\n')


# ---------- v10 interactive bar chart (single toggle, 2-tone, logos) ----------
CHART_BLOCK = '''<div class="bc-wrap">
  <div class="bc-controls">
    <label>Sort
      <select id="bc-sort">
        <option value="skill">Correct % (high&rarr;low)</option>
        <option value="delta">Skill gain (&Delta;)</option>
        <option value="release">Release (new&rarr;old)</option>
        <option value="provider">Provider</option>
        <option value="country">Country</option>
      </select>
    </label>
    <label>Show
      <select id="bc-show">
        <option value="skill">w/ ASE skill (default)</option>
        <option value="both">compare: + w/o ASE knowledge</option>
      </select>
    </label>
    <label>Weights
      <select id="bc-weights">
        <option value="both">open + closed</option>
        <option value="open">open only</option>
        <option value="closed">closed (API) only</option>
      </select>
    </label>
    <label>Models
      <select id="bc-best">
        <option value="all">all models</option>
        <option value="best">best per provider only</option>
      </select>
    </label>
    <label>Country
      <select id="bc-country">
        <option value="all">all countries</option>
      </select>
    </label>
    <span class="bc-pills" id="bc-provfilter"></span>
  </div>
  <div class="bc-chartbox">
  <div id="bc-chart"></div>
  <div id="bc-more-wrap" style="text-align:center;margin:14px 0 2px;display:none"><button id="bc-more" class="i18n" style="padding:8px 22px;border-radius:9px;border:1px solid #d0d5dd;background:#fff;color:#374151;font-weight:700;font-size:12px;cursor:pointer;transition:.12s;box-shadow:0 2px 10px rgba(15,18,25,.1)" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background='#fff'"></button></div>
  </div>
  <div class="bc-legend">
    <span id="bc-leg-van" style="display:none"><span class="bc-key" style="background:#94a3b8;opacity:.4"></span> w/o ASE knowledge (thin, faded)</span>
    <span><span class="bc-key" style="background:#10a37f"></span><span class="bc-key" style="background:#d97757"></span><span class="bc-key" style="background:#4d6bfe"></span> w/ ASE skill &mdash; color = provider</span>
    <span class="bc-note">Correct % = how many of the 50 tasks produced the physically correct answer (each script's printed numbers are checked against pre-computed reference values from real ASE calculations)</span>
  </div>
</div>
<h3 class="tl-title">Release timeline &mdash; ASE-Bench scores over model release dates</h3>
<div class="tl-controls">
  <span class="tl-rangebar"><b id="tl-from-lab"></b><span class="tl-dual"><input type="range" id="tl-from"><input type="range" id="tl-to"></span><b id="tl-to-lab"></b></span>
  <span class="tl-weights">
    <label><input type="checkbox" id="tl-open" checked> open weights</label>
    <label><input type="checkbox" id="tl-closed" checked> closed (API)</label>
  </span>
  <span class="tl-hint">drag to zoom the time range &middot; fewer points &rarr; labels appear</span>
</div>
<div class="tl-wrap">
  <div id="tl-chart"></div>
  <div id="tl-models"></div>
</div>
<h3 class="tl-title">Cost vs accuracy &mdash; the Pareto frontier</h3>
<p style="font-size:11.5px;color:#9ca3af;margin:2px 0 6px">X = benchmark spend per task (generation cost, log scale) &middot; Y = Correct% (w/ skill) &middot; dashed = Pareto frontier (nothing above-left of it). Direct-API models are token&times;price estimates (*)</p>
<div class="tl-controls">
  <span class="tl-weights">
    <label><input type="checkbox" id="pa-open" checked> open weights</label>
    <label><input type="checkbox" id="pa-closed" checked> closed (API)</label>
  </span>
</div>
<div class="tl-wrap">
  <div id="pa-chart" style="flex:1 1 auto;min-width:0"></div>
  <div id="pa-models"></div>
</div>
<h3 class="tl-title">Thinking vs accuracy &mdash; does more reasoning help?</h3>
<p style="font-size:11.5px;color:#9ca3af;margin:2px 0 6px">X = mean reasoning tokens per task (log scale) &middot; Y = pass rate &middot; each line = one model swept across thinking budgets/efforts. Exec-pass (returncode==0) &mdash; judge Correct% pending. Only cleanly thinking-controllable models shown; hover for detail.</p>
<div style="max-width:920px;margin:8px auto 1.4rem;position:relative"><div id="th-chart"></div></div>
<p class="i18n" style="font-size:12.5px;color:#6b7280;text-align:center;max-width:840px;margin:-6px auto 1.6rem;font-style:italic" data-ko="한 줄 요약: 추론을 더 한다고 정답률이 계속 오르진 않는다 — 대개 최대 thinking budget 한참 전에 정체되고 때론 오히려 떨어진다. overthinking이 능사는 아니다." data-en="Takeaway: more reasoning doesn't monotonically help — accuracy usually plateaus (and sometimes dips) well before the max budget. Overthinking isn't always a virtue.">Takeaway: more reasoning doesn't monotonically help — accuracy usually plateaus (and sometimes dips) well before the max budget. Overthinking isn't always a virtue.</p>'''

CHART_SCRIPT = '''<style>
/* breakout: charts get ~full viewport width (container is 1200px; body zoom
   1.08 means real width = css*1.08, so 87vw ~= 94% of the screen) */
.bc-wrap,.tl-wrap{width:min(87vw,1560px);position:relative;left:50%;transform:translateX(-50%)}
.bc-wrap{margin:1.2rem 0 .6rem;text-align:left}
.bc-controls{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin-bottom:14px;font-size:13px}
.bc-controls label{display:flex;flex-direction:column;gap:3px;font-size:11px;color:#6b7280;font-weight:600}
.bc-controls select{font:13px system-ui;padding:4px 8px;border:1px solid #d1d5db;border-radius:6px;background:#fff}
.bc-pills{display:grid;grid-template-rows:repeat(2,auto);grid-auto-flow:column;gap:5px;margin-left:auto;align-items:start}
.bc-pill{min-width:38px;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;padding:4px 6px;border-radius:9px;border:1px solid #e2e6ec;background:#fff;color:#4b5563;cursor:pointer;user-select:none;font-weight:700;font-size:9px;transition:.12s}
.bc-pill:hover{border-color:#94a3b8;transform:translateY(-1px)}
.bc-pill img{height:16px;width:auto;max-width:38px;object-fit:contain}
.bc-pill-name{font-size:7.5px;font-weight:700;color:#6b7280;max-width:60px;white-space:normal;text-align:center;line-height:1.15;word-break:break-word}
.bc-pill.off{opacity:.22;filter:grayscale(1)}
#bc-chart{display:flex;align-items:flex-end;gap:4px;padding:18px 0 0;width:100%}
#bc-chart.bc-faded{-webkit-mask-image:linear-gradient(to right,#000 70%,transparent 100%);mask-image:linear-gradient(to right,#000 70%,transparent 100%)}
#bc-more-wrap.overlay{position:absolute;right:8px;top:46%;transform:translateY(-50%);margin:0!important;z-index:6}
.bc-col{display:flex;flex-direction:column;align-items:center;gap:5px;flex:1 1 0;min-width:0;cursor:default}
.bc-stack{display:flex;align-items:flex-end;justify-content:center;gap:2px;height:260px;width:100%}
.bc-vbar{width:58%;max-width:18px;border-radius:5px 5px 2px 2px;position:relative;min-height:2px;transition:height .35s cubic-bezier(.4,0,.2,1)}
.bc-vbar.van{opacity:.35;width:32%;max-width:10px}
.bc-vval{position:absolute;top:-15px;left:50%;transform:translateX(-50%);font-size:8.5px;font-weight:800;white-space:nowrap}
.bc-clogo{width:15px;height:15px;object-fit:contain}
.bc-clabel{height:132px;overflow:hidden;writing-mode:vertical-rl;transform:rotate(180deg);display:flex;gap:2px;align-items:center;justify-content:flex-end}
.bc-clabel b{font-size:9px;font-weight:700;color:#1f2937;white-space:nowrap}
.bc-clabel span{font-size:7.5px;color:#9ca3af;white-space:nowrap}
.bc-legend{display:flex;gap:18px;align-items:center;margin:10px 0 0 2px;font-size:11.5px;color:#4b5563;flex-wrap:wrap}
.bc-key{display:inline-block;width:12px;height:10px;border-radius:3px;margin-right:2px;vertical-align:-1px}
.bc-note{color:#9ca3af;margin-left:auto}
.tl-title{font-size:14px;font-weight:700;color:#111;margin:26px 0 4px;border:none;text-transform:none;letter-spacing:0}
.tl-controls{display:flex;gap:22px;align-items:center;font-size:11.5px;color:#6b7280;margin:4px 0 6px;flex-wrap:wrap}
.tl-controls input[type=range]{width:150px;vertical-align:middle;accent-color:#4f46e5}
/* single dual-handle range bar (from/to on one track) */
.tl-rangebar{display:inline-flex;align-items:center;gap:9px}
.tl-dual{position:relative;width:240px;height:22px}
.tl-dual input[type=range]{position:absolute;left:0;top:0;width:100%;height:22px;margin:0;background:transparent;pointer-events:none;-webkit-appearance:none;appearance:none;accent-color:#4f46e5}
.tl-dual input[type=range]::-webkit-slider-runnable-track{height:4px;border-radius:999px;background:#e5e7eb}
.tl-dual input#tl-to::-webkit-slider-runnable-track{background:transparent}
.tl-dual input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;pointer-events:auto;width:15px;height:15px;border-radius:50%;background:#4f46e5;border:2px solid #fff;box-shadow:0 1px 3px rgba(15,18,25,.35);cursor:pointer;margin-top:-6px}
.tl-dual input[type=range]::-moz-range-track{height:4px;border-radius:999px;background:#e5e7eb}
.tl-dual input#tl-to::-moz-range-track{background:transparent}
.tl-dual input[type=range]::-moz-range-thumb{pointer-events:auto;width:15px;height:15px;border-radius:50%;background:#4f46e5;border:2px solid #fff;cursor:pointer}
.tl-weights{display:inline-flex;gap:12px}
.tl-weights label{display:inline-flex;align-items:center;gap:4px;cursor:pointer;color:#374151;font-weight:600}
.tl-weights input{accent-color:#4f46e5;cursor:pointer}
.tl-controls b{color:#1f2937;font-size:11px}
.tl-hint{color:#c2c8d2;font-size:10.5px}
#iu-chart{margin:0 0 1.4rem}
.tl-wrap{display:flex;gap:14px;align-items:flex-start;margin:0 0 1.4rem}
#tl-chart{flex:1 1 auto;min-width:0}
#tl-models,#pa-models{flex:0 0 320px;max-height:430px;overflow-y:auto;display:grid;grid-template-columns:1fr 1fr;gap:1px 6px;align-content:start;padding:2px 4px 2px 10px;border-left:1px solid #eef0f3}
@media(max-width:900px){#tl-models,#pa-models{flex-basis:200px;grid-template-columns:1fr}}
.tl-mi{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:600;color:#374151;padding:2.5px 5px;border-radius:6px;cursor:pointer;user-select:none;white-space:nowrap;transition:.12s}
.tl-mi:hover{background:#f3f4f6}
.tl-mi.off{opacity:.25;filter:grayscale(1)}
.tl-mi .dot{width:8px;height:8px;border-radius:999px;flex:0 0 auto}
.tl-mi img{width:13px;height:13px;object-fit:contain;flex:0 0 auto}
.tl-mi span{overflow:hidden;text-overflow:ellipsis}
#tl-chart svg,#iu-chart svg{width:100%;height:auto;display:block}
</style>
<script>
(function(){
  if(typeof SUMMARY==='undefined'){return;}
  // provider brand colors (representative, not official-exact)
  const PAL={OpenAI:'#10a37f',Claude:'#d97757',Gemini:'#4285f4',Google:'#34a853',
    DeepSeek:'#0891b2',Qwen:'#7c3aed',xAI:'#1f2937','OpenAI-oss':'#0d8a6a',
    Meta:'#0866ff',Mistral:'#fa520f',Cohere:'#39594d',Amazon:'#ff9900',
    Baidu:'#2932e1',Tencent:'#0052d9',ByteDance:'#5b8def',Zhipu:'#3859ff',
    Moonshot:'#5f3dc4',MiniMax:'#f23f5d',Xiaomi:'#ff6900',NVIDIA:'#76b900',
    Upstage:'#9775fa',Microsoft:'#00a4ef',Inception:'#0ea5e9',IBM:'#0f62fe',
    StepFun:'#00b8a9',AllenAI:'#f0529c',InclusionAI:'#00b4c5',Sakana:'#c2255c',
    ThinkingMachines:'#7048e8',Poolside:'#12b886',Kwaipilot:'#f59f00',Meituan:'#ffc300'};
  const pcol=p=>PAL[p]||'#64748b';
  const LOGO_ALIAS={'OpenAI-oss':'OpenAI'};
  const logoSrc=p=>'assets/logos/'+(LOGO_ALIAS[p]||p)+'.png';
  // release month (approx; YYYY-MM). Models missing here are skipped by the
  // timeline (console.warn) but still shown in the bar chart.
  const REL={'OpenAI|gpt-5.5':'2026-04','OpenAI|gpt-5.4':'2026-03','OpenAI|gpt-5.4-mini':'2026-03',
    'Claude|Fable 5':'2026-06','Claude|Opus 4.8':'2026-05','Claude|Opus 4.7':'2026-04','Claude|Sonnet 4.6':'2026-02','Claude|Haiku 4.5':'2025-10',
    'Gemini|2.5 Pro':'2025-06','Gemini|2.5 Flash':'2025-06','Gemini|2.5 Flash-Lite':'2025-07',
    'DeepSeek|deepseek-v4-pro':'2026-04','DeepSeek|deepseek-v3.2':'2025-12','DeepSeek|deepseek-r1-0528':'2025-05',
    'Qwen|qwen3-235b-thinking':'2025-07','Qwen|qwen3-235b':'2025-04','Qwen|qwen3-32b':'2025-04','Qwen|qwen3-max':'2025-09',
    'xAI|grok-4.3':'2026-04','Moonshot|kimi-k2.5':'2026-01','MiniMax|minimax-m3':'2026-06',
    'Xiaomi|mimo-v2.5':'2026-04','OpenAI-oss|gpt-oss-120b':'2025-08',
    'NVIDIA|nemotron-3-super-120b':'2026-03','Upstage|solar-pro-3':'2026-01',
    'Meta|llama-4-maverick':'2025-04','Tencent|hunyuan-a13b':'2025-06','Zhipu|glm-4.6':'2025-09',
    'Mistral|mistral-large':'2024-11','Cohere|command-a':'2025-03','Amazon|nova-premier':'2025-04',
    'Baidu|ernie-4.5':'2025-06',
    'Qwen|qwen3-8b':'2025-04','Qwen|qwen3-14b':'2025-04','Zhipu|glm-5.1':'2026-03',
    'ByteDance|seed-1.6':'2025-06','Google|gemma-3-27b':'2025-03','Microsoft|phi-4':'2024-12',
    'Inception|mercury-2':'2026-02','AllenAI|olmo-3-32b-think':'2025-11',
    'Google|gemma-3-4b':'2025-03','Google|gemma-3-12b':'2025-03','Mistral|mistral-medium-3.5':'2026-03',
    'StepFun|step-3.7-flash':'2026-05','IBM|granite-4.1-8b':'2026-04','DeepSeek|deepseek-v4-flash':'2026-04',
    'xAI|grok-4.20':'2026-04',
    'Qwen|qwen3.7-max':'2026-05','Qwen|qwen3.7-plus':'2026-06','Moonshot|kimi-k2.6':'2026-04',
    'NVIDIA|nemotron-3-ultra-550b':'2026-06','Google|gemma-4-31b':'2026-04','Google|gemma-4-26b-a4b':'2026-04',
    'Tencent|hy3-preview':'2026-04','InclusionAI|ring-2.6-1t':'2026-05','InclusionAI|ling-2.6-flash':'2026-04',
    'OpenAI|gpt-3.5-turbo':'2023-03','OpenAI|gpt-4o':'2024-05','OpenAI|gpt-4.1':'2025-04',
    'MiniMax|minimax-m2.7':'2026-03','ByteDance|seed-2.0-lite':'2026-03','Qwen|qwen3-coder-next':'2026-02',
    'Mistral|mistral-nemo':'2024-07','Meta|llama-3.1-8b':'2024-07','Mistral|mistral-small-3':'2025-01',
    'Amazon|nova-lite':'2024-12','Meta|llama-3-8b':'2024-04','Meta|llama-3.3-70b':'2024-12',
    'DeepSeek|deepseek-v3':'2024-12','Qwen|qwen2.5-72b':'2024-09','Meta|llama-3.1-70b':'2024-07',
    'Claude|claude-3-haiku':'2024-03','Meta|llama-3-70b':'2024-04','Google|gemma-2-27b':'2024-06',
    'Qwen|qwen2.5-coder-32b':'2024-11','DeepSeek|deepseek-r1-distill-70b':'2025-01',
    'OpenAI|gpt-3.5-turbo-instruct':'2023-09','DeepSeek|deepseek-r1':'2025-01',
    'Mistral|mixtral-8x22b':'2024-04','Mistral|mistral-large-2407':'2024-07','Cohere|command-r-plus':'2024-08',
    'OpenAI|o1':'2024-12','OpenAI|o3-mini':'2025-01','OpenAI|gpt-4':'2023-03',
    'OpenAI|gpt-4-turbo':'2024-04','OpenAI|gpt-4o-may':'2024-05','OpenAI|gpt-4o-mini':'2024-07',
    'Gemini|gemini-3.5-flash':'2026-05','Gemini|gemini-3.1-pro':'2026-03','Gemini|gemini-3.1-flash-lite':'2026-03',
    'Gemini|gemini-3-flash':'2026-01','Meta|llama-4-scout':'2025-04','OpenAI|o3':'2025-04','OpenAI|o4-mini':'2025-04',
    'Claude|Sonnet 5':'2026-06','Zhipu|glm-5.2':'2026-06','Moonshot|kimi-k2.7-code':'2026-06','Sakana|fugu-ultra':'2026-06',
    'OpenAI|gpt-5.6-sol':'2026-07','OpenAI|gpt-5.6-terra':'2026-07','Moonshot|kimi-k3':'2026-07',
    'xAI|grok-4.5':'2026-07','Gemini|gemini-3.6-flash':'2026-07','ThinkingMachines|inkling':'2026-07',
    'Meta|muse-spark-1.1':'2026-07','Poolside|laguna-s-2.1':'2026-07','Kwaipilot|kat-coder-pro-v2.5':'2026-07',
    'OpenAI|gpt-5.6-luna':'2026-07','Qwen|qwen3.6-flash':'2026-04','Meituan|longcat-2.0':'2026-07',
    'Claude|Opus 5':'2026-07','Zhipu|glm-5.3':'2026-08','Qwen|qwen3.8-max':'2026-08',
    'xAI|grok-4.6':'2026-08','Gemini|gemini-3.7-flash':'2026-08','Upstage|solar-pro4':'2026-08',
    'Qwen|qwen3.8-2.4t':'2026-08','DeepSeek|deepseek-v4-pro-0813':'2026-08','NVIDIA|nemotron-3.5-lightning':'2026-08',
    'DeepSeek|deepseek-v4-flash-0731':'2026-07','Meta|muse-spark-1.2':'2026-08',
    'Tencent|hy3':'2026-07','Xiaomi|mimo-v2.5-pro':'2026-06'};

  // model metadata for tooltips: params (null = undisclosed/unknown) + open weights
  const META={'OpenAI|gpt-5.5':{p:null,o:false},'OpenAI|gpt-5.4':{p:null,o:false},'OpenAI|gpt-5.4-mini':{p:null,o:false},
    'Claude|Fable 5':{p:null,o:false},'Claude|Opus 4.8':{p:null,o:false},'Claude|Opus 4.7':{p:null,o:false},'Claude|Sonnet 4.6':{p:null,o:false},'Claude|Haiku 4.5':{p:null,o:false},
    'Gemini|2.5 Pro':{p:null,o:false},'Gemini|2.5 Flash':{p:null,o:false},'Gemini|2.5 Flash-Lite':{p:null,o:false},
    'DeepSeek|deepseek-r1-0528':{p:'685B MoE (37B act)',o:true},'DeepSeek|deepseek-v3.2':{p:'671B MoE (37B act)',o:true},
    'DeepSeek|deepseek-v4-pro':{p:null,o:true},'DeepSeek|deepseek-v4-flash':{p:null,o:true},
    'DeepSeek|deepseek-v4-flash-0731':{p:null,o:true},'Meta|muse-spark-1.2':{p:null,o:false},
    'Tencent|hy3':{p:null,o:false},'Xiaomi|mimo-v2.5-pro':{p:null,o:true},
    'Qwen|qwen3-8b':{p:'8B',o:true},'Qwen|qwen3-14b':{p:'14B',o:true},'Qwen|qwen3-32b':{p:'32B',o:true},
    'Qwen|qwen3-235b':{p:'235B MoE (22B act)',o:true},'Qwen|qwen3-235b-thinking':{p:'235B MoE (22B act)',o:true},
    'Qwen|qwen3-max':{p:null,o:false},
    'xAI|grok-4.3':{p:null,o:false},'xAI|grok-4.20':{p:null,o:false},
    'Zhipu|glm-4.6':{p:'355B MoE (32B act)',o:true},'Zhipu|glm-5.1':{p:null,o:true},
    'Moonshot|kimi-k2.5':{p:'1T MoE (32B act)',o:true},'MiniMax|minimax-m3':{p:null,o:true},
    'Xiaomi|mimo-v2.5':{p:null,o:true},'OpenAI-oss|gpt-oss-120b':{p:'117B MoE (5.1B act)',o:true},
    'NVIDIA|nemotron-3-super-120b':{p:'120B',o:true},'Upstage|solar-pro-3':{p:null,o:true},
    'Meta|llama-4-maverick':{p:'400B MoE (17B act)',o:true},'Tencent|hunyuan-a13b':{p:'80B MoE (13B act)',o:true},
    'Mistral|mistral-large':{p:'123B',o:true},'Mistral|mistral-medium-3.5':{p:null,o:false},
    'Cohere|command-a':{p:'111B',o:true},'Amazon|nova-premier':{p:null,o:false},
    'Baidu|ernie-4.5':{p:'300B MoE (47B act)',o:true},'ByteDance|seed-1.6':{p:null,o:false},
    'Google|gemma-3-4b':{p:'4B',o:true},'Google|gemma-3-12b':{p:'12B',o:true},'Google|gemma-3-27b':{p:'27B',o:true},
    'Microsoft|phi-4':{p:'14B',o:true},'Inception|mercury-2':{p:null,o:false},
    'IBM|granite-4.1-8b':{p:'8B',o:true},'StepFun|step-3.7-flash':{p:null,o:true},
    'AllenAI|olmo-3-32b-think':{p:'32B',o:true},
    'Qwen|qwen3.7-max':{p:null,o:false},'Qwen|qwen3.7-plus':{p:null,o:false},
    'Moonshot|kimi-k2.6':{p:null,o:true},'NVIDIA|nemotron-3-ultra-550b':{p:'550B MoE (55B act)',o:true},
    'Google|gemma-4-31b':{p:'31B',o:true},'Google|gemma-4-26b-a4b':{p:'26B MoE (4B act)',o:true},
    'Tencent|hy3-preview':{p:null,o:false},'InclusionAI|ring-2.6-1t':{p:'1T MoE',o:true},
    'InclusionAI|ling-2.6-flash':{p:null,o:true},
    'OpenAI|gpt-3.5-turbo':{p:null,o:false},'OpenAI|gpt-4o':{p:null,o:false},'OpenAI|gpt-4.1':{p:null,o:false},
    'MiniMax|minimax-m2.7':{p:null,o:true},'ByteDance|seed-2.0-lite':{p:null,o:false},
    'Qwen|qwen3-coder-next':{p:null,o:true},
    'Mistral|mistral-nemo':{p:'12B',o:true},'Meta|llama-3.1-8b':{p:'8B',o:true},
    'Mistral|mistral-small-3':{p:'24B',o:true},'Amazon|nova-lite':{p:null,o:false},
    'Meta|llama-3-8b':{p:'8B',o:true},'Meta|llama-3.3-70b':{p:'70B',o:true},
    'DeepSeek|deepseek-v3':{p:'671B MoE (37B act)',o:true},'Qwen|qwen2.5-72b':{p:'72B',o:true},
    'Meta|llama-3.1-70b':{p:'70B',o:true},'Claude|claude-3-haiku':{p:null,o:false},
    'Meta|llama-3-70b':{p:'70B',o:true},'Google|gemma-2-27b':{p:'27B',o:true},
    'Qwen|qwen2.5-coder-32b':{p:'32B',o:true},'DeepSeek|deepseek-r1-distill-70b':{p:'70B',o:true},
    'OpenAI|gpt-3.5-turbo-instruct':{p:null,o:false},'DeepSeek|deepseek-r1':{p:'671B MoE (37B act)',o:true},
    'Mistral|mixtral-8x22b':{p:'141B MoE (39B act)',o:true},'Mistral|mistral-large-2407':{p:'123B',o:true},
    'Cohere|command-r-plus':{p:'104B',o:true},
    'OpenAI|o1':{p:null,o:false},'OpenAI|o3-mini':{p:null,o:false},'OpenAI|gpt-4':{p:null,o:false},
    'OpenAI|gpt-4-turbo':{p:null,o:false},'OpenAI|gpt-4o-may':{p:null,o:false},'OpenAI|gpt-4o-mini':{p:null,o:false},
    'Gemini|gemini-3.5-flash':{p:null,o:false},'Gemini|gemini-3.1-pro':{p:null,o:false},
    'Gemini|gemini-3.1-flash-lite':{p:null,o:false},'Gemini|gemini-3-flash':{p:null,o:false},
    'Meta|llama-4-scout':{p:'109B MoE (17B act)',o:true},'OpenAI|o3':{p:null,o:false},'OpenAI|o4-mini':{p:null,o:false},
    'Claude|Sonnet 5':{p:null,o:false},'Zhipu|glm-5.2':{p:null,o:true},'Moonshot|kimi-k2.7-code':{p:null,o:true},'Sakana|fugu-ultra':{p:null,o:false},
    'OpenAI|gpt-5.6-sol':{p:null,o:false},'OpenAI|gpt-5.6-terra':{p:null,o:false},'Moonshot|kimi-k3':{p:null,o:true},
    'xAI|grok-4.5':{p:null,o:false},'Gemini|gemini-3.6-flash':{p:null,o:false},'ThinkingMachines|inkling':{p:null,o:false},
    'Meta|muse-spark-1.1':{p:null,o:false},'Poolside|laguna-s-2.1':{p:null,o:false},'Kwaipilot|kat-coder-pro-v2.5':{p:null,o:false},
    'OpenAI|gpt-5.6-luna':{p:null,o:false},'Qwen|qwen3.6-flash':{p:null,o:false},'Meituan|longcat-2.0':{p:null,o:true},
    'Claude|Opus 5':{p:null,o:false},'Zhipu|glm-5.3':{p:null,o:true},'Qwen|qwen3.8-max':{p:null,o:false},
    'xAI|grok-4.6':{p:null,o:false},'Gemini|gemini-3.7-flash':{p:null,o:false},'Upstage|solar-pro4':{p:null,o:true},
    'Qwen|qwen3.8-2.4t':{p:'2.4T MoE (95B act)',o:true},'DeepSeek|deepseek-v4-pro-0813':{p:null,o:true},'NVIDIA|nemotron-3.5-lightning':{p:null,o:true}};
  const metaLine=m=>{const x=META[m.provider+'|'+m.model]||{};
    return `${x.p||'params undisclosed'} · ${x.o===undefined?'?':x.o?'open weights':'closed (API)'}`;};
  const pair={};
  Object.values(SUMMARY).forEach(s=>{const k=s.provider+'|'+s.model;(pair[k]=pair[k]||{provider:s.provider,model:s.model})[s.condition]=s;});
  const MODELS=Object.values(pair).filter(p=>p.vanilla&&p['skill_v3']).map(p=>({
    provider:p.provider,model:p.model,total:p.vanilla.total||50,
    vCorr:p.vanilla.correct||0,sCorr:p['skill_v3'].correct||0,
    vRun:p.vanilla.pass_count||0,sRun:p['skill_v3'].pass_count||0,
    rel:REL[p.provider+'|'+p.model]||''}));
  const provs=[...new Set(MODELS.map(m=>m.provider))];
  const state={sort:'skill',show:'skill',bcW:'both',bcBest:false,bcCountry:'all',off:new Set(),offP:new Set(),showOpen:true,showClosed:true,
    paOffP:new Set(),paOpen:true,paClosed:true};
  // responsive chart width: match the container's real width so shrinking the
  // window narrows the plot instead of scaling everything down
  const chartW=el=>Math.max(620,Math.round(el&&el.clientWidth||980));
  const pct=(a,t)=>t?Math.round(100*a/t):0;
  const vv=m=>pct(m.vCorr,m.total), sv=m=>pct(m.sCorr,m.total);

  // ---- provider -> HQ country (for the country filter/group view) ----
  const COUNTRY={OpenAI:'US','OpenAI-oss':'US',Claude:'US',Gemini:'US',Google:'US',Meta:'US',xAI:'US',
    NVIDIA:'US',Microsoft:'US',Amazon:'US',IBM:'US',Inception:'US',AllenAI:'US',
    ThinkingMachines:'US',Poolside:'US',
    DeepSeek:'China',Qwen:'China',Moonshot:'China',Zhipu:'China',MiniMax:'China',
    Xiaomi:'China',Baidu:'China',Tencent:'China',ByteDance:'China',StepFun:'China',
    InclusionAI:'China',Kwaipilot:'China',Meituan:'China',
    Mistral:'France',Cohere:'Canada',Upstage:'Korea',Sakana:'Japan'};
  const FLAG={US:'\\uD83C\\uDDFA\\uD83C\\uDDF8',China:'\\uD83C\\uDDE8\\uD83C\\uDDF3',France:'\\uD83C\\uDDEB\\uD83C\\uDDF7',
    Canada:'\\uD83C\\uDDE8\\uD83C\\uDDE6',Korea:'\\uD83C\\uDDF0\\uD83C\\uDDF7',Japan:'\\uD83C\\uDDEF\\uD83C\\uDDF5'};
  const ctry=p=>COUNTRY[p]||'Other';

  // ---- bar chart ----
  const pf=document.getElementById('bc-provfilter');
  provs.forEach(p=>{const sp=document.createElement('span');sp.className='bc-pill';
    sp.title=p+' — click to toggle';
    const im=document.createElement('img');im.src=logoSrc(p);im.alt=p;
    im.onerror=()=>{im.remove();};
    sp.appendChild(im);
    const nm=document.createElement('span');nm.className='bc-pill-name';nm.textContent=p;
    sp.appendChild(nm);
    sp.onclick=()=>{state.off.has(p)?state.off.delete(p):state.off.add(p);sp.classList.toggle('off');render();renderIU();renderTL();renderPA();renderTH();};
    pf.appendChild(sp);});

  const chart=document.getElementById('bc-chart');
  function render(){
    let rows=MODELS.filter(m=>!state.off.has(m.provider));
    if(state.bcCountry&&state.bcCountry!=='all') rows=rows.filter(m=>ctry(m.provider)===state.bcCountry);
    if(state.bcW!=='both') rows=rows.filter(m=>{const o=(META[m.provider+'|'+m.model]||{}).o; return state.bcW==='open'?o===true:o===false;});
    if(state.bcBest){const top={};rows.forEach(m=>{if(!top[m.provider]||sv(m)>sv(top[m.provider]))top[m.provider]=m;});rows=Object.values(top);}
    if(state.sort==='country') rows.sort((a,b)=>ctry(a.provider).localeCompare(ctry(b.provider))||sv(b)-sv(a));
    else if(state.sort==='release') rows.sort((a,b)=>(b.rel||'').localeCompare(a.rel||'')||sv(b)-sv(a));
    else if(state.sort==='provider') rows.sort((a,b)=>a.provider.localeCompare(b.provider)||sv(b)-sv(a));
    else if(state.sort==='delta') rows.sort((a,b)=>(sv(b)-vv(b))-(sv(a)-vv(a)));
    else rows.sort((a,b)=>sv(b)-sv(a));
    const BC_TOP=30,BC_PEEK=42;
    const collapsed=!state.bcExpanded&&rows.length>BC_TOP;
    const shown=collapsed?rows.slice(0,BC_PEEK):rows;
    chart.innerHTML=shown.map(m=>{
      const c=pcol(m.provider);const sk=sv(m),va=vv(m);const d=sk-va;
      // in skill-gain sort the number above the bar IS the gain, not Correct%
      const val=state.sort==='delta'?`${d>0?'+':''}${d}`:`${sk}`;
      const bars=`<div class="bc-vbar" style="height:${Math.max(sk,1)}%;background:${c}"><span class="bc-vval" style="color:${c}">${val}</span></div>`
        +(state.show==='both'?`<div class="bc-vbar van" style="height:${Math.max(va,1)}%;background:${c}"></div>`:'');
      return `<div class="bc-col" title="${m.provider} ${m.model} — w/ Skill ${sk}% · w/o ${va}% (Δ ${sk-va>0?'+':''}${sk-va}%p)">`
        +`<div class="bc-stack">${bars}</div>`
        +`<img class="bc-clogo" src="${logoSrc(m.provider)}" alt="${m.provider}" onerror="this.style.visibility='hidden'">`
        +`<div class="bc-clabel"><b>${m.model}</b></div></div>`;
    }).join('');
    document.getElementById('bc-leg-van').style.display=state.show==='both'?'':'none';
    const _mw=document.getElementById('bc-more-wrap'),_mb=document.getElementById('bc-more');
    chart.classList.toggle('bc-faded',collapsed);
    _mw.classList.toggle('overlay',collapsed);
    if(rows.length>BC_TOP){_mw.style.display='';
      _mb.setAttribute('data-en',state.bcExpanded?('▲ Show top '+BC_TOP):('▼ Show all '+rows.length+' models'));
      _mb.setAttribute('data-ko',state.bcExpanded?('▲ 상위 '+BC_TOP+'개만'):('▼ 전체 '+rows.length+'개 보기'));
      _mb.textContent=_mb.getAttribute('data-'+(typeof currentLang!=='undefined'?currentLang:'en'));
    }else{_mw.style.display='none';}
  }
  document.getElementById('bc-sort').onchange=e=>{state.sort=e.target.value;render();};
  document.getElementById('bc-show').onchange=e=>{state.show=e.target.value;render();};
  document.getElementById('bc-more').onclick=()=>{state.bcExpanded=!state.bcExpanded;render();};
  const _bcW=document.getElementById('bc-weights'); if(_bcW) _bcW.onchange=e=>{state.bcW=e.target.value;render();};
  const _bcB=document.getElementById('bc-best'); if(_bcB) _bcB.onchange=e=>{state.bcBest=e.target.value==='best';render();};
  const _bcC=document.getElementById('bc-country');
  if(_bcC){
    [...new Set(MODELS.map(m=>ctry(m.provider)))].sort().forEach(c=>{
      const o=document.createElement('option');o.value=c;o.textContent=`${FLAG[c]||''} ${c}`.trim();_bcC.appendChild(o);});
    _bcC.onchange=e=>{state.bcCountry=e.target.value;render();};
  }

  // ---- runs vs correct: the inflation gap (kept as code, not rendered:
  // user removed the section; re-add <div id="iu-chart"> to revive) ----
  const iu=document.getElementById('iu-chart');
  function renderIU(){
    if(!iu) return;
    const rows=MODELS.filter(m=>!state.off.has(m.provider));
    if(!rows.length){iu.innerHTML='';return;}
    const W=980,H=400,L=46,R=16,T=18,B=42;
    const rr=m=>pct(m.sRun,m.total);
    const X=v=>L+(W-L-R)*v/100;
    const Y=v=>T+(H-T-B)*(1-v/100);
    let g='';
    for(let v=0;v<=100;v+=20){
      g+=`<line x1="${X(v)}" y1="${T}" x2="${X(v)}" y2="${H-B}" stroke="#f3f4f6"/><text x="${X(v)}" y="${H-B+14}" text-anchor="middle" font-size="10" fill="#9ca3af">${v}</text>`;
      g+=`<line x1="${L}" y1="${Y(v)}" x2="${W-R}" y2="${Y(v)}" stroke="#eef0f3"/><text x="${L-7}" y="${Y(v)+3.5}" text-anchor="end" font-size="10" fill="#9ca3af">${v}</text>`;
    }
    // diagonal: runs == correct (honest); everything below ran but was wrong
    g+=`<line x1="${X(0)}" y1="${Y(0)}" x2="${X(100)}" y2="${Y(100)}" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="6 4"/>`;
    const showL=rows.length<=20;
    let pts='';
    rows.forEach((m,i)=>{
      const x=X(rr(m)),y=Y(sv(m));const c=pcol(m.provider);
      const infl=rr(m)-sv(m);
      pts+=`<g><title>${m.provider} ${m.model} (w/ skill)&#10;runs ${rr(m)}% · correct ${sv(m)}%&#10;inflation ${infl}%p (ran but wrong)</title>`
        +`<circle cx="${x}" cy="${y}" r="5.5" fill="${c}" opacity=".88"/>`
        +(showL?`<text x="${x+7}" y="${y+(i%2?9:-5)}" font-size="8.5" fill="#475569">${m.model}</text>`:'')
        +`</g>`;
    });
    const ann=`<g font-size="10" fill="#9ca3af">`
      +`<text x="${X(50)+10}" y="${Y(56)}" transform="rotate(-37 ${X(50)+10} ${Y(56)})">runs = correct (honest code)</text>`
      +`<text x="${X(68)}" y="${Y(22)}" fill="#c2410c">&darr; below the line: ran, but solved it wrong</text>`
      +`<text x="${L+10}" y="${T+10}" fill="#4b5563" font-weight="700">Y = Correct % (w/ skill)</text>`
      +`<text x="${W-R}" y="${H-B+30}" text-anchor="end">X = Runs % (returncode 0, w/ skill) &middot; hover for labels</text></g>`;
    iu.innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Runs vs correct inflation scatter">${g}${pts}${ann}</svg>`;
  }

  // ---- shared greedy label placer (collision-avoiding) ----
  // cands: [{x,y,text,bold,fill,prio}] point anchors; bounds {L,R,T,B,W,H}.
  // Tries offset slots around each point, skips slots colliding with already-
  // placed label boxes or point positions; draws a leader line when the label
  // lands far from its point. Returns SVG string.
  function placeLabels(cands,pointsXY,bounds,opts){
    opts=opts||{};
    const FS=opts.fs||8.5;
    const placed=[];const est=t=>t.length*FS*0.6+4;
    // default slot order: top-left of the point first (reads naturally),
    // then nearby alternatives. With opts.drop, a label that fits nowhere
    // nearby is hidden instead of dragged far away on a leader line — so
    // label density adapts to zoom level / window width automatically.
    const slots=opts.slots||[[-8,-8,'end'],[8,-8,'start'],[-8,-20,'end'],[8,-20,'start'],
                 [-8,10,'end'],[8,10,'start'],[-8,-32,'end'],[8,-32,'start']];
    const clash=(bx,by,bw)=>{
      if(bx<bounds.L+2||bx+bw>bounds.W-bounds.R-2||by-9<bounds.T||by+2>bounds.H-bounds.B) return true;
      for(const p of placed) if(bx<p.x+p.w&&bx+bw>p.x&&by-9<p.y+2&&by+2>p.y-9) return true;
      for(const q of pointsXY) if(q[0]>bx-4&&q[0]<bx+bw+4&&q[1]>by-11&&q[1]<by+4) return true;
      return false;};
    let out='';
    cands.sort((a,b)=>(b.prio||0)-(a.prio||0));
    for(const c of cands){
      const w=est(c.text);let hit=null;
      // high-priority labels (frontier endpoints) may reach further left
      const mySlots=(c.prio||0)>=2
        ?slots.concat([[-22,-8,'end'],[-36,-8,'end'],[-22,-20,'end'],[-36,-20,'end'],[-52,-12,'end'],
                       [-22,10,'end'],[-40,10,'end'],[-22,22,'end'],[-40,22,'end']])
        :slots;
      for(const [dx,dy,an] of mySlots){
        const bx=an==='start'?c.x+dx:c.x+dx-w;
        if(!clash(bx,c.y+dy,w)){hit=[bx,c.y+dy,an,dx,dy];break;}
      }
      if(!hit&&(c.prio||0)>=2){
        // frontier labels must show: retry allowing overlap with points
        // (but never with other labels or outside the plot)
        for(const [dx,dy,an] of mySlots){
          const bx=an==='start'?c.x+dx:c.x+dx-w, by=c.y+dy;
          if(bx<bounds.L+2||bx+w>bounds.W-bounds.R-2||by-9<bounds.T||by+2>bounds.H-bounds.B) continue;
          let bad=false;
          for(const p of placed) if(bx<p.x+p.w&&bx+w>p.x&&by-9<p.y+2&&by+2>p.y-9){bad=true;break;}
          if(!bad){hit=[bx,by,an,dx,dy];break;}
        }
      }
      if(!hit&&opts.drop) continue;  // no nearby space: hide (tooltip still has it)
      if(!hit){ // fallback: keep inside plot horizontally, stack downward until free
        const right=c.x>bounds.W-bounds.R-90;
        const an=right?'end':'start', dx=right?-8:8;
        let bx=right?c.x+dx-w:c.x+dx, by=c.y-14;
        for(let k=0;k<20&&clash(bx,by,w);k++) by+=11;
        hit=[bx,by,an,dx,by-c.y];
      }
      const [bx,by,an,dx,dy]=hit;
      placed.push({x:bx,y:by,w:w,w2:w});
      if(Math.abs(dy)>=26)
        out+=`<line x1="${c.x}" y1="${c.y}" x2="${an==='start'?bx-2:bx+w+2}" y2="${by-3}" stroke="#cbd5e1" stroke-width=".8"/>`;
      out+=`<text x="${an==='start'?bx:bx+w}" y="${by}" text-anchor="${an}" font-size="${FS}" font-weight="${c.bold?'700':'400'}" fill="${c.fill||'#475569'}">${c.text}</text>`;
    }
    return out;
  }

  // ---- release timeline (SVG scatter) ----
  const tl=document.getElementById('tl-chart');
  const monthIdx=r=>{const[y,m]=r.split('-').map(Number);return y*12+(m-1);};
  function renderTL(){
    const wOk=m=>{const o=(META[m.provider+'|'+m.model]||{}).o;
      return o===undefined||(o?state.showOpen:state.showClosed);};
    const rows=MODELS.filter(m=>!state.off.has(m.provider)&&!state.offP.has(m.provider)&&m.rel&&wOk(m)
      &&monthIdx(m.rel)>=state.tlFrom&&monthIdx(m.rel)<=state.tlTo);
    if(!rows.length){tl.innerHTML='<p style="font-size:12px;color:#9ca3af;padding:20px 0">no models in this range</p>';return;}
    const W=chartW(tl),H=420,L=46,R=16,T=18,B=44;
    const now=new Date();
    const todayMi=now.getFullYear()*12+now.getMonth();
    const m0=state.tlFrom-1,m1=Math.max(state.tlTo,Math.min(todayMi,state.tlTo))+1;
    const X=mi=>L+(W-L-R)*(mi-m0)/(m1-m0||1);
    const Y=v=>T+(H-T-B)*(1-v/100);
    let g='';
    for(let v=0;v<=100;v+=20)
      g+=`<line x1="${L}" y1="${Y(v)}" x2="${W-R}" y2="${Y(v)}" stroke="#eef0f3"/><text x="${L-7}" y="${Y(v)+3.5}" text-anchor="end" font-size="11" fill="#9ca3af">${v}</text>`;
    for(let mi=m0;mi<=m1;mi++){
      const yy=Math.floor(mi/12),mm=mi%12+1;
      if(mm===1||mm===4||mm===7||mm===10)
        g+=`<line x1="${X(mi)}" y1="${T}" x2="${X(mi)}" y2="${H-B}" stroke="#f3f4f6"/><text x="${X(mi)}" y="${H-B+15}" text-anchor="middle" font-size="10.5" fill="#9ca3af">${yy}-${String(mm).padStart(2,'0')}</text>`;
    }
    // jitter models sharing a month; collect positions first
    const seen={};
    const pos=[];
    rows.sort((a,b)=>monthIdx(a.rel)-monthIdx(b.rel)).forEach((m,i)=>{
      const mi=monthIdx(m.rel);const n=(seen[mi]=(seen[mi]||0)+1);
      const x=X(mi)+((n-1)%3-1)*7;
      pos.push({m,i,x,yV:Y(vv(m)),yS:Y(sv(m))});
    });
    // SOTA frontier: running best w/-Skill Correct% over release time
    let best=-1;const fr=[];
    pos.forEach(p=>{if(sv(p.m)>best){best=sv(p.m);fr.push(p);}});
    const frLine=fr.length>1
      ?`<polyline points="${fr.map(p=>p.x+','+p.yS).join(' ')}" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4" opacity=".55"/>`
      :'';
    // labels: all when sparse (<=18 points), otherwise SOTA-frontier only (hover for the rest)
    const showAll=pos.length<=18;
    let pts='';
    const labCands=[];
    const frSet=new Set(fr);
    pos.forEach(p=>{
      const {m,i,x,yV,yS}=p;
      const isFr=frSet.has(p);
      const tip=`<b>${m.model}</b> &middot; ${m.provider} (${m.rel})<br>${metaLine(m)}<br>w/ Skill ${sv(m)}% &middot; w/o ${vv(m)}%${isFr?'<br><span style=color:#fbbf24>SOTA at release</span>':''}`;
      const c=pcol(m.provider);
      if(showAll||isFr) labCands.push({x,y:yS,text:m.model,bold:isFr,prio:isFr?(p===fr[fr.length-1]?4:2):1});
      // when w/o == w/ the markers coincide: draw only the filled one
      // (both numbers are in the tooltip; e.g. Fable 5: 96% = 96%)
      const overlap=Math.abs(yV-yS)<7;
      pts+=`<g data-tip="${tip.replace(/"/g,'&quot;')}" style="cursor:pointer">`
        +(overlap?'':`<rect x="${x-3.5}" y="${Math.min(yV,yS)}" width="7" height="${Math.abs(yS-yV)}" fill="${c}" opacity=".24"/>`
          +`<circle cx="${x}" cy="${yV}" r="4" fill="#fff" stroke="${c}" stroke-width="1.6"/>`)
        +`<circle cx="${x}" cy="${yS}" r="5" fill="${c}"/>`
        +`<circle cx="${x}" cy="${yS}" r="11" fill="transparent"/>`
        +`</g>`;
    });
    const labels=placeLabels(labCands,pos.map(p=>[p.x,p.yS]),{L,R,T,B,W,H},{drop:true,fs:9.5});
    // "Today" marker (client-side date), only when inside the selected range
    let today='';
    if(todayMi>=m0&&todayMi<=m1){
      const tx=X(todayMi+now.getDate()/31);
      today=`<line x1="${tx}" y1="${T}" x2="${tx}" y2="${H-B+18}" stroke="#f43f5e" stroke-width="1.2" stroke-dasharray="5 4" opacity=".75"/>`
        +`<text x="${tx}" y="${H-B+30}" text-anchor="middle" font-size="11" font-weight="700" fill="#f43f5e">Today</text>`;
    }
    // legend, below the time axis (left-aligned)
    const lx=L+12, ly=H-6;
    const legend=`<g font-size="11.5" fill="#4b5563">`
      +`<circle cx="${lx}" cy="${ly}" r="5" fill="#64748b"/><text x="${lx+9}" y="${ly+4}">w/ Skill</text>`
      +`<circle cx="${lx+75}" cy="${ly}" r="4" fill="#fff" stroke="#64748b" stroke-width="1.6"/><text x="${lx+84}" y="${ly+4}">w/o Skill</text>`
      +`<text x="${lx+155}" y="${ly+4}" fill="#9ca3af">color = provider · Y = Correct %</text></g>`;
    tl.innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Correct rate vs model release date">${g}${today}${frLine}${pts}${labels}${legend}</svg>`;
  }

  // ---- timeline range sliders ----
  const dated=MODELS.filter(m=>m.rel).map(m=>monthIdx(m.rel));
  const _now=new Date();
  const gm0=Math.min(...dated), gm1=Math.max(Math.max(...dated),_now.getFullYear()*12+_now.getMonth());
  state.tlFrom=gm0; state.tlTo=gm1;
  const fmtMi=mi=>`${Math.floor(mi/12)}-${String(mi%12+1).padStart(2,'0')}`;
  const frEl=document.getElementById('tl-from'), toEl=document.getElementById('tl-to');
  frEl.min=gm0;frEl.max=gm1;frEl.value=gm0; toEl.min=gm0;toEl.max=gm1;toEl.value=gm1;
  const syncLab=()=>{document.getElementById('tl-from-lab').textContent=fmtMi(+frEl.value);
    document.getElementById('tl-to-lab').textContent=fmtMi(+toEl.value);};
  frEl.oninput=()=>{if(+frEl.value>+toEl.value)frEl.value=toEl.value;state.tlFrom=+frEl.value;syncLab();renderTL();};
  toEl.oninput=()=>{if(+toEl.value<+frEl.value)toEl.value=frEl.value;state.tlTo=+toEl.value;syncLab();renderTL();};
  syncLab();
  const opEl=document.getElementById('tl-open'), clEl=document.getElementById('tl-closed');
  if(opEl){opEl.onchange=()=>{state.showOpen=opEl.checked;renderTL();};}
  if(clEl){clEl.onchange=()=>{state.showClosed=clEl.checked;renderTL();};}
  const paOp=document.getElementById('pa-open'), paCl=document.getElementById('pa-closed');
  if(paOp){paOp.onchange=()=>{state.paOpen=paOp.checked;renderPA();};}
  if(paCl){paCl.onchange=()=>{state.paClosed=paCl.checked;renderPA();};}

  // ---- pareto provider toggle list (same UX as the timeline) ----
  // canonical provider order (best w/-skill score over ALL models) so the
  // timeline and pareto legend lists always match
  const PROV_ORDER=(()=>{const b={};MODELS.forEach(m=>{b[m.provider]=Math.max(b[m.provider]||0,sv(m));});
    return Object.keys(b).sort((x,y)=>b[y]-b[x]);})();
  const pam=document.getElementById('pa-models');
  if(pam&&typeof COSTS!=='undefined'){
    const PROVS2=PROV_ORDER.filter(p=>MODELS.some(m=>m.provider===p&&COSTS[m.model]));
    const items2=[];
    const all2=document.createElement('div');
    all2.className='tl-mi';
    all2.style.cssText='font-weight:800;color:#4f46e5;border:1px solid #c7d2fe;background:#eef2ff;margin-bottom:4px;justify-content:center;grid-column:1/-1';
    const lab2=document.createElement('span');
    const sync2=()=>{lab2.textContent=state.paOffP.size>=PROVS2.length?'All on':'All off';};
    all2.appendChild(lab2);
    all2.onclick=()=>{
      if(state.paOffP.size>=PROVS2.length){
        state.paOffP.clear();items2.forEach(it=>it.classList.remove('off'));
      }else{
        PROVS2.forEach(p=>state.paOffP.add(p));items2.forEach(it=>it.classList.add('off'));
      }
      sync2();renderPA();};
    pam.appendChild(all2);
    PROVS2.forEach(p=>{
      const it=document.createElement('div');it.className='tl-mi';
      it.title=`${p} — click to hide/show in the pareto chart`;
      it.innerHTML=`<span class="dot" style="background:${pcol(p)}"></span>`
        +`<img src="${logoSrc(p)}" alt="" onerror="this.remove()">`
        +`<span>${p}</span>`;
      it.onclick=()=>{
        state.paOffP.has(p)?state.paOffP.delete(p):state.paOffP.add(p);
        it.classList.toggle('off');sync2();renderPA();};
      items2.push(it);
      pam.appendChild(it);
    });
    sync2();
  }

  // ---- responsive re-render on window resize ----
  let _rsz;
  window.addEventListener('resize',()=>{
    clearTimeout(_rsz);
    _rsz=setTimeout(()=>{renderTL();renderPA();renderTH();},150);
  });

  // ---- timeline hover tooltip (instant, custom — native <title> is too slow) ----
  const tlTip=document.createElement('div');
  tlTip.id='tl-tip';
  tlTip.style.cssText='position:fixed;z-index:1000;display:none;background:#111827;color:#fff;'
    +'font:11px/1.55 system-ui;padding:7px 11px;border-radius:8px;pointer-events:none;'
    +'box-shadow:0 6px 24px rgba(0,0,0,.25);max-width:260px';
  // appended to <html>, NOT <body>: body{zoom:1.08} would scale the fixed
  // coordinates and shift the tip ~8% away from the cursor
  document.documentElement.appendChild(tlTip);
  const attachTip=el=>{
    if(!el) return;
    el.addEventListener('mousemove',e=>{
      const g=e.target.closest('g[data-tip]');
      if(!g){tlTip.style.display='none';return;}
      tlTip.innerHTML=g.dataset.tip;
      tlTip.style.display='block';
      const r=tlTip.getBoundingClientRect();
      let x=e.clientX+14, y=e.clientY-12;
      if(x+r.width>window.innerWidth-8) x=e.clientX-r.width-14;
      tlTip.style.left=x+'px';
      tlTip.style.top=y+'px';
    });
    el.addEventListener('mouseleave',()=>{tlTip.style.display='none';});
  };
  attachTip(tl);
  attachTip(document.getElementById('pa-chart'));
  attachTip(document.getElementById('th-chart'));

  // ---- thinking vs accuracy: per-model sweep over reasoning-token budget ----
  const THSWEEP=/*__THSWEEP__*/{};
  const th=document.getElementById('th-chart');
  function renderTH(){
    if(!th) return;
    const models=Object.keys(THSWEEP);
    if(!models.length){th.innerHTML='<p style="font-size:12px;color:#9ca3af;padding:20px 0">thinking-sweep data pending</p>';return;}
    const W=chartW(th),H=420,L=48,R=150,T=18,B=46;
    let allrt=[],allacc=[];
    models.forEach(k=>THSWEEP[k].pts.forEach(p=>{allrt.push(p.rt);allacc.push(p.acc);}));
    const lx0=Math.log10(Math.max(Math.min(...allrt)*0.8,1)),lx1=Math.log10(Math.max(...allrt)*1.25);
    const y0=Math.max(0,Math.min(...allacc)-6),y1=Math.min(100,Math.max(...allacc)+6);
    const X=rt=>L+(W-L-R)*(Math.log10(rt)-lx0)/(lx1-lx0||1);
    const Y=a=>T+(H-T-B)*(1-(a-y0)/(y1-y0||1));
    let g='';
    for(let a=Math.ceil(y0/5)*5;a<=y1;a+=5)
      g+=`<line x1="${L}" y1="${Y(a)}" x2="${W-R}" y2="${Y(a)}" stroke="#eef0f3"/><text x="${L-7}" y="${Y(a)+3.5}" text-anchor="end" font-size="10" fill="#9ca3af">${a}</text>`;
    [50,100,200,300,500,1000,2000,3000].forEach(v=>{if(Math.log10(v)>=lx0&&Math.log10(v)<=lx1)
      g+=`<line x1="${X(v)}" y1="${T}" x2="${X(v)}" y2="${H-B}" stroke="#f6f7f9"/><text x="${X(v)}" y="${H-B+15}" text-anchor="middle" font-size="9.5" fill="#9ca3af">${v}</text>`;});
    let body='',legend='',li=0;
    models.forEach(k=>{
      const md=THSWEEP[k],c=pcol(md.prov),ps=md.pts;
      body+=`<polyline points="${ps.map(p=>X(p.rt)+','+Y(p.acc)).join(' ')}" fill="none" stroke="${c}" stroke-width="2.2" opacity=".9"/>`;
      ps.forEach(p=>{
        const tip=`<b>${k}</b> &middot; ${md.prov}<br>reasoning ${p.rt} tok (${p.lvl})<br>pass ${p.acc}%`;
        const px=X(p.rt),py=Y(p.acc);
        body+=`<g data-tip="${tip.replace(/"/g,'&quot;')}" style="cursor:pointer"><circle cx="${px}" cy="${py}" r="5" fill="${c}"/><circle cx="${px}" cy="${py}" r="12" fill="transparent"/><text x="${px}" y="${py-9}" text-anchor="middle" font-size="8" fill="#94a3b8" style="pointer-events:none">${p.rt}</text></g>`;
      });
      const ly=T+18+li*22;
      legend+=`<g><image href="${logoSrc(md.prov)}" x="${W-R+14}" y="${ly-8}" width="15" height="15"/><circle cx="${W-R+38}" cy="${ly}" r="5" fill="${c}"/><text x="${W-R+48}" y="${ly+4}" font-size="10.5" font-weight="600" fill="#374151">${k}</text></g>`;
      li++;
    });
    const axl=`<text x="${L+(W-L-R)/2}" y="${H-6}" text-anchor="middle" font-size="11" fill="#6b7280">mean reasoning tokens / task  (log)</text>`
      +`<text transform="translate(13,${T+(H-T-B)/2}) rotate(-90)" text-anchor="middle" font-size="11" fill="#6b7280">exec pass %</text>`;
    th.innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Thinking vs accuracy">${g}${body}${legend}${axl}</svg>`;
  }

  // ---- cost-vs-accuracy Pareto scatter ----
  const pa=document.getElementById('pa-chart');
  function renderPA(){
    if(!pa||typeof COSTS==='undefined') return;
    const paOk=m=>{const o=(META[m.provider+'|'+m.model]||{}).o;
      return o===undefined||(o?state.paOpen:state.paClosed);};
    const rows=MODELS.filter(m=>!state.off.has(m.provider)&&!state.paOffP.has(m.provider)&&paOk(m)
      &&COSTS[m.model]&&COSTS[m.model].usd_per_task>0);
    if(!rows.length){pa.innerHTML='';return;}
    // Pareto plot: square drawing area (equal visual weight for both axes)
    const W=Math.min(chartW(pa),600),H=W,L=64,R=16,T=18,B=62;
    const xs=rows.map(m=>Math.log10(COSTS[m.model].usd_per_task));
    const x0=Math.floor(Math.min(...xs)),x1=Math.ceil(Math.max(...xs));
    const X=v=>L+(W-L-R)*(Math.log10(v)-x0)/((x1-x0)||1);
    const Y=v=>T+(H-T-B)*(1-v/100);
    let g='';
    for(let v=0;v<=100;v+=20)
      g+=`<line x1="${L}" y1="${Y(v)}" x2="${W-R}" y2="${Y(v)}" stroke="#eef0f3"/><text x="${L-8}" y="${Y(v)+4}" text-anchor="end" font-size="14" fill="#6b7280">${v}</text>`;
    for(let d=x0;d<=x1;d++){
      const v=Math.pow(10,d);
      g+=`<line x1="${X(v)}" y1="${T}" x2="${X(v)}" y2="${H-B}" stroke="#f3f4f6"/><text x="${X(v)}" y="${H-B+17}" text-anchor="middle" font-size="13.5" fill="#6b7280">$${v>=0.01?v.toFixed(2):v.toFixed(4)}</text>`;
    }
    // axis titles
    g+=`<text x="${(L+W-R)/2}" y="${H-B+38}" text-anchor="middle" font-size="15" font-weight="700" fill="#4b5563">Cost per task, USD (log scale)</text>`
      +`<text x="16" y="${(T+H-B)/2}" text-anchor="middle" font-size="15" font-weight="700" fill="#4b5563" transform="rotate(-90 16 ${(T+H-B)/2})">Correct % (w/ ASE skill)</text>`;
    // pareto frontier: sort by cost asc; keep points strictly above running max
    const sorted=[...rows].sort((a,b)=>COSTS[a.model].usd_per_task-COSTS[b.model].usd_per_task);
    let best=-1;const frontier=[];
    sorted.forEach(m=>{if(sv(m)>best){best=sv(m);frontier.push(m);}});
    const frSet=new Set(frontier);
    const frPts=frontier.map(m=>`${X(COSTS[m.model].usd_per_task)},${Y(sv(m))}`).join(' ');
    const frLine=frontier.length>1?`<polyline points="${frPts}" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4" opacity=".6"/>`:'';
    // sweet spot = knee of the frontier: the point farthest above the line
    // joining the frontier's endpoints in (log-cost, correct%) space
    let knee=null;
    if(frontier.length>2){
      const P=m=>[X(COSTS[m.model].usd_per_task),Y(sv(m))];
      const [ax,ay]=P(frontier[0]), [bx,by]=P(frontier[frontier.length-1]);
      const len=Math.hypot(bx-ax,by-ay)||1;
      let bestD=-1;
      frontier.slice(1,-1).forEach(m=>{
        const [px,py]=P(m);
        const d=Math.abs((bx-ax)*(ay-py)-(ax-px)*(by-ay))/len;
        if(d>bestD){bestD=d;knee=m;}
      });
    }
    // soft top-left shading: the cheap-and-accurate corner
    const sweetBg=`<defs><radialGradient id="sweetg" cx="0%" cy="0%" r="85%">
      <stop offset="0%" stop-color="#22c55e" stop-opacity=".10"/>
      <stop offset="55%" stop-color="#22c55e" stop-opacity=".035"/>
      <stop offset="100%" stop-color="#22c55e" stop-opacity="0"/></radialGradient></defs>
      <rect x="${L}" y="${T}" width="${(W-L-R)*.55}" height="${(H-T-B)*.55}" fill="url(#sweetg)" rx="10"/>
      <text x="${L+10}" y="${T+16}" font-size="13" font-weight="700" fill="#16a34a" opacity=".75">&#8598; sweet spot &mdash; cheap &amp; accurate</text>`;
    let pts='';
    const paLab=[];
    // always label the top-3 most accurate models (Fable 5 etc.), frontier or not
    const top3=new Set([...rows].sort((a,b)=>sv(b)-sv(a)).slice(0,3));
    sorted.forEach((m,i)=>{
      const c=COSTS[m.model];const x=X(c.usd_per_task),y=Y(sv(m));
      const col=pcol(m.provider);const isFr=frSet.has(m);
      const fmt=(v,d)=>v<Math.pow(10,-d)/2?'&lt;$'+Math.pow(10,-d).toFixed(d):'$'+v.toFixed(d);
      const isKnee=m===knee;
      const tip=`<b>${m.model}</b> &middot; ${m.provider}<br>${fmt(c.usd_per_task,4)}/task &middot; ${fmt(c.total_usd,2)} total${c.estimated?' (est.)':''}<br>Correct ${sv(m)}% (w/ skill)${isKnee?'<br><span style=color:#4ade80>&#9733; sweet spot (best accuracy-per-dollar knee)</span>':isFr?'<br><span style=color:#fbbf24>Pareto-optimal</span>':''}`;
      pts+=`<g data-tip="${tip.replace(/"/g,'&quot;')}" style="cursor:pointer">`
        +`<circle cx="${x}" cy="${y}" r="${isFr?6:5}" fill="${col}" opacity="${isFr?1:.8}" ${isFr?'stroke="#475569" stroke-width="1.5"':''}/>`
        +`<circle cx="${x}" cy="${y}" r="11" fill="transparent"/>`
        +`</g>`;
      if(isFr||top3.has(m)) paLab.push({x,y,text:m.model,bold:true,prio:isKnee||top3.has(m)?3:2});
    });
    const paLabels=placeLabels(paLab,sorted.map(m=>[X(COSTS[m.model].usd_per_task),Y(sv(m))]),{L,R,T,B,W,H},{fs:12.5});
    const lx=L+12, ly=H-6;
    const legend=`<g font-size="12" fill="#4b5563"><text x="${lx}" y="${ly}">labels = Pareto-optimal + top-3 accuracy &middot; hover any point for detail</text></g>`;
    pa.innerHTML=`<svg viewBox="0 0 ${W} ${H}" style="display:block;margin:0 auto;max-width:${W}px" role="img" aria-label="Cost vs accuracy Pareto">${sweetBg}${g}${frLine}${pts}${paLabels}${legend}</svg>`;
  }

  // ---- timeline provider toggle list (vertical, click to hide/show) ----
  const tlm=document.getElementById('tl-models');
  if(tlm){
    const PROVS=PROV_ORDER.filter(p=>MODELS.some(m=>m.provider===p&&m.rel));
    const provItems=[];
    // all on/off master button: one click clears everything, so you can
    // re-enable just the providers you want
    const allBtn=document.createElement('div');
    allBtn.className='tl-mi';
    allBtn.style.cssText='font-weight:800;color:#4f46e5;border:1px solid #c7d2fe;background:#eef2ff;margin-bottom:4px;justify-content:center;grid-column:1/-1';
    const allLab=document.createElement('span');
    const syncAllLab=()=>{allLab.textContent=state.offP.size>=PROVS.length?'All on':'All off';};
    allBtn.appendChild(allLab);
    allBtn.onclick=()=>{
      if(state.offP.size>=PROVS.length){
        state.offP.clear();provItems.forEach(it=>it.classList.remove('off'));
      }else{
        PROVS.forEach(p=>state.offP.add(p));provItems.forEach(it=>it.classList.add('off'));
      }
      syncAllLab();renderTL();};
    tlm.appendChild(allBtn);
    PROVS.forEach(p=>{
      const it=document.createElement('div');it.className='tl-mi';
      it.title=`${p} — click to hide/show its models in the timeline`;
      it.innerHTML=`<span class="dot" style="background:${pcol(p)}"></span>`
        +`<img src="${logoSrc(p)}" alt="" onerror="this.remove()">`
        +`<span>${p}</span>`;
      it.onclick=()=>{
        state.offP.has(p)?state.offP.delete(p):state.offP.add(p);
        it.classList.toggle('off');syncAllLab();renderTL();};
      provItems.push(it);
      tlm.appendChild(it);
    });
    syncAllLab();
  }

  render();renderIU();renderTL();renderPA();renderTH();
})();
</script>'''


# ---------- hero banner (Blender-render collage + white wordmark) ------------
HERO_BLOCK = '''<style>
.hero{position:relative;border-radius:18px;overflow:hidden;margin:0 0 14px;min-height:300px;display:flex;align-items:flex-end;background:#0e1118}
.hero-bg{position:absolute;inset:0;background:url('assets/hero_collage.jpg') center/cover no-repeat}
.hero-shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,12,20,.45) 0%,rgba(10,12,20,.68) 55%,rgba(8,10,16,.92) 100%)}
.hero-text{position:relative;padding:34px 36px 26px;color:#fff;max-width:780px}
.hero-text h1{margin:0;border:none;color:#fff;font-size:52px;font-weight:800;letter-spacing:-1.5px;line-height:1.05;text-shadow:0 2px 18px rgba(0,0,0,.45)}
.hero-tag{margin:8px 0 0;font-size:19px;font-weight:600;color:#fff;opacity:.96;text-shadow:0 1px 10px rgba(0,0,0,.5)}
.hero-sub{margin:10px 0 0;font-size:13.5px;line-height:1.55;color:#e3e7ef;text-shadow:0 1px 8px rgba(0,0,0,.55)}
.hero-chips{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
.hero-chip{font-size:11.5px;font-weight:700;padding:5px 12px;border-radius:999px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);color:#fff;backdrop-filter:blur(3px)}
a.hero-chip{text-decoration:none;cursor:pointer;transition:.15s}
a.hero-chip.req{background:#4f46e5;border-color:#6366f1}
a.hero-chip.req:hover{background:#4338ca}
a.hero-chip.wl:hover{background:rgba(255,255,255,.26)}
@media(max-width:640px){.hero-text h1{font-size:34px}.hero-tag{font-size:15px}}
</style>
<div class="hero">
  <div class="hero-bg"></div>
  <div class="hero-shade"></div>
  <div class="hero-text">
    <h1><img src="assets/ase-bench-logo-dark.svg" alt="" style="height:52px;vertical-align:-8px;margin-right:10px">ASE-Bench</h1>
    <p class="hero-tag i18n" data-en="Can LLMs drive atomistic simulations?" data-ko="LLM이 원자단위 시뮬레이션을 수행할 수 있는가?">Can LLMs drive atomistic simulations?</p>
    <p class="hero-sub i18n-html" data-en="Each model writes ASE Python scripts for 50 simulation tasks — crystals, slabs, MD, equations of state, vibrations.<br>Every script is executed and graded for physical correctness, with vs. without a one-page markdown skill." data-ko="각 모델이 50개 시뮬레이션 태스크(결정·슬랩·MD·상태방정식·진동)의 ASE Python 스크립트를 작성한다.<br>전부 실제로 실행해 물리적 정답 여부를 채점하고, 한 장짜리 markdown 스킬 유무를 비교한다.">Each model writes ASE Python scripts for 50 simulation tasks &mdash; crystals, slabs, MD, equations of state, vibrations.<br>Every script is executed and graded for physical correctness, with vs. without a one-page markdown skill.</p>
    <div class="hero-chips">
      <span class="hero-chip">50 tasks &times; 60 models</span>
      <a class="hero-chip req" href="#" onclick="const b=[...document.querySelectorAll('.tab-btn')].find(x=>x.textContent.trim()==='ASE Skill');if(b){b.click();b.scrollIntoView({behavior:'smooth',block:'start'})}return false">ASE Skill</a>
      <a class="hero-chip req" href="/mace">MACE-Bench &nearr;</a>
      <a class="hero-chip wl" href="https://github.com/s-choung/ase-bench" target="_blank" rel="noopener">GitHub &nearr;</a>
      <a class="hero-chip req" href="https://github.com/s-choung/ase-bench/issues/new?template=model-request.yml" target="_blank" rel="noopener">+ Request benchmark</a>
    </div>
  </div>
</div>
<div style="margin:0 0 14px"><video id="introvid" controls preload="metadata" src="assets/ase_bench_intro_16x9.mp4" style="width:100%;display:block;border-radius:18px;background:#0e1118"></video></div>
<script>
window.addEventListener('load',function(){
  var v=document.getElementById('introvid');if(!v)return;
  function sw(l){var s=l==='ko'?'assets/ase_bench_intro_16x9_ko.mp4':'assets/ase_bench_intro_16x9.mp4';
    if(v.getAttribute('src')!==s){var t=v.currentTime,p=!v.paused;v.setAttribute('src',s);v.load();try{v.currentTime=t}catch(e){}if(p)v.play();}}
  var k=document.getElementById('lang-ko'),e=document.getElementById('lang-en');
  if(k)k.addEventListener('click',function(){sw('ko')});
  if(e)e.addEventListener('click',function(){sw('en')});
});
</script>'''


# ---------- Task Visualizer detail modal (click cell -> card, -> explorer) ----
VIZ_MODAL = '''<style>
#tvm-overlay{display:none;position:fixed;inset:0;background:rgba(15,18,25,.62);z-index:1000;align-items:center;justify-content:center;padding:24px}
#tvm-overlay.open{display:flex}
#tvm-card{background:#fff;border-radius:14px;max-width:900px;width:100%;max-height:92vh;overflow-y:auto;box-shadow:0 24px 80px rgba(0,0,0,.35);position:relative}
#tvm-close{position:absolute;top:12px;right:14px;border:none;background:#f3f4f6;border-radius:999px;width:30px;height:30px;font-size:15px;cursor:pointer;color:#374151;z-index:2}
#tvm-close:hover{background:#e5e7eb}
.tvm-nav{position:absolute;top:50%;transform:translateY(-50%);border:none;background:rgba(255,255,255,.92);border-radius:999px;width:34px;height:34px;font-size:16px;cursor:pointer;color:#374151;box-shadow:0 2px 10px rgba(0,0,0,.18);z-index:2}
.tvm-nav:hover{background:#fff}
#tvm-prev{left:10px}#tvm-next{right:10px}
.tvm-imgwrap{background:radial-gradient(circle at 50% 38%,#f3f4f6,#dfe3e9);display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0;min-height:280px}
.tvm-imgwrap img{max-width:100%;max-height:58vh;object-fit:contain}
.tvm-noimg{color:#9ca3af;font-size:13px;padding:60px 0}
.tvm-body{padding:18px 24px 22px}
.tvm-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px}
.tvm-tid{font-weight:800;font-size:20px;color:#4f46e5}
.tvm-pill{font-size:10.5px;font-weight:700;padding:3px 9px;border-radius:999px;background:#eef2ff;color:#4338ca;text-transform:uppercase;letter-spacing:.4px}
.tvm-pill.diff{background:#f0fdf4;color:#15803d}
.tvm-prompt{font-size:14px;color:#1f2937;line-height:1.55;margin:6px 0 2px}
.tvm-prompt-ko{font-size:12.5px;color:#6b7280;line-height:1.5;margin:4px 0 0}
.tvm-stats{display:flex;gap:18px;margin:14px 0 16px;font-size:12.5px;color:#4b5563;flex-wrap:wrap}
.tvm-stats b{color:#111;font-size:15px;margin-right:3px}
.tvm-actions{display:flex;gap:10px;align-items:center}
.tvm-go{border:none;background:#4f46e5;color:#fff;font-weight:700;font-size:13.5px;padding:10px 18px;border-radius:9px;cursor:pointer}
.tvm-go:hover{background:#4338ca}
.tvm-hint{font-size:11px;color:#9ca3af;margin-left:auto}
</style>
<div id="tvm-overlay" onclick="if(event.target===this)closeViz()">
  <div id="tvm-card">
    <button id="tvm-close" onclick="closeViz()" title="close (Esc)">&#10005;</button>
    <button class="tvm-nav" id="tvm-prev" onclick="vizNav(-1)" title="previous task (&larr;)">&#8592;</button>
    <button class="tvm-nav" id="tvm-next" onclick="vizNav(1)" title="next task (&rarr;)">&#8594;</button>
    <div class="tvm-imgwrap" id="tvm-img"></div>
    <div class="tvm-body" id="tvm-info"></div>
  </div>
</div>
<script>
let tvmTid=null;
const TVM_ORDER=Object.keys(DATA).sort((a,b)=>parseInt(a.slice(1))-parseInt(b.slice(1)));
function openViz(tid){
  tvmTid=tid;
  const t=DATA[tid];if(!t)return;
  const img=document.getElementById('tvm-img');
  img.innerHTML=`<img src="renders/${tid}.png" alt="${tid}" onerror="this.parentNode.innerHTML='<div class=tvm-noimg>no structure render</div>'">`;
  const ms=Object.values(t.models||{});
  const ran=ms.filter(m=>m.success).length;
  const judged=ms.filter(m=>m.quality>=0).length;
  const corr=ms.filter(m=>m.quality===2).length;
  const en=t.prompt_en||'';const ko=t.prompt||'';
  document.getElementById('tvm-info').innerHTML=`
    <div class="tvm-head"><span class="tvm-tid">${tid}</span>
      <span class="tvm-pill diff">${t.difficulty||''}</span>
      <span class="tvm-pill">${t.category||''}</span></div>
    <p class="tvm-prompt">${en}</p>
    ${ko&&ko!==en?`<p class="tvm-prompt-ko">${ko}</p>`:''}
    <div class="tvm-stats">
      <span><b>${ran}</b>/${ms.length} ran</span>
      <span><b>${corr}</b>/${judged} judged correct</span>
      <span><b>${ms.length-ran}</b> failed to run</span>
    </div>
    <div class="tvm-actions">
      <button class="tvm-go" onclick="vizToExplorer()">View all model results &rarr;</button>
      <span class="tvm-hint">&larr;/&rarr; prev·next &middot; Esc close</span>
    </div>`;
  document.getElementById('tvm-overlay').classList.add('open');
}
function closeViz(){document.getElementById('tvm-overlay').classList.remove('open');tvmTid=null;}
function vizNav(d){
  if(!tvmTid)return;
  const i=TVM_ORDER.indexOf(tvmTid);
  openViz(TVM_ORDER[(i+d+TVM_ORDER.length)%TVM_ORDER.length]);
}
function vizToExplorer(){
  const tid=tvmTid;closeViz();
  document.querySelectorAll('.tab-btn').forEach(b=>{if(b.textContent.trim()==='Task Explorer')b.click();});
  setTimeout(()=>openTask(tid),120);
}
document.addEventListener('keydown',e=>{
  if(!document.getElementById('tvm-overlay').classList.contains('open'))return;
  if(e.key==='Escape')closeViz();
  else if(e.key==='ArrowLeft')vizNav(-1);
  else if(e.key==='ArrowRight')vizNav(1);
});
</script>'''


def extract_div_block(h, start_idx):
    """Return (block, end_idx) of the <div ...> starting at start_idx, by
    balancing <div / </div> tags."""
    depth = 0
    for m in re.finditer(r"<div\b|</div>", h[start_idx:]):
        depth += 1 if m.group(0) != "</div>" else -1
        if depth == 0:
            end = start_idx + m.end()
            return h[start_idx:end], end
    raise ValueError("unbalanced div block")


def main():
    h = open(V9).read()

    # ---- 1. branding -------------------------------------------------------
    h = h.replace(
        "<title>ASE Skill Benchmark v9 — Pass Rate Dashboard</title>",
        '<title>ASE-Bench — Can LLMs drive atomistic simulations?</title>\n'
        '<link rel="icon" type="image/svg+xml" href="assets/ase-bench-logo.svg">\n'
        '<style>body{zoom:1.08}</style>')
    h = h.replace("<h1>ASE Skill Benchmark v9</h1>", HERO_BLOCK)
    _utc = __import__("datetime").datetime.now(__import__("datetime").timezone.utc)
    h = h.replace(
        '<p class="date">2026.05 &middot; Seokhyun Choung &middot; Pass Rate Dashboard</p>',
        f'<p class="date">last updated {_utc.strftime("%Y-%m-%d %H:%M")} UTC '
        f'&middot; Seokhyun Choung</p>')
    # the hero block now carries the intro -> drop the old standalone paragraph
    intro_p = re.search(
        r'<p data-ko="자연어 지시만으로.*?class="i18n-html"></p>\s*', h, re.S)
    assert intro_p, "old intro paragraph not found"
    h = h.replace(intro_p.group(0), "")
    h = h.replace(
        "<span>ASE Skill Benchmark v9 / Gemini + OpenAI + Claude / Pass Rate Dashboard</span>",
        f"<span>ASE-Bench &middot; last updated {_utc.strftime('%Y-%m-%d %H:%M')} UTC</span>")
    # v9 fixed only the EN funnel description; fix the KO one here
    h = h.replace(
        'data-ko="Pass Rate = 실행 성공(returncode==0) 비율. 50개 태스크 &times; 9개 모델 '
        '&times; 2 조건(w/o Skill / w/ Skill)."',
        'data-ko="Funnel: 50 태스크 &rarr; Runs(returncode==0) &rarr; Correct(Opus-as-judge). '
        'Runs%와 Correct%의 간극 = 돌지만 틀린 코드(인플레이션)."')
    # methodology fine print: removed entirely (the curious can read GitHub)
    h = re.sub(r'<p class="center-text i18n-html" style="font-size:13px"\s*\n\s*data-ko="Funnel: 50 태스크.*?</p>\s*',
               '', h, count=1, flags=re.S)
    h = h.replace("2026.05</span>", "2026.06</span>")

    # ---- 2+3. bar chart (simplified) + timeline ---------------------------
    old_block = re.search(r'<div class="bc-wrap">.*?<div id="bc-chart"></div>\s*</div>', h, re.S)
    assert old_block, "v9 chart block not found"
    h = h.replace(old_block.group(0), CHART_BLOCK)
    old_script = re.search(r'<style>\s*\.bc-wrap\{.*?</script>', h, re.S)
    assert old_script, "v9 chart script not found"
    h = h.replace(old_script.group(0), CHART_SCRIPT)
    # COSTS must be defined before buildSummary (mid-document) AND the chart
    # IIFE (end of document) run -> inject just before the summary table
    costs_path = os.path.join(BASE, "results_v3", "model_costs.json")
    costs = json.load(open(costs_path)) if os.path.exists(costs_path) else {}
    costs_tag = "<script>const COSTS = " + json.dumps(costs) + ";</script>\n"
    assert '<table class="sum-tbl">' in h
    h = h.replace('<table class="sum-tbl">', costs_tag + '<table class="sum-tbl">', 1)

    # ---- 3b. canonical score definition, above the charts AND above the table -
    _h2 = re.search(r'<h2[^>]*>Overall Results &mdash; Runs vs\. Correct</h2>|'
                    r'<h2[^>]*>Overall Results — Runs vs\. Correct</h2>', h)
    assert _h2, "Overall Results heading not found"
    h = h.replace(_h2.group(0), _h2.group(0) + "\n" + SCORE_DEF_BLOCK, 1)
    h = h.replace('<table class="sum-tbl">', SCORE_DEF_BLOCK + '<table class="sum-tbl">', 1)
    assert h.count('class="i18n-html score-def"') == 2

    # ---- 4. Task Explorer: default = w/ Skill, badges wrap -----------------
    assert "let currentCondFilter = 'all';" in h
    h = h.replace("let currentCondFilter = 'all';", "let currentCondFilter = 'skill_v3';")
    h = h.replace(
        "<button class=\"active\" onclick=\"toggleCondFilter(this,'all')\"",
        "<button onclick=\"toggleCondFilter(this,'all')\"")
    h = h.replace(
        "<button onclick=\"toggleCondFilter(this,'skill_v3')\"",
        "<button class=\"active\" onclick=\"toggleCondFilter(this,'skill_v3')\"")
    h = h.replace(
        ".task-mini-dots { display: flex; gap: 2px; }",
        ".task-mini-dots { display: flex; gap: 2px; flex-wrap: wrap; "
        "justify-content: flex-end; max-width: 420px; }")

    # ---- 4b. Task Visualizer: cell click -> detail modal (not explorer) ----
    n_cells = h.count("onclick=\"switchTab('explorer');openTask(")
    h = h.replace("onclick=\"switchTab('explorer');openTask(", 'onclick="openViz(')
    h = h.replace('title="open in Task Explorer"', 'title="task details"')
    h = h.replace("</body>", VIZ_MODAL + "\n</body>")
    print(f"visualizer cells rewired to modal: {n_cells}")

    # ---- 5. DELETE the "How to Use" section (this page sells the benchmark,
    # not the skill) ----------------------------------------------------------
    i = h.find('data-ko="사용법"')
    assert i > 0, "How-to-Use section not found"
    start = h.rfind('<div style="max-width:680px;margin:2rem auto">', 0, i)
    assert start > 0, "How-to-Use container not found"
    _, end = extract_div_block(h, start)
    h = h[:start] + h[end:]

    # ---- 6. heatmap: TRANSPOSED (models on Y, tasks on X), logos, full names
    new_heatmap = r'''(function buildHeatmap() {
  const table = document.querySelector('#tab-heatmap .hm-wrap table');
  const thead = table.querySelector('thead tr');
  const taskIds = Object.keys(DATA).sort((a,b) => parseInt(a.slice(1)) - parseInt(b.slice(1)));
  const LOGO_ALIAS={'OpenAI-oss':'OpenAI'};
  const logoSrc=p=>'assets/logos/'+(LOGO_ALIAS[p]||p)+'.png';

  thead.innerHTML = '<th style="writing-mode:horizontal-tb;border:none;text-align:left;font-size:10px;color:#9ca3af">model \\\\ task</th>';
  taskIds.forEach(tid => {
    const th = document.createElement('th');
    th.textContent = tid.slice(1);
    th.title = tid + ' — ' + ((DATA[tid].prompt_en||DATA[tid].prompt||'').slice(0,120));
    th.style.cssText = 'writing-mode:horizontal-tb;font-size:8.5px;padding:2px 1px;cursor:pointer;color:#6b7280';
    th.onclick = () => openViz(tid);
    thead.appendChild(th);
  });

  // group conditions per model, order models by w/-skill correct (desc)
  const byModel = {};
  CONDITIONS.forEach(c => { (byModel[c.model] = byModel[c.model] || {model:c.model})[c.cond] = c; });
  const models = Object.values(byModel).sort((a,b) => {
    const corr = p => p && p.skill_v3 && SUMMARY[p.skill_v3.key] ? (SUMMARY[p.skill_v3.key].correct||0) : -1;
    return corr(b) - corr(a);
  });

  // ---- controls: condition toggle + per-model on/off pills ----
  const hmState = {cond:'both', off:new Set()};
  const hmWrap = document.querySelector('#tab-heatmap .hm-wrap');
  const ctrl = document.createElement('div');
  ctrl.id = 'hm-controls';
  ctrl.innerHTML = `<style>
#hm-controls{display:flex;flex-direction:column;gap:8px;margin:10px 0 4px;font-size:12px}
#hm-controls select{font:12px system-ui;padding:3px 8px;border:1px solid #d1d5db;border-radius:6px;background:#fff}
#hm-pills{display:flex;flex-wrap:wrap;gap:4px}
.hm-pill{display:inline-flex;align-items:center;gap:4px;padding:2px 8px;border-radius:999px;border:1px solid #e2e6ec;background:#fff;color:#374151;cursor:pointer;user-select:none;font-size:10px;font-weight:600;transition:.12s;white-space:nowrap}
.hm-pill:hover{border-color:#94a3b8}
.hm-pill img{width:12px;height:12px;object-fit:contain}
.hm-pill.off{opacity:.25;filter:grayscale(1)}
</style><label>condition <select id="hm-cond">
<option value="both">both (w/ + w/o skill)</option>
<option value="skill_v3">w/ skill only</option>
<option value="vanilla">w/o skill only</option>
</select> <span style="color:#9ca3af;font-size:11px">click a provider pill to hide/show its rows</span></label>
<div id="hm-pills"></div>`;
  hmWrap.parentNode.insertBefore(ctrl, hmWrap);
  const pills = ctrl.querySelector('#hm-pills');
  const provOf = p => (SUMMARY[(p.skill_v3||p.vanilla).key]||{}).provider || '';
  const PROVS = [...new Set(models.map(provOf))];
  const provPills = [];
  // master all-on/all-off pill (same UX as the timeline list)
  const allPill = document.createElement('span');
  allPill.className = 'hm-pill';
  allPill.style.cssText = 'font-weight:800;color:#4f46e5;border-color:#c7d2fe;background:#eef2ff';
  const syncAll = () => { allPill.textContent = hmState.off.size >= PROVS.length ? 'All on' : 'All off'; };
  allPill.onclick = () => {
    if (hmState.off.size >= PROVS.length) {
      hmState.off.clear(); provPills.forEach(x => x.classList.remove('off'));
    } else {
      PROVS.forEach(v => hmState.off.add(v)); provPills.forEach(x => x.classList.add('off'));
    }
    syncAll(); renderHM();
  };
  pills.appendChild(allPill);
  PROVS.forEach(prov => {
    const sp = document.createElement('span');
    sp.className = 'hm-pill';
    sp.title = prov + ' — click to hide/show its rows';
    sp.innerHTML = `<img src="${logoSrc(prov)}" alt="" onerror="this.remove()"><span>${prov}</span>`;
    sp.onclick = () => {
      hmState.off.has(prov) ? hmState.off.delete(prov) : hmState.off.add(prov);
      sp.classList.toggle('off'); syncAll(); renderHM();
    };
    provPills.push(sp);
    pills.appendChild(sp);
  });
  syncAll();
  ctrl.querySelector('#hm-cond').onchange = e => { hmState.cond = e.target.value; renderHM(); };

  const tbody = document.getElementById('heatmap-body');
  function renderHM() {
  tbody.innerHTML = '';
  models.filter(p => !hmState.off.has(provOf(p))).forEach(p => {
    const conds = hmState.cond === 'both' ? ['skill_v3','vanilla'] : [hmState.cond];
    conds.forEach(cond => {
      const c = p[cond];
      if (!c) return;
      const prov = (SUMMARY[c.key]||{}).provider || '';
      const tr = document.createElement('tr');
      const labelTd = document.createElement('td');
      labelTd.className = 'row-label';
      labelTd.style.cssText = 'white-space:nowrap;font-size:11px';
      const chip = cond==='skill_v3'
        ? '<span style="font-size:9px;font-weight:800;color:#4f46e5;border:1px solid #c7d2fe;background:#eef2ff;border-radius:999px;padding:1px 7px;margin-left:6px">w/ skill</span>'
        : '<span style="font-size:9px;font-weight:700;color:#6b7280;border:1px solid #e5e7eb;background:#f9fafb;border-radius:999px;padding:1px 7px;margin-left:6px">w/o</span>';
      labelTd.innerHTML = '<span style="display:inline-flex;align-items:center;gap:6px">'
        + '<img src="'+logoSrc(prov)+'" alt="'+prov+'" title="'+prov+'" style="width:14px;height:14px;object-fit:contain;border-radius:3px" onerror="this.style.display=\'none\'">'
        + '<b>'+c.model+'</b>'+chip+'</span>';
      tr.appendChild(labelTd);
      taskIds.forEach(tid => {
        const td = document.createElement('td');
        const m = DATA[tid].models[c.key] || {};
        const ran = m.success;
        const q = m.quality;
        let bg, txt, lab;
        if (!ran) { bg='#e5e7eb'; txt='·'; lab='did not run'; }
        else if (q===2) { bg='#16a34a'; txt='C'; lab='correct'; }
        else if (q===1) { bg='#f59e0b'; txt='~'; lab='partial'; }
        else if (q===0) { bg='#dc2626'; txt='X'; lab='WRONG (ran but incorrect)'; }
        else { bg='#93c5fd'; txt='P'; lab='ran (unjudged)'; }
        td.style.background = bg;
        td.style.color = (q===1)?'#000':'#fff';
        td.style.cssText += ';text-align:center;font-weight:700;font-size:9px;cursor:pointer;min-width:15px';
        td.textContent = txt;
        td.title = `${tid} | ${c.model} ${cond==='skill_v3'?'w/ skill':'w/o'} | ${lab}${m.qreason?': '+m.qreason:''}`;
        td.onclick = () => openViz(tid);
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
  });
  }
  renderHM();
})();'''
    h = re.sub(r"\(function buildHeatmap\(\) \{.*?\}\)\(\);", new_heatmap.replace("\\", "\\\\"),
               h, count=1, flags=re.S)
    h = h.replace("50 Tasks &times; 44 Conditions (22 models &times; 2)",
                  "Models &times; 2 conditions (rows) &times; 50 Tasks (columns)")

    # hero model-count badge: derive from SUMMARY so it never goes stale
    _sm = re.search(r"const SUMMARY = (\{.*?\});\s*\n", h, re.S)
    _nmodels = len({(v["provider"], v["model"]) for v in json.loads(_sm.group(1)).values()})
    h = re.sub(r"50 tasks &times; \d+ models",
               f"50 tasks &times; {_nmodels} models", h, count=1)

    # inject thinking-sweep data into the interactive thinking-vs-accuracy chart
    h = h.replace("/*__THSWEEP__*/{}", json.dumps(build_thsweep(), ensure_ascii=False))

    # ---- 7. "The Skill" tab: full ase_skill_v3.md text ----------------------
    skill_md = open(os.path.join(BASE, "tasks", "ase_skill_v3.md")).read()
    esc = skill_md.replace("&", "&amp;").replace("<", "&lt;")
    skill_tab = f'''<div id="tab-skill" class="tab-content">
<style>
.skill-pre{{background:#0f172a;color:#dbe4f0;border-radius:12px;padding:22px 26px;font:12px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;overflow-x:auto;white-space:pre-wrap;word-break:break-word}}
.skill-meta{{font-size:13px;color:#666;margin:0 0 14px;max-width:760px}}
</style>
<h2 class="i18n" data-ko="ASE Skill — 개입의 전부" data-en="ASE Skill — the entire intervention">ASE Skill — the entire intervention</h2>
<p class="skill-meta">
  <span class="i18n" data-ko="ASE API 레퍼런스를 markdown 한 장(~250줄)으로 압축한 스킬 — 시스템 프롬프트에 이 텍스트를 덧붙이는 것이 w/와 w/o 조건의 유일한 차이다." data-en="A one-page (~250-line) markdown distillation of the ASE API — appending this text to the system prompt is the only difference between the w/ and w/o conditions.">A one-page (~250-line) markdown distillation of the ASE API &mdash; appending this text to the system prompt is the only difference between the w/ and w/o conditions.</span>
  <a href="https://github.com/s-choung/ase-bench/blob/main/tasks/ase_skill_v3.md" target="_blank" rel="noopener" style="display:inline-block;margin-left:8px;font-size:12px;font-weight:700;color:#4f46e5;text-decoration:none;border:1px solid #c7d2fe;background:#eef2ff;border-radius:999px;padding:3px 12px">Original file &nearr;</a>
</p>
<pre class="skill-pre">{esc}</pre>
</div>'''
    vis_btn = ('<div class="tab-btn" onclick="switchTab(\'visualizer\')" '
               'data-ko="Task Visualizer" data-en="Task Visualizer" class="i18n">Task Visualizer</div>')
    assert vis_btn in h, "visualizer tab button not found"
    skill_btn = ('\n  <div class="tab-btn" onclick="switchTab(\'skill\')" '
                 'data-ko="ASE Skill" data-en="ASE Skill" class="i18n">ASE Skill</div>')
    h = h.replace(vis_btn, vis_btn + skill_btn, 1)
    h = h.replace("</body>", skill_tab + "\n</body>")

    # ---- 8. summary-table polish + sentence-case sweep (user feedback 06-10)
    # 8a. bar fill: .pass-bar-fill is an inline <span> with no content, so its
    # width/height collapsed to 0 and every bar looked empty. display:block
    # makes the gray track the 100% reference and the fill the achieved share.
    old_fill = ".pass-bar-fill {\n  height: 100%; border-radius: 4px;\n}"
    assert old_fill in h, "pass-bar-fill css not found"
    h = h.replace(old_fill,
                  ".pass-bar-fill {\n  display: block; height: 100%; border-radius: 4px;\n}")
    # 8b. provider cell: logo + provider name (site-wide pill convention)
    old_prov_css = (".provider-tag {\n"
                    "  font-size: 10px; font-weight: 600; text-transform: uppercase;\n"
                    "  letter-spacing: 0.3px; color: var(--ash); padding: 2px 6px;\n"
                    "  border: 1px solid var(--fog); border-radius: 9999px;\n"
                    "}")
    assert old_prov_css in h, "provider-tag css not found"
    h = h.replace(old_prov_css,
                  ".provider-tag {\n"
                  "  display: inline-flex; align-items: center; gap: 5px;\n"
                  "  font-size: 10px; font-weight: 600;\n"
                  "  letter-spacing: 0.3px; color: var(--ash); padding: 2px 8px 2px 5px;\n"
                  "  border: 1px solid var(--fog); border-radius: 9999px;\n"
                  "}\n"
                  ".provider-tag img { width: 13px; height: 13px; object-fit: contain; }")
    old_prov_td = '<td class="lbl"><span class="provider-tag">${mk.provider}</span></td>'
    assert old_prov_td in h, "provider td not found"
    h = h.replace(old_prov_td,
                  '<td class="lbl"><span class="provider-tag">'
                  "<img src=\"assets/logos/${({'OpenAI-oss':'OpenAI'})[mk.provider]||mk.provider}.png\" "
                  'alt="" onerror="this.remove()">${mk.provider}</span></td>')
    # 8c. sentence case site-wide: kill styled ALL-CAPS (h2, table headers,
    # condition/output labels, category pills) + literal-caps UI strings.
    # Technical acronyms in content (EMT, BFGS, NEB, ...) are untouched.
    h = h.replace("text-transform: uppercase", "text-transform: none")
    h = h.replace("text-transform:uppercase", "text-transform:none")
    h = h.replace("'WRONG (ran but incorrect)'", "'Wrong (ran but incorrect)'")
    h = h.replace("${s ? 'PASS' : 'FAIL'}", "${s ? 'Pass' : 'Fail'}")

    # ---- 8c1. cost columns in the summary table -----------------------------
    h = h.replace('  <th class="r">&Delta; Correct</th>',
                  '  <th class="r">&Delta; Correct</th>\n'
                  '  <th class="r">$ / task</th>\n'
                  '  <th class="r">Total $</th>')
    old_row_end = "<td class=\"r ${dClass}\">${dCorr>0?'+':''}${dPct}%p</td>`;"
    assert old_row_end in h, "summary row template not found"
    h = h.replace(old_row_end,
                  "<td class=\"r ${dClass}\">${dCorr>0?'+':''}${dPct}%p</td>"
                  "${(()=>{const c=(typeof COSTS!=='undefined'&&COSTS[mk.model])||null;"
                  "return c?`<td class=\"r\" style=\"color:#6b7280\">${c.usd_per_task<0.0005?'&lt;$0.001':'$'+c.usd_per_task.toFixed(3)}</td>"
                  "<td class=\"r\" style=\"color:#6b7280\">${c.total_usd<0.01?'&lt;$0.01':'$'+c.total_usd.toFixed(2)}${c.estimated?'*':''}</td>`"
                  ":'<td class=\"r\">&mdash;</td><td class=\"r\">&mdash;</td>';})()}`;")

    # ---- 8c2. drop the stale "Key finding" box (v1-era numbers) ------------
    h = re.sub(r'<div class="key-finding">.*?</div>\s*', '', h, count=1, flags=re.S)

    # ---- 8c3. default language = English ------------------------------------
    h = h.replace("setLang('ko');\n", "setLang('en');\n")

    # ---- 8d. judge v2 labels: the grader is no longer bare Opus ------------
    h = h.replace("Opus-as-judge verdict",
                  "graded answer: each task has a rubric with pre-computed correct "
                  "values (from real ASE calculations); an LLM judge compares the "
                  "script's printed output against those values")
    h = h.replace("Opus-as-judge", "the rubric-based grader")
    h = h.replace("Opus-judged",
                  "graded-correct (output matches the task's pre-computed answer)")

    # ---- 9. GitHub button next to the ENG/KOR toggle ------------------------
    old_lang = ('  <button id="lang-ko" onclick="setLang(\'ko\')">KOR</button>\n'
                '</div>')
    assert old_lang in h, "lang toggle not found"
    gh_svg = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" '
              'd="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
              '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13'
              '-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07'
              '-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08'
              '-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 '
              '.27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 '
              '2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 '
              '2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>')
    h = h.replace(old_lang,
                  '  <button id="lang-ko" onclick="setLang(\'ko\')">KOR</button>\n'
                  '  <a class="gh-btn" href="https://github.com/s-choung/ase-bench" '
                  'target="_blank" rel="noopener" title="GitHub repository">' + gh_svg + '</a>\n'
                  '</div>')
    h = h.replace(".lang-toggle button.active {",
                  ".lang-toggle a.gh-btn { display:flex; align-items:center; padding:6px 12px; "
                  "border-left:1px solid rgba(0,0,0,0.12); color:#000; }\n"
                  ".lang-toggle a.gh-btn:hover { background:#f3f4f6; }\n"
                  ".lang-toggle a.gh-btn svg { width:15px; height:15px; display:block; }\n"
                  ".lang-toggle button.active {")

    # ---- global type scale (user: fonts too small + too many ad-hoc sizes) ----
    # Bump every CSS `font-size:Npx` up one notch and snap to a small
    # representative set {11,12,13,14,16,19,24,30}. SVG chart labels
    # (font-size="N", no px) are left untouched to avoid overlap in dense plots.
    _SCALE = [11, 12, 13, 14, 16, 19, 24, 30]
    def _fs(mm):
        v = float(mm.group(1))
        for s in _SCALE:
            if s > v:
                return f"font-size:{s}px"
        return f"font-size:{int(round(v)) + 3}px"
    h = re.sub(r"font-size:\s*([\d.]+)px", _fs, h)

    with open(OUT, "w") as f:
        f.write(h)
    print(f"wrote {OUT} ({len(h):,} bytes)")


if __name__ == "__main__":
    main()
