# ADR 0015: Constitution v1 publication and conformance

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#48 — Publish Studio Constitution v1.0 and compliance checklist](https://github.com/DefinitelySecureStudio/studio/issues/48)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)
- Constitutional baseline: [Definitely Secure Studio Constitution v1.0.0](../CONSTITUTION.md)
- Compliance checklist: [Constitution compliance checklist](../CONSTITUTION_COMPLIANCE.md)
- Impact plan: [Constitution v1.0 downstream impact and adoption plan](../CONSTITUTION_V1_IMPACT.md)

## Context

Constitution versions 0.1.0 through 0.8.0 established the complete Epic #3
foundation: scope and authority; human/AI boundaries; Canon, Lore, and
continuity; provenance and audit; security, privacy, confidentiality, and
rights; quality and release governance; portability and vendor neutrality; and
constitutional amendment and exception control.

The document is comprehensive, but the pre-v1 state reserves its final
compliance procedure and still contains roadmap scaffolding. No downstream
organization repository currently pins a Constitution version. Publishing a
stable baseline therefore requires an integrated contradiction audit, a usable
checklist, exact reference guidance, a Major-change impact inventory, and an
effective point that does not precede the immutable tag and release required by
Article 12.

## Decision

Publish the integrated Constitution as version 1.0.0, the first stable
constitutional compatibility baseline. Replace the pre-v1 status with a stable
status whose effective point is publication of `constitution/v1.0.0`. Remove the
completed constitutional roadmap and expand the final article into conformance
and adoption governance without moving schemas or implementation mechanics into
the Constitution.

Resolve the final integration tensions explicitly:

- external obligations constrain the highest internal authority but are not
  Studio-created permission;
- capable agents remain subordinate to delegated authority and A4 human
  decisions;
- publication history remains separate from active/deprecated Canon;
- nondeterministic generation may be audit-only while exact selected outputs and
  deterministic release assembly remain preserved;
- public provenance links safely to restricted Lore and security evidence
  without disclosing it;
- continuity decisions, release waivers, provider-dependency decisions, and
  constitutional exceptions remain distinct;
- emergency action is protective and narrow, never an implicit amendment or
  publication approval;
- portability preserves information within its protective boundary rather than
  authorizing broad exports; and
- automated validation proves bounded facts while humans retain creative,
  contextual, rights, risk, and publication judgment.

Define conformance as an evidence-backed claim about an exact subject, scope,
Constitution version, immutable tag and commit, checklist revision, owner,
reviewers, evidence, time, and status. A subject does not inherit conformance
from an organization, dependency, template, or tool. Use only five statuses:
`Conforming`, `Authorized exception`, `Transition required`, `Nonconforming —
blocked`, and `Not assessed`.

Adopt `CONSTITUTION_COMPLIANCE.md` as the operational minimum. It contains a
universal profile plus specialized profiles for ADRs/RFCs/specifications,
repositories and systems, agents and automation, creative/Canon/Lore work,
releases, and amendments/exceptions. A lower-level checklist may add evidence or
stricter gates but cannot remove an applicable question. A checked box without
evidence and an unexplained inapplicable item establish nothing.

Adopt `repository-standards/CONSTITUTION-REFERENCE.md` as the downstream
reference standard. Every repository declaration records version, immutable
tag, full commit, status, scope and exclusions, owner, assessment revision and
date, evidence, active exception IDs, and next review. Branches, `latest`,
ranges, or copied texts are not conformance references. Major versions require
full reassessment, Minor versions require explicit additive review, and Patches
require verification and a new pin before claiming the Patch.

Treat v1.0.0 as a Major transition. Adopt `CONSTITUTION_V1_IMPACT.md` as its
required impact inventory. It covers all seven active organization repositories:
`studio`, `.github`, `codex`, `lab`, `platform`, `universe`, and `lore`. At tag
publication, v1 governs new and materially changed consequential work. Studio
adopts at publication, `.github` records adoption within 14 days, and the other
downstream repositories do so before their next consequential action and no
later than 30 days. A conflict, missing A4 approval, or Blocker pauses
immediately; transition status is not a waiver.

Merge the exact approved candidate before publication. Then create an immutable
annotated or signed `constitution/v1.0.0` tag targeting the merged commit and a
matching GitHub release that links the Constitution, checklist, changelog,
reference standard, impact plan, exception register, commit, and adoption
deadlines. Version 1.0.0 becomes effective only at that tag and release event.
If correction is required beforehand, amend or revert the candidate without
tagging. After effectiveness, preserve v1.0.0 and publish a new Patch or higher
version under Article 12.

## Rationale

The delayed effective point closes the gap between merge and the immutable
publication evidence required for a stable version. Exact declarations prevent
`main` or a copied document from silently changing the rules governing a
historical decision. Scoped statuses make incomplete adoption and active
exceptions visible without weakening the meaning of `Conforming`.

The checklist translates a long constitutional document into reviewable gates
while preserving the Constitution as authority. Specialized profiles keep it
practical for different work classes. The impact inventory makes the first
stable baseline an owned organization transition rather than an assumption that
all repositories became conforming when Studio published a tag.

## Consequences

### Positive

- Epic #3 has one stable, integrated constitutional authority.
- Future governance, contracts, agents, repositories, and releases can perform
  consistent evidence-backed assessments.
- Every downstream claim identifies exact immutable text and assessed scope.
- Incomplete adoption, exceptions, and blockers are represented honestly.
- v1 publication and all later changes follow the amendment process they govern.

### Tradeoffs

- Seven repositories require explicit adoption work after publication.
- Conformance records and evidence freshness require continuing maintenance.
- A merged v1 candidate is not effective until the tag and release are created.
- The checklist is intentionally broad and each domain may need stricter
  lower-level evidence requirements.

## Rejected alternatives

### Treat merge to `main` as sufficient v1 publication

Rejected because `main` is mutable and Article 12 requires an immutable tag and
release for every effective stable Constitution version.

### Let repositories declare compatibility with `^1.0`

Rejected because a range does not identify the text that governed an assessment
and would let future additions appear adopted without review.

### Use one undifferentiated checklist

Rejected because an ADR, agent workflow, Canon decision, provider integration,
and release require different evidence even though they share universal rules.

### Mark every repository conforming at publication

Rejected because none currently records an exact constitutional reference or
completed assessment, and organizational ownership is not evidence of local
conformance.

### Keep the roadmap in the stable Constitution

Rejected because Epic #3 is complete at publication; an obsolete roadmap would
mix project tracking with durable governance.

## Implementation

Merge the v1 candidate and record its pull request in the changelog. Publish the
exact merged commit under `constitution/v1.0.0` with a matching GitHub release.
Close issue #48 and Epic #3 only after the tag and release are verified. Open
tracked adoption work for `.github`, Codex, Lab, Platform, Universe, and Lore,
and record each completed declaration and checklist assessment against the
immutable v1 reference.
