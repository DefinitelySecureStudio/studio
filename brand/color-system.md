# Definitely Secure color system

Status: Proposed

Owner: Definitely Secure Studio

Token version: 1.0.0

Last updated: 2026-08-11

## Principles

The Definitely Secure palette pairs a precise dark ink with warm, editorial accents. Assurance Ink provides technical confidence; Meeting Coral and Status Gold introduce workplace-comedy warmth; Protocol Violet and Signal Teal broaden the system without turning it into a generic neon cybersecurity palette.

Color supports hierarchy but never carries meaning alone. Text, icons, patterns, labels, and line work must preserve meaning in grayscale and for people with color-vision differences. Character colors are not promoted to brand tokens.

## Palette

### Brand primary

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Assurance Ink | `brand.primary.assurance-ink` | `#101828` | 16, 24, 40 | 220°, 43%, 11% | 60, 40, 0, 84 | Pantone 296 C approx. | Primary logo, headings, key text, dark surfaces Use with Console Paper or Neutral 50 for text. |
| Console Paper | `brand.primary.console-paper` | `#F8FAFC` | 248, 250, 252 | 210°, 40%, 98% | 2, 1, 0, 1 | No controlled match | Reverse logo, light surface, dark-mode foreground Use with Assurance Ink or Neutral 800–900. |

### Brand secondary

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Meeting Coral | `brand.secondary.meeting-coral` | `#D95D52` | 217, 93, 82 | 5°, 64%, 59% | 0, 57, 62, 15 | Pantone 7416 C approx. | Warm editorial accent, social graphics, callouts Decorative on light surfaces; use Assurance Ink for overlaid text. |
| Protocol Violet | `brand.secondary.protocol-violet` | `#6E62A6` | 110, 98, 166 | 251°, 28%, 52% | 34, 41, 0, 35 | Pantone 7676 C approx. | Secondary editorial accent, links on pale surfaces, focus Console Paper text passes AA but not AAA; prefer Assurance Ink when maximum contrast is needed. |

### Brand accent

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Status Gold | `brand.accent.status-gold` | `#F4B942` | 244, 185, 66 | 40°, 89%, 61% | 0, 24, 73, 4 | Pantone 7408 C approx. | Logo status light, highlights, emphasis, focus on dark Use Assurance Ink for text; never use gold text on white. |
| Signal Teal | `brand.accent.signal-teal` | `#2F7F79` | 47, 127, 121 | 176°, 46%, 34% | 63, 0, 5, 50 | Pantone 7475 C approx. | Charts, secondary emphasis, environmental detail Console Paper text passes AA; do not use as a success signal without a label. |

### Neutral

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Neutral 50 | `neutral.50` | `#F8FAFC` | 248, 250, 252 | 210°, 40%, 98% | 2, 1, 0, 1 | — | Light-mode page background Use Neutral 700–900 for text. |
| Neutral 100 | `neutral.100` | `#F2F4F7` | 242, 244, 247 | 216°, 24%, 96% | 2, 1, 0, 3 | — | Subtle surface and table stripe Use Neutral 700–900 for text. |
| Neutral 200 | `neutral.200` | `#E4E7EC` | 228, 231, 236 | 218°, 17%, 91% | 3, 2, 0, 7 | — | Divider on dark surfaces and disabled fill Not a text color on light backgrounds. |
| Neutral 300 | `neutral.300` | `#D0D5DD` | 208, 213, 221 | 217°, 16%, 84% | 6, 4, 0, 13 | — | Light-mode borders and controls Not a text color on white. |
| Neutral 400 | `neutral.400` | `#98A2B3` | 152, 162, 179 | 218°, 15%, 65% | 15, 9, 0, 30 | — | Placeholder and disabled content Not approved for normal text on light surfaces. |
| Neutral 500 | `neutral.500` | `#667085` | 102, 112, 133 | 221°, 13%, 46% | 23, 16, 0, 48 | — | Secondary iconography and large muted text Use only for large text on Neutral 50 or lighter. |
| Neutral 600 | `neutral.600` | `#475467` | 71, 84, 103 | 216°, 18%, 34% | 31, 18, 0, 60 | — | Secondary body text Passes AA on Neutral 50 and white. |
| Neutral 700 | `neutral.700` | `#344054` | 52, 64, 84 | 218°, 24%, 27% | 38, 24, 0, 67 | — | Strong secondary text Passes AAA on Neutral 50. |
| Neutral 800 | `neutral.800` | `#1D2939` | 29, 41, 57 | 214°, 33%, 17% | 49, 28, 0, 78 | — | Dark-mode surface and light-mode heading Use Neutral 50–200 for text when used as a surface. |
| Neutral 900 | `neutral.900` | `#101828` | 16, 24, 40 | 220°, 43%, 11% | 60, 40, 0, 84 | — | Primary text and deepest surface Use Console Paper or Neutral 50 for reverse text. |

### Status info

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Info | `status.info.base` | `#2F6FAD` | 47, 111, 173 | 210°, 57%, 43% | 73, 36, 0, 32 | — | Info icon, border, and chart mark Pair with a text label; not approved as small text on its surface. |
| Info Surface | `status.info.surface` | `#EAF2FA` | 234, 242, 250 | 210°, 62%, 95% | 6, 3, 0, 2 | — | Info message background Use Info Text for body copy. |
| Info Text | `status.info.text` | `#1D4E79` | 29, 78, 121 | 208°, 61%, 29% | 76, 36, 0, 53 | — | Info message text Passes AAA on Info Surface. |

### Status success

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Success | `status.success.base` | `#2F7D61` | 47, 125, 97 | 158°, 45%, 34% | 62, 0, 22, 51 | — | Success icon and border Pair with icon or text; do not encode success by color alone. |
| Success Surface | `status.success.surface` | `#E8F4EE` | 232, 244, 238 | 150°, 35%, 93% | 5, 0, 2, 4 | — | Success message background Use Success Text for body copy. |
| Success Text | `status.success.text` | `#205642` | 32, 86, 66 | 158°, 46%, 23% | 63, 0, 23, 66 | — | Success message text Passes AAA on Success Surface. |

### Status warning

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Warning | `status.warning.base` | `#B36B00` | 179, 107, 0 | 36°, 100%, 35% | 0, 40, 100, 30 | — | Warning icon and border Use Assurance Ink or Warning Text for nearby copy. |
| Warning Surface | `status.warning.surface` | `#FFF2D6` | 255, 242, 214 | 41°, 100%, 92% | 0, 5, 16, 0 | — | Warning message background Use Warning Text for body copy. |
| Warning Text | `status.warning.text` | `#704200` | 112, 66, 0 | 35°, 100%, 22% | 0, 41, 100, 56 | — | Warning message text Passes AAA on Warning Surface. |

### Status danger

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Danger | `status.danger.base` | `#B5474F` | 181, 71, 79 | 356°, 44%, 49% | 0, 61, 56, 29 | — | Danger icon, border, and destructive control Console Paper is reserved for large or bold control text; use Danger Text on pale surfaces. |
| Danger Surface | `status.danger.surface` | `#FBEAEC` | 251, 234, 236 | 353°, 68%, 95% | 0, 7, 6, 2 | — | Danger message background Use Danger Text for body copy. |
| Danger Text | `status.danger.text` | `#7A2730` | 122, 39, 48 | 353°, 52%, 32% | 0, 68, 61, 52 | — | Danger message text Passes AAA on Danger Surface. |

### Comic

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Panel Mist | `comic.panel-background` | `#E8EEEF` | 232, 238, 239 | 189°, 18%, 92% | 3, 0, 0, 6 | — | Default comic panel field Use Comic Ink for dialogue and line work. |
| Breakroom Paper | `comic.panel-alternate` | `#F3E9DC` | 243, 233, 220 | 34°, 49%, 91% | 0, 4, 9, 5 | — | Warm alternate panel or flashback field Use Comic Ink for text; do not use as Cavapoo fur. |
| Comic Ink | `comic.border` | `#101828` | 16, 24, 40 | 220°, 43%, 11% | 60, 40, 0, 84 | — | Panel borders, line work, and primary lettering Passes AAA on all approved comic fields. |
| Speech White | `comic.speech-bubble` | `#FFFFFF` | 255, 255, 255 | 0°, 0%, 100% | 0, 0, 0, 0 | — | Speech balloons and clean negative space Use Comic Ink; outline balloons on pale panels. |
| Caption Cream | `comic.caption` | `#F5E6B8` | 245, 230, 184 | 45°, 75%, 84% | 0, 6, 25, 4 | — | Narration and caption boxes Use Comic Ink; not approved for white text. |
| Gutter Gray | `comic.gutter` | `#D0D5DD` | 208, 213, 221 | 217°, 16%, 84% | 6, 4, 0, 13 | — | Panel gutters and quiet separators Not approved for body text. |

### Environment

| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cubicle Mist | `environment.wall` | `#DCE5E8` | 220, 229, 232 | 195°, 21%, 89% | 5, 1, 0, 9 | — | Office walls and broad background planes Keep character silhouettes outlined in Comic Ink. |
| Conference Glass | `environment.glass` | `#BFD9D7` | 191, 217, 215 | 175°, 25%, 80% | 12, 0, 1, 15 | — | Glass, windows, and reflective dividers Do not use as text or a status signal. |
| Desk Bluegray | `environment.desk` | `#AABAC0` | 170, 186, 192 | 196°, 15%, 71% | 11, 3, 0, 25 | — | Desks, cabinets, and office fixtures Use Comic Ink for detail lines. |
| Carpet Slate | `environment.carpet` | `#596274` | 89, 98, 116 | 220°, 13%, 40% | 23, 16, 0, 55 | — | Carpet and deep environmental planes Console Paper passes AA for text when necessary. |
| Monitor Blue | `environment.screen` | `#26384A` | 38, 56, 74 | 210°, 32%, 22% | 49, 24, 0, 71 | — | Inactive monitors and dark equipment Use Console Paper or Status Gold for readable content. |

## Light mode

Use Neutral 50 for the page, Speech White for raised surfaces, Neutral 900 for primary text, Neutral 600 for secondary text, and Neutral 300 for borders. Primary controls use Assurance Ink with Console Paper. Links use Info Text and remain underlined in body copy. Protocol Violet is the focus-ring color; focus must also have a visible shape, not color alone.

Approved light-mode text pairs are recorded in the [contrast report](accessibility-contrast-report.md). Do not use Neutral 400 or lighter for readable text, Meeting Coral as body text, Status Gold on white, or white text on Status Gold.

## Dark mode

Use Assurance Ink for the page, Neutral 800 for raised surfaces, Neutral 700 for subtle surfaces, Console Paper for primary text, and Neutral 200 for secondary text. Dark-mode primary controls use Status Gold with Assurance Ink text. Conference Glass is the standard dark-mode link color; underlines remain required in body copy.

Dark logo variants contain Console Paper shapes and transparent backgrounds. Place them only on Assurance Ink, Neutral 800, Monitor Blue, or another tested dark field. Never place a dark variant on a light surface simply because its filename contains the word `dark`; the suffix names the intended surface.

## Comic usage

Panel Mist is the default environment-neutral field. Breakroom Paper introduces warmth for alternate scenes and memory without borrowing the Cavapoo’s coat. Speech White balloons and Caption Cream boxes always use Comic Ink lettering and a visible outline when adjacent values are close. Panel borders, dialogue, and essential detail remain Comic Ink so a comic stays legible without color.

Environment tokens are intentionally cool and muted. They may shift for lighting and story needs, but recurring props should begin from these values. Status colors can appear inside fictional interfaces only when the interface also uses text, shape, or icon labels; a green or red dot alone is not sufficient storytelling information.

## Cavapoo separation

The Cavapoo’s reference coat colors—caramel around `#B9855A` and warm white around `#FFFDF8`—are character colors, not brand or environment tokens. Do not reuse either value for buttons, status, panel fields, furniture, or large social backgrounds. Place warm-white fur against Panel Mist, Cubicle Mist, Carpet Slate, or another cool field, and retain Comic Ink outlines. Place caramel fur away from Meeting Coral and Breakroom Paper when their values would merge; use cool environment tokens between them.

## Status usage

Each status has a base, surface, and text token. The base is for icons and borders, the surface is for the message field, and the text token is for copy. Every status component also needs a word or recognizable icon. Status Gold belongs to the brand and warning-adjacent emphasis but is not the semantic warning token; `status.warning.*` is darker and tested for interface use.

## Approved combinations

- Assurance Ink on Console Paper, Neutral 50, Speech White, Panel Mist, Breakroom Paper, or Caption Cream
- Console Paper on Assurance Ink, Neutral 800, Monitor Blue, Signal Teal, or Carpet Slate
- Assurance Ink on Status Gold and Meeting Coral for display elements and controls
- Each status text token on its matching status surface
- The light logo on light approved surfaces and the dark logo on approved dark surfaces

Always consult the numerical [accessibility contrast report](accessibility-contrast-report.md) for text size and conformance details.

## Prohibited combinations

- Status Gold text on Console Paper, Speech White, Neutral 50, Caption Cream, or Warning Surface
- Console Paper body text on Status Gold, Meeting Coral, or Protocol Violet
- Meeting Coral against Danger without a border and explicit label
- Signal Teal as an unlabeled synonym for success
- Neutral 400 or lighter as normal text on a light surface
- Neutral 500 or darker as normal text on a dark surface
- Brand accents used simultaneously in equal proportions
- Gradients inside approved logos or status components
- Caramel and warm-white Cavapoo coat references reused as UI or brand tokens

## Print guidance

CMYK values in this guide are mathematical approximations for coated stock, not press-ready guarantees. Convert through the printer’s ICC profile, request a contract proof, and adjust for paper, ink, and finish. Pantone references are visual starting points only; they are not licensed digital definitions or exact matches.

For one-color printing, use Assurance Ink or the approved monochrome logo. On uncoated stock, expect Status Gold and Meeting Coral to lose saturation; proof both next to Comic Ink line work. Rich black is not approved for small type or comic outlines—use a single-channel press black chosen with the printer. Maintain at least 0.25 pt for positive rules and 0.5 pt for reversed rules.

## Machine-readable tokens

- [`brand/tokens/colors.json`](tokens/colors.json) uses Design Tokens Community Group-compatible `$type` and `$value` fields plus Studio metadata.
- [`brand/tokens/colors.yaml`](tokens/colors.yaml) mirrors the JSON hierarchy.
- [`brand/tokens/colors.css`](tokens/colors.css) provides raw `--ds-*` variables and semantic light/dark theme variables.

Raw palette tokens describe stable colors. Semantic `--ds-color-*` variables should be used by interfaces whenever a role exists, because their values change by theme.

## Visual examples

- [`assets/brand/colors/preview/definitely-secure-color-palette.png`](../assets/brand/colors/preview/definitely-secure-color-palette.png)
- [`assets/brand/colors/preview/definitely-secure-light-mode-example.png`](../assets/brand/colors/preview/definitely-secure-light-mode-example.png)
- [`assets/brand/colors/preview/definitely-secure-dark-mode-example.png`](../assets/brand/colors/preview/definitely-secure-dark-mode-example.png)
- [`assets/brand/colors/preview/definitely-secure-comic-panel-example.png`](../assets/brand/colors/preview/definitely-secure-comic-panel-example.png)
- [`assets/brand/colors/preview/definitely-secure-social-post-example.png`](../assets/brand/colors/preview/definitely-secure-social-post-example.png)

## Release checklist

1. Use a semantic token when one exists instead of copying a raw HEX value.
2. Confirm text pairs against the current contrast report at the actual size and weight.
3. Preserve a non-color cue for status, links, selection, and chart meaning.
4. Test light mode, dark mode, grayscale, and a representative color-vision simulation.
5. Confirm the selected logo surface variant passes the background rules.
6. Keep Cavapoo coat colors outside brand, status, and environment token roles.
7. Proof CMYK and spot-color output on the intended stock before production.
