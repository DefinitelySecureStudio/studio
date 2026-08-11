#!/usr/bin/env python3
"""Build Definitely Secure color tokens, documentation, reports, and previews."""

from __future__ import annotations

import colorsys
import hashlib
import json
import math
import shutil
import subprocess
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path


VERSION = "1.0.0"
REPO = Path(__file__).resolve().parents[4]
ROOT = Path(__file__).resolve().parents[1]
TOKENS_DIR = REPO / "brand/tokens"
PREVIEW_DIR = ROOT / "preview"
FONT = "Arial, Helvetica, sans-serif"


@dataclass(frozen=True)
class Color:
    name: str
    token: str
    hex: str
    usage: str
    accessibility: str
    pantone: str = "—"


COLORS: dict[str, list[Color]] = {
    "Brand primary": [
        Color("Assurance Ink", "brand.primary.assurance-ink", "#101828", "Primary logo, headings, key text, dark surfaces", "Use with Console Paper or Neutral 50 for text.", "Pantone 296 C approx."),
        Color("Console Paper", "brand.primary.console-paper", "#F8FAFC", "Reverse logo, light surface, dark-mode foreground", "Use with Assurance Ink or Neutral 800–900.", "No controlled match"),
    ],
    "Brand secondary": [
        Color("Meeting Coral", "brand.secondary.meeting-coral", "#D95D52", "Warm editorial accent, social graphics, callouts", "Decorative on light surfaces; use Assurance Ink for overlaid text.", "Pantone 7416 C approx."),
        Color("Protocol Violet", "brand.secondary.protocol-violet", "#6E62A6", "Secondary editorial accent, links on pale surfaces, focus", "Console Paper text passes AA but not AAA; prefer Assurance Ink when maximum contrast is needed.", "Pantone 7676 C approx."),
    ],
    "Brand accent": [
        Color("Status Gold", "brand.accent.status-gold", "#F4B942", "Logo status light, highlights, emphasis, focus on dark", "Use Assurance Ink for text; never use gold text on white.", "Pantone 7408 C approx."),
        Color("Signal Teal", "brand.accent.signal-teal", "#2F7F79", "Charts, secondary emphasis, environmental detail", "Console Paper text passes AA; do not use as a success signal without a label.", "Pantone 7475 C approx."),
    ],
    "Neutral": [
        Color("Neutral 50", "neutral.50", "#F8FAFC", "Light-mode page background", "Use Neutral 700–900 for text."),
        Color("Neutral 100", "neutral.100", "#F2F4F7", "Subtle surface and table stripe", "Use Neutral 700–900 for text."),
        Color("Neutral 200", "neutral.200", "#E4E7EC", "Divider on dark surfaces and disabled fill", "Not a text color on light backgrounds."),
        Color("Neutral 300", "neutral.300", "#D0D5DD", "Light-mode borders and controls", "Not a text color on white."),
        Color("Neutral 400", "neutral.400", "#98A2B3", "Placeholder and disabled content", "Not approved for normal text on light surfaces."),
        Color("Neutral 500", "neutral.500", "#667085", "Secondary iconography and large muted text", "Use only for large text on Neutral 50 or lighter."),
        Color("Neutral 600", "neutral.600", "#475467", "Secondary body text", "Passes AA on Neutral 50 and white."),
        Color("Neutral 700", "neutral.700", "#344054", "Strong secondary text", "Passes AAA on Neutral 50."),
        Color("Neutral 800", "neutral.800", "#1D2939", "Dark-mode surface and light-mode heading", "Use Neutral 50–200 for text when used as a surface."),
        Color("Neutral 900", "neutral.900", "#101828", "Primary text and deepest surface", "Use Console Paper or Neutral 50 for reverse text."),
    ],
    "Status info": [
        Color("Info", "status.info.base", "#2F6FAD", "Info icon, border, and chart mark", "Pair with a text label; not approved as small text on its surface."),
        Color("Info Surface", "status.info.surface", "#EAF2FA", "Info message background", "Use Info Text for body copy."),
        Color("Info Text", "status.info.text", "#1D4E79", "Info message text", "Passes AAA on Info Surface."),
    ],
    "Status success": [
        Color("Success", "status.success.base", "#2F7D61", "Success icon and border", "Pair with icon or text; do not encode success by color alone."),
        Color("Success Surface", "status.success.surface", "#E8F4EE", "Success message background", "Use Success Text for body copy."),
        Color("Success Text", "status.success.text", "#205642", "Success message text", "Passes AAA on Success Surface."),
    ],
    "Status warning": [
        Color("Warning", "status.warning.base", "#B36B00", "Warning icon and border", "Use Assurance Ink or Warning Text for nearby copy."),
        Color("Warning Surface", "status.warning.surface", "#FFF2D6", "Warning message background", "Use Warning Text for body copy."),
        Color("Warning Text", "status.warning.text", "#704200", "Warning message text", "Passes AAA on Warning Surface."),
    ],
    "Status danger": [
        Color("Danger", "status.danger.base", "#B5474F", "Danger icon, border, and destructive control", "Console Paper is reserved for large or bold control text; use Danger Text on pale surfaces."),
        Color("Danger Surface", "status.danger.surface", "#FBEAEC", "Danger message background", "Use Danger Text for body copy."),
        Color("Danger Text", "status.danger.text", "#7A2730", "Danger message text", "Passes AAA on Danger Surface."),
    ],
    "Comic": [
        Color("Panel Mist", "comic.panel-background", "#E8EEEF", "Default comic panel field", "Use Comic Ink for dialogue and line work."),
        Color("Breakroom Paper", "comic.panel-alternate", "#F3E9DC", "Warm alternate panel or flashback field", "Use Comic Ink for text; do not use as Cavapoo fur."),
        Color("Comic Ink", "comic.border", "#101828", "Panel borders, line work, and primary lettering", "Passes AAA on all approved comic fields."),
        Color("Speech White", "comic.speech-bubble", "#FFFFFF", "Speech balloons and clean negative space", "Use Comic Ink; outline balloons on pale panels."),
        Color("Caption Cream", "comic.caption", "#F5E6B8", "Narration and caption boxes", "Use Comic Ink; not approved for white text."),
        Color("Gutter Gray", "comic.gutter", "#D0D5DD", "Panel gutters and quiet separators", "Not approved for body text."),
    ],
    "Environment": [
        Color("Cubicle Mist", "environment.wall", "#DCE5E8", "Office walls and broad background planes", "Keep character silhouettes outlined in Comic Ink."),
        Color("Conference Glass", "environment.glass", "#BFD9D7", "Glass, windows, and reflective dividers", "Do not use as text or a status signal."),
        Color("Desk Bluegray", "environment.desk", "#AABAC0", "Desks, cabinets, and office fixtures", "Use Comic Ink for detail lines."),
        Color("Carpet Slate", "environment.carpet", "#596274", "Carpet and deep environmental planes", "Console Paper passes AA for text when necessary."),
        Color("Monitor Blue", "environment.screen", "#26384A", "Inactive monitors and dark equipment", "Use Console Paper or Status Gold for readable content."),
    ],
}


SEMANTIC = {
    "light": {
        "background": "#F8FAFC",
        "foreground": "#101828",
        "surface": "#FFFFFF",
        "surface-subtle": "#F2F4F7",
        "border": "#D0D5DD",
        "text-muted": "#475467",
        "interactive": "#101828",
        "interactive-foreground": "#F8FAFC",
        "link": "#1D4E79",
        "focus": "#6E62A6",
    },
    "dark": {
        "background": "#101828",
        "foreground": "#F8FAFC",
        "surface": "#1D2939",
        "surface-subtle": "#344054",
        "border": "#475467",
        "text-muted": "#E4E7EC",
        "interactive": "#F4B942",
        "interactive-foreground": "#101828",
        "link": "#BFD9D7",
        "focus": "#F4B942",
    },
}


CONTRAST_TESTS = [
    ("Light body", "#101828", "#F8FAFC", "normal"),
    ("Light secondary", "#475467", "#F8FAFC", "normal"),
    ("Light link", "#1D4E79", "#F8FAFC", "normal"),
    ("Primary reverse", "#F8FAFC", "#101828", "normal"),
    ("Gold control", "#101828", "#F4B942", "normal"),
    ("Coral callout", "#101828", "#D95D52", "normal"),
    ("Teal reverse", "#F8FAFC", "#2F7F79", "normal"),
    ("Violet reverse", "#F8FAFC", "#6E62A6", "normal"),
    ("Dark body", "#F8FAFC", "#101828", "normal"),
    ("Dark secondary", "#E4E7EC", "#1D2939", "normal"),
    ("Dark link", "#BFD9D7", "#101828", "normal"),
    ("Info message", "#1D4E79", "#EAF2FA", "normal"),
    ("Success message", "#205642", "#E8F4EE", "normal"),
    ("Warning message", "#704200", "#FFF2D6", "normal"),
    ("Danger message", "#7A2730", "#FBEAEC", "normal"),
    ("Comic panel", "#101828", "#E8EEEF", "normal"),
    ("Comic alternate", "#101828", "#F3E9DC", "normal"),
    ("Comic caption", "#101828", "#F5E6B8", "normal"),
]


def rgb(hex_value: str) -> tuple[int, int, int]:
    value = hex_value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def hsl(hex_value: str) -> tuple[int, int, int]:
    red, green, blue = (channel / 255 for channel in rgb(hex_value))
    hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
    return round(hue * 360), round(saturation * 100), round(lightness * 100)


def cmyk(hex_value: str) -> tuple[int, int, int, int]:
    red, green, blue = (channel / 255 for channel in rgb(hex_value))
    key = 1 - max(red, green, blue)
    if math.isclose(key, 1):
        return 0, 0, 0, 100
    cyan = (1 - red - key) / (1 - key)
    magenta = (1 - green - key) / (1 - key)
    yellow = (1 - blue - key) / (1 - key)
    return tuple(round(channel * 100) for channel in (cyan, magenta, yellow, key))


def luminance(hex_value: str) -> float:
    channels = []
    for channel in rgb(hex_value):
        value = channel / 255
        channels.append(value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(foreground: str, background: str) -> float:
    lighter, darker = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def enriched(color: Color) -> dict:
    red, green, blue = rgb(color.hex)
    hue, saturation, lightness = hsl(color.hex)
    cyan, magenta, yellow, key = cmyk(color.hex)
    return {
        "$type": "color",
        "$value": color.hex,
        "$description": color.usage,
        "$extensions": {
            "studio.definitelysecure": {
                "name": color.name,
                "rgb": {"r": red, "g": green, "b": blue},
                "hsl": {"h": hue, "s": saturation, "l": lightness},
                "cmykApproximation": {"c": cyan, "m": magenta, "y": yellow, "k": key},
                "pantoneApproximation": color.pantone,
                "accessibility": color.accessibility,
            }
        },
    }


def nested_tokens() -> dict:
    root: dict = {"$schema": "https://design-tokens.github.io/community-group/format/"}
    for colors in COLORS.values():
        for color in colors:
            cursor = root
            parts = color.token.split(".")
            for part in parts[:-1]:
                cursor = cursor.setdefault(part, {})
            cursor[parts[-1]] = enriched(color)
    root["semantic"] = {
        theme: {
            key: {"$type": "color", "$value": value}
            for key, value in values.items()
        }
        for theme, values in SEMANTIC.items()
    }
    return root


def yaml_scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def yaml_lines(value, indent: int = 0) -> list[str]:
    prefix = " " * indent
    if isinstance(value, dict):
        output = []
        for key, item in value.items():
            safe_key = json.dumps(key) if any(char in key for char in "$.-") else key
            if isinstance(item, dict):
                output.append(f"{prefix}{safe_key}:")
                output.extend(yaml_lines(item, indent + 2))
            else:
                output.append(f"{prefix}{safe_key}: {yaml_scalar(item)}")
        return output
    raise TypeError(type(value))


def write_tokens() -> None:
    TOKENS_DIR.mkdir(parents=True, exist_ok=True)
    tokens = nested_tokens()
    (TOKENS_DIR / "colors.json").write_text(json.dumps(tokens, indent=2) + "\n", encoding="utf-8")
    (TOKENS_DIR / "colors.yaml").write_text("\n".join(yaml_lines(tokens)) + "\n", encoding="utf-8")
    css = [
        "/** Definitely Secure color tokens v1.0.0. Generated; do not edit directly. */",
        ":root {",
    ]
    for colors in COLORS.values():
        for color in colors:
            css.append(f"  --ds-{color.token.replace('.', '-')}: {color.hex};")
    for key, value in SEMANTIC["light"].items():
        css.append(f"  --ds-color-{key}: {value};")
    css.extend(["}", "", '[data-theme="dark"] {'])
    for key, value in SEMANTIC["dark"].items():
        css.append(f"  --ds-color-{key}: {value};")
    css.extend(["}", ""])
    (TOKENS_DIR / "colors.css").write_text("\n".join(css), encoding="utf-8")


def color_table(colors: list[Color]) -> list[str]:
    rows = ["| Name | Token | HEX | RGB | HSL | CMYK approx. | Pantone approx. | Usage and accessibility |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for color in colors:
        red, green, blue = rgb(color.hex)
        hue, saturation, lightness = hsl(color.hex)
        cyan, magenta, yellow, key = cmyk(color.hex)
        note = f"{color.usage} {color.accessibility}"
        rows.append(
            f"| {color.name} | `{color.token}` | `{color.hex}` | {red}, {green}, {blue} | {hue}°, {saturation}%, {lightness}% | {cyan}, {magenta}, {yellow}, {key} | {color.pantone} | {note} |"
        )
    return rows


def write_color_system() -> None:
    sections = [
        "# Definitely Secure color system",
        "",
        "Status: Approved",
        "",
        "Owner: Definitely Secure Studio",
        "",
        f"Token version: {VERSION}",
        "",
        f"Last updated: {date.today().isoformat()}",
        "",
        "## Principles",
        "",
        "The Definitely Secure palette pairs a precise dark ink with warm, editorial accents. Assurance Ink provides technical confidence; Meeting Coral and Status Gold introduce workplace-comedy warmth; Protocol Violet and Signal Teal broaden the system without turning it into a generic neon cybersecurity palette.",
        "",
        "Color supports hierarchy but never carries meaning alone. Text, icons, patterns, labels, and line work must preserve meaning in grayscale and for people with color-vision differences. Character colors are not promoted to brand tokens.",
        "",
        "## Palette",
        "",
    ]
    for group, colors in COLORS.items():
        sections.extend([f"### {group}", "", *color_table(colors), ""])
    sections.extend(
        [
            "## Light mode",
            "",
            "Use Neutral 50 for the page, Speech White for raised surfaces, Neutral 900 for primary text, Neutral 600 for secondary text, and Neutral 300 for borders. Primary controls use Assurance Ink with Console Paper. Links use Info Text and remain underlined in body copy. Protocol Violet is the focus-ring color; focus must also have a visible shape, not color alone.",
            "",
            "Approved light-mode text pairs are recorded in the [contrast report](accessibility-contrast-report.md). Do not use Neutral 400 or lighter for readable text, Meeting Coral as body text, Status Gold on white, or white text on Status Gold.",
            "",
            "## Dark mode",
            "",
            "Use Assurance Ink for the page, Neutral 800 for raised surfaces, Neutral 700 for subtle surfaces, Console Paper for primary text, and Neutral 200 for secondary text. Dark-mode primary controls use Status Gold with Assurance Ink text. Conference Glass is the standard dark-mode link color; underlines remain required in body copy.",
            "",
            "Dark logo variants contain Console Paper shapes and transparent backgrounds. Place them only on Assurance Ink, Neutral 800, Monitor Blue, or another tested dark field. Never place a dark variant on a light surface simply because its filename contains the word `dark`; the suffix names the intended surface.",
            "",
            "## Comic usage",
            "",
            "Panel Mist is the default environment-neutral field. Breakroom Paper introduces warmth for alternate scenes and memory without borrowing the Cavapoo’s coat. Speech White balloons and Caption Cream boxes always use Comic Ink lettering and a visible outline when adjacent values are close. Panel borders, dialogue, and essential detail remain Comic Ink so a comic stays legible without color.",
            "",
            "Environment tokens are intentionally cool and muted. They may shift for lighting and story needs, but recurring props should begin from these values. Status colors can appear inside fictional interfaces only when the interface also uses text, shape, or icon labels; a green or red dot alone is not sufficient storytelling information.",
            "",
            "## Cavapoo separation",
            "",
            "The Cavapoo’s reference coat colors—caramel around `#B9855A` and warm white around `#FFFDF8`—are character colors, not brand or environment tokens. Do not reuse either value for buttons, status, panel fields, furniture, or large social backgrounds. Place warm-white fur against Panel Mist, Cubicle Mist, Carpet Slate, or another cool field, and retain Comic Ink outlines. Place caramel fur away from Meeting Coral and Breakroom Paper when their values would merge; use cool environment tokens between them.",
            "",
            "## Status usage",
            "",
            "Each status has a base, surface, and text token. The base is for icons and borders, the surface is for the message field, and the text token is for copy. Every status component also needs a word or recognizable icon. Status Gold belongs to the brand and warning-adjacent emphasis but is not the semantic warning token; `status.warning.*` is darker and tested for interface use.",
            "",
            "## Approved combinations",
            "",
            "- Assurance Ink on Console Paper, Neutral 50, Speech White, Panel Mist, Breakroom Paper, or Caption Cream",
            "- Console Paper on Assurance Ink, Neutral 800, Monitor Blue, Signal Teal, or Carpet Slate",
            "- Assurance Ink on Status Gold and Meeting Coral for display elements and controls",
            "- Each status text token on its matching status surface",
            "- The light logo on light approved surfaces and the dark logo on approved dark surfaces",
            "",
            "Always consult the numerical [accessibility contrast report](accessibility-contrast-report.md) for text size and conformance details.",
            "",
            "## Prohibited combinations",
            "",
            "- Status Gold text on Console Paper, Speech White, Neutral 50, Caption Cream, or Warning Surface",
            "- Console Paper body text on Status Gold, Meeting Coral, or Protocol Violet",
            "- Meeting Coral against Danger without a border and explicit label",
            "- Signal Teal as an unlabeled synonym for success",
            "- Neutral 400 or lighter as normal text on a light surface",
            "- Neutral 500 or darker as normal text on a dark surface",
            "- Brand accents used simultaneously in equal proportions",
            "- Gradients inside approved logos or status components",
            "- Caramel and warm-white Cavapoo coat references reused as UI or brand tokens",
            "",
            "## Print guidance",
            "",
            "CMYK values in this guide are mathematical approximations for coated stock, not press-ready guarantees. Convert through the printer’s ICC profile, request a contract proof, and adjust for paper, ink, and finish. Pantone references are visual starting points only; they are not licensed digital definitions or exact matches.",
            "",
            "For one-color printing, use Assurance Ink or the approved monochrome logo. On uncoated stock, expect Status Gold and Meeting Coral to lose saturation; proof both next to Comic Ink line work. Rich black is not approved for small type or comic outlines—use a single-channel press black chosen with the printer. Maintain at least 0.25 pt for positive rules and 0.5 pt for reversed rules.",
            "",
            "## Machine-readable tokens",
            "",
            "- [`brand/tokens/colors.json`](tokens/colors.json) uses Design Tokens Community Group-compatible `$type` and `$value` fields plus Studio metadata.",
            "- [`brand/tokens/colors.yaml`](tokens/colors.yaml) mirrors the JSON hierarchy.",
            "- [`brand/tokens/colors.css`](tokens/colors.css) provides raw `--ds-*` variables and semantic light/dark theme variables.",
            "",
            "Raw palette tokens describe stable colors. Semantic `--ds-color-*` variables should be used by interfaces whenever a role exists, because their values change by theme.",
            "",
            "## Visual examples",
            "",
            "- [`assets/brand/colors/preview/definitely-secure-color-palette.png`](../assets/brand/colors/preview/definitely-secure-color-palette.png)",
            "- [`assets/brand/colors/preview/definitely-secure-light-mode-example.png`](../assets/brand/colors/preview/definitely-secure-light-mode-example.png)",
            "- [`assets/brand/colors/preview/definitely-secure-dark-mode-example.png`](../assets/brand/colors/preview/definitely-secure-dark-mode-example.png)",
            "- [`assets/brand/colors/preview/definitely-secure-comic-panel-example.png`](../assets/brand/colors/preview/definitely-secure-comic-panel-example.png)",
            "- [`assets/brand/colors/preview/definitely-secure-social-post-example.png`](../assets/brand/colors/preview/definitely-secure-social-post-example.png)",
            "",
            "## Release checklist",
            "",
            "1. Use a semantic token when one exists instead of copying a raw HEX value.",
            "2. Confirm text pairs against the current contrast report at the actual size and weight.",
            "3. Preserve a non-color cue for status, links, selection, and chart meaning.",
            "4. Test light mode, dark mode, grayscale, and a representative color-vision simulation.",
            "5. Confirm the selected logo surface variant passes the background rules.",
            "6. Keep Cavapoo coat colors outside brand, status, and environment token roles.",
            "7. Proof CMYK and spot-color output on the intended stock before production.",
        ]
    )
    (REPO / "brand/color-system.md").write_text("\n".join(sections) + "\n", encoding="utf-8")


def write_contrast_report() -> None:
    rows = [
        "# Definitely Secure accessibility contrast report",
        "",
        "Status: Approved",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"Token version: {VERSION}",
        "",
        "Ratios use the WCAG relative-luminance formula with unrounded sRGB token values. AA normal text requires 4.5:1, AA large text requires 3:1, and AAA normal text requires 7:1. Large text means at least 24 px regular or approximately 18.66 px bold.",
        "",
        "| Pair | Foreground | Background | Ratio | AA normal | AA large | AAA normal | Approved role |",
        "| --- | --- | --- | ---: | --- | --- | --- | --- |",
    ]
    for name, foreground, background, role in CONTRAST_TESTS:
        ratio = contrast(foreground, background)
        rows.append(
            f"| {name} | `{foreground}` | `{background}` | {ratio:.2f}:1 | {'Pass' if ratio >= 4.5 else 'Fail'} | {'Pass' if ratio >= 3 else 'Fail'} | {'Pass' if ratio >= 7 else 'Fail'} | {'Large/display only' if role == 'large' else 'Normal text'} |"
        )
    rows.extend(
        [
            "",
            "## Required failures and restrictions",
            "",
            f"- Status Gold on Console Paper is {contrast('#F4B942', '#F8FAFC'):.2f}:1 and is prohibited for text.",
            f"- Console Paper on Status Gold is the same {contrast('#F8FAFC', '#F4B942'):.2f}:1 and is prohibited for text; use Assurance Ink instead.",
            f"- Console Paper on Meeting Coral is {contrast('#F8FAFC', '#D95D52'):.2f}:1 and is not approved for body text.",
            f"- Neutral 400 on Neutral 50 is {contrast('#98A2B3', '#F8FAFC'):.2f}:1 and is restricted to disabled or nonessential decoration.",
            f"- Console Paper on Protocol Violet is {contrast('#F8FAFC', '#6E62A6'):.2f}:1; it passes AA normal text but not AAA.",
            "",
            "## Non-text requirements",
            "",
            "Interactive boundaries, focus indicators, and meaningful graphic objects require at least 3:1 against adjacent colors. Links in body copy are underlined. Status messages use a label or icon in addition to hue. Comic dialogue and essential line work remain legible in grayscale. Re-test after opacity, blending, antialiasing, imagery, or print conversion changes an effective color.",
        ]
    )
    (REPO / "brand/accessibility-contrast-report.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def svg_document(width: int, height: int, title: str, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 {width} {height}">
  <title id="title">{title}</title>
  <desc id="desc">Definitely Secure color system example, version {VERSION}.</desc>
  <metadata>Copyright {date.today().year} Definitely Secure Studio. All rights reserved.</metadata>
{body}
</svg>
'''


def prompt_mark(x: int, y: int, size: int, outer: str, inner: str, accent: str) -> str:
    scale = size / 120
    return f'''  <g transform="translate({x} {y}) scale({scale})">
    <path fill="{outer}" d="M22 12h76c7.73 0 14 6.27 14 14v48c0 7.73-6.27 14-14 14H63l-23 20V88H22C14.27 88 8 81.73 8 74V26c0-7.73 6.27-14 14-14Z"/>
    <path fill="none" stroke="{inner}" stroke-linecap="round" stroke-linejoin="round" stroke-width="8" d="m35 36 16 16-16 16M62 68h22"/>
    <circle cx="84" cy="35" r="7" fill="{accent}"/>
  </g>'''


def palette_preview() -> str:
    swatches = [
        ("ASSURANCE INK", "#101828"), ("CONSOLE PAPER", "#F8FAFC"),
        ("MEETING CORAL", "#D95D52"), ("PROTOCOL VIOLET", "#6E62A6"),
        ("STATUS GOLD", "#F4B942"), ("SIGNAL TEAL", "#2F7F79"),
    ]
    blocks = []
    for index, (name, value) in enumerate(swatches):
        x = 80 + (index % 3) * 480
        y = 240 + (index // 3) * 250
        outline = ' stroke="#D0D5DD"' if value == "#F8FAFC" else ""
        blocks.append(f'''  <rect x="{x}" y="{y}" width="420" height="150" rx="24" fill="{value}"{outline}/>
  <text x="{x}" y="{y + 190}" font-family="{FONT}" font-size="26" font-weight="700" fill="#101828">{name}</text>
  <text x="{x}" y="{y + 224}" font-family="{FONT}" font-size="22" fill="#475467">{value}</text>''')
    return svg_document(1600, 900, "Definitely Secure color palette", f'''  <rect width="1600" height="900" fill="#FFFFFF"/>
{prompt_mark(80, 60, 120, '#101828', '#F8FAFC', '#F4B942')}
  <text x="230" y="118" font-family="{FONT}" font-size="48" font-weight="800" fill="#101828">DEFINITELY SECURE</text>
  <text x="230" y="162" font-family="{FONT}" font-size="25" fill="#475467">CORE COLOR SYSTEM • VERSION {VERSION}</text>
{''.join(blocks)}''')


def mode_example(dark: bool) -> str:
    theme = SEMANTIC["dark" if dark else "light"]
    status_surface = "#FFF2D6" if not dark else "#344054"
    status_text = "#704200" if not dark else "#F8FAFC"
    return svg_document(1200, 760, f"Definitely Secure {'dark' if dark else 'light'} mode example", f'''  <rect width="1200" height="760" fill="{theme['background']}"/>
  <rect x="0" y="0" width="1200" height="110" fill="{theme['surface']}"/>
{prompt_mark(44, 20, 74, theme['foreground'], theme['background'], '#F4B942')}
  <text x="140" y="70" font-family="{FONT}" font-size="34" font-weight="800" fill="{theme['foreground']}">DEFINITELY SECURE</text>
  <text x="900" y="68" font-family="{FONT}" font-size="22" fill="{theme['link']}" text-decoration="underline">Episode archive</text>
  <rect x="60" y="160" width="700" height="520" rx="28" fill="{theme['surface']}" stroke="{theme['border']}" stroke-width="2"/>
  <text x="110" y="230" font-family="{FONT}" font-size="24" font-weight="700" fill="{theme['foreground']}">SYSTEM OVERVIEW</text>
  <text x="110" y="280" font-family="{FONT}" font-size="21" fill="{theme['text-muted']}">Everything is operating within expected parameters.</text>
  <rect x="110" y="330" width="600" height="120" rx="18" fill="{status_surface}"/>
  <circle cx="155" cy="390" r="15" fill="#B36B00"/>
  <text x="190" y="383" font-family="{FONT}" font-size="20" font-weight="700" fill="{status_text}">Expected parameters changed</text>
  <text x="190" y="417" font-family="{FONT}" font-size="18" fill="{status_text}">Review the status report before replying.</text>
  <rect x="110" y="510" width="240" height="68" rx="14" fill="{theme['interactive']}"/>
  <text x="230" y="553" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="{theme['interactive-foreground']}">OPEN REPORT</text>
  <rect x="810" y="160" width="330" height="250" rx="28" fill="#D95D52"/>
  <text x="850" y="230" font-family="{FONT}" font-size="20" font-weight="700" fill="#101828">TODAY'S CERTAINTY</text>
  <text x="850" y="315" font-family="{FONT}" font-size="68" font-weight="800" fill="#101828">94%</text>
  <text x="850" y="360" font-family="{FONT}" font-size="18" fill="#101828">± several assumptions</text>
  <rect x="810" y="450" width="330" height="230" rx="28" fill="{theme['surface-subtle']}"/>
  <text x="850" y="515" font-family="{FONT}" font-size="20" font-weight="700" fill="{theme['foreground']}">NOTES</text>
  <text x="850" y="560" font-family="{FONT}" font-size="18" fill="{theme['text-muted']}">Links stay underlined.</text>
  <text x="850" y="598" font-family="{FONT}" font-size="18" fill="{theme['text-muted']}">Status always has a label.</text>
  <text x="850" y="636" font-family="{FONT}" font-size="18" fill="{theme['text-muted']}">Accent color stays scarce.</text>''')


def comic_example() -> str:
    return svg_document(1400, 820, "Definitely Secure comic panel color example", f'''  <rect width="1400" height="820" fill="#D0D5DD"/>
  <rect x="50" y="50" width="620" height="720" fill="#E8EEEF" stroke="#101828" stroke-width="12"/>
  <rect x="730" y="50" width="620" height="720" fill="#F3E9DC" stroke="#101828" stroke-width="12"/>
  <rect x="120" y="120" width="270" height="140" rx="60" fill="#FFFFFF" stroke="#101828" stroke-width="7"/>
  <path d="M300 250 330 295 260 260Z" fill="#FFFFFF" stroke="#101828" stroke-width="7"/>
  <text x="165" y="175" font-family="{FONT}" font-size="24" font-weight="700" fill="#101828">IS IT FIXED?</text>
  <text x="165" y="214" font-family="{FONT}" font-size="20" fill="#344054">The dashboard is green.</text>
  <rect x="155" y="410" width="420" height="170" rx="24" fill="#AABAC0" stroke="#101828" stroke-width="8"/>
  <rect x="220" y="335" width="290" height="120" rx="18" fill="#26384A" stroke="#101828" stroke-width="8"/>
  <circle cx="465" cy="370" r="14" fill="#F4B942"/>
  <path d="M270 380h110" stroke="#BFD9D7" stroke-width="12" stroke-linecap="round"/>
  <rect x="800" y="115" width="475" height="120" rx="20" fill="#F5E6B8" stroke="#101828" stroke-width="7"/>
  <text x="840" y="168" font-family="{FONT}" font-size="21" font-weight="700" fill="#101828">CAPTION: TEN MINUTES LATER</text>
  <text x="840" y="207" font-family="{FONT}" font-size="19" fill="#344054">Confidence remained operational.</text>
  <rect x="850" y="390" width="390" height="220" rx="24" fill="#BFD9D7" stroke="#101828" stroke-width="8"/>
  <rect x="900" y="435" width="290" height="105" rx="14" fill="#26384A"/>
  <path d="M945 487h145" stroke="#F8FAFC" stroke-width="12" stroke-linecap="round"/>
  <circle cx="1145" cy="487" r="15" fill="#B5474F"/>
  <text x="820" y="670" font-family="{FONT}" font-size="21" font-weight="700" fill="#101828">Cool environment colors</text>
  <text x="820" y="706" font-family="{FONT}" font-size="21" font-weight="700" fill="#101828">preserve room for characters.</text>''')


def social_example() -> str:
    return svg_document(1080, 1080, "Definitely Secure social post color example", f'''  <rect width="1080" height="1080" fill="#D95D52"/>
  <rect x="72" y="72" width="936" height="936" rx="54" fill="#F8FAFC"/>
{prompt_mark(126, 126, 140, '#101828', '#F8FAFC', '#F4B942')}
  <text x="310" y="190" font-family="{FONT}" font-size="48" font-weight="800" fill="#101828">DEFINITELY SECURE</text>
  <text x="310" y="238" font-family="{FONT}" font-size="24" fill="#475467">A WORKPLACE COMIC</text>
  <text x="126" y="430" font-family="{FONT}" font-size="72" font-weight="800" fill="#101828">THE SYSTEM</text>
  <text x="126" y="510" font-family="{FONT}" font-size="72" font-weight="800" fill="#101828">IS CONFIDENT.</text>
  <rect x="126" y="570" width="530" height="16" rx="8" fill="#F4B942"/>
  <text x="126" y="680" font-family="{FONT}" font-size="34" fill="#344054">The evidence has been invited</text>
  <text x="126" y="728" font-family="{FONT}" font-size="34" fill="#344054">to a follow-up meeting.</text>
  <rect x="126" y="840" width="500" height="92" rx="22" fill="#101828"/>
  <text x="376" y="898" text-anchor="middle" font-family="{FONT}" font-size="27" font-weight="700" fill="#F8FAFC">DEFINITELYSECURE.COM</text>
  <circle cx="866" cy="872" r="75" fill="#6E62A6"/>
  <path d="m832 868 26 26 48-56" fill="none" stroke="#F8FAFC" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>''')


PREVIEWS = {
    "definitely-secure-color-palette.svg": palette_preview(),
    "definitely-secure-light-mode-example.svg": mode_example(False),
    "definitely-secure-dark-mode-example.svg": mode_example(True),
    "definitely-secure-comic-panel-example.svg": comic_example(),
    "definitely-secure-social-post-example.svg": social_example(),
}


def render_previews() -> None:
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    for filename, content in PREVIEWS.items():
        svg_path = PREVIEW_DIR / filename
        svg_path.write_text(content, encoding="utf-8")
        png_path = svg_path.with_suffix(".png")
        subprocess.run(["rsvg-convert", "-w", "1600", "-o", str(png_path), str(svg_path)], check=True)


def write_license() -> None:
    (ROOT / "LICENSE.md").write_text(
        "# Definitely Secure color asset license\n\n"
        "Copyright © 2026 Definitely Secure Studio. All rights reserved.\n\n"
        "The color names, coordinated palette, preview compositions, and brand presentation in this directory are proprietary brand assets. Repository access does not grant trademark, endorsement, merchandising, or adaptation rights. Definitely Secure Studio projects may use them according to `brand/color-system.md`; third-party use requires prior written permission unless applicable law permits it.\n",
        encoding="utf-8",
    )


def write_manifest() -> None:
    files = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name == "manifest.json":
            continue
        payload = path.read_bytes()
        files.append({"path": str(path.relative_to(ROOT)), "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()})
    manifest = {
        "brand": "Definitely Secure",
        "owner": "Definitely Secure Studio",
        "version": VERSION,
        "generated": date.today().isoformat(),
        "files": files,
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if not shutil.which("rsvg-convert"):
        raise SystemExit("rsvg-convert is required to render previews")
    write_tokens()
    write_color_system()
    write_contrast_report()
    render_previews()
    write_license()
    write_manifest()
    print(f"Built Definitely Secure color system v{VERSION}: {sum(len(v) for v in COLORS.values())} raw tokens, {len(PREVIEWS)} previews.")


if __name__ == "__main__":
    main()
