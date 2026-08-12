# ADR 0003: Repository topology and ownership boundaries

- Status: Accepted
- Date: 2026-08-12
- Decision owners: Definitely Secure Studio
- Related issue: [#25 — Define repository architecture, naming, and ownership boundaries](https://github.com/DefinitelySecureStudio/studio/issues/25)
- Parent epic: [#2 — Repository Architecture](https://github.com/DefinitelySecureStudio/studio/issues/2)

## Context

Definitely Secure Studio needs separate homes for organization governance,
stable creative-production contracts, experiments, production software, public
canon, and unrevealed lore. If those concerns share a repository, a public tool
can accidentally disclose proprietary story material, an experiment can become
an undocumented production contract, or an implementation can become the de
facto owner of a specification.

The first repository, `studio`, already owns the public Studio identity and
organization-level decisions. Epic #2 proposes five additional repositories:
`platform`, `codex`, `lab`, `universe`, and `lore`. Their visibility, authority,
and allowed relationships must be decided before they are created.

## Decision

Adopt six v1 repositories, each with one responsibility:

- public `studio` owns organization governance, portfolio direction, and the
  public brand system;
- public `codex` owns stable, implementation-neutral specifications and schemas;
- public `lab` owns experimental creative-production research using synthetic or
  already-public data;
- public `platform` owns production software and deployable tooling;
- public `universe` owns reader-safe canon and the public publication record; and
- private `lore` owns hidden world-building, unrevealed continuity, and approved
  private context packages.

Public tooling repositories must remain content-neutral. They may define or
implement mechanisms for handling creative context, but they must not contain
private lore, unpublished canon, secrets, or real private context in examples,
fixtures, logs, or source. `platform` consumes public canon or minimal approved
private exports; it never owns the underlying creative material.

`lab` is explicitly non-authoritative. A stable contract is promoted to `codex`;
a proven implementation is promoted or reimplemented in `platform`. Promotion
subjects the work to the destination repository's review and versioning rules.

`universe` and `lore` are deliberately separate. Reader-safe facts move from
`lore` to `universe` only through editorial review. The public repository must
remain independently usable without access to the private repository.

Cross-repository dependencies follow the direction documented in
[`ARCHITECTURE.md`](../ARCHITECTURE.md). Circular build dependencies are
prohibited. Cross-repository artifacts record source revision and contract
version; issue #33 will select the precise versioning and distribution
mechanisms.

Repository names use lowercase ASCII kebab-case, omit a redundant organization
prefix, and name one durable responsibility. New repositories require a distinct
ownership or access boundary and an amendment to the architecture decision.

Brand source remains in `studio`; approved public creative assets and comic
release records live in `universe`; production software releases live with
`platform`. High-resolution masters and editable creative sources remain in
approved private asset storage outside the v1 Git repositories and are referred
to by immutable release metadata.

## Rationale

The topology follows the types of authority that change at different speeds.
Governance, stable contracts, experiments, implementations, public canon, and
private story planning have different reviewers, publication risk, and release
cadences. Giving each one a single home makes provenance and access decisions
explicit.

Keeping `codex`, `lab`, and `platform` public supports reusable open tooling and
matches the Studio's public technical identity without exposing proprietary IP.
Keeping `universe` public provides a transparent reader-safe canon source.
Keeping `lore` private is the hard security boundary for unrevealed material.

Short repository names remain legible under the organization namespace and
avoid binding repositories to a current language, team, or deployment model.

## Consequences

### Positive

- Every v1 concern has one authoritative owner.
- Public tooling can be developed without granting access to proprietary lore.
- Experiments have an explicit path into stable contracts and production code.
- Public canon remains available without private repository access.
- The production pipeline can consume content without taking ownership of it.
- Future repositories have a predictable naming and approval rule.

### Tradeoffs

- Related changes may require coordinated pull requests across repositories.
- Public test fixtures must be curated or synthetic rather than copied from
  private production context.
- Lore-to-canon promotion is an editorial step instead of automatic sync.
- Large creative masters need a separate private storage and backup policy.
- Version distribution and compatibility require a follow-up decision in issue
  #33.

## Rejected alternatives

### Keep all work in `studio`

Rejected because governance, code, experiments, and creative IP would share an
access boundary and authority model. The repository would become a monolith with
high accidental-disclosure risk.

### Combine `codex`, `lab`, and `platform`

Rejected because exploratory work, stable contracts, and production
implementations have different maturity and change-control requirements.
Combining them would make it difficult to know which behavior is authoritative.

### Combine `universe` and `lore`

Rejected because one repository cannot be both a public canon source and a safe
home for unrevealed material. Directory conventions are not a sufficient access
control boundary.

### Make all repositories private

Rejected because it prevents public collaboration on content-neutral tooling and
reader-safe canon without materially improving the protection of lore, which has
its own private repository.

### Put creative source assets in `platform`

Rejected because a software implementation must not own brand or story IP, and
large editable assets have storage and access requirements that differ from
source code.

## Implementation

The complete matrix, diagram, content-location rules, dependency map, and naming
convention live in [`ARCHITECTURE.md`](../ARCHITECTURE.md).

Issues #26–#30 create the five remaining repositories using these boundaries.
Issue #31 decides licensing without changing visibility. Issue #32 establishes
organization-wide templates and defaults. Issue #33 finalizes dependency
versioning, compatibility, and release provenance.
