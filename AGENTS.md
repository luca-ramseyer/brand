# AGENTS.md — Luca Ramseyer brand

Use this design system when building any UI, site, email, or graphic for the Luca Ramseyer / lram.ch personal brand. Keep it minimal and faithful; the identity is restraint, made of soft clay (v3.0).

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
- Spacing scale (px): 8 / 16 / 24 / 32 / 48 / 64 / 96. Radius: 14px controls, 24px cards, 32px panels, pill for chips/switches only. Nested radius = outer minus padding.
- Well `#ECE5D8` (dark `#161412`): the recessed ground for inputs, tracks, wells, code.

## Depth: soft clay (v3.0)
- Light comes from the top left. Use only the elevation tokens, never hand-written shadows:
  - `--raise-1` controls and chips, `--raise-2` cards and panels, `--raise-3` one hero object per page (usually the clay mark). Pair raised ivory surfaces with `--clay-body`: `box-shadow: var(--clay-body), var(--raise-2)`.
  - `--press` + `background: var(--well)` for inputs, wells, toggle tracks, code blocks, and buttons while `:active`.
  - `--sheen` on ink and red fills: `box-shadow: var(--sheen), var(--raise-1)`.
- Raised surfaces are `--surface` on `--paper`. Clay never adds a hue.
- No clay inside clay: inside a card use hairlines or a well.
- Type, icons, logos, tables and charts stay flat. Never shadow or emboss the wordmark.
- Signature: the segmented track (`.seg`): a pressed groove where the current item (`aria-current`) rises out. Use it for primary nav and view switches.
- The clay mark (red tile with `--sheen` + `--raise-3`, cross debossed with an SVG inner shadow) only at 64px and up, once per view. Below that, and in email, print, favicons: the flat mark.
- Leave ≥24px between raised surfaces so shadows never touch.
- Depth is never the only signal: keep labels, text and the focus outline. Add `@media (prefers-contrast: more)` that swaps shadows for 1px `--muted` borders.
- Email stays flat (mail clients drop shadows).
- Scoped themes (a dark panel inside a light page): re-declare `--raise-*`, `--press`, `--clay-body` inside the scope after the `--clay-*` overrides. CSS resolves `var()` inside custom properties where they are declared, so the `:root` values keep the light shadows otherwise.

## Defaults when building
- Plain web: link `tokens/tokens.css`, then use `var(--ink)`, `var(--serif)`, `var(--s4)`, etc.
- Tailwind v4: `@import "tailwindcss";` then `@import "./theme.css";` → utilities like `bg-surface rounded-card shadow-raise-2 text-ink text-h2 p-4` (`font-wordmark` for the wordmark).
- Webfonts: include the Google Fonts link from `tokens.json#font.googleImport`. Fallbacks are already in the font stacks.
- Layout: generous whitespace; centre hero content; left-align reading content in a ~920px column. Whitespace is the primary design element — when unsure, remove something.
- Components: clay surfaces per the depth rules, 48px controls, sentence-case 15px medium button labels, hairlines only inside cards. No hue gradients, no glows. Reference: `style-guide.html` (section 05–06). Ready-made CSS: https://pages.lram.ch/brand.css
- Motion: 200ms colour transitions naming their properties (never `transition: all`); `:active` press swaps the shadow to `--press` and `scale(0.98)` over 140ms; hover never lifts or grows; entrances under 500ms with `cubic-bezier(0.23, 1, 0.32, 1)`, transform/opacity only; respect `prefers-reduced-motion`. Visible `:focus-visible` outline.

## Mobile first (most visitors are on phones)
- Viewport: `width=device-width, initial-scale=1, viewport-fit=cover`. Never `user-scalable=no` or `maximum-scale=1`.
- Design the 360–430px single column first. No fixed widths; the page never scrolls sideways (wide tables/code/charts scroll in their own box).
- 16px side padding plus `env(safe-area-inset-*)` on edges and fixed elements.
- Touch targets ≥ 48×48px, 8px apart. Hover styles only inside `@media (hover: hover)`; nothing hover-only.
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
