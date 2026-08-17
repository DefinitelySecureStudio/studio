# ADR 0012: Quality, validation, and release governance

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#45 — Define quality, validation, and release governance](https://github.com/DefinitelySecureStudio/studio/issues/45)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)
- Constitutional article: [Quality, validation, and release governance](../CONSTITUTION.md#9-quality-validation-and-release-governance)

## Context

Studio outputs include software, manifests, illustrations, comics, dialogue,
metadata, and AI-assisted assets. A generator can complete successfully while
producing inconsistent characters, incorrect reading order, broken text,
continuity conflicts, invalid metadata, private Lore leakage, missing rights,
or an artifact that no human intended to publish. Conversely, a subjective
human impression cannot establish schema validity, byte identity, provenance,
or technical behavior.

The Studio needs one constitutional release model that combines objective
validation with accountable creative and domain judgment. It must define when
an output becomes a release candidate, the minimum gates for publication, the
effect of findings, and the limited conditions under which a release-level risk
may be accepted without turning urgency into a routine bypass.

## Decision

Treat generation, assembly, rendering, building, and validation as production
steps rather than release authority. Establish explicit states for draft output,
identified release candidate, gate-complete candidate, A4-approved release,
published release, and superseded or withdrawn release. Bind all validation and
approval to exact bytes, scope, destination, audience, criteria, and governing
versions. Material change invalidates affected evidence and approval.

Require acceptance criteria before consequential validation. They identify the
artifact's purpose, audience, creative target, canon scope, authoritative inputs,
quality and compatibility expectations, applicable validators and reviewers,
severity thresholds, evidence handling, and rollback or withdrawal path.
Criteria may preserve intentional creative variation but cannot be rewritten
after generation merely to accept the result.

Adopt a minimum release-gate matrix covering candidate identity; creative and
editorial quality; canon and continuity; visual and media consistency; dialogue
and text; manifest, schema, and artifact integrity; technical behavior and
compatibility; provenance and audit; security, privacy, confidentiality, and
rights; accessibility and audience safety; release packaging; and final A4
approval. Artifact policies may add gates but cannot remove an applicable one.

Allow automation to establish bounded machine-verifiable facts only when the
validator, configuration, inputs, coverage, limitations, and current result are
known. Require qualified human review of the actual artifact for creative
intent, meaning, voice, visual storytelling, canon, disclosure, audience harm,
rights, residual risk, and publication. The producing agent cannot be the sole
verifier of its consequential work, and green automated checks do not authorize
release.

Classify findings as Blocker, Major, Minor, or Advisory by consequence. Blockers
stop release and cannot be waived. Majors stop normal release but may be
eligible for one narrow release waiver when no higher obligation is violated.
Minors require an accountable disposition; Advisories do not represent a failed
criterion. Aggregate related findings and treat uncertainty about protected
boundaries, rights, identity, authority, or material provenance as blocking
until resolved.

Record evidence per gate, including exact candidate, criterion and validator
versions, reviewer, inputs and environment, time, result, findings, limitations,
severity, disposition, and approvals. Distinguish pass, fail, inconclusive,
not-run, inapplicable, and waived. Revalidate whenever a changed artifact,
input, destination, audience, provider, dependency, environment, or assumption
makes evidence stale.

Permit a release waiver only for an identified Major or Minor whose governing
requirement allows risk acceptance. Never waive law, contract, rights, security
or privacy boundaries, Lore disclosure, missing authority or A4 approval,
unknown identity, corrupt audit evidence, required provenance, or uncontrolled
material harm. Bind a waiver to one exact release and record rationale, residual
risk, mitigations, domain-owner concurrence, publisher approval, follow-up,
expiry, safe disclosure, and rollback. It creates no precedent.

Limit emergency releases to the narrowest action that reduces immediate
security, privacy, safety, availability, rights, or disclosure harm. Preserve
exact identity, focused validation, provenance, human approval, deferred-gate
records, rollback, and time-bounded follow-up. Deadlines, cost, marketing, or
convenience do not create an emergency.

Require publication to bind approved bytes to immutable release and provenance
records. Classify post-release defects under the same severity model and record
corrections, withdrawals, deprecations, and replacements as append-only events.

## Rationale

Separating production success from approval preserves human creative authority
without discarding the precision of automated validation. A shared gate matrix
prevents comics, assets, code, and manifests from developing incompatible ideas
of readiness while still allowing their policies to add domain-specific checks.

Exact candidate binding prevents a validated draft from being silently replaced
before publication. Severity makes release effect predictable, while a narrow,
nonprecedential waiver path allows an accountable response to bounded risk
without permitting constitutional, rights, privacy, or security obligations to
become optional.

## Consequences

### Positive

- Successful generation or a green build cannot publish an unreviewed artifact.
- Creative, continuity, visual, dialogue, technical, provenance, rights, and
  safety concerns receive explicit ownership and evidence.
- Automated validators have a clear sufficiency boundary.
- Human editorial and publisher decisions are mandatory and bound to exact
  candidate identities.
- Blocking findings and single-release waivers are explicit, reviewable, and
  traceable.

### Tradeoffs

- Candidate identity and evidence freshness add work when artifacts change.
- Qualified human review limits fully autonomous release throughput.
- Different artifact classes need maintained implementations of the common
  gates.
- Emergency and waived releases create mandatory follow-up and retention work.

## Rejected alternatives

### Publish whenever automated checks pass

Rejected because validators cannot determine creative intent, contextual harm,
canon authority, rights permission, or publication accountability.

### Use human review without objective gates

Rejected because subjective approval cannot prove exact identity, schema
validity, referential integrity, reproducibility, or supported technical
behavior.

### Use one generic quality approval

Rejected because a single opaque result hides which domain was evaluated, by
whom, against which criteria, and whether a failure is blocking.

### Treat every finding as equally blocking

Rejected because it makes low-impact observations indistinguishable from rights,
security, continuity, or integrity failures and encourages blanket suppression.

### Permit deadline or cost waivers

Rejected because predictable business pressure would normalize bypass. Only a
bounded risk eligible under the governing requirement or an immediate protective
emergency can use the recorded release paths.

## Implementation

The Constitution owns candidate states, the minimum gate categories, human
review boundaries, severity, evidence freshness, waivers, and publication
requirements. Repository release standards define tagging, packaging, and
review mechanics. Codex may define versioned manifests, validator contracts,
and evidence schemas; Universe and Lore retain canon and private-truth authority;
artifact owners may add stricter quality criteria without weakening the common
minimum.
