# Luca Ramseyer — Brand Guidelines (v3.0, soft clay)

Systems · Cybersecurity · Software. A quiet, precise identity built on Swiss restraint: generous whitespace, a clean modern grotesk, a refined serif wordmark, one calm accent, and surfaces made of soft clay lit from the top left. When in doubt, remove something.

## 1. Wordmark & logo

- Primary logo: the name in **Cormorant Garamond Medium**, all caps, letter-spacing `0.24em`, with the tagline beneath in **Schibsted Grotesk**.
- Tracking is part of the identity — never tighten it.
- Reversed lockup (paper text on ink) is allowed; the separator dots turn red.
- Clear space: keep the cap-height of the "L" clear on all sides. Minimum width ~32 mm print / ~180 px screen.
- Don't: tighten tracking, recolour the wordmark, stretch/distort, add shadows/effects, or place on busy backgrounds.

## 2. The mark (Swiss cross)

A muted-red rounded square with the cross knocked out so the surface shows through. Use the wordmark wherever space allows; use the mark only where the wordmark won't read (favicons, avatars, app icons).

- Cross geometry (fixed at any size): arm thickness 21.5% of the square, arm length 62%, corner radius 10%.
- On cream → cross is paper colour. On white → white. On ink → matches the field.
- Two finishes, one geometry. **Flat** for favicons, app icons, print, email and anything under 64px. **Clay** (red tile with `--sheen` + `--raise-3`, cross debossed with a soft inner shadow) as the one rich object on a page, 64px and up, once per view. The clay finish adds light, never shape.

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
| line | hairline rules inside cards | `#DAD2C4` | 218 210 196 | 0 4 10 15 |
| well | pressed ground: inputs, tracks, wells | `#ECE5D8` | 236 229 216 | 5 8 14 0 |
| good (Sage) | positive / success, sparingly | `#5B7A52` | 91 122 82 | 25 0 33 52 |

Usage balance: paper dominates (~70%), ink for type (~20%), muted small (~5%), red a thin seasoning (~3%).
\* Ink prints as rich black **C40 M30 Y30 K100**. Official flag-red alternative for the mark: Pantone 485 (≈ `#D52B1E`). Body and Stone Text on paper clear WCAG AA; Stone (`#857E72`) is 3.5:1, so never use it for text.

**Dark mode** (follows `prefers-color-scheme`, from the mono-dark wallpapers): paper `#1C1A18`, surface `#24221F`, ink `#F4EFE4`, body `#CFC8BB`, muted `#A39B8E`, red `#DB6B5D`, red-deep `#E58478`, line `#36332E`, good `#8FAE85`, well `#161412`. Dark clay is lit the same way: a faint warm highlight up-left, a deep shadow down-right. `tokens/tokens.css` switches automatically; never hardcode light-only colours.

**Charts**, in series order: ink `#211F1C`, red `#C0473A`, stone `#857E72`, sage `#5B7A52`, sand `#C9BFAE` (dark: `#F4EFE4`, `#DB6B5D`, `#A39B8E`, `#8FAE85`, `#5A554D`). Ink carries the main series; red marks only the one value that matters. Hairline gridlines, Stone Text labels, direct labels over legends.

## 4. Typography

- **Schibsted Grotesk** (400 / 500 / 600) does all the work: headlines, body, labels, buttons, data. Headlines medium 500, tracked `-0.02em` (display `-0.03em`), sentence case. Tabular figures only in aligned columns such as tables; prices and stats use default figures.
- **Cormorant Garamond** Medium is the signature only: the wordmark and the LR monogram. Never headings or body.
- Don't introduce a third family. Code may use the system monospace stack (`--mono`).

Type scale (px): display 56 · h1 44 · h2 28 · h3 19 (600) · body 16 · small 13 · label 12.
Line-height: body 1.6, headings 1.1. Labels/eyebrows: 12px, 500, uppercase, tracked `0.08em`; use sparingly. Buttons are sentence case, not uppercase.

Webfonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500&family=Schibsted+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
```

## 5. Depth & clay

Everything is made of the same clay as the page. Light comes from the top left: raised surfaces catch a highlight up-left and cast a warm shadow down-right; pressed surfaces invert it. Use the tokens, never hand-written shadows.

| Token | Use |
|---|---|
| `--raise-1` | controls, chips |
| `--raise-2` | cards, panels |
| `--raise-3` | one hero object per page (the clay mark) |
| `--press` | inputs, wells, tracks, code, buttons while held (on `--well`) |
| `--clay-body` | soft inner rim, paired with any raise on ivory |
| `--sheen` | the same for ink and red fills |

- Raised = `--surface` on `--paper`. Clay never adds a hue.
- No clay inside clay: inside a card, use hairlines or a well.
- Type, icons, logos, tables and charts stay flat. Never emboss the wordmark.
- ≥24px between raised surfaces so shadows never touch.
- Depth is never the only signal. With `prefers-contrast: more` or forced colours, shadows give way to 1px borders.
- Email, print, favicons and social image files stay flat.
- Radius: 14px controls, 24px cards, 32px panels, pills for chips and switches only. Nested radius = outer minus padding.

## 6. Web components

- Buttons: 48px, 14px corners, sentence-case 15px medium labels. Primary = ink with sheen; secondary = ivory clay; accent = red with sheen (rare).
- Cards and panels: ivory, 24px corners, `--clay-body` + `--raise-2`, no border.
- Inputs: `--well` fill, `--press`, hairline border, 2px ink focus outline. Font size 16px so iOS does not zoom.
- Segmented track (the signature): a pressed groove where the current item (`aria-current`) rises out. Primary nav and view switches.
- Chips: pill, ivory, `--raise-1`. Switches: pressed track, raised knob, red when on.
- Links: flat, ink with a hairline underline, red on hover.
- Divider: hairline rules with a red middot — the recurring brand motif.
- Press: on `:active` the shadow swaps to `--press` and the control scales to 0.98 (140ms). Touch targets at least 48×48px.
- Hover changes colour only, inside `@media (hover: hover)`. Nothing lifts or grows. Nothing may be visible only on hover.
- Motion: transitions name their properties (`box-shadow`, `transform`, `color`; never `transition: all`). Entrances under 500ms with ease-out `cubic-bezier(0.23, 1, 0.32, 1)`, transform and opacity only. Respect `prefers-reduced-motion`.
- Focus: visible 2px ink outline on `:focus-visible`.
- No hue gradients, no glows, no coloured shadows.
- Ready-made implementation of tokens + components (light and dark): https://pages.lram.ch/brand.css

## 7. Layout, spacing & mobile

Whitespace is the most important element. Centre hero content; left-align reading content within a ~920px column. Spacing scale (px): 8 / 16 / 24 / 32 / 48 / 64 / 96.

**Mobile first.** Most people meet the brand on a phone. Design the 360–430px layout first, then let it open up.

- One column at 360px; add columns with `min-width` queries or `repeat(auto-fit, minmax(240px, 1fr))`. No fixed widths.
- The page never scrolls sideways. Wide tables, code and charts scroll inside their own box.
- 16px side padding that respects the notch: `viewport-fit=cover` plus `env(safe-area-inset-*)`.
- Touch targets 48×48px at least, 8px apart. Card padding drops to 24px; raise-2 is enough on phones, keep raise-3 for the hero mark. Nothing only on hover; tooltips also open on tap.
- Type: body 16px, nothing under 12px, h1 32–40px on phones. Form fields 16px.
- Never block zoom (`user-scalable=no`, `maximum-scale=1`).
- Full-height heroes use `100svh`, not `100vh`.
- One `theme-color` per colour scheme, matching the page ground.
- Test on a real phone; desktop emulation hides sticky hover, input zoom and safe areas.

## 8. Email

- Signature: small mark, hairline divider, name and role in Schibsted Grotesk, contact lines below.
- Template: white or cream ground, wordmark, one ink button, thin footer rule. Text-first. Email stays flat: mail clients drop shadows.

## 9. Social media

- Avatar: the clay mark on an ivory disc, or an "LR" monogram in Cormorant. (Files in `assets/` are still the flat v2 set.)
- Banner: wordmark + tagline centred on cream. Sizes supplied: 1500×500 (X), 1584×396 (LinkedIn).
- Posts: cream ground, lots of air, Schibsted Grotesk medium headline, small mark top-left.

## 10. Voice & tone

Calm, precise, expert. Do: lead with what changed and what it means; plain verbs (block, review, restore); be specific; keep it short. Don't: sell with fear, hide behind jargon, over-promise ("100% secure"), shout in caps.

## 11. Licensing & credits

Both typefaces are licensed under the **SIL Open Font License 1.1** — free for personal and commercial use, including embedding and modification.

- **Cormorant Garamond** — © 2015 The Cormorant Project Authors (Christian Thalmann / Catharsis Fonts). License: `fonts/OFL-CormorantGaramond.txt`.
- **Schibsted Grotesk** — © 2023 The Schibsted-Grotesk Project Authors. License: `fonts/OFL-SchibstedGrotesk.txt`.

**When to ship the OFL file:** only when you redistribute the font *files* themselves — self-hosting webfonts or bundling them into an app. Keep the matching `OFL-*.txt` beside the fonts, and never rename a modified font to "Cormorant" or "Schibsted Grotesk".

**When you don't need it:** Google Fonts CDN usage, and any document or export made with the fonts (PDF, PNG, SVG, the printed card). No attribution is required for normal use.

Colours (hex/RGB/CMYK), the layout, the wordmark, the cross mark, and the code are original to this brand and free to use and modify. "Pantone 485" is named only as a colour reference; the working values here are independent of Pantone's proprietary system.
