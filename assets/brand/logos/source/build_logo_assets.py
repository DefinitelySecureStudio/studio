#!/usr/bin/env python3
"""Build the Definitely Secure logo system from its canonical vector geometry."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path


VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parents[1]
TYPOGRAPHY_FONTS = ROOT.parent / "typography/fonts"
INK = "#101828"
PAPER = "#F8FAFC"
SIGNAL = "#F4B942"
SLATE = "#475467"
FONT = "Barlow Condensed, Arial Narrow, Arial, sans-serif"
RENDER_ENV: dict[str, str] | None = None


def svg_document(width: int, height: int, title: str, description: str, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 {width} {height}">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
  <metadata>Definitely Secure Studio logo system v{VERSION}. Copyright {date.today().year} Definitely Secure Studio. All rights reserved.</metadata>
{body}
</svg>
'''


def mark(x: float, y: float, size: float, outer: str, inner: str, accent: str) -> str:
    scale = size / 120
    return f'''  <g transform="translate({x} {y}) scale({scale})">
    <path fill="{outer}" d="M22 12h76c7.73 0 14 6.27 14 14v48c0 7.73-6.27 14-14 14H63l-23 20V88H22C14.27 88 8 81.73 8 74V26c0-7.73 6.27-14 14-14Z"/>
    <path fill="none" stroke="{inner}" stroke-linecap="round" stroke-linejoin="round" stroke-width="8" d="m35 36 16 16-16 16M62 68h22"/>
    <circle cx="84" cy="35" r="7" fill="{accent}"/>
  </g>'''


def horizontal_studio(dark: bool = False) -> str:
    text = PAPER if dark else INK
    secondary = PAPER if dark else SLATE
    return svg_document(
        720,
        160,
        "Definitely Secure Studio horizontal logo",
        "The terminal prompt speech-bubble mark beside the words Definitely Secure Studio.",
        f'''{mark(20, 20, 120, text, INK if dark else PAPER, SIGNAL)}
  <g fill="{text}" font-family="{FONT}">
    <text x="166" y="74" font-size="49" font-weight="800" letter-spacing="-1.5">DEFINITELY SECURE</text>
    <text x="169" y="116" fill="{secondary}" font-size="25" font-weight="700" letter-spacing="7">STUDIO</text>
  </g>''',
    )


def vertical_studio(dark: bool = False) -> str:
    text = PAPER if dark else INK
    secondary = PAPER if dark else SLATE
    return svg_document(
        480,
        440,
        "Definitely Secure Studio vertical logo",
        "The terminal prompt speech-bubble mark above the words Definitely Secure Studio.",
        f'''{mark(150, 34, 180, text, INK if dark else PAPER, SIGNAL)}
  <g fill="{text}" font-family="{FONT}" text-anchor="middle">
    <text x="240" y="286" font-size="42" font-weight="800" letter-spacing="-1">DEFINITELY SECURE</text>
    <text x="240" y="334" fill="{secondary}" font-size="24" font-weight="700" letter-spacing="8">STUDIO</text>
  </g>''',
    )


def comic_logo(dark: bool = False) -> str:
    text = PAPER if dark else INK
    return svg_document(
        780,
        190,
        "Definitely Secure comic logo",
        "The terminal prompt speech-bubble mark beside a bold Definitely Secure comic wordmark.",
        f'''{mark(18, 25, 140, text, INK if dark else PAPER, SIGNAL)}
  <g fill="{text}" font-family="{FONT}" font-style="italic" font-weight="900">
    <text x="181" y="76" font-size="52" letter-spacing="1">DEFINITELY</text>
    <text x="177" y="145" font-size="78" letter-spacing="-2">SECURE</text>
  </g>
  <rect x="344" y="157" width="172" height="10" rx="5" fill="{SIGNAL}"/>''',
    )


def icon(dark: bool = False, monochrome: str | None = None) -> str:
    if monochrome:
        outer = monochrome
        inner = PAPER if monochrome == INK else INK
        accent = inner
    else:
        outer = PAPER if dark else INK
        inner = INK if dark else PAPER
        accent = SIGNAL
    return svg_document(
        120,
        120,
        "Definitely Secure prompt mark",
        "A speech bubble containing a terminal prompt and status light.",
        mark(0, 0, 120, outer, inner, accent),
    )


def small_icon() -> str:
    return svg_document(
        120,
        120,
        "Definitely Secure small prompt mark",
        "A simplified speech-bubble terminal prompt optimized for very small display sizes.",
        '''  <path fill="#101828" d="M22 12h76c7.73 0 14 6.27 14 14v48c0 7.73-6.27 14-14 14H63l-23 20V88H22C14.27 88 8 81.73 8 74V26c0-7.73 6.27-14 14-14Z"/>
  <path fill="none" stroke="#F8FAFC" stroke-linecap="round" stroke-linejoin="round" stroke-width="10" d="m35 35 17 17-17 17M63 69h22"/>
  <circle cx="84" cy="34" r="8" fill="#F4B942"/>''',
    )


def social_avatar(dark: bool = True) -> str:
    background = INK if dark else PAPER
    outer = PAPER if dark else INK
    inner = INK if dark else PAPER
    return svg_document(
        1024,
        1024,
        "Definitely Secure social avatar",
        "The Definitely Secure prompt mark centered on a square background.",
        f'''  <rect width="1024" height="1024" rx="208" fill="{background}"/>
{mark(152, 152, 720, outer, inner, SIGNAL)}''',
    )


def footer_mark(dark: bool = False) -> str:
    text = PAPER if dark else INK
    return svg_document(
        1000,
        92,
        "Definitely Secure comic footer mark",
        "Compact Definitely Secure comic wordmark with episode number and website placeholder.",
        f'''{mark(8, 8, 76, text, INK if dark else PAPER, SIGNAL)}
  <g fill="{text}" font-family="{FONT}" font-weight="800">
    <text x="104" y="57" font-size="35" letter-spacing=".5">DEFINITELY SECURE</text>
    <text x="500" y="57" font-size="28" font-weight="700">• #NNNN • DEFINITELYSECURE.COM</text>
  </g>''',
    )


def production_lockup(dark: bool = False) -> str:
    text = PAPER if dark else INK
    return svg_document(
        820,
        120,
        "A Definitely Secure Studio production lockup",
        "The Definitely Secure prompt mark beside the production credit.",
        f'''{mark(8, 8, 104, text, INK if dark else PAPER, SIGNAL)}
  <g fill="{text}" font-family="{FONT}">
    <text x="140" y="48" font-size="23" font-weight="600" letter-spacing="2">A</text>
    <text x="140" y="82" font-size="31" font-weight="800">DEFINITELY SECURE STUDIO PRODUCTION</text>
  </g>''',
    )


def watermark() -> str:
    return svg_document(
        120,
        120,
        "Definitely Secure watermark",
        "A single-color, low-opacity Definitely Secure prompt mark.",
        f'''  <g opacity="0.22">
{mark(0, 0, 120, INK, PAPER, PAPER)}
  </g>''',
    )


def source_sheet() -> str:
    return svg_document(
        1600,
        1000,
        "Definitely Secure logo source sheet",
        "Master geometry, color palette, and approved logo arrangements.",
        f'''  <rect width="1600" height="1000" fill="{PAPER}"/>
  <g font-family="{FONT}" fill="{INK}">
    <text x="80" y="90" font-size="48" font-weight="800">DEFINITELY SECURE LOGO SYSTEM</text>
    <text x="80" y="130" font-size="22" fill="{SLATE}">MASTER VECTOR SOURCE • VERSION {VERSION}</text>
  </g>
{mark(80, 190, 280, INK, PAPER, SIGNAL)}
  <g font-family="{FONT}" fill="{INK}">
    <text x="410" y="265" font-size="34" font-weight="800">THE PROMPT MARK</text>
    <text x="410" y="310" font-size="24">Speech bubble + terminal prompt</text>
    <text x="410" y="344" font-size="24">+ status indicator</text>
    <text x="410" y="392" font-size="22" fill="{SLATE}">Clear-space unit x = status-light diameter</text>
  </g>
  <g transform="translate(80 560)">
    <rect width="260" height="180" rx="24" fill="{INK}"/>
{mark(65, 25, 130, PAPER, INK, SIGNAL)}
    <text x="0" y="224" font-family="{FONT}" font-size="20" fill="{INK}">DARK SURFACE</text>
  </g>
  <g transform="translate(400 560)">
    <rect width="260" height="180" rx="24" fill="#E4E7EC"/>
{mark(65, 25, 130, INK, PAPER, SIGNAL)}
    <text x="0" y="224" font-family="{FONT}" font-size="20" fill="{INK}">LIGHT SURFACE</text>
  </g>
  <g font-family="{FONT}" fill="{INK}">
    <text x="900" y="220" font-size="28" font-weight="800">CORE PALETTE</text>
    <rect x="900" y="260" width="170" height="120" rx="16" fill="{INK}"/>
    <rect x="1100" y="260" width="170" height="120" rx="16" fill="{SIGNAL}"/>
    <rect x="1300" y="260" width="170" height="120" rx="16" fill="{PAPER}" stroke="#D0D5DD"/>
    <text x="900" y="415" font-size="20">Assurance Ink</text><text x="900" y="444" font-size="18" fill="{SLATE}">{INK}</text>
    <text x="1100" y="415" font-size="20">Status Gold</text><text x="1100" y="444" font-size="18" fill="{SLATE}">{SIGNAL}</text>
    <text x="1300" y="415" font-size="20">Console Paper</text><text x="1300" y="444" font-size="18" fill="{SLATE}">{PAPER}</text>
    <text x="780" y="570" font-size="28" font-weight="800">WORDMARK CONSTRUCTION</text>
    <text x="780" y="645" font-size="58" font-weight="900" font-style="italic">DEFINITELY SECURE</text>
    <rect x="1118" y="666" width="190" height="10" rx="5" fill="{SIGNAL}"/>
    <text x="780" y="744" font-size="21" fill="{SLATE}">Barlow Condensed Black Italic</text>
    <text x="780" y="778" font-size="21" fill="{SLATE}">Never substitute the fictional company for the Studio credit.</text>
  </g>''',
    )


ASSETS = {
    "primary/definitely-secure-primary-light.svg": horizontal_studio(False),
    "primary/definitely-secure-primary-dark.svg": horizontal_studio(True),
    "studio/definitely-secure-studio-horizontal-light.svg": horizontal_studio(False),
    "studio/definitely-secure-studio-horizontal-dark.svg": horizontal_studio(True),
    "studio/definitely-secure-studio-vertical-light.svg": vertical_studio(False),
    "studio/definitely-secure-studio-vertical-dark.svg": vertical_studio(True),
    "studio/definitely-secure-production-lockup-light.svg": production_lockup(False),
    "studio/definitely-secure-production-lockup-dark.svg": production_lockup(True),
    "comic/definitely-secure-comic-horizontal-light.svg": comic_logo(False),
    "comic/definitely-secure-comic-horizontal-dark.svg": comic_logo(True),
    "comic/definitely-secure-comic-footer-light.svg": footer_mark(False),
    "comic/definitely-secure-comic-footer-dark.svg": footer_mark(True),
    "icon/definitely-secure-prompt-mark-light.svg": icon(False),
    "icon/definitely-secure-prompt-mark-dark.svg": icon(True),
    "icon/definitely-secure-prompt-mark-small.svg": small_icon(),
    "monochrome/definitely-secure-mark-black.svg": icon(monochrome=INK),
    "monochrome/definitely-secure-mark-white.svg": icon(monochrome=PAPER),
    "monochrome/definitely-secure-watermark.svg": watermark(),
    "social/definitely-secure-social-avatar-dark.svg": social_avatar(True),
    "social/definitely-secure-social-avatar-light.svg": social_avatar(False),
    "favicon/definitely-secure-favicon.svg": small_icon(),
    "source/definitely-secure-logo-master.svg": source_sheet(),
}


def run(*args: str) -> None:
    subprocess.run(args, check=True, env=RENDER_ENV)


def font_environment(tmpdir: Path) -> dict[str, str]:
    cache = tmpdir / "cache"
    cache.mkdir()
    config = tmpdir / "fonts.conf"
    config.write_text(
        f'''<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
<fontconfig>
  <dir>{TYPOGRAPHY_FONTS}</dir>
  <cachedir>{cache}</cachedir>
  <config></config>
</fontconfig>
''',
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["FONTCONFIG_FILE"] = str(config)
    return env


def render_svg(svg_path: Path) -> None:
    relative = svg_path.relative_to(ROOT)
    if relative.parts[0] == "source":
        return
    basename = svg_path.with_suffix("")
    width_by_group = {
        "primary": 720,
        "studio": 820,
        "comic": 1000,
        "icon": 512,
        "monochrome": 512,
        "social": 1024,
        "favicon": 512,
    }
    native_width = width_by_group[relative.parts[0]]
    transparent_png = basename.with_name(basename.name + "-transparent.png")
    highres_png = basename.with_name(basename.name + "-transparent@4x.png")
    if relative.parts[0] == "social":
        transparent_png = basename.with_suffix(".png")
        highres_png = basename.with_name(basename.name + "@2x.png")
    run("rsvg-convert", "-w", str(native_width), "-o", str(transparent_png), str(svg_path))
    scale = 2 if relative.parts[0] == "social" else 4
    run("rsvg-convert", "-w", str(native_width * scale), "-o", str(highres_png), str(svg_path))
    run("rsvg-convert", "-f", "pdf", "-o", str(basename.with_suffix(".pdf")), str(svg_path))


def build_favicons() -> None:
    source = ROOT / "favicon/definitely-secure-favicon.svg"
    for size in (16, 32, 48, 180, 256, 512):
        output = ROOT / f"favicon/definitely-secure-favicon-{size}.png"
        run("rsvg-convert", "-w", str(size), "-h", str(size), "-o", str(output), str(source))
    run(
        "sips",
        "-s",
        "format",
        "ico",
        str(ROOT / "favicon/definitely-secure-favicon-256.png"),
        "--out",
        str(ROOT / "favicon/favicon.ico"),
    )


def write_manifest() -> None:
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name == "manifest.json" or "__pycache__" in path.parts:
            continue
        data = path.read_bytes()
        entries.append(
            {
                "path": str(path.relative_to(ROOT)),
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    manifest = {
        "brand": "Definitely Secure",
        "owner": "Definitely Secure Studio",
        "version": VERSION,
        "generated": date.today().isoformat(),
        "license": "All rights reserved; see LICENSE.md",
        "assets": entries,
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    global RENDER_ENV
    if not shutil.which("rsvg-convert"):
        raise SystemExit("rsvg-convert is required to build logo exports")
    if not shutil.which("sips"):
        raise SystemExit("sips is required to build favicon.ico")
    if not TYPOGRAPHY_FONTS.exists():
        raise SystemExit("Bundled typography fonts are required to build logo exports")
    with tempfile.TemporaryDirectory(prefix="ds-logo-fontconfig-") as tmp:
        RENDER_ENV = font_environment(Path(tmp))
        for relative, content in ASSETS.items():
            target = ROOT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        for svg_path in sorted(ROOT.rglob("*.svg")):
            render_svg(svg_path)
        build_favicons()
    RENDER_ENV = None
    write_manifest()
    print(f"Built {len(ASSETS)} SVG assets and raster/PDF exports for logo system v{VERSION}.")


if __name__ == "__main__":
    main()
