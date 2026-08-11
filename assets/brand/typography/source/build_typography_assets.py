#!/usr/bin/env python3
"""Build webfonts, typography proofs, glyph checks, and asset metadata."""

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
FONTS = ROOT / "fonts"
SAMPLES_DIR = ROOT / "samples"

FONT_FILES = [
    "barlow-condensed/BarlowCondensed-SemiBold.ttf",
    "barlow-condensed/BarlowCondensed-Bold.ttf",
    "barlow-condensed/BarlowCondensed-ExtraBold.ttf",
    "barlow-condensed/BarlowCondensed-BlackItalic.ttf",
    "atkinson-hyperlegible/AtkinsonHyperlegible-Regular.ttf",
    "atkinson-hyperlegible/AtkinsonHyperlegible-Italic.ttf",
    "atkinson-hyperlegible/AtkinsonHyperlegible-Bold.ttf",
    "atkinson-hyperlegible/AtkinsonHyperlegible-BoldItalic.ttf",
    "ibm-plex-mono/IBMPlexMono-Regular.ttf",
    "ibm-plex-mono/IBMPlexMono-Italic.ttf",
    "ibm-plex-mono/IBMPlexMono-Medium.ttf",
    "ibm-plex-mono/IBMPlexMono-SemiBold.ttf",
]

GLYPH_TEXT = r"0 O 1 l I | / \  {} [] ()  <= != ==  --flag=value"


def run(args: list[str], env: dict[str, str] | None = None, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, env=env, text=True, capture_output=capture)


def verify_font_sources() -> None:
    for relative in FONT_FILES:
        source = FONTS / relative
        if not source.exists():
            raise SystemExit(f"Missing approved font file: {source}")


def font_environment(tmpdir: Path) -> dict[str, str]:
    cache = tmpdir / "cache"
    cache.mkdir()
    config = tmpdir / "fonts.conf"
    config.write_text(
        f'''<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
<fontconfig>
  <dir>{FONTS}</dir>
  <cachedir>{cache}</cachedir>
  <config></config>
</fontconfig>
''',
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["FONTCONFIG_FILE"] = str(config)
    return env


def svg_document(width: int, height: int, title: str, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 {width} {height}">
  <title id="title">{title}</title>
  <desc id="desc">Definitely Secure typography system proof, version {VERSION}.</desc>
  <metadata>Copyright {date.today().year} Definitely Secure Studio. Font software licensed under SIL OFL 1.1.</metadata>
{body}
</svg>
'''


def specimen_svg() -> str:
    return svg_document(
        1600,
        1200,
        "Definitely Secure typography specimen",
        r'''  <rect width="1600" height="1200" fill="#F8FAFC"/>
  <text x="80" y="105" font-family="Barlow Condensed" font-size="66" font-weight="800" fill="#101828">DEFINITELY SECURE TYPOGRAPHY</text>
  <text x="82" y="150" font-family="Atkinson Hyperlegible" font-size="22" fill="#475467">DISPLAY • BODY • DIALOGUE • MONOSPACE • SOUND EFFECTS</text>
  <line x1="80" y1="190" x2="1520" y2="190" stroke="#D0D5DD" stroke-width="2"/>

  <text x="80" y="245" font-family="Atkinson Hyperlegible" font-size="18" font-weight="700" fill="#D95D52">DISPLAY — BARLOW CONDENSED</text>
  <text x="80" y="345" font-family="Barlow Condensed" font-size="96" font-weight="800" letter-spacing="-1" fill="#101828">THE SYSTEM IS CONFIDENT.</text>
  <text x="83" y="400" font-family="Barlow Condensed" font-size="42" font-weight="600" fill="#344054">Major headings stay compact, direct, and technically credible.</text>

  <text x="80" y="485" font-family="Atkinson Hyperlegible" font-size="18" font-weight="700" fill="#D95D52">BODY AND DIALOGUE — ATKINSON HYPERLEGIBLE</text>
  <text x="80" y="540" font-family="Atkinson Hyperlegible" font-size="27" fill="#101828">Clear forms distinguish O and 0, I and l,</text>
  <text x="80" y="582" font-family="Atkinson Hyperlegible" font-size="27" fill="#101828">with technical detail that excludes no one.</text>
  <text x="80" y="630" font-family="Atkinson Hyperlegible" font-size="23" font-style="italic" fill="#475467">Regular, true italic, bold, and bold italic cover continuous reading.</text>

  <rect x="80" y="690" width="690" height="230" rx="78" fill="#FFFFFF" stroke="#101828" stroke-width="6"/>
  <path d="M580 900 650 970 530 915Z" fill="#FFFFFF" stroke="#101828" stroke-width="6"/>
  <text x="145" y="775" font-family="Atkinson Hyperlegible" font-size="34" font-weight="700" fill="#101828">Is it fixed?</text>
  <text x="145" y="830" font-family="Atkinson Hyperlegible" font-size="31" fill="#101828">The dashboard is green.</text>
  <text x="145" y="875" font-family="Atkinson Hyperlegible" font-size="26" fill="#475467">That wasn't the question.</text>

  <rect x="840" y="470" width="680" height="450" rx="30" fill="#101828"/>
  <text x="900" y="530" font-family="Atkinson Hyperlegible" font-size="18" font-weight="700" fill="#F4B942">MONOSPACE — IBM PLEX MONO</text>
  <text x="900" y="595" font-family="IBM Plex Mono" font-size="27" font-weight="500" fill="#F8FAFC">$ status --environment=prod</text>
  <text x="900" y="645" font-family="IBM Plex Mono" font-size="24" fill="#BFD9D7">[INFO] confidence=0.94</text>
  <text x="900" y="695" font-family="IBM Plex Mono" font-size="24" fill="#F5E6B8">[WARN] evidence=pending</text>
  <text x="900" y="765" font-family="IBM Plex Mono" font-size="27" fill="#F8FAFC">0 O  1 l I  | / \</text>
  <text x="900" y="815" font-family="IBM Plex Mono" font-size="27" fill="#F8FAFC">{}  []  ()  &lt;=  !=  ==</text>
  <text x="900" y="865" font-family="IBM Plex Mono" font-size="24" font-style="italic" fill="#E4E7EC">literal glyphs, no decorative glow</text>

  <text x="80" y="1060" font-family="Barlow Condensed" font-size="132" font-style="italic" font-weight="900" letter-spacing="-2" fill="#F4B942" stroke="#101828" stroke-width="5" paint-order="stroke">PING!</text>
  <text x="480" y="1030" font-family="Atkinson Hyperlegible" font-size="18" font-weight="700" fill="#D95D52">SOUND EFFECT</text>
  <text x="480" y="1075" font-family="Atkinson Hyperlegible" font-size="25" fill="#344054">Barlow Condensed Black Italic begins the custom lettering treatment.</text>
  <text x="80" y="1150" font-family="IBM Plex Mono" font-size="18" fill="#667085">TYPE SYSTEM 1.0.0 • MOBILE MINIMUM BODY 16px • DIALOGUE 16px • CODE 14px</text>''',
    )


def mobile_svg() -> str:
    return svg_document(
        1200,
        900,
        "Definitely Secure mobile typography test",
        r'''  <rect width="1200" height="900" fill="#D0D5DD"/>
  <rect x="80" y="55" width="430" height="790" rx="48" fill="#F8FAFC" stroke="#101828" stroke-width="8"/>
  <text x="125" y="125" font-family="Barlow Condensed" font-size="34" font-weight="800" fill="#101828">DEFINITELY SECURE</text>
  <text x="125" y="170" font-family="Atkinson Hyperlegible" font-size="18" fill="#475467">Simulated 390px mobile reading width</text>
  <text x="125" y="250" font-family="Barlow Condensed" font-size="37" font-weight="800" fill="#101828">THE STATUS</text>
  <text x="125" y="292" font-family="Barlow Condensed" font-size="37" font-weight="800" fill="#101828">REPORT</text>
  <text x="125" y="360" font-family="Atkinson Hyperlegible" font-size="18" fill="#101828">Body copy stays at or above 16px, with</text>
  <text x="125" y="390" font-family="Atkinson Hyperlegible" font-size="18" fill="#101828">comfortable line height and deliberate measure.</text>
  <rect x="125" y="445" width="340" height="175" rx="52" fill="#FFFFFF" stroke="#101828" stroke-width="5"/>
  <text x="165" y="510" font-family="Atkinson Hyperlegible" font-size="22" font-weight="700" fill="#101828">Still readable?</text>
  <text x="165" y="550" font-family="Atkinson Hyperlegible" font-size="20" fill="#101828">At the final crop, yes.</text>
  <text x="125" y="700" font-family="IBM Plex Mono" font-size="16" fill="#1D4E79">0O 1lI |/\ {}[]()</text>
  <text x="125" y="770" font-family="Atkinson Hyperlegible" font-size="15" fill="#475467">Caption minimum: 15px / 1.45 line height</text>
  <rect x="590" y="55" width="530" height="790" rx="36" fill="#101828"/>
  <text x="650" y="125" font-family="Barlow Condensed" font-size="46" font-weight="800" fill="#F8FAFC">FINAL-SIZE CHECKS</text>
  <text x="650" y="220" font-family="Atkinson Hyperlegible" font-size="24" font-weight="700" fill="#F4B942">BODY</text>
  <text x="650" y="262" font-family="Atkinson Hyperlegible" font-size="22" fill="#F8FAFC">16px minimum • 1.55 line height</text>
  <text x="650" y="345" font-family="Atkinson Hyperlegible" font-size="24" font-weight="700" fill="#F4B942">DIALOGUE</text>
  <text x="650" y="387" font-family="Atkinson Hyperlegible" font-size="22" fill="#F8FAFC">16px minimum • 18–22px preferred</text>
  <text x="650" y="470" font-family="Atkinson Hyperlegible" font-size="24" font-weight="700" fill="#F4B942">CODE</text>
  <text x="650" y="512" font-family="IBM Plex Mono" font-size="22" fill="#F8FAFC">14px minimum • ligatures off</text>
  <text x="650" y="595" font-family="Atkinson Hyperlegible" font-size="24" font-weight="700" fill="#F4B942">SOCIAL</text>
  <text x="650" y="637" font-family="Atkinson Hyperlegible" font-size="22" fill="#F8FAFC">Inspect exports at 360px wide</text>
  <text x="650" y="720" font-family="Atkinson Hyperlegible" font-size="24" font-weight="700" fill="#F4B942">RULE</text>
  <text x="650" y="762" font-family="Atkinson Hyperlegible" font-size="22" fill="#F8FAFC">Edit copy before shrinking type.</text>''',
    )


SAMPLE_DOCS = {
    "definitely-secure-typography-specimen.svg": specimen_svg(),
    "definitely-secure-typography-mobile-test.svg": mobile_svg(),
}


def render_samples(env: dict[str, str]) -> None:
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    for filename, content in SAMPLE_DOCS.items():
        svg = SAMPLES_DIR / filename
        svg.write_text(content, encoding="utf-8")
        run(["rsvg-convert", "-w", "1600", "-o", str(svg.with_suffix(".png")), str(svg)], env=env)
        run(["rsvg-convert", "-f", "pdf", "-o", str(svg.with_suffix(".pdf")), str(svg)], env=env)


def write_glyph_report() -> None:
    shaper = shutil.which("hb-shape")
    if not shaper:
        raise SystemExit("hb-shape is required for glyph verification")
    lines = [
        "# Typography glyph verification",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"Test string: `{GLYPH_TEXT}`",
        "",
        "Every approved production font was shaped with HarfBuzz. A `.notdef` or glyph ID 0 would fail the build.",
        "",
        "| Font file | Result | Glyph count |",
        "| --- | --- | ---: |",
    ]
    for relative in FONT_FILES:
        font = FONTS / relative
        result = run([shaper, "--no-glyph-names", str(font), GLYPH_TEXT], capture=True)
        output = result.stdout.strip()
        if output.startswith("[0=") or "|0=" in output:
            raise SystemExit(f"Missing required glyph in {font}: {output}")
        glyph_count = output.count("|") + 1
        lines.append(f"| `{relative}` | Pass | {glyph_count} |")
    lines.extend(
        [
            "",
            "Visual differentiation is recorded in the specimen and mobile test. Automated coverage confirms presence, not perceptual quality; inspect the generated proofs whenever files or renderers change.",
        ]
    )
    (ROOT / "glyph-test-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manifest() -> None:
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name == "manifest.json":
            continue
        data = path.read_bytes()
        entries.append({"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    manifest = {
        "brand": "Definitely Secure",
        "owner": "Definitely Secure Studio",
        "version": VERSION,
        "generated": date.today().isoformat(),
        "fontLicense": "SIL Open Font License 1.1",
        "files": entries,
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    for command in ("rsvg-convert", "hb-shape"):
        if not shutil.which(command):
            raise SystemExit(f"{command} is required")
    verify_font_sources()
    with tempfile.TemporaryDirectory(prefix="ds-fontconfig-") as tmp:
        env = font_environment(Path(tmp))
        render_samples(env)
    write_glyph_report()
    write_manifest()
    print(f"Built typography system v{VERSION}: {len(FONT_FILES)} font styles and {len(SAMPLE_DOCS)} proof sheets.")


if __name__ == "__main__":
    main()
