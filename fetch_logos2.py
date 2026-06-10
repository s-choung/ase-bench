"""Fetch high-quality provider logos from lobehub/icons (an icon set built FOR
LLM providers), with favicon fallback. Tries color then mono variants for each
candidate slug. Saves assets/logos/<provider>.png (overwrites the low-res
favicons from fetch_logos.py)."""
import os
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "assets", "logos")
os.makedirs(OUT, exist_ok=True)

# provider -> candidate lobehub slugs (first that resolves wins)
PROVIDERS = {
    "OpenAI":  ["openai"],
    "Claude":  ["claude", "anthropic"],
    "Gemini":  ["gemini"],
    "DeepSeek":["deepseek"],
    "Qwen":    ["qwen", "qwen3", "tongyi"],
    "MiniMax": ["minimax"],
    "Moonshot":["kimi", "moonshot"],
    "Xiaomi":  ["mimo", "xiaomi"],
    "NVIDIA":  ["nvidia"],
    "Upstage": ["upstage", "solar"],
    "xAI":     ["grok", "xai"],
    "Zhipu":   ["zhipu", "chatglm", "z-ai"],
    "Mistral": ["mistral"],
    "Meta":    ["meta", "llama"],
    "Cohere":  ["cohere"],
    "Amazon":  ["bedrock", "aws", "amazon", "nova"],
    "Baidu":   ["wenxin", "baidu", "ernie"],
    "Tencent": ["hunyuan", "tencent"],
    # round-2/3 vendors (2026-06-10)
    "Microsoft": ["microsoft", "phi", "azure"],
    "ByteDance": ["doubao", "bytedance", "seed"],
    "Inception": ["inception", "mercury"],
    "AllenAI":   ["ai2", "allenai", "olmo"],
    "StepFun":   ["stepfun", "step"],
    "IBM":       ["granite", "ibm", "watsonx"],
    "Google":    ["gemma", "google"],
}

CDNS = [
    "https://unpkg.com/@lobehub/icons-static-png@latest/light/{slug}-color.png",
    "https://unpkg.com/@lobehub/icons-static-png@latest/light/{slug}.png",
    "https://cdn.jsdelivr.net/npm/@lobehub/icons-static-png/light/{slug}-color.png",
    "https://cdn.jsdelivr.net/npm/@lobehub/icons-static-png/light/{slug}.png",
]


def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def main():
    got, missing = [], []
    for prov, slugs in PROVIDERS.items():
        data = src = None
        for slug in slugs:
            for tmpl in CDNS:
                url = tmpl.format(slug=slug)
                try:
                    d = fetch(url)
                    if d and len(d) > 600:
                        data, src = d, url.split("/light/")[-1]
                        break
                except Exception:
                    continue
            if data:
                break
        if data:
            with open(os.path.join(OUT, f"{prov}.png"), "wb") as f:
                f.write(data)
            got.append(f"{prov}({src}, {len(data)}B)")
        else:
            missing.append(prov)
    print("GOT:", ", ".join(got))
    print("MISSING (kept favicon):", ", ".join(missing) or "none")


if __name__ == "__main__":
    main()
