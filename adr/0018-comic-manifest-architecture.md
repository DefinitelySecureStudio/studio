# ADR 0018: Comic Manifest architecture and authority boundaries

- Status: Proposed; acceptance requires owner-approved merge and coordinated Codex/Platform review
- Date: 2026-09-17
- Decision owner: @andrewperis; Universe editors retain publication/canon authority; source owners retain access/disclosure authority
- Issue: [#88](https://github.com/DefinitelySecureStudio/studio/issues/88)
- Epic: [#6](https://github.com/DefinitelySecureStudio/studio/issues/6)
- Constitution: v1.0.0, tag `constitution/v1.0.0`, commit `a9cc8a503aa30e17820edc62ac95f7cbe10e0564`
- Profiles: universal; ADR/specification; repository/production system; automated workflow
- Evidence: [architecture, acceptance slice and scoped assessment](../comic-manifest/ARCHITECTURE.md); adopting PR and affected-owner reviews
- Supplements: [ADR 0002](0002-comic-naming-and-publication-architecture.md), [ADR 0006](0006-cross-repository-dependencies-and-versioning.md), [ADR 0016](0016-prompt-sdk-architecture.md), [ADR 0017](0017-context-builder-architecture.md)

## Context

Released Prompt SDK and Context Builder foundations provide execution and
authorized context preparation. Comic production needs a portable declaration of
intent, exact inputs and required outputs without introducing a workflow engine
or confusing build success with publication permission. A single mutable record
would mix protected drafts, execution evidence and reader-safe publication data.

## Decision

Adopt the proposed [Comic Manifest v1 architecture](../comic-manifest/ARCHITECTURE.md)
as the design boundary for Epic #6. Define three separately versioned, immutable,
linked records: production manifest, build-result record and public release
manifest. Links to protected records stay restricted; public private-context
evidence uses an explicitly approved, random opaque attestation.

Studio owns this cross-repository decision. Codex owns normative contracts and
fixtures. Platform owns validation, integrity verification, review tooling and
safe projection; future Epic #7 execution produces build results. Universe owns
approved public release records. Lore or an approved private store holds
protected production material and provenance; public tooling never checks out
Lore. Lab is optional experimentation, never a production dependency.

Use stable opaque draft identities and immutable revisions. Assign permanent
`DS-NNNN` identities separately under Universe editorial authority in canonical
publication order; never reuse them. Corrections preserve episode identity and
append revisions/events. V1 describes ordered panels, text, assets and rendition
requirements, not illustration, lettering or layout execution.

Preparation, current exact-instance package use, review, attestation, and A4
publication/canon decisions are distinct gates. Approval binds actual candidate
bytes, artifact set, inputs, scope and release conditions. A digest, status field,
successful validator or historical grant cannot create or renew authority.

## Alternatives and consequences

- One mutable manifest is rejected: it obscures revision history and risks
  publishing protected evidence. Separate records require explicit linkage and
  invalidation checks but preserve independent authority and visibility.
- Reserving public episode numbers at draft creation is rejected: drafts do not
  establish canonical publication order. Separate identities require a reviewed
  mapping and collision handling at the publication boundary.
- Embedded commands/workflows are rejected: the manifest declares requirements;
  Epic #7 owns execution policy and coordination.
- Automatic redaction/publication is rejected: omission rules cannot determine
  whether prose, URLs or artifacts disclose private meaning. An allowlisted
  projection still requires qualified human disclosure and publication review.
- New local variants of released foundations are rejected: gaps return to Codex
  for versioned contracts and compatibility review, preserving released bytes.

## Rollout and acceptance

#89 resolves the contract gaps identified in the architecture before #90–#98
implement and test consumers. #99 separately publishes immutable releases.
An offline synthetic slice exercises the complete record boundary without real
canon, private sources, providers or orchestration. Focused tests accompany each
implementation; the final suite consolidates them.

Owner acceptance approves this architecture only. Record Codex contract review
and Platform feasibility review against the exact proposed revision before
marking this ADR accepted or #88 owner-reviewed. Production trust onboarding,
real-source access, creative decisions and publication remain separately scoped.
Reassess on contract, authority, classification, identity, storage, consumer or
release-boundary changes. No constitutional amendment or exception is proposed.
