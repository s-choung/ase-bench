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
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
V9 = os.path.join(BASE, "benchmark_report_v9.html")
VER = sys.argv[1] if len(sys.argv) > 1 else "10"   # e.g. `build_v10.py 11` -> v11
OUT = os.path.join(BASE, f"benchmark_report_v{VER}.html")


# ---------- v10 interactive bar chart (single toggle, 2-tone, logos) ----------
CHART_BLOCK = '''<div class="bc-wrap">
  <div class="bc-controls">
    <label>Sort
      <select id="bc-sort">
        <option value="skill">Correct % (high&rarr;low)</option>
        <option value="delta">Skill gain (&Delta;)</option>
        <option value="release">Release (new&rarr;old)</option>
        <option value="provider">Provider</option>
      </select>
    </label>
    <label>Show
      <select id="bc-show">
        <option value="skill">w/ ASE skill (default)</option>
        <option value="both">compare: + w/o ASE knowledge</option>
      </select>
    </label>
    <span class="bc-pills" id="bc-provfilter"></span>
  </div>
  <div id="bc-chart"></div>
  <div class="bc-legend">
    <span id="bc-leg-van" style="display:none"><span class="bc-key" style="background:#94a3b8;opacity:.4"></span> w/o ASE knowledge (thin, faded)</span>
    <span><span class="bc-key" style="background:#10a37f"></span><span class="bc-key" style="background:#d97757"></span><span class="bc-key" style="background:#4d6bfe"></span> w/ ASE skill &mdash; color = provider</span>
    <span class="bc-note">Correct % = Opus-judged correct / 50 tasks</span>
  </div>
</div>
<h3 class="tl-title">Release timeline &mdash; ASE-Bench scores over model release dates</h3>
<div class="tl-controls">
  <span>From <input type="range" id="tl-from"> <b id="tl-from-lab"></b></span>
  <span>To <input type="range" id="tl-to"> <b id="tl-to-lab"></b></span>
  <span class="tl-hint">drag to zoom the time range &middot; fewer points &rarr; labels appear</span>
</div>
<div id="tl-chart"></div>'''

CHART_SCRIPT = '''<style>
.bc-wrap{margin:1.2rem 0 .6rem;text-align:left}
.bc-controls{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin-bottom:14px;font-size:13px}
.bc-controls label{display:flex;flex-direction:column;gap:3px;font-size:11px;color:#6b7280;font-weight:600}
.bc-controls select{font:13px system-ui;padding:4px 8px;border:1px solid #d1d5db;border-radius:6px;background:#fff}
.bc-pills{display:flex;flex-wrap:wrap;gap:5px;margin-left:auto}
.bc-pill{min-width:38px;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;padding:4px 6px;border-radius:9px;border:1px solid #e2e6ec;background:#fff;color:#4b5563;cursor:pointer;user-select:none;font-weight:700;font-size:9px;transition:.12s}
.bc-pill:hover{border-color:#94a3b8;transform:translateY(-1px)}
.bc-pill img{width:16px;height:16px;object-fit:contain}
.bc-pill-name{font-size:7.5px;font-weight:700;color:#6b7280;max-width:52px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bc-pill.off{opacity:.22;filter:grayscale(1)}
#bc-chart{display:flex;align-items:flex-end;gap:4px;padding:18px 0 0;width:100%}
.bc-col{display:flex;flex-direction:column;align-items:center;gap:5px;flex:1 1 0;min-width:0;cursor:default}
.bc-stack{display:flex;align-items:flex-end;justify-content:center;gap:2px;height:260px;width:100%}
.bc-vbar{width:58%;max-width:18px;border-radius:5px 5px 2px 2px;position:relative;min-height:2px;transition:height .35s cubic-bezier(.4,0,.2,1)}
.bc-vbar.van{opacity:.35;width:32%;max-width:10px}
.bc-vval{position:absolute;top:-15px;left:50%;transform:translateX(-50%);font-size:8.5px;font-weight:800;white-space:nowrap}
.bc-clogo{width:15px;height:15px;object-fit:contain}
.bc-clabel{height:132px;overflow:hidden;writing-mode:vertical-rl;transform:rotate(180deg);display:flex;gap:2px;align-items:center}
.bc-clabel b{font-size:9px;font-weight:700;color:#1f2937;white-space:nowrap}
.bc-clabel span{font-size:7.5px;color:#9ca3af;white-space:nowrap}
.bc-legend{display:flex;gap:18px;align-items:center;margin:10px 0 0 2px;font-size:11.5px;color:#4b5563;flex-wrap:wrap}
.bc-key{display:inline-block;width:12px;height:10px;border-radius:3px;margin-right:2px;vertical-align:-1px}
.bc-note{color:#9ca3af;margin-left:auto}
.tl-title{font-size:14px;font-weight:700;color:#111;margin:26px 0 4px;border:none;text-transform:none;letter-spacing:0}
.tl-controls{display:flex;gap:22px;align-items:center;font-size:11.5px;color:#6b7280;margin:4px 0 6px;flex-wrap:wrap}
.tl-controls input[type=range]{width:150px;vertical-align:middle;accent-color:#4f46e5}
.tl-controls b{color:#1f2937;font-size:11px}
.tl-hint{color:#c2c8d2;font-size:10.5px}
#tl-chart,#iu-chart{margin:0 0 1.4rem}
#tl-chart svg,#iu-chart svg{width:100%;height:auto;display:block}
</style>
<script>
(function(){
  if(typeof SUMMARY==='undefined'){return;}
  // provider brand colors (representative, not official-exact)
  const PAL={OpenAI:'#10a37f',Claude:'#d97757',Gemini:'#4285f4',Google:'#34a853',
    DeepSeek:'#4d6bfe',Qwen:'#7c3aed',xAI:'#1f2937','OpenAI-oss':'#0d8a6a',
    Meta:'#0866ff',Mistral:'#fa520f',Cohere:'#39594d',Amazon:'#ff9900',
    Baidu:'#2932e1',Tencent:'#0052d9',ByteDance:'#5b8def',Zhipu:'#3859ff',
    Moonshot:'#5f3dc4',MiniMax:'#f23f5d',Xiaomi:'#ff6900',NVIDIA:'#76b900',
    Upstage:'#9775fa',Microsoft:'#00a4ef',Inception:'#0ea5e9',IBM:'#0f62fe',
    StepFun:'#00b8a9',AllenAI:'#f0529c'};
  const pcol=p=>PAL[p]||'#64748b';
  const LOGO_ALIAS={'OpenAI-oss':'OpenAI'};
  const logoSrc=p=>'assets/logos/'+(LOGO_ALIAS[p]||p)+'.png';
  // release month (approx; YYYY-MM). Models missing here are skipped by the
  // timeline (console.warn) but still shown in the bar chart.
  const REL={'OpenAI|gpt-5.5':'2026-01','OpenAI|gpt-5.4':'2025-11','OpenAI|gpt-5.4-mini':'2025-11',
    'Claude|Fable 5':'2026-06','Claude|Opus 4.7':'2025-12','Claude|Sonnet 4.6':'2025-11','Claude|Haiku 4.5':'2025-10',
    'Gemini|2.5 Pro':'2025-06','Gemini|2.5 Flash':'2025-06','Gemini|2.5 Flash-Lite':'2025-07',
    'DeepSeek|deepseek-v4-pro':'2025-12','DeepSeek|deepseek-v3.2':'2025-09','DeepSeek|deepseek-r1-0528':'2025-05',
    'Qwen|qwen3-235b-thinking':'2025-07','Qwen|qwen3-235b':'2025-04','Qwen|qwen3-32b':'2025-04','Qwen|qwen3-max':'2025-09',
    'xAI|grok-4.3':'2026-01','Moonshot|kimi-k2.5':'2025-11','MiniMax|minimax-m3':'2025-10',
    'Xiaomi|mimo-v2.5':'2025-10','OpenAI-oss|gpt-oss-120b':'2025-08',
    'NVIDIA|nemotron-3-super-120b':'2025-09','Upstage|solar-pro-3':'2025-11',
    'Meta|llama-4-maverick':'2025-04','Tencent|hunyuan-a13b':'2025-06','Zhipu|glm-4.6':'2025-09',
    'Mistral|mistral-large':'2024-11','Cohere|command-a':'2025-03','Amazon|nova-premier':'2025-03',
    'Baidu|ernie-4.5':'2025-06',
    'Qwen|qwen3-8b':'2025-04','Qwen|qwen3-14b':'2025-04','Zhipu|glm-5.1':'2026-02',
    'ByteDance|seed-1.6':'2025-06','Google|gemma-3-27b':'2025-03','Microsoft|phi-4':'2024-12',
    'Inception|mercury-2':'2025-11','AllenAI|olmo-3-32b-think':'2025-11',
    'Google|gemma-3-4b':'2025-03','Google|gemma-3-12b':'2025-03','Mistral|mistral-medium-3.5':'2026-03',
    'StepFun|step-3.7-flash':'2026-01','IBM|granite-4.1-8b':'2025-12','DeepSeek|deepseek-v4-flash':'2025-12',
    'xAI|grok-4.20':'2026-04'};

  const pair={};
  Object.values(SUMMARY).forEach(s=>{const k=s.provider+'|'+s.model;(pair[k]=pair[k]||{provider:s.provider,model:s.model})[s.condition]=s;});
  const MODELS=Object.values(pair).filter(p=>p.vanilla&&p['skill_v3']).map(p=>({
    provider:p.provider,model:p.model,total:p.vanilla.total||50,
    vCorr:p.vanilla.correct||0,sCorr:p['skill_v3'].correct||0,
    vRun:p.vanilla.pass_count||0,sRun:p['skill_v3'].pass_count||0,
    rel:REL[p.provider+'|'+p.model]||''}));
  const provs=[...new Set(MODELS.map(m=>m.provider))];
  const state={sort:'skill',show:'skill',off:new Set()};
  const pct=(a,t)=>t?Math.round(100*a/t):0;
  const vv=m=>pct(m.vCorr,m.total), sv=m=>pct(m.sCorr,m.total);

  // ---- bar chart ----
  const pf=document.getElementById('bc-provfilter');
  provs.forEach(p=>{const sp=document.createElement('span');sp.className='bc-pill';
    sp.title=p+' — click to toggle';
    const im=document.createElement('img');im.src=logoSrc(p);im.alt=p;
    im.onerror=()=>{im.remove();};
    sp.appendChild(im);
    const nm=document.createElement('span');nm.className='bc-pill-name';nm.textContent=p;
    sp.appendChild(nm);
    sp.onclick=()=>{state.off.has(p)?state.off.delete(p):state.off.add(p);sp.classList.toggle('off');render();renderIU();renderTL();};
    pf.appendChild(sp);});

  const chart=document.getElementById('bc-chart');
  function render(){
    let rows=MODELS.filter(m=>!state.off.has(m.provider));
    if(state.sort==='release') rows.sort((a,b)=>(b.rel||'').localeCompare(a.rel||'')||sv(b)-sv(a));
    else if(state.sort==='provider') rows.sort((a,b)=>a.provider.localeCompare(b.provider)||sv(b)-sv(a));
    else if(state.sort==='delta') rows.sort((a,b)=>(sv(b)-vv(b))-(sv(a)-vv(a)));
    else rows.sort((a,b)=>sv(b)-sv(a));
    chart.innerHTML=rows.map(m=>{
      const c=pcol(m.provider);const sk=sv(m),va=vv(m);
      const bars=`<div class="bc-vbar" style="height:${Math.max(sk,1)}%;background:${c}"><span class="bc-vval" style="color:${c}">${sk}</span></div>`
        +(state.show==='both'?`<div class="bc-vbar van" style="height:${Math.max(va,1)}%;background:${c}"></div>`:'');
      return `<div class="bc-col" title="${m.provider} ${m.model} — w/ Skill ${sk}% · w/o ${va}% (Δ ${sk-va>0?'+':''}${sk-va}%p)">`
        +`<div class="bc-stack">${bars}</div>`
        +`<img class="bc-clogo" src="${logoSrc(m.provider)}" alt="${m.provider}" onerror="this.style.visibility='hidden'">`
        +`<div class="bc-clabel"><b>${m.model}</b><span>${m.provider}</span></div></div>`;
    }).join('');
    document.getElementById('bc-leg-van').style.display=state.show==='both'?'':'none';
  }
  document.getElementById('bc-sort').onchange=e=>{state.sort=e.target.value;render();};
  document.getElementById('bc-show').onchange=e=>{state.show=e.target.value;render();};

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

  // ---- release timeline (SVG scatter) ----
  const tl=document.getElementById('tl-chart');
  const monthIdx=r=>{const[y,m]=r.split('-').map(Number);return y*12+(m-1);};
  function renderTL(){
    const rows=MODELS.filter(m=>!state.off.has(m.provider)&&m.rel
      &&monthIdx(m.rel)>=state.tlFrom&&monthIdx(m.rel)<=state.tlTo);
    if(!rows.length){tl.innerHTML='<p style="font-size:12px;color:#9ca3af;padding:20px 0">no models in this range</p>';return;}
    const W=980,H=420,L=46,R=16,T=18,B=44;
    const now=new Date();
    const todayMi=now.getFullYear()*12+now.getMonth();
    const m0=state.tlFrom-1,m1=Math.max(state.tlTo,Math.min(todayMi,state.tlTo))+1;
    const X=mi=>L+(W-L-R)*(mi-m0)/(m1-m0||1);
    const Y=v=>T+(H-T-B)*(1-v/100);
    let g='';
    for(let v=0;v<=100;v+=20)
      g+=`<line x1="${L}" y1="${Y(v)}" x2="${W-R}" y2="${Y(v)}" stroke="#eef0f3"/><text x="${L-7}" y="${Y(v)+3.5}" text-anchor="end" font-size="10" fill="#9ca3af">${v}</text>`;
    for(let mi=m0;mi<=m1;mi++){
      const yy=Math.floor(mi/12),mm=mi%12+1;
      if(mm===1||mm===4||mm===7||mm===10)
        g+=`<line x1="${X(mi)}" y1="${T}" x2="${X(mi)}" y2="${H-B}" stroke="#f3f4f6"/><text x="${X(mi)}" y="${H-B+15}" text-anchor="middle" font-size="9.5" fill="#9ca3af">${yy}-${String(mm).padStart(2,'0')}</text>`;
    }
    // jitter models sharing a month; collect positions first
    const seen={};
    const pos=[];
    rows.sort((a,b)=>monthIdx(a.rel)-monthIdx(b.rel)).forEach((m,i)=>{
      const mi=monthIdx(m.rel);const n=(seen[mi]=(seen[mi]||0)+1);
      const x=X(mi)+((n-1)%3-1)*7;
      pos.push({m,i,x,yV:Y(vv(m)),yS:Y(sv(m))});
    });
    // per-provider trajectory lines (chronological, >=2 dated models)
    const byProv={};
    pos.forEach(p=>{(byProv[p.m.provider]=byProv[p.m.provider]||[]).push(p);});
    let provLines='';
    Object.entries(byProv).forEach(([pv,ps])=>{
      if(ps.length>1) provLines+=`<polyline points="${ps.map(p=>p.x+','+p.yS).join(' ')}" fill="none" stroke="${pcol(pv)}" stroke-width="1.3" opacity=".35"/>`;
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
    const frSet=new Set(fr);
    pos.forEach(p=>{
      const {m,i,x,yV,yS}=p;
      const isFr=frSet.has(p);
      const tip=`${m.provider} ${m.model} (${m.rel})&#10;w/ Skill ${sv(m)}% · w/o ${vv(m)}%${isFr?'&#10;SOTA at release':''}`;
      const c=pcol(m.provider);
      const lab=(showAll||isFr)?`<text x="${x+7}" y="${yS+(i%2?9:-5)}" font-size="8.5" font-weight="${isFr?'700':'400'}" fill="#475569">${m.model}</text>`:'';
      // when w/o == w/ the markers coincide: draw only the filled one
      // (both numbers are in the tooltip; e.g. Fable 5: 96% = 96%)
      const overlap=Math.abs(yV-yS)<7;
      pts+=`<g><title>${tip}</title>`
        +(overlap?'':`<line x1="${x}" y1="${yV}" x2="${x}" y2="${yS}" stroke="#cbd5e1" stroke-dasharray="3 3"/>`
          +`<circle cx="${x}" cy="${yV}" r="4" fill="#fff" stroke="${c}" stroke-width="1.6"/>`)
        +`<circle cx="${x}" cy="${yS}" r="5" fill="${c}"/>`
        +lab+`</g>`;
    });
    // "Today" marker (client-side date), only when inside the selected range
    let today='';
    if(todayMi>=m0&&todayMi<=m1){
      const tx=X(todayMi+now.getDate()/31);
      today=`<line x1="${tx}" y1="${T}" x2="${tx}" y2="${H-B+18}" stroke="#f43f5e" stroke-width="1.2" stroke-dasharray="5 4" opacity=".75"/>`
        +`<text x="${tx}" y="${H-B+30}" text-anchor="middle" font-size="10" font-weight="700" fill="#f43f5e">Today</text>`;
    }
    // legend, top-left
    const lx=L+12;
    const legend=`<g font-size="10.5" fill="#4b5563">`
      +`<circle cx="${lx}" cy="${T+6}" r="5" fill="#64748b"/><text x="${lx+9}" y="${T+10}">w/ Skill</text>`
      +`<circle cx="${lx+75}" cy="${T+6}" r="4" fill="#fff" stroke="#64748b" stroke-width="1.6"/><text x="${lx+84}" y="${T+10}">w/o Skill</text>`
      +`<text x="${lx+155}" y="${T+10}" fill="#9ca3af">color = provider · Y = Correct %</text></g>`;
    tl.innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Correct rate vs model release date">${g}${today}${provLines}${frLine}${pts}${legend}</svg>`;
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

  render();renderIU();renderTL();
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
      <span class="hero-chip">50 tasks &times; 45 models</span>
      <span class="hero-chip">4,500+ scripts executed &amp; graded</span>
      <a class="hero-chip req" href="https://github.com/s-choung/ase-bench/issues/new?template=model-request.yml" target="_blank" rel="noopener">+ Request a model</a>
      <a class="hero-chip wl" href="https://github.com/s-choung/ase-bench/issues?q=is%3Aissue+label%3Amodel-request" target="_blank" rel="noopener">waiting list &nearr;</a>
    </div>
  </div>
</div>'''


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
    h = h.replace(
        '<p class="date">2026.05 &middot; Seokhyun Choung &middot; Pass Rate Dashboard</p>',
        f'<p class="date">v1.0 &middot; report v{VER} &middot; '
        f'last updated {__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M")} KST '
        f'&middot; Seokhyun Choung</p>')
    # the hero block now carries the intro -> drop the old standalone paragraph
    intro_p = re.search(
        r'<p data-ko="자연어 지시만으로.*?class="i18n-html"></p>\s*', h, re.S)
    assert intro_p, "old intro paragraph not found"
    h = h.replace(intro_p.group(0), "")
    h = h.replace(
        "<span>ASE Skill Benchmark v9 / Gemini + OpenAI + Claude / Pass Rate Dashboard</span>",
        f"<span>ASE-Bench v1.0 / report v{VER} / runs&rarr;correct funnel</span>")
    # v9 fixed only the EN funnel description; fix the KO one here
    h = h.replace(
        'data-ko="Pass Rate = 실행 성공(returncode==0) 비율. 50개 태스크 &times; 9개 모델 '
        '&times; 2 조건(w/o Skill / w/ Skill)."',
        'data-ko="Funnel: 50 태스크 &rarr; Runs(returncode==0) &rarr; Correct(Opus-as-judge). '
        'Runs%와 Correct%의 간극 = 돌지만 틀린 코드(인플레이션)."')
    # methodology fine print -> muted gray (secondary info, not the headline)
    h = h.replace(
        '<p class="center-text i18n-html" style="font-size:13px"\n   data-ko="Funnel: 50 태스크',
        '<p class="center-text i18n-html" style="font-size:10.5px;color:#c2c8d2"\n   data-ko="Funnel: 50 태스크')
    h = h.replace("2026.05</span>", "2026.06</span>")

    # ---- 2+3. bar chart (simplified) + timeline ---------------------------
    old_block = re.search(r'<div class="bc-wrap">.*?<div id="bc-chart"></div>\s*</div>', h, re.S)
    assert old_block, "v9 chart block not found"
    h = h.replace(old_block.group(0), CHART_BLOCK)
    old_script = re.search(r'<style>\s*\.bc-wrap\{.*?</script>', h, re.S)
    assert old_script, "v9 chart script not found"
    h = h.replace(old_script.group(0), CHART_SCRIPT)

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

  const tbody = document.getElementById('heatmap-body');
  tbody.innerHTML = '';
  models.forEach(p => {
    ['skill_v3','vanilla'].forEach(cond => {
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
})();'''
    h = re.sub(r"\(function buildHeatmap\(\) \{.*?\}\)\(\);", new_heatmap.replace("\\", "\\\\"),
               h, count=1, flags=re.S)
    h = h.replace("50 Tasks &times; 44 Conditions (22 models &times; 2)",
                  "Models &times; 2 conditions (rows) &times; 50 Tasks (columns)")

    # ---- 7. "The Skill" tab: full ase_skill_v3.md text ----------------------
    skill_md = open(os.path.join(BASE, "tasks", "ase_skill_v3.md")).read()
    esc = skill_md.replace("&", "&amp;").replace("<", "&lt;")
    skill_tab = f'''<div id="tab-skill" class="tab-content">
<style>
.skill-pre{{background:#0f172a;color:#dbe4f0;border-radius:12px;padding:22px 26px;font:12px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;overflow-x:auto;white-space:pre-wrap;word-break:break-word}}
.skill-meta{{font-size:13px;color:#666;margin:0 0 14px;max-width:760px}}
</style>
<h2 class="i18n" data-ko="The Skill — 개입의 전부" data-en="The Skill — the entire intervention">The Skill — the entire intervention</h2>
<p class="skill-meta i18n" data-ko="아래 markdown 한 장이 w/와 w/o 조건의 유일한 차이다. 시스템 프롬프트에 이 텍스트를 덧붙이는 것이 개입의 전부 — 파인튜닝도, 도구도, 예제 답안도 없다." data-en="This single markdown page is the only difference between the w/ and w/o conditions. Appending this text to the system prompt is the entire intervention — no fine-tuning, no tools, no answer examples.">This single markdown page is the only difference between the two conditions.</p>
<pre class="skill-pre">{esc}</pre>
</div>'''
    vis_btn = ('<div class="tab-btn" onclick="switchTab(\'visualizer\')" '
               'data-ko="Task Visualizer" data-en="Task Visualizer" class="i18n">Task Visualizer</div>')
    assert vis_btn in h, "visualizer tab button not found"
    skill_btn = ('\n  <div class="tab-btn" onclick="switchTab(\'skill\')" '
                 'data-ko="The Skill" data-en="The Skill" class="i18n">The Skill</div>')
    h = h.replace(vis_btn, vis_btn + skill_btn, 1)
    h = h.replace("</body>", skill_tab + "\n</body>")

    with open(OUT, "w") as f:
        f.write(h)
    print(f"wrote {OUT} ({len(h):,} bytes)")


if __name__ == "__main__":
    main()
