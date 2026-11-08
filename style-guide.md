# Luca Ramseyer — Brand Guidelines (v1.1)

Systems · Cybersecurity · Software. A quiet, precise identity built on Swiss restraint: generous whitespace, a refined serif wordmark, one calm accent. When in doubt, remove something.

## 1. Wordmark & logo

- Primary logo: the name in **Cormorant Garamond Medium**, all caps, letter-spacing `0.24em`, with the tagline beneath in **Montserrat**.
- Tracking is part of the identity — never tighten it.
- Reversed lockup (paper text on ink) is allowed; the separator dots turn red.
- Clear space: keep the cap-height of the "L" clear on all sides. Minimum width ~32 mm print / ~180 px screen.
- Don't: tighten tracking, recolour the wordmark, stretch/distort, add shadows/effects, or place on busy backgrounds.

## 2. The mark (Swiss cross)

A muted-red rounded square with the cross knocked out so the surface shows through. Use the wordmark wherever space allows; use the mark only where the wordmark won't read (favicons, avatars, app icons).

- Cross geometry (fixed at any size): arm thickness 21.5% of the square, arm length 62%, corner radius 10%.
- On cream → cross is paper colour. On white → white. On ink → matches the field.

## 3. Colour

| Token | Role | HEX | RGB | CMYK |
|---|---|---|---|---|
| paper | primary surface / paper | `#F4EFE4` | 244 239 228 | 4 6 11 0 |
| surface | elevated panels / cards | `#FBF8F1` | 251 248 241 | 1 2 5 0 |
| ink | wordmark / headings | `#211F1C` | 33 31 28 | 40 30 30 100* |
| body | body text | `#423D37` | 66 61 55 | 0 0 0 82 |
| muted (Stone Text) | captions / secondary text, 4.8:1 AA | `#6F685D` | 111 104 93 | 0 6 16 56 |
| stone | non-text only: icons, disabled, charts (3.5:1) | `#857E72` | 133 126 114 | 0 5 14 48 |
| red | accent (sparingly) | `#C0473A` | 192 71 58 | 0 65 72 22 |
| red-deep | accent hover/pressed | `#A63B30` | 166 59 48 | 0 64 71 35 |
| line | hairline rules/borders | `#DAD2C4` | 218 210 196 | 0 4 10 15 |
| good (Sage) | positive / success, sparingly | `#5B7A52` | 91 122 82 | 25 0 33 52 |

Usage balance: paper dominates (~70%), ink for type (~20%), muted small (~5%), red a thin seasoning (~3%).
\* Ink prints as rich black **C40 M30 Y30 K100**. Official flag-red alternative for the mark: Pantone 485 (≈ `#D52B1E`). Body and Stone Text on paper clear WCAG AA; Stone (`#857E72`) is 3.5:1, so never use it for text.

**Dark mode** (follows `prefers-color-scheme`, from the mono-dark wallpapers): paper `#1C1A18`, surface `#24221F`, ink `#F4EFE4`, body `#CFC8BB`, muted `#A39B8E`, red `#DB6B5D`, red-deep `#E58478`, line `#36332E`, good `#8FAE85`. `tokens/tokens.css` switches automatically; never hardcode light-only colours.

**Charts**, in series order: ink `#211F1C`, red `#C0473A`, stone `#857E72`, sage `#5B7A52`, sand `#C9BFAE` (dark: `#F4EFE4`, `#DB6B5D`, `#A39B8E`, `#8FAE85`, `#5A554D`). Ink carries the main series; red marks only the one value that matters. Hairline gridlines, Stone Text labels, direct labels over legends.

## 4. Typography

- **Display:** Cormorant Garamond — 400 / 500 / 600 / italic. Headlines, wordmark (tracked, uppercase), pull quotes.
- **Text & UI:** Montserrat — 300 / 400 / 500 / 600. Body (400), labels & buttons (500, uppercase, tracked `0.14em`).
- Don't introduce a third family. Code may use the system monospace stack (`--mono`).

Type scale (px): display 56 · h1 40 · h2 30 · h3 21 · body 16 · small 13 · eyebrow 12.
Line-height: body 1.75, headings 1.15. Eyebrows: uppercase, tracked `0.22em`.

Webfonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
```

## 5. Web components

- Buttons: near-square (3px radius), uppercase tracked labels. Primary = ink fill / paper text; ghost = ink outline; accent = red (rare).
- Inputs: surface fill, hairline border, border turns ink on focus. Font size 16px so iOS does not zoom.
- Links: ink with a hairline underline, red on hover.
- Divider: hairline rules with a red middot — the recurring brand motif.
- Press: buttons scale to 0.97 on `:active` (140ms), so touch gets feedback the moment a finger lands. Touch targets at least 44×44px.
- Hover effects only inside `@media (hover: hover)`; phones leave faked hover stuck. Nothing may be visible only on hover.
- Motion: 200ms colour transitions; transitions name their properties (never `transition: all`). Entrances under 500ms with ease-out `cubic-bezier(0.23, 1, 0.32, 1)`, transform and opacity only. Respect `prefers-reduced-motion`.
- Focus: visible 2px ink outline on `:focus-visible`.
- No shadows, no gradients.
- Ready-made implementation of tokens + components (light and dark): https://pages.lram.ch/brand.css

## 6. Layout, spacing & mobile

Whitespace is the most important element. Centre hero content; left-align reading content within a ~920px column. Spacing scale (px): 8 / 16 / 24 / 32 / 48 / 64 / 96.

**Mobile first.** Most people meet the brand on a phone. Design the 360–430px layout first, then let it open up.

- One column at 360px; add columns with `min-width` queries or `repeat(auto-fit, minmax(240px, 1fr))`. No fixed widths.
- The page never scrolls sideways. Wide tables, code and charts scroll inside their own box.
- 16px side padding that respects the notch: `viewport-fit=cover` plus `env(safe-area-inset-*)`.
- Touch targets 44×44px at least, 8px apart. Nothing only on hover; tooltips also open on tap.
- Type: body 16px, nothing under 12px, h1 32–40px on phones. Form fields 16px.
- Never block zoom (`user-scalable=no`, `maximum-scale=1`).
- Full-height heroes use `100svh`, not `100vh`.
- One `theme-color` per colour scheme, matching the page ground.
- Test on a real phone; desktop emulation hides sticky hover, input zoom and safe areas.

## 7. Email

- Signature: small mark, hairline divider, name in Cormorant, role in tracked Montserrat, contact lines in Montserrat.
- Template: white or cream ground, wordmark, one accent button, thin footer rule. Text-first.

## 8. Social media

- Avatar: the Swiss-cross mark, or an "LR" monogram in Cormorant. (Files in `assets/`.)
- Banner: wordmark + tagline centred on cream. Sizes supplied: 1500×500 (X), 1584×396 (LinkedIn).
- Posts: cream ground, lots of air, Cormorant headline, small mark top-left.

## 9. Voice & tone

Calm, precise, expert. Do: lead with what changed and what it means; plain verbs (block, review, restore); be specific; keep it short. Don't: sell with fear, hide behind jargon, over-promise ("100% secure"), shout in caps.

## 10. Licensing & credits

Both typefaces are licensed under the **SIL Open Font License 1.1** — free for personal and commercial use, including embedding and modification.

- **Cormorant Garamond** — © 2015 The Cormorant Project Authors (Christian Thalmann / Catharsis Fonts). License: `fonts/OFL-CormorantGaramond.txt`.
- **Montserrat** — © 2024 The Montserrat Project Authors (Julieta Ulanovsky et al.). License: `fonts/OFL-Montserrat.txt`.

**When to ship the OFL file:** only when you redistribute the font *files* themselves — self-hosting webfonts or bundling them into an app. Keep the matching `OFL-*.txt` beside the fonts, and never rename a modified font to "Cormorant" or "Montserrat".

**When you don't need it:** Google Fonts CDN usage, and any document or export made with the fonts (PDF, PNG, SVG, the printed card). No attribution is required for normal use.

Colours (hex/RGB/CMYK), the layout, the wordmark, the cross mark, and the code are original to this brand and free to use and modify. "Pantone 485" is named only as a colour reference; the working values here are independent of Pantone's proprietary system.
