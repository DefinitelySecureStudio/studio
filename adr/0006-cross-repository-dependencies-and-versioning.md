# ADR 0006: Cross-repository dependencies, versioning, and provenance

- Status: Accepted
- Date: 2026-08-15
- Decision owners: Definitely Secure Studio
- Related issue: [#33 — Define cross-repository dependency and versioning strategy](https://github.com/DefinitelySecureStudio/studio/issues/33)
- Parent epic: [#2 — Repository Architecture](https://github.com/DefinitelySecureStudio/studio/issues/2)

## Context

The Studio architecture assigns stable contracts, experiments, production
software, public canon, and private lore to separate repositories. Production
still needs exact inputs from several owners. Depending on moving branches,
cloning content repositories at build time, or recording only a friendly
version would create hidden coupling and make a published comic impossible to
audit or reproduce.

The workflow also appears cyclic: Platform consumes Universe and Lore inputs,
then proposes a release record back to Universe. That editorial workflow must
not become a cyclic build graph or allow Platform to take ownership of canon.

Private Lore creates a second tension. Internal provenance must identify the
exact private source, but the public release record must not reveal private
paths, revisions, filenames, or derivable content hashes.

## Decision

Use released, content-addressed artifacts as the cross-repository boundary.
Every stable reference combines:

1. a human-readable semantic version and immutable release tag;
2. the exact source commit SHA;
3. an artifact URI, media type, and byte size; and
4. a verified `sha256:` content digest.

Tags and versions support discovery and compatibility decisions. Digests are
the artifact identity. Commit SHAs provide source traceability. A branch name,
tag, version range, or commit SHA alone is not a complete production pin.

Enable immutable GitHub Releases for public repositories that publish release
assets. Attach all assets to a draft, then publish it once. Codex publishes
versioned contract bundles; Universe publishes canon snapshots; Platform
publishes software packages or OCI images. Prefer the ecosystem registry for a
package and an OCI digest for containers. Use GitHub Release assets for portable
specification, schema, fixture, canon, and provenance bundles.

Do not use Git submodules, branch references, live cross-repository checkouts,
or vendored repository copies as production dependencies. A temporary commit-
SHA reference is allowed before the first artifact release only when it is
recorded as provisional and replaced before a production release.

Stable contracts move from Lab to Codex by review, not dependency. A promotion
records the Lab source commit as lineage, then Codex assigns authority, owners,
version, schemas, fixtures, and an immutable release. Platform implements the
released Codex contract. A promoted Platform implementation is likewise new
production-owned work, not an import from a Lab branch.

Platform consumes public canon as a released Universe snapshot and private
context as a minimal, encrypted, versioned Lore export delivered through an
approved secure artifact store. It never clones Universe or Lore during a build
and never embeds their authoritative source.

Provenance has paired records:

- the public Universe release manifest records exact public dependencies,
  rendition digests, build identity, and an opaque private-context attestation
  ID; and
- a restricted Lore or production provenance record maps that opaque ID to the
  exact Lore commit, context-package object version and digest, contract
  version, approval, retention, and deletion requirements.

The opaque attestation ID must be random and non-derivable from private content.
The public record never exposes a Lore commit, path, object URI, or content
digest.

The apparent Platform/Universe cycle is split into ordered releases. Platform
builds against canon snapshot `C(n)` and emits release `R`. Canon editors then
accept `R` into a later snapshot `C(n+1)`. `R` records `C(n)` as its input;
`C(n+1)` may record `R` as included output. No artifact depends on itself or on
a downstream result.

Semantic Versioning 2.0.0 governs software and Codex contracts. Universe keeps
its documented semantic canon policy. Breaking contract changes require a new
major version, accepted RFC, migration guide, affected-consumer inventory,
parallel fixtures, and a dated compatibility window. Exact rules live in
[`dependency-strategy/COMPATIBILITY.md`](../dependency-strategy/COMPATIBILITY.md).

## Rationale

This model separates compatibility intent from artifact identity. Versions tell
maintainers whether an upgrade should be compatible; digests prove which bytes
were consumed. Source SHAs and build attestations preserve an audit path without
making Git repositories runtime dependencies.

Immutable releases fit the current GitHub-based workflow and protect tags and
assets after publication. OCI digests extend the same content-addressed model to
containers. Paired public and private provenance preserves auditability without
turning private Lore metadata into a spoiler channel.

## Consequences

### Positive

- Production dependencies are exact, verifiable, and independently retrievable.
- Contract and implementation authority remain in their owning repositories.
- Build and runtime dependency graphs remain acyclic.
- Comic releases can be audited to exact public inputs and securely to exact
  private inputs.
- A compromised or moved human-readable reference cannot silently change pinned
  bytes when digest verification is enforced.

### Tradeoffs

- Releases require packaging, checksums, and provenance records in addition to
  tags.
- Cross-repository upgrades become explicit pull requests.
- Private provenance requires a secure store and retention process outside the
  public repositories.
- Existing pre-release work must create initial artifact releases before it can
  become a production dependency.

## Rejected alternatives

### Pin only a Git tag or semantic version

Rejected because a friendly reference communicates compatibility but does not
by itself verify downloaded bytes or preserve all build provenance.

### Pin only a commit SHA

Rejected as the stable mechanism because a commit does not identify the packaged
artifact, its media type, build process, or compatibility promise.

### Git submodules or build-time repository clones

Rejected because they couple availability, permissions, directory layout, and
source ownership to the consumer build and make private boundaries fragile.

### Publish private Lore revisions in public manifests

Rejected because even metadata can leak editorial timing, enable correlation,
or expose identifiers useful in a later compromise.

## Implementation

The normative operating policy, compatibility rules, provenance fields, and
non-normative examples live in
[`dependency-strategy/`](../dependency-strategy/README.md). Codex owns the future
machine-readable schemas for contract bundles, release manifests, and context
packages; these Studio examples do not become competing specifications.
