# Definitely Secure logo guidelines

Status: Approved

Owner: Definitely Secure Studio

Asset version: 1.0.0

Last updated: 2026-08-11

## Logo rationale

The Definitely Secure **Prompt Mark** combines three ideas in one small silhouette:

- a speech bubble for comics, characters, and workplace conversation;
- a terminal prompt for technical fluency and work in progress; and
- a Status Gold indicator that says a system is reporting something—without guaranteeing that the report tells the whole story.

The open conversational shape feels more human than a shield or padlock. The prompt supplies technical character without hacker imagery, while the slightly detached status light introduces the brand’s central tension: confidence with a trace of uncertainty. The geometry remains recognizable at favicon and avatar sizes.

The Studio wordmark is upright and orderly. The comic wordmark is heavier and italic, bringing more motion and personality while retaining the same mark and palette. This makes the Studio and comic related without making the real producer look like the fictional company.

## Logo family

| Asset | Approved use | Preferred file |
| --- | --- | --- |
| Primary studio logo | Default institutional identification | `primary/definitely-secure-primary-light.svg` |
| Studio horizontal lockup | Wide headers, repository and partner pages | `studio/definitely-secure-studio-horizontal-light.svg` |
| Studio vertical lockup | Covers, title cards, narrow placements | `studio/definitely-secure-studio-vertical-light.svg` |
| Comic wordmark | Comic headers, series pages, covers, promotion | `comic/definitely-secure-comic-horizontal-light.svg` |
| Comic footer | Episode artwork with sufficient width | `comic/definitely-secure-comic-footer-light.svg` |
| Prompt Mark | Icon-only identification and compact ownership marks | `icon/definitely-secure-prompt-mark-light.svg` |
| Small Prompt Mark | Placements below 24 px | `icon/definitely-secure-prompt-mark-small.svg` |
| Social avatar | Instagram and other square profiles | `social/definitely-secure-social-avatar-dark.svg` |
| Production lockup | Opening/closing cards and partner credits | `studio/definitely-secure-production-lockup-light.svg` |
| Watermark | Subtle ownership marking over light imagery | `monochrome/definitely-secure-watermark.svg` |
| Favicon | Browser tabs and bookmarks | `favicon/definitely-secure-favicon.svg` or `favicon/favicon.ico` |

The unqualified word “primary” refers to the Studio lockup. Use the comic wordmark when the subject is the comic rather than the parent Studio.

## Core palette

| Name | Hex | Role |
| --- | --- | --- |
| Assurance Ink | `#101828` | Primary mark and text on light surfaces |
| Console Paper | `#F8FAFC` | Reverse mark and text on dark surfaces |
| Status Gold | `#F4B942` | Status indicator and comic accent only |
| Operations Slate | `#475467` | Secondary Studio descriptor |

Status Gold is an accent, never a substitute for text or the entire mark. Do not rely on it alone to communicate state or meaning. Light SVG variants have transparent backgrounds and use Assurance Ink; dark variants also have transparent backgrounds and use Console Paper.

## Clear space

Let **x** equal the diameter of the Prompt Mark’s Status Gold indicator.

- Keep at least `2x` clear on every side of an icon-only mark.
- Keep at least `3x` around Studio, comic, and production lockups.
- Keep at least `2x` between the mark and a trim, crop, panel border, speech bubble, or other logo.
- The built-in gap between the mark and wordmark is fixed; do not close or expand it manually.

Clear space may contain the background color or non-detailed image area, but no readable text, character face, border, or high-contrast graphic.

## Minimum sizes

| Asset | Digital minimum | Print minimum |
| --- | ---: | ---: |
| Prompt Mark, full color | 20 px | 6 mm |
| Small Prompt Mark | 16 px | 5 mm |
| Studio horizontal lockup | 180 px wide | 38 mm wide |
| Studio vertical lockup | 96 px wide | 25 mm wide |
| Comic wordmark | 200 px wide | 42 mm wide |
| Production lockup | 220 px wide | 48 mm wide |
| Comic footer | 320 px wide | 68 mm wide |

At 16–19 px, use only the small Prompt Mark. Do not use a wordmark, production lockup, status-light animation, or watermark at favicon size.

## Background usage

### Light surfaces

Use a `-light` asset on white, Console Paper, pale neutral colors, or imagery whose effective background is light and quiet. Assurance Ink must remain clearly distinguishable from the surface.

### Dark surfaces

Use a `-dark` asset on Assurance Ink, charcoal, dark blue, or quiet dark imagery. Console Paper provides the primary silhouette; Status Gold remains unchanged.

### Photography and comic artwork

Prefer a calm corner with sufficient contrast. If the art is busy, place the logo on a solid Assurance Ink or Console Paper holding shape that respects clear space. Do not add glow, shadow, stroke, or a semitransparent patch to rescue an unsuitable placement.

### Monochrome

Use the black-equivalent mark for one-color dark printing and the white-equivalent mark for reverse applications. In monochrome, the status light intentionally takes the same color as the internal prompt. Do not simulate gray or introduce another spot color.

## Social avatar, GitHub, favicon, and watermark

- **Primary social avatar:** `social/definitely-secure-social-avatar-dark.svg`; export or upload the supplied 1024 px PNG when SVG is unsupported.
- **GitHub organization avatar:** use the same dark social avatar so the organization is recognizable beside repositories at small size.
- **Light avatar:** reserve for dark platform chrome or campaigns that need a light tile.
- **Favicon:** prefer the SVG favicon where supported; provide 32 px PNG and `favicon.ico` fallbacks.
- **Watermark:** use only the supplied 22% opacity asset. Keep it small enough to identify ownership without competing with the comic. Do not use the watermark as a primary logo.

Platform masking can turn a square avatar into a circle. Keep the supplied artwork centered and do not crop inside its rounded tile.

## Approved combinations

- Prompt Mark + Studio wordmark + “STUDIO” descriptor
- Prompt Mark + comic wordmark and Status Gold underline
- Prompt Mark + “A Definitely Secure Studio production” credit
- Prompt Mark alone, when the brand is already clear from context
- Comic footer mark with the episode number and `DEFINITELYSECURE.COM`

Do not combine the comic wordmark with “STUDIO” to make an improvised Studio logo. Do not attach “Inc.,” “Comics,” “Press,” a product name, a character, or a sponsor directly to the mark.

## Incorrect use

Never:

1. stretch, squeeze, rotate, skew, or redraw the mark;
2. move, recolor, resize, or remove the Status Gold indicator;
3. change the words, casing, typography, tracking, or arrangement in a lockup;
4. put the light variant on a dark surface or the dark variant on a light surface;
5. use gradients, bevels, shadows, outlines, textures, or animation inside the logo;
6. place the logo over a character face, speech balloon, high-detail panel, or low-contrast image;
7. use the social tile as a footer mark or the watermark as an avatar;
8. pair the logo with a shield, padlock, hacker silhouette, or another symbol that changes its meaning;
9. recreate a PNG from a screenshot when an approved vector or high-resolution export exists; or
10. imply that Definitely Secure, the fictional company, produced real-world work.

## File naming and export standard

Vector filenames follow:

```text
definitely-secure-[asset]-[arrangement]-[surface].svg
```

Not every component applies to every asset. Use lowercase ASCII kebab case. Surface is `light`, `dark`, `black`, or `white`; it names the intended background, not an opaque background embedded in the file.

Raster exports use:

- `-transparent.png` for the standard transparent-background export;
- `-transparent@4x.png` for the high-resolution transparent export;
- `.png` and `@2x.png` for social tiles whose background is intentionally part of the design; and
- `-[size].png` for favicons and touch icons.

Do not append `final`, `new`, `latest`, or editor names. Release a new semantic asset version instead.

## Source, builds, and version metadata

The canonical design geometry and build process are stored in:

- `assets/brand/logos/source/build_logo_assets.py`
- `assets/brand/logos/source/definitely-secure-logo-master.svg`

Run the build script from any directory with `rsvg-convert` and macOS `sips` available:

```sh
python3 assets/brand/logos/source/build_logo_assets.py
```

The script regenerates SVG, standard PNG, high-resolution PNG, PDF, favicon, and `manifest.json` outputs. The manifest records asset version, byte size, and SHA-256 digest for every distributed file. Commit the source and generated outputs together. Version 1.0.0 is the first proposed public system; increment the major version for incompatible geometry or naming changes, the minor version for new approved lockups, and the patch version for export-only corrections.

## Ownership and licensing

Copyright © 2026 Definitely Secure Studio. All rights reserved.

The Prompt Mark, wordmarks, and lockups are proprietary brand assets. Repository access does not grant trademark, endorsement, merchandising, or adaptation rights. Definitely Secure Studio projects may use the assets according to this guide; third parties need prior written permission unless applicable law permits the use. Software and content licenses elsewhere in a repository do not override [`assets/brand/logos/LICENSE.md`](../assets/brand/logos/LICENSE.md).

## Release checklist

Before publishing a logo asset or placement, confirm:

1. The lockup identifies the Studio or comic correctly.
2. The surface variant provides strong contrast.
3. Clear space and minimum size meet this guide.
4. Geometry, color, wording, and proportions are unchanged.
5. The export filename follows the standard and appears in `manifest.json`.
6. SVG and PDF render without missing text or clipped geometry.
7. Transparent PNGs retain alpha and social tiles retain their intended background.
8. Ownership metadata and license files accompany redistributed source assets.
