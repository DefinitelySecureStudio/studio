# ADR 0014: Constitutional amendment and exception process

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#47 — Define constitutional amendment and exception process](https://github.com/DefinitelySecureStudio/studio/issues/47)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)
- Constitutional article: [Amendment, versioning, and exceptions](../CONSTITUTION.md#12-amendment-versioning-and-exceptions)

## Context

The Constitution must evolve as the Studio learns, adds capabilities, and
discovers conflicts. Without its own change process, an ADR, urgent workaround,
repeated waiver, or convenient implementation could become a de facto amendment
without accountable approval or a durable record. Conversely, making every
editorial correction require the same migration as a breaking authority change
would make the Constitution unnecessarily rigid.

The first seven pre-v1 amendments established authority, Canon/Lore, provenance,
security/privacy/rights, quality/release, and portability. Their Git history is
traceable, but the Constitution needs an explicit semantic version policy,
version index, breaking-change procedure, downstream notification model, and
temporary exception register before it can become a stable v1 authority.

## Decision

Assign constitutional authority to Definitely Secure Studio acting through
named A4 constitutional stewards. Agents may draft, analyze, compare, and carry
out approved mechanical publication, but cannot propose on their own behalf,
approve, or make constitutional changes or exceptions effective.

Define an amendment by effect rather than label: any change to normative
meaning, authority, applicability, guarantees, obligations, prohibitions,
reserved decisions, definitions, the amendment process, or conformance is an
amendment. ADRs, specifications, policies, prompts, schemas, workflows, code,
and domain decisions remain lower-level implementations when conforming. An ADR
may explain an amendment but cannot make it effective.

Require each amendment proposal to pin the exact base; provide reviewable text,
rationale, alternatives, classification, version, affected rules and external
constraints; inventory downstream repositories and mechanisms; define per-
consumer migration, validation, communication, rollback, and risk; and identify
the review, approval, effective point, transition, and audit records. Sensitive
evidence remains paired with a reader-safe public explanation.

Require a Studio ADR and protected PR for Major and Minor amendments. Patches
may use a reasoned PR when meaning does not change. All amendments receive
constitutional-steward and affected-domain review, A4 concurrence when reserved
authority or a protective boundary changes, qualified review for affected
domains, independent approval when available, disposition of objections, and
final A4 approval for the exact commit.

Adopt an amendment at merge to protected `main`; default effectiveness to merge
unless a later unambiguous condition is recorded. Before v1.0, the merged commit
is the immutable reference. Beginning with v1.0, add an immutable annotated or
signed `constitution/vMAJOR.MINOR.PATCH` tag and release record. Never move or
reuse a tag, retroactively authorize a violation, or rewrite historical meaning.

Use semantic versioning. Major changes can make unchanged conforming consumers
nonconforming, weaken relied-on guarantees, move authority, or incompatibly
change normative meaning. Minor changes add backward-compatible governance.
Patches change no normative or relied-on meaning. Before v1.0, Minor versions
may still be breaking but must declare actual compatibility and impact. Version
1.0.0 establishes the stable compatibility baseline.

Create `CONSTITUTION_CHANGELOG.md` as the authoritative version index and
reconstruct versions 0.1.0 through 0.7.0 from Git. Every amendment adds its
version, dates, revision and tag, issue, PR, ADR, classification, summary,
rationale, affected areas, compatibility, migration, exception effects, and
review references without rewriting prior entries.

For Major changes, require an A4-approved downstream plan before merge. Classify
each consumer, name an owner, pin old and new versions, order updates across
governance and mechanisms, set durable notification and adoption evidence, and
record completion or block. References never float silently, and a consumer
cannot claim the new version before completing required changes and validation.

Define a constitutional exception as a bounded, maximum-90-day departure from
one explicitly eligible internal requirement. It does not amend meaning,
authority, version, precedent, or out-of-scope conformance. It cannot override
external obligations, transfer A4 decisions to agents, authorize uncontrolled
protected-data or Lore disclosure, permit questionable rights, erase evidence,
authorize deception, or retroactively legalize conduct.

Require exact scope, necessity, alternatives, risk, compensating controls,
monitoring, stop and rollback conditions, remediation, owner, affected-domain
review, constitutional-steward approval, dates, and public or paired restricted
evidence. Enter an exception in `CONSTITUTION_EXCEPTIONS.md` before use, except
for already authorized narrow emergency protection. Expiry is automatic;
renewal is a new decision. A second consecutive request also opens an amendment
or permanent-conformance plan.

Monitor active exceptions, revoke them when facts or controls change, record use
and closure, preserve their effect in artifact provenance, review active entries
monthly, and review historical patterns annually. Repetition signals a defect or
amendment candidate, not normalization.

## Rationale

Defining amendments by semantic effect prevents lower-level documents and
workarounds from silently changing constitutional authority. Semantic versions
communicate compatibility, while immutable commits, tags, and the changelog let
every downstream record identify the rule that actually governed it.

An impact inventory forces breaking changes to account for real workflows rather
than stopping at document approval. The narrow exception process allows a
time-limited response to genuine necessity while automatic expiry, dual-domain
approval, registers, renewal friction, and pattern review prevent temporary
departures from becoming hidden permanent policy.

## Consequences

### Positive

- Amendment authority, review, approval, and effective points are explicit.
- Every constitutional version has an immutable, auditable history.
- ADRs and implementation changes cannot amend higher authority by implication.
- Breaking changes trigger owned downstream migration and validation.
- Exceptions are narrow, expiring, visible, and nonprecedential.

### Tradeoffs

- Major and Minor amendments require impact inventories and coordinated review.
- Stable tags and downstream pins require deliberate adoption rather than
  automatic propagation.
- Sensitive exceptions need paired public and restricted records.
- Monthly active-exception and annual historical reviews create recurring
  governance work.

## Rejected alternatives

### Allow ADRs to amend the Constitution

Rejected because lower authority could silently override higher rules and leave
the controlling text inconsistent with actual policy.

### Use dates or commit hashes without semantic versions

Rejected because identity alone does not communicate compatibility or the scale
of required downstream review.

### Make every textual edit a Major amendment

Rejected because spelling, links, and non-semantic clarifications do not justify
a breaking migration process.

### Permit open-ended exceptions

Rejected because an exception without automatic expiry becomes unreviewed
permanent policy.

### Treat repeated renewal as implicit approval

Rejected because continued operation may reflect inertia or dependence rather
than evidence that the departure remains necessary and safe.

## Implementation

The Constitution owns amendment authority, semantic classification, review,
effective points, historical preservation, breaking-change adoption, and
exception eligibility. The changelog indexes versions and the exception register
indexes active and historical departures. Issue #48 will publish the first
stable version, immutable tag, release record, and compliance checklist under
this process.
