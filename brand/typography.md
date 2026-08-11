# Definitely Secure typography system

Status: Approved

Owner: Definitely Secure Studio

Version: 1.0.0

Last updated: 2026-08-11

## System summary

| Role | Family | Approved styles | Primary use |
| --- | --- | --- | --- |
| Display | Barlow Condensed | SemiBold 600, Bold 700, ExtraBold 800 | Comic title, major headings, posters, promotion, merchandise |
| Body | Atkinson Hyperlegible | Regular 400, Italic 400, Bold 700, Bold Italic 700 | Websites, documentation, captions, long-form print |
| Dialogue | Atkinson Hyperlegible | Regular 400, Italic 400, Bold 700 | Speech balloons, thought balloons, short comic copy |
| Monospace | IBM Plex Mono | Regular 400, Italic 400, Medium 500, SemiBold 600 | Terminals, logs, code, identifiers, technical Easter eggs |
| Sound effects | Barlow Condensed custom treatment | Black Italic 900 | Sound effects and short expressive lettering |

The system uses three open-source families. Barlow Condensed provides compact, technically credible display lettering without superhero or novelty-comic styling. Atkinson Hyperlegible makes character recognition the priority for both continuous reading and dialogue. IBM Plex Mono provides authentic technical texture and clear punctuation without making the entire brand resemble a terminal.

## Hierarchy

### Display

Use Barlow Condensed ExtraBold for the comic title, campaign headlines, cover titles, and major page headings. Use Bold for ordinary headings and SemiBold for compact labels. The approved logo lockups use Barlow Condensed as their live-text source; distributed production exports remain the canonical logo artwork.

| Level | Family and weight | Digital size | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Hero/display | Barlow Condensed 800 | `clamp(48px, 7vw, 88px)` | 0.92 | `-0.01em` |
| H1 | Barlow Condensed 800 | `clamp(36px, 5vw, 64px)` | 0.98 | `-0.01em` |
| H2 | Barlow Condensed 700 | `clamp(28px, 3vw, 40px)` | 1.08 | `0` |
| H3 | Barlow Condensed 700 | 24px | 1.15 | `0` |
| Eyebrow/label | Barlow Condensed 600 | 14–16px | 1.2 | `0.025em` uppercase |

Keep headings short. Do not use condensed display type for paragraphs, legal copy, metadata, or dialogue.

### Body and documentation

Use Atkinson Hyperlegible Regular for continuous text, Bold for emphasis and labels, and true italics for titles, internal thought, terminology, or conventional emphasis. Never synthesize bold or italic styles.

| Context | Size | Line height | Measure |
| --- | ---: | ---: | ---: |
| Website body | 16px minimum; 18px preferred | 1.55 | 45–75 characters |
| Documentation | 16px minimum | 1.55–1.65 | 55–80 characters |
| Long-form print | 9.5–11pt | 1.35–1.5 | 50–75 characters |
| Caption | 15px minimum | 1.45 | 35–65 characters |
| Footnote/legal | 13px minimum digital; 8pt print | 1.45 | 45–80 characters |

Body tracking is zero. Do not tighten body copy to make it fit; edit, resize the container, or move content instead.

## Comic dialogue

Atkinson Hyperlegible Regular is the default dialogue face. It is not a conventional hand-lettering font; that restraint keeps the comic adult, readable, and distinct from superhero aesthetics. Character voice comes from writing, balloon shape, pacing, weight, and controlled scale rather than a different novelty font for each speaker.

- Set dialogue in sentence case by default. All caps is reserved for interfaces, labels, shouting, or a specific in-world convention.
- Target 16px minimum at final viewing size; 18–22px is preferred.
- For a 1080px-wide social export expected to display near 540 CSS pixels, set dialogue at 32–44 source pixels and verify the downsampled result at 360 CSS pixels.
- Use a 1.28–1.36 line height and zero tracking.
- Keep lines near 20–38 characters and balloons near two to five lines.
- Keep at least one cap-height of internal balloon padding; never let text touch the tail or outline.
- Center short dialogue blocks optically. Left-align longer explanations, lists, logs, or more than five lines.
- Use Bold for one short point of emphasis. Avoid bolding entire balloons.
- Use true Italic for quiet internal thought or ordinary title emphasis. Do not skew Regular.
- Use ellipses and em dashes consistently; do not add manual spaces around punctuation to imitate lettering.

When dialogue cannot remain readable at the intended crop, reduce copy before reducing type.

## Narration and captions

Narration uses Atkinson Hyperlegible Bold for a compact label followed by Regular text when needed. Use 15px minimum at final viewing size, 1.35–1.45 line height, and zero tracking. Caption Cream and other approved fields must retain the contrast combinations in the [color system](color-system.md).

Narration boxes use sentence case. Uppercase is acceptable for very short time or location labels such as “TEN MINUTES LATER,” with `0.02em` tracking and no more than one line.

## Terminal, logs, and code

IBM Plex Mono is the only approved family for code, logs, terminal sessions, identifiers, and technical Easter eggs.

- Use Regular 400 for code and logs, Medium 500 for prompts and selected values, and SemiBold 600 for very short labels.
- Use 14px minimum digital and 8.5pt minimum print; 15–16px is preferred for documentation.
- Use a 1.5–1.65 line height and zero tracking.
- Disable discretionary ligatures so source characters remain literal.
- Enable tabular figures and the slashed-zero feature where the renderer supports them.
- Preserve whitespace with real code formatting; never align code using repeated proportional spaces.
- Keep terminal text horizontal and unwarped. Authenticity comes from syntax and spacing, not glow, scanlines, or Matrix-green styling.
- Wrap long prose comments, not commands or identifiers. Provide horizontal scrolling in live interfaces when breaking code would change meaning.

Required differentiation test string:

```text
0 O 1 l I | / \  {} [] ()  <= != ==  --flag=value
```

The bundled font files contain every required character; the generated glyph report records shaping checks.

## Sound effects

Sound effects use Barlow Condensed Black Italic as a starting structure, then may receive custom vector lettering treatment. This is a style, not permission to distort ordinary headings.

- Use uppercase for short sounds: “PING,” “THUNK,” “BZZT.”
- Start with weight 900 italic and tracking from `-0.02em` to `0.02em`.
- Scale, rotate, outline, or stagger the completed word as a single illustration when the sound requires motion.
- Preserve counters and recognizable letter skeletons; test at the final social crop.
- Limit effects to two brand or scene colors plus Comic Ink unless the story requires otherwise.
- Keep the editable live-type source alongside any outlined or warped production version.
- Do not apply the SFX treatment to UI labels, captions, episode titles, or safety-critical text.

## Social graphics

Use Barlow Condensed ExtraBold for headlines and Atkinson Hyperlegible for supporting copy. On a 1080px square:

- headline: 72–120px, 0.9–1.0 line height;
- supporting copy: 32–44px, 1.3–1.45 line height;
- small credit: 24px minimum; and
- web address or call to action: Atkinson Bold, 28–36px.

Export once, then inspect the actual image at 360px wide. No required word may depend on platform captions to become legible.

## Merchandise and print

Use Barlow Condensed ExtraBold for large, short messages and Atkinson Hyperlegible Bold for secondary information. Avoid thin strokes, especially when screen printing, embroidering, engraving, or reducing to a small label. Convert final production lettering to outlines only in the printer-specific copy; retain live text in the Studio source.

Do not use IBM Plex Mono as decorative “tech texture” across an entire product. It is reserved for information that is actually technical or intentionally in-world.

## Letter spacing

| Treatment | Approved tracking |
| --- | --- |
| Barlow display sentence/title case | `-0.01em` to `0` |
| Barlow uppercase headings | `0` to `0.015em` |
| Barlow uppercase eyebrow labels | `0.025em` to `0.05em` |
| Atkinson body, captions, and dialogue | `0` |
| Atkinson short uppercase labels | `0.02em` maximum |
| IBM Plex Mono | `0` |
| Barlow SFX | `-0.02em` to `0.02em`, then optical adjustment |

Never use browser letter spacing to justify text. Do not exceed `0.05em` in ordinary brand typography.

## Fallback stacks

```css
--font-display: "Barlow Condensed", "Arial Narrow", "Roboto Condensed", sans-serif;
--font-body: "Atkinson Hyperlegible", "Segoe UI", Arial, sans-serif;
--font-dialogue: "Atkinson Hyperlegible", "Segoe UI", Arial, sans-serif;
--font-mono: "IBM Plex Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
--font-sfx: "Barlow Condensed", "Arial Narrow", Impact, sans-serif;
```

Fallbacks preserve category and approximate metrics, not exact composition. Never approve line breaks, balloon fit, or logo spacing using a fallback. Production artwork must load the selected font or use the canonical outlined export.

## CSS and assets

[`brand/tokens/typography.css`](tokens/typography.css) contains font-face declarations, role tokens, weights, responsive sizes, line heights, tracking, and utility examples. The web definitions load the untouched upstream TTF files directly. Modern browsers support TrueType webfonts, and retaining the original binaries avoids creating a modified webfont that could conflict with a Reserved Font Name.

The reproducible asset builder and source live under `assets/brand/typography/source/`. Generated samples and the asset manifest live beside them. Run:

```sh
python3 assets/brand/typography/source/build_typography_assets.py
```

## Licensing

All selected families are distributed under the SIL Open Font License 1.1. Commercial design, web use, print, document embedding, and app/software bundling are permitted under that license. The font software may be redistributed with projects when its license and copyright notice remain with it; it may not be sold by itself. Modified font software must follow the OFL’s naming and licensing requirements. IBM’s license declares “Plex” as a Reserved Font Name, so the Studio distributes and self-hosts the original IBM Plex Mono TTF files without conversion or subsetting.

No attribution line is required in ordinary comics, websites, merchandise, or documents. Keep the applicable `OFL.txt` beside every redistributed font family and preserve font metadata. See the complete [font licensing record](../assets/brand/typography/FONT-LICENSES.md).

Do not add another font family without a documented license review, glyph test, fallback, and sample update. Do not upload bundled font files to third-party generators whose terms claim ownership or prohibit licensed redistribution.

## Release checklist

1. Use the role token instead of naming a font directly when the medium supports tokens.
2. Load a real approved weight; do not synthesize bold, italic, or condensed forms.
3. Verify the final work at its actual mobile or print size.
4. Confirm dialogue and captions stay above their minimum sizes after cropping and downsampling.
5. Run the technical glyph string in every environment that displays code.
6. Preserve line breaks intentionally in balloons, headlines, and artwork.
7. Keep font licenses with redistributed font software.
8. Retain editable live text before creating printer-specific outlines.
9. Use canonical logo exports rather than retyping a logo lockup.
