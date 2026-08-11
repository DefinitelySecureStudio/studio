# ADR 0002: Comic naming and publication architecture

- Status: Proposed
- Date: 2026-08-11
- Decision owners: Definitely Secure Studio
- Related issue: [#9 — Finalize comic branding](https://github.com/DefinitelySecureStudio/studio/issues/9)
- Supersedes the working title: *Layer 8*

## Context

The flagship comic needs one title and a durable publication system across artwork, Instagram, the website, repositories, archives, and future collections. The earlier working title, *Layer 8*, is already used by many unrelated brands and projects. ADR 0001 establishes Definitely Secure Studio as the real-world parent, *Definitely Secure* as the flagship comic and creative universe, and Definitely Secure as the fictional workplace without a corporate suffix.

Issue #9 proposed three architectures:

- Option A: *Definitely Secure* as the comic, “Definitely Secure Universe” as the universe, and Definitely Secure Inc. as the setting.
- Option B: *Definitely Secure Inc.* as both comic and setting beneath a *Definitely Secure* universe.
- Option C: *Incident Report* as the comic beneath a *Definitely Secure* universe, set at Definitely Secure Inc.

The identity also needs a subtitle, reader promise, episode-title policy, stable numbering, credits, social naming, and search conventions.

## Decision

Adopt a refined **Option A** that conforms to ADR 0001:

```text
Definitely Secure Studio
└── Definitely Secure (comic, series, and creative universe)
    ├── Definitely Secure (fictional company and primary setting)
    └── DS-NNNN — Episode Title (individual comic episode)
```

The official comic and series title is ***Definitely Secure***. Its official subtitle is **“A workplace comic about systems, certainty, and the people in between.”** The subtitle is descriptive copy rather than part of the legal or canonical title.

The creative setting is referred to descriptively as “the *Definitely Secure* universe.” It does not receive a separate consumer-facing “Definitely Secure Universe” brand. The fictional company is **Definitely Secure**, without “Inc.”

Every published strip receives:

- a permanent canonical ID in the form `DS-NNNN`, beginning with `DS-0001`;
- a public number in the form `#NNNN`;
- a concise, final episode title; and
- a display title in the form `Definitely Secure #NNNN — Episode Title`.

The number records canonical publication order. It is stable across corrections, platform reposts, translations, and collections. Publication dates remain metadata rather than part of the identifier.

The comic is described as “ongoing.” No daily, weekday, weekly, or other fixed cadence is promised until a publishing plan separately approves one.

The standard publication credit is “A Definitely Secure Studio production.” Social profiles lead with the comic title and “Workplace Comic.” Search titles combine the episode title, series title, and public number.

## Rationale

Using *Definitely Secure* for the comic preserves the strongest connection among the property, domain, and established Studio identity. It also makes the title itself part of the joke: confident assurance sits against the operational reality depicted in each strip. The approved subtitle explains the premise to new readers without narrowing the comic to cybersecurity or requiring technical knowledge.

Treating the universe name as a descriptive use of the comic title avoids creating a fourth brand for readers to learn. Keeping the fictional company free of “Inc.” follows the approved parent architecture and leaves legal suffixes available as story details rather than identity requirements.

Four-digit sequential IDs are legible, sortable, and sufficient for a long-running publication. Separating immutable IDs from dates and platform-specific filenames makes archives and corrections predictable. Requiring episode titles improves navigation, accessibility, conversation, and search while allowing each strip to retain a compact numeric reference.

## Consequences

### Positive

- One title works consistently across artwork, profiles, archives, and search.
- The subtitle immediately communicates genre, tone, and subject.
- Stable IDs support long-term archives, files, feeds, and collections.
- Episode titles make strips easier to remember, share, and discover.
- “Ongoing” leaves room to establish a sustainable publishing cadence later.
- Studio credits remain distinct from the fictional company.

### Tradeoffs

- The comic, universe, and fictional company deliberately share a name, so typography or a clarifying noun is sometimes necessary.
- Four-digit numbers look more formal than unpadded numbers, particularly in early episodes.
- Every episode needs a title before publication.
- Renaming from *Layer 8* requires old internal references and early promotional material to migrate.

## Rejected alternatives

### Option A exactly as proposed

Rejected because “Definitely Secure Universe” adds an unnecessary branded layer and “Definitely Secure Inc.” conflicts with ADR 0001. The refined Option A keeps the useful comic-title choice without those conflicts.

### Option B: *Definitely Secure Inc.*

Rejected because a corporate suffix makes the comic sound like a legal entity, weakens the cleaner title, and conflicts with the approved studio architecture.

### Option C: *Incident Report*

Rejected because it gives up the strongest established name, frames every story as an incident, and makes the relationship among the comic, domain, and public profiles less obvious. “Incident Report” remains available for an episode, recurring feature, or collection title.

### Unnumbered episodes

Rejected because titles and dates alone do not provide a compact, immutable ordering key across platforms and archives.

### Date-based canonical IDs

Rejected because release dates can change and do not express canonical order cleanly. Dates remain publication metadata.

## Implementation

The canonical descriptions, presentation copy, social rules, episode identifiers, filenames, metadata, and release checklist live in [`brand/comic-identity.md`](../brand/comic-identity.md). Existing references to *Layer 8* should be inventoried and migrated as public surfaces and production systems are built or revised.

This decision depends on [ADR 0001](0001-studio-naming-and-brand-architecture.md). If the parent architecture changes, review this ADR for naming conflicts before publishing new material.
