# AGENTS.md — Luca Ramseyer brand

Use this design system when building any UI, site, email, or graphic for the Luca Ramseyer / raml.ch personal brand. Keep it minimal and faithful; the whole identity is restraint.

## Non-negotiable rules
- **Never invent colours or fonts.** Use only the tokens below (full set: `tokens/tokens.css`, Tailwind: `tokens/theme.css`, raw: `tokens.json`).
- **Two typefaces only:** Schibsted Grotesk for everything (headings, body, UI, data) and Cormorant Garamond Medium for the wordmark and LR monogram only. Never set headings or body in the serif. Do not add a third family.
- **Red is seasoning,** not a theme colour. One accent per view at most (a hover, a dot, a single button). Backgrounds and large areas are paper or ink.
- **The wordmark "LUCA RAMSEYER"** is set in Cormorant Garamond Medium, all caps, letter-spacing `0.24em`. Never tighten the tracking, recolour it, stretch it, or add effects.
- **The mark** is a muted-red rounded square with the cross knocked out (paper/white shows through). Cross geometry is fixed: arm thickness 21.5% of the square, arm length 62%, corner radius 10%. Assets in `assets/`.

## Tokens (authoritative values live in tokens.json)
- Colours: paper `#F4EFE4`, surface `#FBF8F1`, ink `#211F1C`, body `#423D37`, muted `#6F685D` (captions, AA), stone `#857E72` (non-text only), red `#C0473A`, red-deep `#A63B30`, line `#DAD2C4`, good `#5B7A52`.
- Dark mode (automatic in `tokens/tokens.css` via `prefers-color-scheme`): paper `#1C1A18`, surface `#24221F`, ink `#F4EFE4`, body `#CFC8BB`, muted `#A39B8E`, red `#DB6B5D`, line `#36332E`. Use tokens, never light-only hex values.
- Charts in order: `--chart-1` ink (main series), `--chart-2` red (only the one value that matters), then stone, sage, sand.
- Type scale (px): display 56, h1 44, h2 28, h3 19 (600), body 16, small 13, label 12.
- Headings: weight 500, letter-spacing `-0.02em` (display `-0.03em`), line-height 1.1, sentence case. Body 400, line-height 1.6. Labels: 12px 500 uppercase `0.08em`, sparingly. Buttons sentence case. Tabular figures only in aligned columns (Schibsted's tabular set also widens `.` and `,`).
- Spacing scale (px): 8 / 16 / 24 / 32 / 48 / 64 / 96. Radius: 6px controls, 8px cards.

## Defaults when building
- Plain web: link `tokens/tokens.css`, then use `var(--ink)`, `var(--serif)`, `var(--s4)`, etc.
- Tailwind v4: `@import "tailwindcss";` then `@import "./theme.css";` → utilities like `bg-paper text-ink font-sans text-h2 p-4 (font-wordmark for the wordmark)`.
- Webfonts: include the Google Fonts link from `tokens.json#font.googleImport`. Fallbacks are already in the font stacks.
- Layout: generous whitespace; centre hero content; left-align reading content in a ~920px column. Whitespace is the primary design element — when unsure, remove something.
- Components: small corners (6px controls, 8px cards), hairline (`--line`) borders, sentence-case 14px medium button labels. No shadows, no gradients. Ready-made CSS: https://pages.lram.ch/brand.css
- Motion: 200ms colour transitions naming their properties (never `transition: all`); `:active` press `scale(0.97)` over 140ms; entrances under 500ms with `cubic-bezier(0.23, 1, 0.32, 1)`, transform/opacity only; respect `prefers-reduced-motion`. Visible `:focus-visible` outline.

## Mobile first (most visitors are on phones)
- Viewport: `width=device-width, initial-scale=1, viewport-fit=cover`. Never `user-scalable=no` or `maximum-scale=1`.
- Design the 360–430px single column first. No fixed widths; the page never scrolls sideways (wide tables/code/charts scroll in their own box).
- 16px side padding plus `env(safe-area-inset-*)` on edges and fixed elements.
- Touch targets ≥ 44×44px, 8px apart. Hover styles only inside `@media (hover: hover)`; nothing hover-only.
- Body 16px, nothing under 12px, h1 32–40px on phones; inputs 16px (prevents iOS zoom); right `inputmode`/`type` for keyboards.
- `100svh` for full-height heroes, never `100vh`. One `theme-color` per colour scheme.
- Check on a real phone before calling it done.

## Voice
Calm, precise, expert. Plain verbs (block, review, restore). Explain security without fear or hype. Never "100% secure". Sentence case, no exclamation stacks.

## Print note
On paper, ink = rich black `C40 M30 Y30 K100`; red = `C0 M65 Y72 K22`. Cards print with no background ink — the cream comes from the stock.

## Licensing (fonts) — IMPORTANT
Both typefaces are under the **SIL Open Font License 1.1** — free for personal and commercial use, including embedding. License files live in `fonts/` (`OFL-SchibstedGrotesk.txt`, `OFL-CormorantGaramond.txt`).
- **Include the matching OFL file** in your output ONLY when you redistribute the font *files themselves*: self-hosting webfonts (`.woff2`/`.ttf`) on a site, or bundling fonts into an app/installer. Put the `OFL-*.txt` in the same folder as the fonts.
- **Do NOT add a license file** when: loading from the Google Fonts CDN (the default), or producing documents/exports (PDF, PNG, SVG, the business card) — the OFL does not bind documents created with the fonts.
- Never rename a modified font to "Cormorant" or "Schibsted Grotesk" (reserved names apply to derivatives).
- No attribution is required for normal use.

## Regenerating
`tokens.json` is the source of truth. After editing it run `python3 build_tokens.py` to rebuild `tokens/tokens.css`, `tokens/theme.css`, and the `:root` block + embedded JSON in `style-guide.html`. Do not hand-edit generated blocks.
