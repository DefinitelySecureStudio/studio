# ADR 0004: Repository licensing and intellectual-property boundaries

- Status: Accepted
- Date: 2026-08-15
- Decision owners: Definitely Secure Studio
- Related issue: [#31 — Define and apply repository licensing strategy](https://github.com/DefinitelySecureStudio/studio/issues/31)
- Parent epic: [#2 — Repository Architecture](https://github.com/DefinitelySecureStudio/studio/issues/2)

## Context

The Studio publishes reusable software and specifications alongside public
governance, brand material, comics, characters, artwork, and reader-safe canon.
Repository visibility alone does not communicate which material may be reused.
Without an explicit boundary, an open-source software license could appear to
cover proprietary creative work, or public access could be mistaken for a grant
of trademark or merchandising rights.

The licensing model must also account for third-party dependencies and assets,
whose licenses cannot be replaced by a Studio-wide decision.

## Decision

Apply Apache License 2.0 to original work in the public, content-neutral tooling
repositories `platform`, `codex`, and `lab`. This includes original source code,
configuration, documentation, specifications, schemas, prompts, test fixtures,
and examples unless a file is explicitly marked otherwise. These repositories
must contain only synthetic, licensed, or already-public creative fixtures.

Do not apply an open-source license at repository scope to `studio`, `universe`,
or `lore`:

- `studio` remains public but proprietary. Its governance documents, brand
  system, logos, Prompt Mark, wordmarks, and original assets are all rights
  reserved unless a file or directory has an explicit separate license.
- `universe` remains public but proprietary. Characters, settings, canon,
  stories, comics, dialogue, artwork, publication assets, and metadata are all
  rights reserved unless an individual release expressly grants narrower
  rights.
- `lore` remains private and proprietary. Access is limited to authorized Studio
  work and grants no right to disclose, reproduce, or distribute its contents.

Each repository must have a root `LICENSE`, a root `NOTICE`, and an explicit
README licensing section. Apache-2.0 repositories use the unmodified canonical
license text. Their NOTICE files identify the work and state that the software
license grants no rights in Studio marks or separately supplied creative
material. Proprietary repositories use the standard all-rights-reserved
language maintained in `studio/licensing/templates/`.

Software licensing, copyright ownership, and trademark permission are separate.
Apache-2.0 does not grant permission to use Studio names, trademarks, service
marks, logos, or product names except as the license permits for origin and
attribution. Brand or creative assets are never imported into an Apache-2.0
repository unless they carry a compatible, explicit asset license.

Third-party material remains under its original terms. Maintainers must verify
provenance and compatibility before adding it, preserve required notices, and
record it in the repository's dependency or attribution inventory. Unknown or
unverifiable material is not accepted. Copyleft code, restricted data, model
outputs, fonts, artwork, audio, and other non-code assets require review under
the rules in [`licensing/THIRD_PARTY.md`](../licensing/THIRD_PARTY.md).

## Rationale

Apache-2.0 supports broad use of the Studio's reusable tooling and provides an
express patent grant while preserving notices and excluding trademark rights.
Keeping the creative and brand repositories proprietary preserves a clear
commercial and editorial boundary without making public canon inaccessible to
readers.

Per-repository files make the applicable terms visible to people who encounter
a repository without the organization architecture. A shared policy and
templates keep those files consistent.

## Consequences

### Positive

- Every v1 repository has an explicit licensing classification.
- Reusable tooling can accept contributions and be redistributed under a known
  license.
- Public creative content is visibly readable without being implicitly reusable.
- Trademark, creative-IP, and software-license boundaries are stated separately.
- Third-party provenance and notice obligations are part of repository review.

### Tradeoffs

- Changes that move between tooling and creative repositories need a licensing
  review as well as an architectural review.
- Mixed repositories require file-level notices and cannot rely only on the root
  license.
- Some third-party licenses or asset terms will require case-by-case review.
- The policy and templates should be reviewed by qualified counsel before they
  are relied on for a material commercial transaction or enforcement action.

## Rejected alternatives

### Apache-2.0 across all public repositories

Rejected because public visibility is not an intent to grant adaptation,
merchandising, or redistribution rights in the Studio's brand or creative
universe.

### A custom source-available license for tooling

Rejected because a standard OSI-approved license is clearer for contributors
and downstream users and avoids creating an unfamiliar software license.

### No root license in proprietary repositories

Rejected because silence leaves public visitors uncertain. An explicit
all-rights-reserved notice states the boundary and identifies third-party
exceptions.

## Implementation

The authoritative matrix and operational rules live in
[`licensing/POLICY.md`](../licensing/POLICY.md). Standard repository files and
README language live in [`licensing/templates/`](../licensing/templates/) and
[`licensing/README-BOILERPLATE.md`](../licensing/README-BOILERPLATE.md).
