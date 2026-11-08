# Fonts & licensing

Both brand typefaces are licensed under the **SIL Open Font License 1.1 (OFL)**: free for personal and commercial use, including embedding.

- **Schibsted Grotesk** (headings, body, UI): Copyright 2023 The Schibsted-Grotesk Project Authors (github.com/schibsted/schibsted-grotesk). License: `OFL-SchibstedGrotesk.txt`.
- **Cormorant Garamond** (wordmark and monogram only): Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant). License: `OFL-CormorantGaramond.txt`.

Older exported assets (banners, wallpapers) were set with Montserrat before v2.0. Exported images need no licence file.

## When you MUST include the OFL file

Only when you **redistribute the font files themselves**, e.g. self-hosting webfonts (`.woff2`/`.ttf`) on lram.ch or bundling a font into an app. Keep the matching `OFL-*.txt` in the same folder as the fonts, and don't rename a modified font to "Cormorant" or "Schibsted Grotesk".

## When you DON'T need it

- Loading fonts from the Google Fonts CDN (the default).
- Documents and exports made with the fonts: PDFs, PNG/SVG graphics, the business card, social images.

## Self-hosting (optional)

```
fonts/
  OFL-CormorantGaramond.txt
  OFL-SchibstedGrotesk.txt
  CormorantGaramond-Medium.woff2      (add if self-hosting)
  SchibstedGrotesk-Variable.woff2     (add if self-hosting)
```
