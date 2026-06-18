# Fonts & licensing

Both brand typefaces are licensed under the **SIL Open Font License 1.1 (OFL)** — free for personal and commercial use, including embedding.

- **Cormorant Garamond** — Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant). License: `OFL-CormorantGaramond.txt`.
- **Montserrat** — Copyright 2024 The Montserrat Project Authors (github.com/JulietaUla/Montserrat). License: `OFL-Montserrat.txt`.

## When you MUST include the OFL file

Only when you **redistribute the font files themselves** — e.g. self-hosting webfonts (`.woff2`/`.ttf`) on raml.ch, or bundling the font into an app/installer. In that case, keep the matching `OFL-*.txt` in the same folder as the fonts, and don't rename a modified font to "Cormorant" or "Montserrat".

## When you DON'T need it

- Loading fonts from the Google Fonts CDN (the default in `style-guide.html`).
- Documents/exports made with the fonts — PDFs, PNG/SVG graphics, the business card, social images. The OFL explicitly does not bind documents created with the font.

## Self-hosting (optional)

Drop the webfont files here next to the license files:

```
fonts/
  OFL-CormorantGaramond.txt
  OFL-Montserrat.txt
  CormorantGaramond-Medium.woff2   (add if self-hosting)
  Montserrat-Regular.woff2         (add if self-hosting)
  …
```

Get the files from Google Fonts (fonts.google.com) or the source repos linked above.
