"""Build v9 dashboard = v8 (22 models, RUNS only) + a CORRECTNESS layer.

Why: success = returncode==0 = "does it RUN". An Opus-as-judge pass over every
PASS case (1 agent per model_cond, uniform rubric) found a large fraction of
"runs" are actually WRONG (wrong supercell, wrong atom/layer count, NaN/complex
freqs, fabricated output, ...). So the headline pass-rate overstates competence.

v9 makes the report a 2-tier FUNNEL:  total 50  ->  Runs (returncode 0)  ->
Correct (Opus verdict == 2).  The Runs%-Correct% gap = inflation.

Inputs:
  benchmark_report_v8.html              (TEMPLATE: 22-model DATA/SUMMARY/etc.)
  results_v3/judge_out/<key>.json       (Opus judge: {verdicts:[{tid,verdict,reason}]})
  results_v3/correctness.json           (deterministic structural anchor, secondary)
Output:
  benchmark_report_v9.html

Edits to the spliced HTML:
  - DATA[tid].models[key].quality   <- Opus verdict (2 correct / 1 partial / 0 wrong / -1 n/a)
  - DATA[tid].models[key].qreason   <- Opus one-line reason
  - DATA[tid].models[key].det       <- deterministic verdict (2/0/-1), anchor
  - SUMMARY[key] += {correct, partial, wrong, judged}
  - Overview <thead> + buildSummary()  -> Runs% / Correct% per condition + ΔCorrect
  - buildHeatmap() cell color          -> correctness (green/amber/red) vs fail (gray)
"""
import json
import os
import re
import glob

BASE = os.path.dirname(os.path.abspath(__file__))
V8 = os.path.join(BASE, "benchmark_report_v8.html")
OUT = os.path.join(BASE, "benchmark_report_v9.html")
JUDGE_DIR = os.path.join(BASE, "results_v3", "judge_out")
DET_PATH = os.path.join(BASE, "results_v3", "correctness.json")


# ---- interactive horizontal bar chart (replaces the static matplotlib PNG) ----
CHART_BLOCK = '''<div class="bc-wrap">
  <div class="bc-controls">
    <label>Sort
      <select id="bc-sort">
        <option value="skill">Accuracy &mdash; w/ Skill (high&rarr;low)</option>
        <option value="vanilla">Accuracy &mdash; w/o Skill</option>
        <option value="delta">Skill gain (&Delta;)</option>
        <option value="release">Release (new&rarr;old, approx)</option>
        <option value="provider">Provider</option>
      </select>
    </label>
    <label>Metric
      <select id="bc-metric">
        <option value="correct">Correct % (Opus-judged)</option>
        <option value="runs">Runs % (returncode 0)</option>
      </select>
    </label>
    <label>Skill
      <select id="bc-skill">
        <option value="both">Both (w/o + w/)</option>
        <option value="skill">w/ Skill only</option>
        <option value="vanilla">w/o Skill only</option>
      </select>
    </label>
    <span class="bc-pills" id="bc-provfilter"></span>
  </div>
  <div id="bc-chart"></div>
</div>'''

CHART_SCRIPT = '''<style>
.bc-wrap{margin:1.2rem 0 1.6rem;text-align:left}
.bc-controls{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin-bottom:14px;font-size:13px}
.bc-controls label{display:flex;flex-direction:column;gap:3px;font-size:11px;color:#6b7280;font-weight:600}
.bc-controls select{font:13px system-ui;padding:4px 8px;border:1px solid #d1d5db;border-radius:6px;background:#fff}
.bc-pills{display:flex;flex-wrap:wrap;gap:5px;margin-left:auto}
.bc-pill{font-size:11px;padding:3px 9px;border-radius:999px;border:1px solid #d1d5db;cursor:pointer;user-select:none;font-weight:600}
.bc-pill.off{opacity:.32;text-decoration:line-through}
.bc-row{display:flex;align-items:center;gap:10px;padding:3px 0}
.bc-name{width:210px;min-width:210px;display:flex;align-items:center;gap:7px;justify-content:flex-end;text-align:right}
.bc-prov{font-size:9.5px;font-weight:700;color:#fff;padding:2px 6px;border-radius:4px;white-space:nowrap}
.bc-mdl{font-size:12.5px;font-weight:600;color:#1f2937;white-space:nowrap}
.bc-track{flex:1;display:flex;flex-direction:column;gap:2px}
.bc-bar{height:14px;border-radius:3px 7px 7px 3px;position:relative;min-width:2px;transition:width .35s cubic-bezier(.4,0,.2,1)}
.bc-bar .bc-val{position:absolute;right:-4px;top:50%;transform:translate(100%,-50%);font-size:10px;font-weight:700;white-space:nowrap}
.bc-bar.skill .bc-val{font-weight:800}
.bc-meta{font-size:10px;color:#9ca3af;margin-left:6px}
@media(max-width:640px){.bc-name{width:130px;min-width:130px}.bc-mdl{font-size:11px}}
</style>
<script>
(function(){
  if(typeof SUMMARY==='undefined'){return;}
  const PAL={Gemini:['#9ecae1','#3182bd'],OpenAI:['#a8ddb5','#2e8b57'],Claude:['#e5b8a0','#c05a3c'],
    DeepSeek:['#c9c0e8','#6c4fb0'],Qwen:['#f3c6a5','#d97a34'],MiniMax:['#9fd3d0','#2c8c88'],
    Moonshot:['#c7d3e8','#3f5e9c'],Xiaomi:['#f4b8b8','#d24a4a'],'OpenAI-oss':['#b8e0c2','#3fa15c'],
    NVIDIA:['#cbe6a6','#6f9e2c'],Upstage:['#d5c3e8','#8a52c0'],xAI:['#b8bcc4','#374151']};
  const REL={'OpenAI|gpt-5.5':'2026-01','OpenAI|gpt-5.4':'2025-11','OpenAI|gpt-5.4-mini':'2025-11',
    'Claude|Opus 4.7':'2025-12','Claude|Sonnet 4.6':'2025-11','Claude|Haiku 4.5':'2025-10',
    'Gemini|2.5 Pro':'2025-06','Gemini|2.5 Flash':'2025-06','Gemini|2.5 Flash-Lite':'2025-07',
    'DeepSeek|deepseek-v4-pro':'2025-12','DeepSeek|deepseek-v3.2':'2025-09','DeepSeek|deepseek-r1-0528':'2025-05',
    'Qwen|qwen3-235b-thinking':'2025-07','Qwen|qwen3-235b':'2025-04','Qwen|qwen3-32b':'2025-04',
    'xAI|grok-4.3':'2026-01','Moonshot|kimi-k2.5':'2025-11','MiniMax|minimax-m3':'2025-10',
    'Xiaomi|mimo-v2.5':'2025-10','OpenAI-oss|gpt-oss-120b':'2025-08',
    'NVIDIA|nemotron-3-super-120b':'2025-09','Upstage|solar-pro-3':'2025-11'};
  const pair={};
  Object.values(SUMMARY).forEach(s=>{const k=s.provider+'|'+s.model;(pair[k]=pair[k]||{provider:s.provider,model:s.model})[s.condition]=s;});
  const MODELS=Object.values(pair).filter(p=>p.vanilla&&p['skill_v3']).map(p=>({
    provider:p.provider,model:p.model,total:p.vanilla.total||50,
    vCorr:p.vanilla.correct||0,sCorr:p['skill_v3'].correct||0,
    vRun:p.vanilla.pass_count||0,sRun:p['skill_v3'].pass_count||0,
    rel:REL[p.provider+'|'+p.model]||''}));
  const provs=[...new Set(MODELS.map(m=>m.provider))];
  const state={metric:'correct',skill:'both',sort:'skill',off:new Set()};
  const pct=(a,t)=>t?Math.round(100*a/t):0;
  const val=(m,cond)=>{const c=state.metric==='correct';
    return cond==='skill'?pct(c?m.sCorr:m.sRun,m.total):pct(c?m.vCorr:m.vRun,m.total);};

  const pf=document.getElementById('bc-provfilter');
  provs.forEach(p=>{const sp=document.createElement('span');sp.className='bc-pill';
    sp.textContent=p;sp.style.borderColor=PAL[p]?PAL[p][1]:'#999';sp.style.color=PAL[p]?PAL[p][1]:'#555';
    sp.onclick=()=>{state.off.has(p)?state.off.delete(p):state.off.add(p);sp.classList.toggle('off');render();};
    pf.appendChild(sp);});

  const chart=document.getElementById('bc-chart');
  function bar(m,cond){const c=PAL[m.provider]||['#ccc','#666'];const v=val(m,cond);
    const isSkill=cond==='skill';
    return `<div class="bc-bar ${isSkill?'skill':''}" style="width:${Math.max(v,1)}%;background:${isSkill?c[1]:c[0]}" title="${m.provider} ${m.model} — ${isSkill?'w/ Skill':'w/o Skill'} — ${state.metric}=${v}%"><span class="bc-val" style="color:${isSkill?c[1]:'#999'}">${v}%</span></div>`;}
  function render(){
    let rows=MODELS.filter(m=>!state.off.has(m.provider));
    if(state.sort==='release') rows.sort((a,b)=>(b.rel||'').localeCompare(a.rel||'')||val(b,'skill')-val(a,'skill'));
    else if(state.sort==='provider') rows.sort((a,b)=>a.provider.localeCompare(b.provider)||val(b,'skill')-val(a,'skill'));
    else{const key=m=>state.sort==='vanilla'?val(m,'vanilla'):state.sort==='delta'?val(m,'skill')-val(m,'vanilla'):val(m,'skill');
      rows.sort((a,b)=>key(b)-key(a));}
    chart.innerHTML=rows.map(m=>{
      const c=PAL[m.provider]||['#ccc','#666'];
      let bars='';
      if(state.skill!=='skill') bars+=bar(m,'vanilla');
      if(state.skill!=='vanilla') bars+=bar(m,'skill');
      const dlt=val(m,'skill')-val(m,'vanilla');
      const meta=state.sort==='delta'?`<span class="bc-meta">${dlt>0?'+':''}${dlt}%p</span>`
        :state.sort==='release'?`<span class="bc-meta">${m.rel||'?'}</span>`:'';
      return `<div class="bc-row"><div class="bc-name"><span class="bc-prov" style="background:${c[1]}">${m.provider}</span><span class="bc-mdl">${m.model}</span></div><div class="bc-track">${bars}</div>${meta}</div>`;
    }).join('');
  }
  document.getElementById('bc-sort').onchange=e=>{state.sort=e.target.value;render();};
  document.getElementById('bc-metric').onchange=e=>{state.metric=e.target.value;render();};
  document.getElementById('bc-skill').onchange=e=>{state.skill=e.target.value;render();};
  render();
})();
</script>'''


def build_visualizer_html(DATA):
    """Task Visualizer tab: 5-col grid of Blender structure renders, grouped by
    difficulty (L1/L2/L3). Cells link to the Task Explorer."""
    DIFF_LABEL = {"L1": "L1 — basic", "L2": "L2 — intermediate", "L3": "L3 — advanced"}
    by_diff = {}
    for tid in sorted(DATA, key=lambda t: int(t[1:])):
        by_diff.setdefault(DATA[tid].get("difficulty", "") or "L?", []).append(tid)
    sections = []
    for diff in ["L1", "L2", "L3", "L?"]:
        tids = by_diff.get(diff, [])
        if not tids:
            continue
        cells = []
        for tid in tids:
            t = DATA[tid]
            prompt = (t.get("prompt_en") or t.get("prompt", "")).replace('"', "&quot;")
            short = prompt if len(prompt) < 92 else prompt[:90] + "…"
            has = os.path.exists(os.path.join(BASE, "renders", f"{tid}.png"))
            img = (f'<img src="renders/{tid}.png" loading="lazy" alt="{tid}">' if has
                   else '<div class="tv-noimg">no structure</div>')
            cells.append(
                f'<figure class="tv-cell" onclick="switchTab(\'explorer\');openTask(\'{tid}\')" title="open in Task Explorer">'
                f'<div class="tv-thumb">{img}</div>'
                f'<figcaption><span class="tv-tid">{tid}</span>'
                f'<span class="tv-cat">{t.get("category","")}</span>'
                f'<span class="tv-desc">{short}</span></figcaption></figure>')
        sections.append(
            f'<h3 class="tv-sec">{DIFF_LABEL.get(diff, diff)} '
            f'<span class="tv-n">{len(tids)} tasks</span></h3>'
            f'<div class="tv-grid">{"".join(cells)}</div>')
    return f'''<div id="tab-visualizer" class="tab-content">
<style>
.tv-intro{{font-size:13px;color:#666;margin:0 0 16px;max-width:760px}}
.tv-sec{{font-size:14px;font-weight:700;color:#111;margin:22px 0 10px;border:none;text-transform:none;letter-spacing:0}}
.tv-sec .tv-n{{font-weight:500;color:#9ca3af;font-size:12px;margin-left:6px}}
.tv-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}}
.tv-cell{{margin:0;background:#fff;border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;cursor:pointer;transition:.15s;display:flex;flex-direction:column}}
.tv-cell:hover{{border-color:#94a3b8;box-shadow:0 4px 14px rgba(0,0,0,.08);transform:translateY(-2px)}}
.tv-thumb{{aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 38%,#f3f4f6,#e2e5ea)}}
.tv-thumb img{{width:100%;height:100%;object-fit:contain}}
.tv-noimg{{color:#9ca3af;font-size:12px}}
.tv-cell figcaption{{padding:7px 9px;display:flex;flex-direction:column;gap:1px;border-top:1px solid #eef0f3}}
.tv-tid{{font-weight:800;font-size:12px;color:#4f46e5}}
.tv-cat{{font-size:9.5px;color:#9ca3af;text-transform:uppercase;letter-spacing:.4px}}
.tv-desc{{font-size:10.5px;color:#475569;line-height:1.32}}
@media(max-width:900px){{.tv-grid{{grid-template-columns:repeat(3,1fr)}}}}
@media(max-width:600px){{.tv-grid{{grid-template-columns:repeat(2,1fr)}}}}
</style>
<h2 class="i18n" data-ko="Task Visualizer — 무엇을 만드는가" data-en="Task Visualizer — what each task builds">Task Visualizer — what each task builds</h2>
<p class="tv-intro i18n" data-ko="50개 벤치마크 태스크가 만드는 구조를 GPT-5.5(skill)의 코드로 생성해 Blender로 렌더링. 추상적인 태스크 목록을 시각적으로 파악하는 키. 셀을 누르면 Task Explorer로 이동." data-en="The structure each of the 50 tasks builds, generated from GPT-5.5 (skill) code and rendered in Blender. A visual key to the otherwise abstract task list. Click a cell to open it in the Task Explorer.">The structure each task builds, rendered in Blender. Click a cell to open it in the Task Explorer.</p>
{"".join(sections)}
</div>'''


def load_judge():
    """-> {key: {tid: {'v':verdict, 'r':reason}}}"""
    out = {}
    for f in glob.glob(os.path.join(JUDGE_DIR, "*.json")):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        key = d.get("model_cond") or os.path.basename(f)[:-5]
        m = {}
        for v in d.get("verdicts", []):
            tid = v.get("tid")
            if tid:
                m[tid] = {"v": int(v.get("verdict", -1)), "r": (v.get("reason", "") or "")[:160]}
        out[key] = m
    return out


def main():
    h = open(V8).read()
    DATA = json.loads(re.search(r"const DATA = (\{.*?\});\s*\n", h, re.S).group(1))
    SUMMARY = json.loads(re.search(r"const SUMMARY = (\{.*?\});\s*\n", h, re.S).group(1))

    # relabel Gemini (the runner stored bare "flash"/"pro"/"flash-lite"; they are
    # all Gemini 2.5). Fix model display names in DATA + SUMMARY here, and in the
    # MODEL_KEYS JS block via text replace below.
    GEM = {"flash-lite": "2.5 Flash-Lite", "flash": "2.5 Flash", "pro": "2.5 Pro"}
    for s in SUMMARY.values():
        if s.get("provider") == "Gemini":
            s["model"] = GEM.get(s["model"], s["model"])
    for t in DATA.values():
        for m in t["models"].values():
            if m.get("provider") == "Gemini":
                m["model"] = GEM.get(m["model"], m["model"])

    judge = load_judge()
    det = json.load(open(DET_PATH)) if os.path.exists(DET_PATH) else {}

    # inject verdicts into DATA + tally into SUMMARY
    tally = {k: {"correct": 0, "partial": 0, "wrong": 0, "judged": 0} for k in SUMMARY}
    for tid, t in DATA.items():
        for key, m in t["models"].items():
            jv = judge.get(key, {}).get(tid)
            if jv is not None:
                m["quality"] = jv["v"]
                m["qreason"] = jv["r"]
                if key in tally:
                    tally[key]["judged"] += 1
                    if jv["v"] == 2:
                        tally[key]["correct"] += 1
                    elif jv["v"] == 1:
                        tally[key]["partial"] += 1
                    elif jv["v"] == 0:
                        tally[key]["wrong"] += 1
            else:
                m["quality"] = m.get("quality", -1)
            dv = det.get(key, {}).get(tid)
            if dv is not None:
                m["det"] = dv.get("verdict", -1)
    for key, t in tally.items():
        SUMMARY[key].update(t)

    njudged = sum(1 for k in judge)
    print(f"judge files: {njudged} | det model_conds: {len(det)}")

    # ---- write back DATA / SUMMARY ----
    h = re.sub(r"const DATA = \{.*?\};\s*\n",
               lambda m: "const DATA = " + json.dumps(DATA, ensure_ascii=False) + ";\n",
               h, count=1, flags=re.S)
    h = re.sub(r"const SUMMARY = \{.*?\};\s*\n",
               lambda m: "const SUMMARY = " + json.dumps(SUMMARY, ensure_ascii=False) + ";\n",
               h, count=1, flags=re.S)

    # ---- Overview thead: add Correct% columns ----
    old_head = ('  <th class="r">w/o Skill Pass%</th>\n'
                '  <th class="r">w/ Skill Pass%</th>\n'
                '  <th class="r">Delta</th>')
    new_head = ('  <th class="r">w/o Skill<br>Runs%</th>\n'
                '  <th class="r">w/o Skill<br>Correct%</th>\n'
                '  <th class="r">w/ Skill<br>Runs%</th>\n'
                '  <th class="r">w/ Skill<br>Correct%</th>\n'
                '  <th class="r">&Delta; Correct</th>')
    assert old_head in h, "overview thead not found"
    h = h.replace(old_head, new_head)

    # ---- buildSummary(): Runs% + Correct% funnel, sorted by w/ skill correct ----
    new_buildsummary = r'''(function buildSummary() {
  const tbody = document.getElementById('summary-body');
  const pct = (a,b) => b ? (a/b*100).toFixed(0) : '0';
  const col = p => p>=80?'var(--green)':p>=50?'var(--amber)':'var(--red)';
  const cell = (num,tot,c) => {
    const p = pct(num,tot);
    return `${num}/${tot} (${p}%)<span class="pass-bar"><span class="pass-bar-fill" style="width:${p}%;background:${c}"></span></span>`;
  };
  const rows = MODEL_KEYS.map(mk => {
    const vs = SUMMARY[mk.van], ss = SUMMARY[mk.skill];
    const vCorr = vs.correct||0, sCorr = ss.correct||0;
    return {mk, vs, ss, vCorr, sCorr, dCorr: sCorr - vCorr};
  });
  rows.sort((a,b) => (b.sCorr/b.ss.total) - (a.sCorr/a.ss.total));
  rows.forEach(({mk,vs,ss,vCorr,sCorr,dCorr}) => {
    const dPct = (dCorr / ss.total * 100).toFixed(0);
    const dClass = dCorr>0?'delta-pos':dCorr<0?'delta-neg':'delta-zero';
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td class="lbl"><span class="provider-tag">${mk.provider}</span></td>
      <td class="lbl">${mk.model}</td>
      <td class="r">${cell(vs.pass_count, vs.total, col(+pct(vs.pass_count,vs.total)))}</td>
      <td class="r">${cell(vCorr, vs.total, col(+pct(vCorr,vs.total)))}</td>
      <td class="r">${cell(ss.pass_count, ss.total, col(+pct(ss.pass_count,ss.total)))}</td>
      <td class="r">${cell(sCorr, ss.total, col(+pct(sCorr,ss.total)))}</td>
      <td class="r ${dClass}">${dCorr>0?'+':''}${dPct}%p</td>`;
    tbody.appendChild(tr);
  });
})();'''
    h = re.sub(r"\(function buildSummary\(\) \{.*?\}\)\(\);", new_buildsummary, h, count=1, flags=re.S)

    # ---- buildHeatmap(): color by correctness, not just pass ----
    # cell: quality 2=correct(green) 1=partial(amber) 0=wrong(red) ; ran-but-unjudged=blue ; fail=gray
    new_cellblock = r'''    CONDITIONS.forEach(c => {
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
      td.style.textAlign='center'; td.style.fontWeight='700'; td.style.fontSize='11px';
      td.textContent = txt;
      td.title = `${tid} | ${c.model} ${COND_LABEL[c.cond]||c.cond} | ${lab}${m.qreason?': '+m.qreason:''}`;
      td.onclick = () => { switchTab('explorer'); openTask(tid); };
      tr.appendChild(td);
    });'''
    old_cellblock = re.search(
        r"    CONDITIONS\.forEach\(c => \{\n"
        r"      const td = document\.createElement\('td'\);\n"
        r"      const s = DATA\[tid\]\.models\[c\.key\]\?\.success;.*?"
        r"      tr\.appendChild\(td\);\n    \}\);", h, re.S)
    assert old_cellblock, "heatmap cell block not found"
    h = h.replace(old_cellblock.group(0), new_cellblock)

    # ---- heatmap legend ----
    old_legend = ('  <span><span class="legend-box" style="background:#dcfce7"></span> Pass</span>\n'
                  '  <span><span class="legend-box" style="background:#fee2e2"></span> Fail</span>')
    new_legend = ('  <span><span class="legend-box" style="background:#16a34a"></span> Correct</span>\n'
                  '  <span><span class="legend-box" style="background:#f59e0b"></span> Partial</span>\n'
                  '  <span><span class="legend-box" style="background:#dc2626"></span> Wrong (ran but incorrect)</span>\n'
                  '  <span><span class="legend-box" style="background:#93c5fd"></span> Ran (unjudged)</span>\n'
                  '  <span><span class="legend-box" style="background:#e5e7eb"></span> Did not run</span>')
    if old_legend in h:
        h = h.replace(old_legend, new_legend)

    # ---- texts / title ----
    h = h.replace("Overall Results — Pass Rate", "Overall Results — Runs vs. Correct (Opus-judged)")
    h = h.replace("Skill Benchmark v8", "Skill Benchmark v9")
    # point the overview image at the correct-rate barplot (sits next to this html)
    h = re.sub(r'src="[^"]*ase_bench_barplot[^"]*"', 'src="ase_bench_barplot_v9.png"', h)
    h = h.replace("50 Tasks &times; 18 Conditions", "50 Tasks &times; 44 Conditions (22 models &times; 2)")
    h = h.replace(
        'data-en="Pass Rate = fraction of successful executions (returncode==0). 50 tasks &times; 9 models &times; 2 conditions (w/o Skill / w/ Skill)."',
        'data-en="Funnel: 50 tasks &rarr; Runs (returncode==0) &rarr; Correct (Opus-as-judge verdict). The Runs%&ndash;Correct% gap is inflation: code that runs but solves the task wrong. 22 models &times; 2 conditions."')

    # Gemini relabel in the MODEL_KEYS JS block (model values only; keys untouched)
    h = h.replace('model: "flash-lite"', 'model: "2.5 Flash-Lite"')
    h = h.replace('model: "flash"', 'model: "2.5 Flash"')
    h = h.replace('model: "pro"', 'model: "2.5 Pro"')

    # replace the static matplotlib PNG <p> with an INTERACTIVE horizontal bar chart
    h = re.sub(r'<p align="center"[^>]*>\s*<img[^>]*ase_bench_barplot[^>]*>\s*</p>',
               CHART_BLOCK, h, count=1, flags=re.S)
    h = h.replace("</body>", CHART_SCRIPT + "\n</body>")

    # ---- Task Visualizer tab (Blender structure gallery) ----
    explorer_btn = ('<div class="tab-btn" onclick="switchTab(\'explorer\')" '
                    'data-ko="Task Explorer" data-en="Task Explorer" class="i18n">Task Explorer</div>')
    vis_btn = ('\n  <div class="tab-btn" onclick="switchTab(\'visualizer\')" '
               'data-ko="Task Visualizer" data-en="Task Visualizer" class="i18n">Task Visualizer</div>')
    if explorer_btn in h:
        h = h.replace(explorer_btn, explorer_btn + vis_btn, 1)
    else:
        print("WARN: explorer tab button not found; visualizer tab not added")
    h = h.replace("</body>", build_visualizer_html(DATA) + "\n</body>")

    with open(OUT, "w") as f:
        f.write(h)
    print(f"wrote {OUT}")
    # console funnel summary
    print(f"\n{'model_cond':34s} {'runs':>5s} {'corr':>5s} {'part':>5s} {'wrong':>6s}")
    for k in sorted(SUMMARY, key=lambda k: -(SUMMARY[k].get('correct', 0))):
        s = SUMMARY[k]
        print(f"{k:34s} {s.get('pass_count',0):>5d} {s.get('correct',0):>5d} "
              f"{s.get('partial',0):>5d} {s.get('wrong',0):>6d}")


if __name__ == "__main__":
    main()
