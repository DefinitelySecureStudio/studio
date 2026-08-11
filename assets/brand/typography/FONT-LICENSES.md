# Definitely Secure font licensing record

Reviewed: 2026-08-11

This record covers the exact font software bundled in `assets/brand/typography/fonts/`. It is an operational inventory, not legal advice.

## Rights summary

All three families use the SIL Open Font License 1.1. The OFL permits commercial and noncommercial use, modification, bundling, embedding, and redistribution, subject to the license terms. Font software may not be sold by itself. The license and copyright notice must accompany redistributed font software. Documents and artwork made with the fonts are not required to use the OFL. Modified fonts must remain under OFL and must respect any Reserved Font Names declared in their license.

| Family | Role | License | Commercial design | Webfont | Print/PDF embedding | App/software embedding | Redistribution | Required attribution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Barlow Condensed | Display and SFX | SIL OFL 1.1 | Permitted | Permitted | Permitted | Permitted | Permitted with OFL and copyright notice; not sold alone | None in ordinary artwork; retain OFL with font files |
| Atkinson Hyperlegible | Body and dialogue | SIL OFL 1.1 | Permitted | Permitted | Permitted | Permitted | Permitted with OFL and copyright notice; not sold alone | None in ordinary artwork; retain OFL with font files |
| IBM Plex Mono | Code and terminal | SIL OFL 1.1 | Permitted | Permitted | Permitted | Permitted | Permitted with OFL and copyright notice; not sold alone | None in ordinary artwork; retain OFL with font files |

## Barlow Condensed

- **Copyright holder:** The Barlow Project Authors.
- **License file:** [`fonts/barlow-condensed/OFL.txt`](fonts/barlow-condensed/OFL.txt)
- **Canonical upstream:** [jpt/barlow](https://github.com/jpt/barlow)
- **Distribution source:** [Google Fonts Barlow Condensed directory](https://github.com/google/fonts/tree/main/ofl/barlowcondensed)
- **Bundled weights:** SemiBold 600, Bold 700, ExtraBold 800, Black Italic 900.
- **Restrictions:** Keep the OFL with redistributed font software. Do not sell the font files alone. Review the license before renaming or distributing modified versions.

## Atkinson Hyperlegible

- **Copyright holder:** Braille Institute of America, Inc.
- **License file:** [`fonts/atkinson-hyperlegible/OFL.txt`](fonts/atkinson-hyperlegible/OFL.txt)
- **Canonical upstream:** [googlefonts/atkinson-hyperlegible](https://github.com/googlefonts/atkinson-hyperlegible)
- **Distribution source:** [Google Fonts Atkinson Hyperlegible directory](https://github.com/google/fonts/tree/main/ofl/atkinsonhyperlegible)
- **Bundled weights:** Regular 400, Italic 400, Bold 700, Bold Italic 700.
- **Restrictions:** Keep the OFL with redistributed font software. Do not sell the font files alone. Review the license before renaming or distributing modified versions.

## IBM Plex Mono

- **Copyright holder:** IBM Corp.
- **License file:** [`fonts/ibm-plex-mono/OFL.txt`](fonts/ibm-plex-mono/OFL.txt)
- **Canonical upstream:** [IBM/plex](https://github.com/IBM/plex)
- **Distribution source:** [Google Fonts IBM Plex Mono directory](https://github.com/google/fonts/tree/main/ofl/ibmplexmono)
- **Bundled weights:** Regular 400, Italic 400, Medium 500, SemiBold 600.
- **Restrictions:** Keep the OFL with redistributed font software. Do not sell the font files alone. “Plex” is a Reserved Font Name; do not convert, subset, rename, or otherwise modify the files for distribution under that name without confirming OFL compliance.

## Operational rules

1. Keep each `OFL.txt` in the same family directory as the TTF and WOFF2 files.
2. Preserve copyright and naming metadata in unmodified files.
3. Do not convert, subset, rename, or modify a family for distribution without reviewing OFL Reserved Font Name requirements.
4. Web CSS loads the original upstream TTF binaries. Do not introduce generated WOFF/WOFF2 files without verifying that the conversion preserves original font data and metadata as required by the OFL FAQ.
5. When providing editable production packages to printers, agencies, or contractors, include this record and the relevant family license.
6. Do not commit proprietary substitutes or desktop-license-only fonts to this repository.
