# Typography glyph verification

Generated: 2026-08-11

Test string: `0 O 1 l I | / \  {} [] ()  <= != ==  --flag=value`

Every approved production font was shaped with HarfBuzz. A `.notdef` or glyph ID 0 would fail the build.

| Font file | Result | Glyph count |
| --- | --- | ---: |
| `barlow-condensed/BarlowCondensed-SemiBold.ttf` | Pass | 47 |
| `barlow-condensed/BarlowCondensed-Bold.ttf` | Pass | 47 |
| `barlow-condensed/BarlowCondensed-ExtraBold.ttf` | Pass | 47 |
| `barlow-condensed/BarlowCondensed-BlackItalic.ttf` | Pass | 47 |
| `atkinson-hyperlegible/AtkinsonHyperlegible-Regular.ttf` | Pass | 49 |
| `atkinson-hyperlegible/AtkinsonHyperlegible-Italic.ttf` | Pass | 49 |
| `atkinson-hyperlegible/AtkinsonHyperlegible-Bold.ttf` | Pass | 49 |
| `atkinson-hyperlegible/AtkinsonHyperlegible-BoldItalic.ttf` | Pass | 49 |
| `ibm-plex-mono/IBMPlexMono-Regular.ttf` | Pass | 49 |
| `ibm-plex-mono/IBMPlexMono-Italic.ttf` | Pass | 49 |
| `ibm-plex-mono/IBMPlexMono-Medium.ttf` | Pass | 49 |
| `ibm-plex-mono/IBMPlexMono-SemiBold.ttf` | Pass | 49 |

Visual differentiation is recorded in the specimen and mobile test. Automated coverage confirms presence, not perceptual quality; inspect the generated proofs whenever files or renderers change.
