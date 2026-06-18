# Luca Ramseyer — Brand Guidelines

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
| muted | captions / secondary | `#857E72` | 133 126 114 | 0 5 14 48 |
| red | accent (sparingly) | `#C0473A` | 192 71 58 | 0 65 72 22 |
| red-deep | accent hover/pressed | `#A63B30` | 166 59 48 | 0 64 71 35 |
| line | hairline rules/borders | `#DAD2C4` | 218 210 196 | 0 4 10 15 |

Usage balance: paper dominates (~70%), ink for type (~20%), muted small (~5%), red a thin seasoning (~3%).
\* Ink prints as rich black **C40 M30 Y30 K100**. Official flag-red alternative for the mark: Pantone 485 (≈ `#D52B1E`). Body-on-paper clears WCAG AA.

## 4. Typography

- **Display:** Cormorant Garamond — 400 / 500 / 600 / italic. Headlines, wordmark (tracked, uppercase), pull quotes.
- **Text & UI:** Montserrat — 300 / 400 / 500 / 600. Body (400), labels & buttons (500, uppercase, tracked `0.14em`).
- Don't introduce a third family.

Type scale (px): display 56 · h1 40 · h2 30 · h3 21 · body 16 · small 13 · eyebrow 12.
Line-height: body 1.75, headings 1.15. Eyebrows: uppercase, tracked `0.22em`.

Webfonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
```

## 5. Web components

- Buttons: near-square (3px radius), uppercase tracked labels. Primary = ink fill / paper text; ghost = ink outline; accent = red (rare).
- Inputs: surface fill, hairline border, border turns ink on focus.
- Links: ink with a hairline underline, red on hover.
- Divider: hairline rules with a red middot — the recurring brand motif.
- Motion: 200ms colour transitions only. No shadows, no gradients.

## 6. Layout & spacing

Whitespace is the most important element. Centre hero content; left-align reading content within a ~920px column. Spacing scale (px): 8 / 16 / 24 / 32 / 48 / 64 / 96.

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
