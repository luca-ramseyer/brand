# Luca Ramseyer — Brand

The visual identity for the Luca Ramseyer / raml.ch personal brand: systems, cybersecurity, software. Quiet, precise, Swiss restraint.

- **Humans:** open [`style-guide.html`](style-guide.html) in a browser for the full guide — colour, type, logo, components, email, social, voice.
- **AI / coding agents:** read [`AGENTS.md`](AGENTS.md) and import the tokens. See below.

## What's here

```
tokens.json          Single source of truth (colour, type, spacing, radius…)
build_tokens.py      Regenerates the files below from tokens.json (no dependencies)
tokens/
  tokens.css         CSS custom properties — plain CSS / vanilla projects
  theme.css          Tailwind v4 @theme — drop into Tailwind projects
AGENTS.md            Short, high-signal rules for coding agents
style-guide.html     Beautiful human guide (also embeds the tokens as JSON)
style-guide.md       Markdown mirror of the guide (AI- and human-friendly)
llms.txt             Pointer file for LLMs/agents that fetch the site
assets/              Logos, marks, favicons, social banners
fonts/               OFL licence files (+ self-hosted webfonts if you add them)
```

## Use it in a project

**Plain CSS**
```html
<link rel="stylesheet" href="tokens/tokens.css">
<!-- then: color: var(--ink); font-family: var(--serif); padding: var(--s4); -->
```

**Tailwind v4**
```css
@import "tailwindcss";
@import "./theme.css";
/* utilities: bg-paper text-ink font-display text-h2 p-4 */
```

**With a coding agent (Claude Code, Cursor, Codex, …)**
- Drop `AGENTS.md` + `tokens/` into the project (or add this repo as a git submodule), or
- Add one line to the project's `AGENTS.md`:
  `Brand: follow https://raw.githubusercontent.com/<you>/raml-brand/main/AGENTS.md — use tokens/tokens.css, never invent colours or fonts.`
- For Claude Code specifically: keep `CLAUDE.md` thin (Claude-only config) and let `AGENTS.md` carry the shared brand rules.

## Editing

`tokens.json` is the only file you hand-edit for design values. Then:

```bash
python3 build_tokens.py
```

This regenerates `tokens/tokens.css`, `tokens/theme.css`, and the `:root` block + embedded JSON inside `style-guide.html`, so the human page and the machine files never drift.

## Hosting

- Push this repo to GitHub (public) — it becomes the canonical, fetchable source.
- Serve `style-guide.html` via Cloudflare Pages or GitHub Pages at e.g. `brand.raml.ch`.
- Keep `llms.txt` at the site root so browsing agents can discover the guide.

## Licensing

Both typefaces are under the **SIL Open Font License 1.1** — free for personal and commercial use, including embedding. Licence files are in `fonts/`. You only need to ship an `OFL-*.txt` when you redistribute the font *files* (self-hosting webfonts or bundling into an app) — not for Google Fonts CDN use or document exports (PDF, PNG, SVG, the card). See `fonts/README.md`. Colours, layout, the wordmark, the mark, and the code are original to this brand and free to use and modify.
