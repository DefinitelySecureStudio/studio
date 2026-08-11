# Definitely Secure comic identity

Status: Approved

Owner: Definitely Secure Studio

Last updated: 2026-08-11

## Core identity

- **Official comic title:** *Definitely Secure*
- **Official subtitle:** A workplace comic about systems, certainty, and the people in between.
- **Series title:** *Definitely Secure*
- **Universe reference:** the *Definitely Secure* universe
- **Fictional company:** Definitely Secure
- **Publisher and producer:** Definitely Secure Studio
- **Publication cadence:** ongoing
- **Canonical comic ID prefix:** `DS`

The subtitle is descriptive copy, not part of the title. It may accompany the title on profile pages, launch materials, collection covers, and metadata, but individual episodes do not need to display it.

## Positioning

### Reader promise

The name *Definitely Secure* promises a workplace where confidence is abundant, systems are complicated, and the truth lives somewhere between the status report and the people doing the work. The comic combines technically observant humor with character-driven stories that remain accessible without specialist knowledge.

### One-sentence pitch

*Definitely Secure* is a workplace comic about confident systems, messy reality, and the people trying to keep both running.

### Short description

*Definitely Secure* is a character-driven workplace comic about technology, bureaucracy, and the gap between confident language and operational reality. Inside a company that always has everything under control, people troubleshoot broken systems, shifting priorities, and one another. No technical background—and absolutely no incident report—is required.

### Long description

*Definitely Secure* is a character-driven workplace comic about technology, bureaucracy, and the systems people are expected to trust. Set inside a fictional company that projects absolute confidence, the series follows the people doing their best behind the dashboards, status reports, policies, and reassuringly green indicators.

Each episode finds humor in the gap between how work is described and how it actually happens: plans meet production, certainty meets evidence, and ordinary people inherit extraordinary technical decisions. The details reward readers who know the territory, but the stories do not require a technical background. The real subject is the human experience of modern work—communication, ambition, confusion, care, and the small negotiations that keep organizations moving.

*Definitely Secure* is an ongoing comic and expanding creative universe from Definitely Secure Studio. Individual strips stand on their own while recurring characters, workplace history, and consequences build over time. It is for anyone who has watched a simple request become a process, attended a meeting about another meeting, or wondered why the system marked everything healthy while smoke came out of the server room.

## Naming architecture

```text
Definitely Secure Studio (real-world studio, publisher, and producer)
└── Definitely Secure (comic, series, and creative universe)
    ├── Definitely Secure (fictional company and primary setting)
    ├── DS-0001 — Episode Title
    ├── DS-0002 — Episode Title
    └── Characters, locations, lore, and supporting stories
```

*Definitely Secure* serves as both the comic title and the umbrella for its creative universe. “The *Definitely Secure* universe” is a descriptive phrase, not a separate consumer-facing brand such as “Definitely Secure Universe.” The fictional company is Definitely Secure; do not add “Inc.” unless a future story establishes a specific legal entity for an in-world purpose.

Typography and context distinguish the uses:

- Italicize *Definitely Secure* when referring to the comic, series, or universe.
- Use plain text for Definitely Secure, the fictional company.
- Use Definitely Secure Studio for the real-world creator and publisher.
- In plain-text systems that cannot use italics, add a clarifying noun when ambiguity matters: “the Definitely Secure comic” or “the Definitely Secure company.”

## Episode system

### Public episode format

Every published strip receives a permanent sequential number and a title:

> *Definitely Secure* #0001 — Episode Title

Numbers begin at `#0001`, use four digits, and are never reused. Number episodes by canonical publication order, not chronology inside the story. Titles use headline-style capitalization, remain concise, and should add context or a second joke without explaining the punchline.

Public numbering is required on archive pages, permalinks, accessible descriptions, and collection tables of contents. Artwork should include the number where legible; promotional crops may omit it. A title may be temporarily recorded as “Untitled” during production, but every published episode receives a final title.

### Canonical identifiers

| Item | Format | Example |
| --- | --- | --- |
| Comic ID | `DS-NNNN` | `DS-0001` |
| Public number | `#NNNN` | `#0001` |
| Display title | `Definitely Secure #NNNN — Episode Title` | `Definitely Secure #0001 — Green Across the Board` |
| URL slug | `NNNN-episode-title` | `0001-green-across-the-board` |
| Release basename | `definitely-secure-NNNN-episode-title` | `definitely-secure-0001-green-across-the-board` |
| Source directory | `DS-NNNN/` | `DS-0001/` |

The comic ID is immutable. Correcting a published episode does not create a new number; append a revision identifier such as `-r2` to internal or distribution filenames when a platform needs to distinguish the corrected asset. Publication dates belong in metadata, not canonical IDs or filenames.

### Cadence language

Describe *Definitely Secure* as an “ongoing workplace comic” or say “new episodes ongoing.” Do not promise “daily,” “weekday,” “weekly,” or another fixed schedule until a separately approved publishing plan establishes one.

## Presentation standards

### Cover and collection presentation

The primary cover hierarchy is:

1. *Definitely Secure*
2. A workplace comic about systems, certainty, and the people in between.
3. A Definitely Secure Studio production.

Episode covers and social cards may replace the subtitle with `#NNNN — Episode Title`. Collection titles follow `Definitely Secure: Collection Title`; volume numbering is optional until a collection program is defined.

### Standard comic footer

Use this compact footer on episode artwork:

> DEFINITELY SECURE • #NNNN • DEFINITELYSECURE.COM

Use this expanded footer in web pages, downloads, collections, and contexts with adequate room:

```text
Definitely Secure #NNNN — Episode Title
A Definitely Secure Studio production • definitelysecure.com
© [YEAR] Definitely Secure Studio. All rights reserved.
```

The title may use its approved wordmark treatment. Do not replace the Studio credit with the fictional company name.

### Publication credit

> A Definitely Secure Studio production.

Use joint-production wording from the [studio identity guide](studio-identity.md) when a partner shares production responsibility.

## Social media

### Instagram profile

- **Profile name:** Definitely Secure | Workplace Comic
- **Preferred handle:** `@definitelysecure`
- **Fallback handle:** `@definitelysecurecomic`
- **Profile text:** A workplace comic about systems, certainty, and the people in between. New episodes ongoing. A Definitely Secure Studio production.

Use the episode display title at first mention in post copy. Place the permalink or canonical URL in the post, profile link, or platform link surface when available.

### Hashtags

Use a small, consistent set rather than filling every available tag slot:

- Always: `#DefinitelySecure`
- Usually: `#DefinitelySecureComic`, `#WorkplaceComic`
- Optional, when genuinely relevant: up to three topical tags such as `#TechHumor`, `#OfficeHumor`, or `#Cybersecurity`
- Studio launches or behind-the-scenes posts: `#DefinitelySecureStudio`

Do not use `#Layer8` as a comic identifier. Do not invent episode-specific brand hashtags unless a campaign needs one.

## Website, search, and metadata

### Page naming

- Series home title: `Definitely Secure — A Workplace Comic`
- Episode SEO title: `Episode Title | Definitely Secure #NNNN`
- Episode heading: `#NNNN — Episode Title`
- Archive label: `Definitely Secure archive`

### Metadata description

> Definitely Secure is a workplace comic about confident systems, messy reality, and the people trying to keep both running. An ongoing series from Definitely Secure Studio.

Use “workplace comic,” “technology,” “office humor,” and the episode’s actual subject naturally in descriptions. Do not stuff pages with repeated variants or lead with the retired working title “Layer 8.” Historical material may say “originally developed under the working title *Layer 8*” when provenance is relevant.

Each episode page should expose its canonical ID, episode number, title, publication date, creator or Studio credit, canonical URL, social-sharing image, and useful image alternative text. Alternative text describes the strip rather than repeating keyword lists.

## Naming rules

| Do | Don’t | Reason |
| --- | --- | --- |
| *Definitely Secure* | *Definitely Secure Inc.* | The comic title has no corporate suffix. |
| the *Definitely Secure* universe | the Definitely Secure Universe™ | The universe does not need a separate branded name. |
| Definitely Secure (fictional company) | Definitely Secure Studio (fictional company) | The Studio is the real-world producer. |
| *Definitely Secure* #0007 — Title | Episode 7 / DS7 | Four-digit numbering is stable and sortable. |
| ongoing workplace comic | daily comic | Do not promise an unapproved cadence. |
| `#DefinitelySecure` | `#Layer8` | Use the official public title for discovery. |
| A Definitely Secure Studio production. | Presented by Definitely Secure. | Credit the real producer, not the fictional company. |

## Publication checklist

Before release, confirm:

1. The episode has an unused `DS-NNNN` identifier and final title.
2. The display title, slug, filename, and artwork number agree.
3. The comic title is distinct from the fictional company through typography or context.
4. The Studio production credit and current copyright year are present where space permits.
5. Metadata includes the canonical URL, publication date, social image, and useful alternative text.
6. Social copy uses the primary hashtag and makes no unsupported cadence promise.

## Decision record

The rationale and consequences of this system are recorded in [ADR 0002](../adr/0002-comic-naming-and-publication-architecture.md).
