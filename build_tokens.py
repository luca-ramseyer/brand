#!/usr/bin/env python3
"""Generate machine + human assets from tokens.json (no dependencies).

Outputs:
  tokens/tokens.css   CSS custom properties (used by the HTML guide and any plain CSS project)
  tokens/theme.css    Tailwind v4 @theme block (drop-in for Tailwind projects)
Patches in place:
  style-guide.html    the :root{...} block + an embedded <script id="brand-tokens"> JSON

Run:  python3 build_tokens.py
"""
import json, re, os

ROOT = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(ROOT, "tokens.json")))

def css_vars():
    L = []
    for k, v in T["color"].items():
        L.append((f"--{k}", v["hex"]))
    L.append(("--serif", T["font"]["serif"]))
    L.append(("--sans",  T["font"]["sans"]))
    for k, v in T["type"].items():
        L.append((f"--text-{k}", f"{v}px"))
    for k, v in T["tracking"].items():
        L.append((f"--tracking-{k}", v))
    for k, v in T["leading"].items():
        L.append((f"--leading-{k}", str(v)))
    for i, px in enumerate(T["space"], start=1):
        L.append((f"--s{i}", f"{px}px"))
    L.append(("--radius-ui", T["radius"]["ui"]))
    L.append(("--motion-fast", T["motion"]["fast"]))
    L.append(("--maxw", T["layout"]["maxWidth"]))
    return L

def write_tokens_css():
    lines = ["/* Generated from tokens.json — do not edit by hand. */", ":root {"]
    for name, val in css_vars():
        lines.append(f"  {name}: {val};")
    lines.append("}")
    os.makedirs(os.path.join(ROOT, "tokens"), exist_ok=True)
    open(os.path.join(ROOT, "tokens", "tokens.css"), "w").write("\n".join(lines) + "\n")

def write_theme_css():
    """Tailwind v4 @theme — utilities like bg-paper, text-ink, font-display, text-h2, p-4."""
    lines = ["/* Tailwind v4 theme — generated from tokens.json. Import after `@import \"tailwindcss\";` */",
             "@theme {"]
    for k, v in T["color"].items():
        lines.append(f"  --color-{k}: {v['hex']};")
    lines.append(f"  --font-display: {T['font']['serif']};")
    lines.append(f"  --font-sans: {T['font']['sans']};")
    for k, v in T["type"].items():
        lines.append(f"  --text-{k}: {v}px;")
    for i, px in enumerate(T["space"], start=1):
        lines.append(f"  --spacing-{i}: {px}px;")
    lines.append(f"  --radius-ui: {T['radius']['ui']};")
    lines.append("}")
    open(os.path.join(ROOT, "tokens", "theme.css"), "w").write("\n".join(lines) + "\n")

def patch_html():
    path = os.path.join(ROOT, "style-guide.html")
    if not os.path.exists(path):
        return
    html = open(path).read()

    # 1) regenerate :root{...}
    root = ["  :root{",
            "    /* TOKENS:START — generated from tokens.json by build_tokens.py. Do not edit by hand. */"]
    for name, val in css_vars():
        root.append(f"    {name}:{val};")
    root.append("    /* TOKENS:END */")
    root.append("  }")
    root_block = "\n".join(root)
    html = re.sub(r":root\{.*?\}", root_block.strip(), html, count=1, flags=re.S)

    # 2) embed machine-readable JSON for agents that fetch the page
    payload = json.dumps(T, ensure_ascii=False, separators=(",", ":"))
    script = f'<script type="application/json" id="brand-tokens">{payload}</script>'
    if 'id="brand-tokens"' in html:
        html = re.sub(r'<script type="application/json" id="brand-tokens">.*?</script>', script, html, flags=re.S)
    else:
        html = html.replace("</head>", f"  {script}\n</head>", 1)

    open(path, "w").write(html)

if __name__ == "__main__":
    write_tokens_css()
    write_theme_css()
    patch_html()
    print("Generated tokens/tokens.css, tokens/theme.css; patched style-guide.html")
