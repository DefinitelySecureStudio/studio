# ADR 0017: Context Builder architecture and authority boundaries

- Status: Proposed; acceptance requires owner-approved merge
- Date: 2026-09-11
- Decision owner: @andrewperis; source owners retain source-access decisions
- Issue: [#75](https://github.com/DefinitelySecureStudio/studio/issues/75)
- Epic: [#5](https://github.com/DefinitelySecureStudio/studio/issues/5)
- Constitution: v1.0.0, tag `constitution/v1.0.0`, commit `a9cc8a503aa30e17820edc62ac95f7cbe10e0564`
- Profiles: universal; ADR/specification; repository/production system; automated workflow
- Evidence: [architecture and scoped assessment](../context-builder/ARCHITECTURE.md), coordinated Platform ADR, adopting PR review
- Supplements: [ADR 0016](0016-prompt-sdk-architecture.md); no change to repository topology

## Context

Prompt SDK v1 is released and consumes prepared Context Package v1 documents,
references and separate use-authorization decisions. It does not implement
source discovery, selection or assembly. Builder v1 must fill that producer
boundary without treating a generated package, matching digest, retrieved fact
or caller-supplied allow flag as access authority.

ADR 0016 assigned context approval to the Builder boundary. This ADR clarifies
that wording: the Builder coordinates and verifies approval evidence; it does
not make reserved human judgments or issue its own production permissions.

## Decision

Adopt [Context Builder v1 architecture](../context-builder/ARCHITECTURE.md).
Platform implements the Builder as a separate capability from Prompt SDK.
Codex owns versioned build/source/policy/result meanings. Universe owns public
canon snapshots; Lore provides minimal approved exports through secure artifact
interfaces. Neither is cloned, mirrored or vendored into production tooling.

Use explicit deterministic selection and a versioned lexical ranking baseline.
All clocks, source bytes/identities, policy versions and budgets are explicit.
Keep I/O, trust verification and optional persistence behind injected interfaces.
Source content is data, never permission or executable instructions.

Distinguish four gates: preparation authority before access; classification
propagation during processing; separate exact-instance package use authorization;
and human canon/publication judgment. No gate substitutes for another.
Public evidence about private work contains approved opaque attestations rather
than private source identifiers, commits, locations, hashes or bodies.

Builder results are prepared artifacts, not approved creative truth. Downstream
Manifest and Orchestrator consume explicit package references and safe evidence;
they do not gain permission to refresh sources or renew authority implicitly.

## Alternatives and consequences

- Direct repository search/checkout is rejected: it broadens access and violates
  immutable artifact and private-export boundaries.
- Retrieval inside Prompt SDK is rejected: it creates competing ownership and
  hidden inputs to rendering.
- Embeddings, remote vector services and model summarization are deferred:
  they introduce provider, cost, nondeterminism and privacy decisions unnecessary
  for the explicit/lexical v1 baseline.
- Self-issued approval is rejected: integrity and schema validity do not establish
  human authority or authenticity of policy evidence.
- Pure core plus explicit adapters improves replay and testing, at the cost of
  requiring separately configured trust, source and secure-store mechanisms.
- Byte budgets are authoritative. Optional token estimates need named/versioned
  estimators and do not replace actual provider limits.

## Rollout and review

#76 defines contract gaps before implementation; #77–#85 implement and verify
the scoped pipeline. #86 publishes new contracts and implementation artifacts.
Released Context Package v1 bytes remain immutable; incompatible changes need
new versions, migration and owner review. No new contract is published by #75.

Owner merge approves this design only. Production trust, private data access,
storage/retention, real-source onboarding and release publication require their
own evidence and authorized decisions. Review this ADR on authority, source,
classification, ranking, persistence, provider or downstream-boundary changes.
