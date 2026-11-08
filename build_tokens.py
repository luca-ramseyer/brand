#!/usr/bin/env python3
"""Generate machine + human assets from tokens.json (no dependencies).

Outputs:
  tokens/tokens.css   CSS custom properties, light + dark (used by the HTML guide and any plain CSS project)
  tokens/theme.css    Tailwind v4 @theme block + dark overrides (drop-in for Tailwind projects)
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
    L.append(("--mono",  T["font"]["mono"]))
    for i, hexv in enumerate(T["chart"]["light"], start=1):
        L.append((f"--chart-{i}", hexv))
    for k, v in T["type"].items():
        L.append((f"--text-{k}", f"{v}px"))
    for k, v in T["tracking"].items():
        L.append((f"--tracking-{k}", v))
    for k, v in T["leading"].items():
        L.append((f"--leading-{k}", str(v)))
    for k, v in T["weight"].items():
        L.append((f"--weight-{k}", str(v)))
    for i, px in enumerate(T["space"], start=1):
        L.append((f"--s{i}", f"{px}px"))
    L.append(("--radius-ui", T["radius"]["ui"]))
    L.append(("--radius-card", T["radius"]["card"]))
    L.append(("--motion-fast", T["motion"]["fast"]))
    L.append(("--motion-press", T["motion"]["press"]))
    L.append(("--motion-enter", T["motion"]["enter"]))
    L.append(("--ease-out", T["motion"]["easeOut"]))
    L.append(("--press-scale", T["motion"]["pressScale"]))
    L.append(("--maxw", T["layout"]["maxWidth"]))
    return L

def dark_vars(prefix="--"):
    L = [(f"{prefix}{k}", v) for k, v in T["dark"].items() if not k.startswith("$")]
    chart_prefix = "--color-chart-" if prefix == "--color-" else "--chart-"
    L += [(f"{chart_prefix}{i}", v) for i, v in enumerate(T["chart"]["dark"], start=1)]
    return L

def dark_block(prefix="--"):
    lines = ["@media (prefers-color-scheme: dark) {", "  :root {"]
    lines += [f"    {n}: {v};" for n, v in dark_vars(prefix)]
    lines += ["  }", "}"]
    return lines

def write_tokens_css():
    lines = ["/* Generated from tokens.json — do not edit by hand. */", ":root {"]
    for name, val in css_vars():
        lines.append(f"  {name}: {val};")
    lines.append("}")
    lines.append("/* Dark theme: drop this block if a surface must stay light (print, the style guide). */")
    lines += dark_block()
    os.makedirs(os.path.join(ROOT, "tokens"), exist_ok=True)
    open(os.path.join(ROOT, "tokens", "tokens.css"), "w").write("\n".join(lines) + "\n")

def write_theme_css():
    """Tailwind v4 @theme — utilities like bg-paper, text-ink, font-display, text-h2, p-4."""
    lines = ["/* Tailwind v4 theme — generated from tokens.json. Import after `@import \"tailwindcss\";` */",
             "@theme {"]
    for k, v in T["color"].items():
        lines.append(f"  --color-{k}: {v['hex']};")
    lines.append(f"  --font-wordmark: {T['font']['serif']};")
    lines.append(f"  --font-sans: {T['font']['sans']};")
    lines.append(f"  --font-mono: {T['font']['mono']};")
    for i, hexv in enumerate(T["chart"]["light"], start=1):
        lines.append(f"  --color-chart-{i}: {hexv};")
    for k, v in T["type"].items():
        lines.append(f"  --text-{k}: {v}px;")
    for i, px in enumerate(T["space"], start=1):
        lines.append(f"  --spacing-{i}: {px}px;")
    lines.append(f"  --radius-ui: {T['radius']['ui']};")
    lines.append(f"  --radius-card: {T['radius']['card']};")
    lines.append(f"  --ease-out: {T['motion']['easeOut']};")
    lines.append("}")
    lines += dark_block("--color-")
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
