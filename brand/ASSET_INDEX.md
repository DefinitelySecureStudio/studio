# Definitely Secure brand asset index

Status: Proposed for v1.0 approval

Version: 1.0.0

Last updated: 2026-08-11

Use this page to locate canonical assets. Family manifests provide the complete file inventory, sizes, and SHA-256 digests.

## Quick selection

| Need | Asset | Notes |
| --- | --- | --- |
| Studio logo on a light surface | [`primary-light.svg`](../assets/brand/logos/primary/definitely-secure-primary-light.svg) | Default institutional mark |
| Studio header | [`studio-horizontal-light.svg`](../assets/brand/logos/studio/definitely-secure-studio-horizontal-light.svg) | Wide headers and repositories |
| Comic wordmark | [`comic-horizontal-light.svg`](../assets/brand/logos/comic/definitely-secure-comic-horizontal-light.svg) | Comic pages, covers, promotion |
| Comic episode footer | [`comic-footer-light.svg`](../assets/brand/logos/comic/definitely-secure-comic-footer-light.svg) | Minimum width 320px |
| Icon | [`prompt-mark-light.svg`](../assets/brand/logos/icon/definitely-secure-prompt-mark-light.svg) | Use small variant below 20px |
| Social avatar | [`social-avatar-dark.png`](../assets/brand/logos/social/definitely-secure-social-avatar-dark.png) | 1024px tile for common platforms |
| Browser icon | [`favicon.svg`](../assets/brand/logos/favicon/definitely-secure-favicon.svg) | ICO and PNG fallbacks are adjacent |
| Color reference | [`color-palette.png`](../assets/brand/colors/preview/definitely-secure-color-palette.png) | Visual aid; tokens are canonical |
| Typography reference | [`typography-specimen.png`](../assets/brand/typography/samples/definitely-secure-typography-specimen.png) | Display, body, dialogue, mono, SFX |
| Mobile typography proof | [`typography-mobile-test.png`](../assets/brand/typography/samples/definitely-secure-typography-mobile-test.png) | Final-size readability proof |

## Logo assets

Root: [`assets/brand/logos/`](../assets/brand/logos/)

- Complete manifest: [`manifest.json`](../assets/brand/logos/manifest.json)
- Usage rules: [logo guidelines](logo-guidelines.md)
- Rights: [`LICENSE.md`](../assets/brand/logos/LICENSE.md)
- Canonical source: [`source/definitely-secure-logo-master.svg`](../assets/brand/logos/source/definitely-secure-logo-master.svg)
- Reproducible builder: [`source/build_logo_assets.py`](../assets/brand/logos/source/build_logo_assets.py)

SVG is preferred for web and scalable layout. Use the supplied PDF for compatible print workflows and the supplied PNG only where vector upload is unavailable. Never create a production asset from a screenshot.

## Color assets

Root: [`assets/brand/colors/`](../assets/brand/colors/)

- Complete manifest: [`manifest.json`](../assets/brand/colors/manifest.json)
- Rules and palette: [color system](color-system.md)
- Contrast evidence: [accessibility contrast report](accessibility-contrast-report.md)
- Preview set: [`preview/`](../assets/brand/colors/preview/)
- Reproducible builder: [`source/build_color_assets.py`](../assets/brand/colors/source/build_color_assets.py)

Preview images illustrate intended use but never replace semantic tokens or contrast testing.

## Typography assets

Root: [`assets/brand/typography/`](../assets/brand/typography/)

- Complete manifest: [`manifest.json`](../assets/brand/typography/manifest.json)
- Rules: [typography system](typography.md)
- Font licensing: [`FONT-LICENSES.md`](../assets/brand/typography/FONT-LICENSES.md)
- Samples: [`samples/`](../assets/brand/typography/samples/)
- Glyph test: [`glyph-test-report.md`](../assets/brand/typography/glyph-test-report.md)
- Reproducible builder: [`source/build_typography_assets.py`](../assets/brand/typography/source/build_typography_assets.py)

Bundled font files are unchanged upstream TTFs. Preserve the `OFL.txt` beside each redistributed family.

## Design tokens

Root: [`brand/tokens/`](tokens/)

| File | Purpose |
| --- | --- |
| [`colors.json`](tokens/colors.json) | Canonical DTCG-compatible color tokens |
| [`colors.yaml`](tokens/colors.yaml) | YAML mirror of the color hierarchy |
| [`colors.css`](tokens/colors.css) | Raw and semantic color custom properties |
| [`typography.json`](tokens/typography.json) | Canonical DTCG-compatible typography roles and scale |
| [`typography.css`](tokens/typography.css) | Font faces, role variables, and utility examples |
| [`index.css`](tokens/index.css) | Single CSS import entry point |

## Version policy

All listed v1.0 families are released together with Brand Guide v1.0.0. A major version changes naming, identity, core geometry, or incompatible token meaning. A minor version adds an approved asset or compatible role. A patch version corrects documentation or exports without changing intended use.
