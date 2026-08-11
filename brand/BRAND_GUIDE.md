# Definitely Secure Brand Guide

Status: Proposed for v1.0 approval

Owner: Definitely Secure Studio

Version: 1.0.0

Last updated: 2026-08-11

## Authority and use

This is the entry point for the Definitely Secure Studio brand system. It consolidates the approved Epic 1 decisions and resolves everyday questions; the linked component guides remain authoritative for production detail. If two rules appear to conflict, use this order:

1. the latest accepted architecture decision record;
2. the relevant approved component guide;
3. this guide; and
4. examples or generated previews.

Do not silently invent a new name, lockup, color, font, credit, or publication convention. Propose a documented revision and record it in the [changelog](CHANGELOG.md).

## Brand in one minute

| Element | Approved rule |
| --- | --- |
| Real-world organization | Definitely Secure Studio |
| Flagship property | *Definitely Secure* |
| Fictional company | Definitely Secure |
| Mission | Create funny, humane, technically curious stories and tools that help people see the systems shaping their work and lives—and imagine better ones. |
| Studio tagline | Serious craft. Questionable systems. |
| Comic subtitle | A workplace comic about systems, certainty, and the people in between. |
| Production credit | A Definitely Secure Studio production. |
| Domain | `definitelysecure.com` |
| GitHub organization | `DefinitelySecureStudio` |

### Approved public description

> Definitely Secure Studio creates character-driven comics, animation, publications, and open-source tools about technology, work, and the people caught inside both.

### Comic pitch

> *Definitely Secure* is a workplace comic about confident systems, messy reality, and the people trying to keep both running.

## Architecture and naming

```text
Definitely Secure Studio (real-world studio and publisher)
├── Definitely Secure (flagship comic and creative universe)
│   ├── Definitely Secure (fictional workplace/company)
│   ├── DS-NNNN — Episode Title
│   └── Characters, locations, and lore
├── Future creative properties
└── Open-source tools and experiments
```

- Write **Definitely Secure Studio** as three words; never “Definitely Secure Studios.”
- After the full name appears, “the Studio” is the only public prose shorthand.
- Italicize *Definitely Secure* when it means the comic, series, or universe.
- Use plain text for Definitely Secure, the fictional company.
- In plain text, add “comic” or “fictional company” when context does not disambiguate.
- Reserve `DefinitelySecureStudio` for the GitHub organization and other constrained technical identifiers.
- Do not add `Inc.`, `LLC`, `Press`, `Comics`, or `Productions` to the public name. Legal documents may use the registered entity name when required.
- The real Studio is not part of the fictional universe unless a work deliberately identifies a meta-fictional exception.

The rationale is recorded in [ADR 0001](../adr/0001-studio-naming-and-brand-architecture.md) and [ADR 0002](../adr/0002-comic-naming-and-publication-architecture.md).

## Voice and tone

The voice is technically observant, humane, dry, and clear. It notices the absurdity of systems without treating the people inside them as disposable punchlines.

### Voice principles

1. **Know the detail.** Use accurate technical language when it adds meaning; explain it when a general reader needs the bridge.
2. **Keep the human in frame.** Critique incentives, process, and misplaced certainty before mocking someone for lacking information or power.
3. **Understate the joke.** Prefer precise contrast and earned irony to meme phrasing, forced snark, or a stream of exclamation marks.
4. **Say what happened.** Public information, documentation, and accessibility copy favor direct language over fictional corporate fog.
5. **Leave room for curiosity.** Confidence is part of the joke, not a license to sound contemptuous or omniscient.

### Tone by context

| Context | Tone | Example |
| --- | --- | --- |
| Studio introduction | Warm, assured, concise | “Stories and tools about technology, work, and the people caught inside both.” |
| Comic promotion | Wry and inviting | “Everything is green. The server room has requested comment.” |
| Documentation | Direct and technically exact | “Use the dark-surface logo on Assurance Ink.” |
| Incident or correction | Plain, accountable, specific | “The earlier image omitted alternative text. The corrected post includes it.” |
| In-world campaign | Deliberately overconfident, clearly labeled | “An in-world transmission from Definitely Secure.” |

Avoid generic hacker language, fear marketing, superiority jokes, childish comic-book phrasing, and claims that real products or systems are “secure” without evidence.

## Logo system

The Prompt Mark combines a speech bubble, a terminal prompt, and a Status Gold indicator. Use supplied assets; never redraw or retype a lockup.

| Need | Preferred asset |
| --- | --- |
| Default Studio identification | [`primary/definitely-secure-primary-light.svg`](../assets/brand/logos/primary/definitely-secure-primary-light.svg) |
| Wide Studio header | [`studio/definitely-secure-studio-horizontal-light.svg`](../assets/brand/logos/studio/definitely-secure-studio-horizontal-light.svg) |
| Comic title | [`comic/definitely-secure-comic-horizontal-light.svg`](../assets/brand/logos/comic/definitely-secure-comic-horizontal-light.svg) |
| Episode footer | [`comic/definitely-secure-comic-footer-light.svg`](../assets/brand/logos/comic/definitely-secure-comic-footer-light.svg) |
| Compact icon | [`icon/definitely-secure-prompt-mark-light.svg`](../assets/brand/logos/icon/definitely-secure-prompt-mark-light.svg) |
| Social profile | [`social/definitely-secure-social-avatar-dark.png`](../assets/brand/logos/social/definitely-secure-social-avatar-dark.png) |

Use the light-surface variant on light, quiet backgrounds and the dark-surface variant on dark, quiet backgrounds. Keep at least `3x` clear space around lockups and `2x` around icon-only marks, where `x` is the status-dot diameter. Minimum digital widths are 180px for the Studio horizontal lockup, 200px for the comic wordmark, and 320px for the comic footer. Use the small Prompt Mark at 16–19px.

Never stretch, rotate, recolor, crop, shadow, outline, animate, rearrange, or attach new words to a logo. Full production rules and all minimum sizes are in the [logo guidelines](logo-guidelines.md).

## Color

### Core palette

| Token | Name | Value | Primary role |
| --- | --- | --- | --- |
| `brand.primary.assurance-ink` | Assurance Ink | `#101828` | Primary text, marks, dark surfaces |
| `brand.primary.console-paper` | Console Paper | `#F8FAFC` | Light surfaces and reverse text |
| `brand.secondary.meeting-coral` | Meeting Coral | `#D95D52` | Warm editorial accent |
| `brand.secondary.protocol-violet` | Protocol Violet | `#6E62A6` | Secondary accent and focus |
| `brand.accent.status-gold` | Status Gold | `#F4B942` | Brand indicator and emphasis |
| `brand.accent.signal-teal` | Signal Teal | `#2F7F79` | Charts and environmental detail |

Assurance Ink and Console Paper carry the system. Use one supporting accent with them whenever possible. Status Gold is not the semantic warning token, and Signal Teal is not an unlabeled success state. Color never carries meaning alone.

For interfaces, use semantic tokens rather than raw values. For comics, use Comic Ink on Speech White, Panel Mist, Breakroom Paper, or Caption Cream. Character colors are not brand tokens. Consult the [color system](color-system.md), [machine-readable colors](tokens/colors.json), and [contrast report](accessibility-contrast-report.md) before production.

## Typography

| Role | Family | Approved weights |
| --- | --- | --- |
| Display | Barlow Condensed | 600, 700, 800 |
| Body | Atkinson Hyperlegible | 400, 400 italic, 700, 700 italic |
| Dialogue | Atkinson Hyperlegible | 400, 400 italic, 700 |
| Monospace | IBM Plex Mono | 400, 400 italic, 500, 600 |
| Sound effects | Barlow Condensed custom treatment | 900 italic |

- Website body is at least 16px with 1.55 line height; 18px is preferred.
- Comic dialogue is at least 16px at final size, with 18–22px preferred and 1.28–1.36 line height.
- Code is at least 14px digital with 1.5–1.65 line height, literal characters, and ligatures disabled.
- Body, dialogue, and mono tracking is zero. Do not tighten copy to force a fit.
- All-caps dialogue is reserved for shouting, labels, interfaces, or deliberate in-world convention.
- Use actual approved weights and canonical logo exports; never synthesize a face or retype a wordmark.

Full hierarchy, fallbacks, comic lettering rules, font licensing, and samples are in the [typography guide](typography.md). Implementations should use the [typography tokens](tokens/typography.json) and [CSS definitions](tokens/typography.css).

## Comic publication system

Every published episode receives an immutable four-digit identifier and final title.

| Field | Format | Example |
| --- | --- | --- |
| Canonical ID | `DS-NNNN` | `DS-0001` |
| Public number | `#NNNN` | `#0001` |
| Display title | `Definitely Secure #NNNN — Episode Title` | `Definitely Secure #0001 — Green Across the Board` |
| URL slug | `NNNN-episode-title` | `0001-green-across-the-board` |
| Release basename | `definitely-secure-NNNN-episode-title` | `definitely-secure-0001-green-across-the-board` |

Number by canonical publication order; never reuse an identifier. Describe cadence as “ongoing” until a publishing plan approves a fixed schedule.

Compact artwork footer:

> DEFINITELY SECURE • #NNNN • DEFINITELYSECURE.COM

Expanded credit:

```text
Definitely Secure #NNNN — Episode Title
A Definitely Secure Studio production • definitelysecure.com
© [YEAR] Definitely Secure Studio. All rights reserved.
```

Every episode page needs its ID, number, title, publication date, Studio credit, canonical URL, social image, and useful image alternative text. See the [comic identity guide](comic-identity.md) for complete publication and metadata rules.

## Social presentation

### Studio account

- Display name: **Definitely Secure Studio**
- Preferred handle: `@definitelysecure`; fallback: `@definitelysecurestudio`
- Bio: “Independent comics, animation, publications, and open-source tools about technology and work. Home of Definitely Secure. Serious craft. Questionable systems.”

### Comic account or comic-led profile

- Profile name: **Definitely Secure | Workplace Comic**
- Preferred handle: `@definitelysecure`; fallback: `@definitelysecurecomic`
- Bio: “A workplace comic about systems, certainty, and the people in between. New episodes ongoing. A Definitely Secure Studio production.”
- Always use `#DefinitelySecure`; usually add `#DefinitelySecureComic` and `#WorkplaceComic`; add no more than three genuinely relevant topical tags.

Do not present an ordinary account as the fictional company. Label an in-world post or campaign clearly enough that a reasonable reader can distinguish fiction from a Studio statement. Inspect final social graphics at 360px wide and include platform-native alternative text.

## Copyright, licensing, and attribution

Standard copyright line:

> © [YEAR] Definitely Secure Studio. All rights reserved.

Use a year range when appropriate. This wording does not replace a registered legal name when a contract or law requires it.

The Prompt Mark, wordmarks, and lockups are proprietary brand assets. Public repository access does not grant trademark, endorsement, merchandising, or adaptation rights. Third parties require written permission unless applicable law provides otherwise. See the [logo asset license](../assets/brand/logos/LICENSE.md).

Bundled Barlow Condensed, Atkinson Hyperlegible, and IBM Plex Mono files use the SIL Open Font License 1.1. Preserve each `OFL.txt` and the original font metadata when redistributing them. See the [font licensing record](../assets/brand/typography/FONT-LICENSES.md).

For open-source work, use:

> An open-source project from Definitely Secure Studio. See the repository license for terms.

The project’s license controls software reuse. Do not add “All rights reserved” in a way that contradicts it, and do not assume a software license grants rights to Studio branding.

## Accessibility baseline

All public and internal production work must meet this baseline:

1. Target WCAG AA for normal text and meaningful non-text contrast; use the approved tested pairs.
2. Do not encode status, links, selection, charts, or story-critical information through color alone.
3. Underline links in body copy and provide a visible keyboard focus shape.
4. Use useful alternative text for comics and promotional imagery; describe content and relevant action rather than repeating keywords.
5. Respect the final-size typography minimums after cropping and downsampling.
6. Keep comic dialogue and essential line work understandable in grayscale.
7. Preserve literal technical characters and test `0 O 1 l I | / \ {} [] () <= != == --flag=value` wherever code is shown.
8. Re-test after opacity, imagery, blending, compression, or print conversion changes effective contrast.

## Public and internal use

| Surface | Public requirement | Internal allowance |
| --- | --- | --- |
| Names | Full approved name and hierarchy | `DSS` may be a compact identifier, never release copy |
| Logos | Canonical exported asset | Editable master may be used only to generate canonical assets |
| Colors | Semantic token or approved print conversion | Raw values may be used for tests and asset generation |
| Type | Bundled approved family and real weight | Fallbacks may support drafts, never final line-break approval |
| Comic ID | Final immutable `DS-NNNN` | “Untitled” may be temporary; ID cannot be recycled |
| In-world voice | Clearly framed as fiction | Draft labels may be abbreviated but must not reach publication |
| Copyright | Current public ownership line | Legal entity name may replace display name where required |

Internal convenience does not create a new public brand rule. Draft files should make their status visible and must not be distributed as approved assets.

## Repository presentation

The organization is `DefinitelySecureStudio`; prose says Definitely Secure Studio. A public Studio repository should include:

- a clear project title and one-sentence purpose;
- “An open-source project from Definitely Secure Studio. See the repository license for terms.”;
- an applicable software or content license;
- the Studio horizontal logo only when ownership needs emphasis and minimum-size rules can be met;
- accessible image descriptions; and
- links that distinguish project documentation from brand-asset licensing.

Use the [repository README](../README.md) as the index for this brand repository. Do not turn ordinary developer documentation into fictional corporate copy.

## Production checklist

Before release, confirm:

1. The Studio, comic, and fictional company are named distinctly.
2. The correct canonical logo and surface variant are used at an approved size.
3. Colors use approved roles and retain non-color cues.
4. Typography uses approved families, weights, sizes, and final line breaks.
5. Comic IDs, titles, filenames, URLs, and credits agree.
6. Alternative text, contrast, focus, and mobile readability have been checked.
7. Copyright, open-source, font, and brand-asset terms are not conflated.
8. Public copy uses the appropriate voice and does not make an unsupported cadence or security claim.
9. The asset appears in the [asset index](ASSET_INDEX.md) or its family manifest.
10. Any rule change is recorded in the [changelog](CHANGELOG.md) and approved at the correct version level.

## Related records

- [Studio identity](studio-identity.md)
- [Comic identity](comic-identity.md)
- [Logo guidelines](logo-guidelines.md)
- [Color system](color-system.md)
- [Typography system](typography.md)
- [Accessibility contrast report](accessibility-contrast-report.md)
- [Asset index](ASSET_INDEX.md)
- [Design tokens](tokens/README.md)
- [Approval record](APPROVAL.md)
- [Changelog](CHANGELOG.md)

## Versioning and release

Brand Guide v1.0.0 becomes approved when issue #18 is verified, the approval record is updated, and Git tag `brand-v1.0.0` is created from the accepted commit. Until then, this file is a release candidate and must not be described as the final public guide.
