# Constitution changelog

This file is the authoritative version index for the
[Definitely Secure Studio Constitution](CONSTITUTION.md). It records normative
history; it is not a substitute for reading the exact version that governed an
action.

Before v1.0, the source revision is the first Git commit containing the named
version. Beginning with v1.0, each effective version also has an immutable
`constitution/vMAJOR.MINOR.PATCH` tag and matching release record. A correction
adds a new version and entry; historical text and entries are not rewritten.

## Unreleased

No unreleased constitutional changes.

## 1.0.0 — 2026-08-16

- Status: Stable baseline; effective when `constitution/v1.0.0` is published
- Classification: Major; establishes the first stable constitutional
  compatibility baseline
- Source revision: the exact merged commit targeted by `constitution/v1.0.0`
- Tag: [`constitution/v1.0.0`](https://github.com/DefinitelySecureStudio/studio/releases/tag/constitution%2Fv1.0.0)
- Release: [Constitution v1.0.0](https://github.com/DefinitelySecureStudio/studio/releases/tag/constitution%2Fv1.0.0)
- Pull request: [#73](https://github.com/DefinitelySecureStudio/studio/pull/73)
- Issue: [#48](https://github.com/DefinitelySecureStudio/studio/issues/48)
- Decision: [ADR 0015](adr/0015-constitution-v1-publication-conformance.md)
- Impact and transition: [Constitution v1.0 downstream impact and adoption plan](CONSTITUTION_V1_IMPACT.md)
- Affected articles: document status and version, constitutional structure,
  foundational framing, amendment publication language, authority and references,
  removal of the completed roadmap, and expanded Article 15

Integrated every approved Epic #3 constitutional article into the first stable
baseline. Added the practical compliance checklist, immutable repository-
reference standard, five conformance statuses, specialized applicability
profiles, assessment-record requirements, v1 impact inventory, adoption
deadlines, and publication verification.

Version 1.0.0 is a deliberate Major transition from the pre-v1 development
series. It becomes effective only when the exact merged commit is published under
the immutable annotated or signed tag and matching GitHub release. Existing
repositories receive a bounded `Transition required` period under the
[impact plan](CONSTITUTION_V1_IMPACT.md); the window is not a waiver and does not
permit work that conflicts with v1.

## 0.8.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Minor pre-v1 development amendment; introduces normative
  change control and may require downstream additions
- Source revision: [`6582c3b`](https://github.com/DefinitelySecureStudio/studio/commit/6582c3b5ed37195621170bc1314807c01bff86d1)
- Pull request: [#59](https://github.com/DefinitelySecureStudio/studio/pull/59)
- Issue: [#47](https://github.com/DefinitelySecureStudio/studio/issues/47)
- Decision: [ADR 0014](adr/0014-constitutional-amendment-exception-process.md)
- Affected articles: constitutional structure, conflict resolution, definitions,
  authority and references, roadmap, conformance, and new Article 12

Added explicit A4 amendment authority; proposal, review, approval, and effective-
point rules; semantic versioning; immutable history; breaking-change impact and
downstream adoption; and bounded constitutional exceptions with a 90-day maximum,
renewal controls, public or paired restricted records, monitoring, and closure.

Downstream repositories must pin exact versions and adopt future changes through
the impact process. This amendment creates the process but does not grant an
active exception or retroactively authorize prior conduct.

## 0.7.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Minor pre-v1 development amendment
- Source revision: [`67a583b`](https://github.com/DefinitelySecureStudio/studio/commit/67a583b20b66d296173aa78aa750a73ca8e02ab6)
- Issue: [#46](https://github.com/DefinitelySecureStudio/studio/issues/46)
- Decision: [ADR 0013](adr/0013-portability-interoperability-vendor-neutrality.md)

Added portability, interoperability, vendor-neutrality, durable-representation,
provider-adapter, migration, and exit requirements.

## 0.6.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Minor pre-v1 development amendment
- Source revision: [`04a264a`](https://github.com/DefinitelySecureStudio/studio/commit/04a264a733f815717eac6b1752c46bf1e47f2c5e)
- Issue: [#45](https://github.com/DefinitelySecureStudio/studio/issues/45)
- Decision: [ADR 0012](adr/0012-quality-validation-release-governance.md)

Added candidate states, quality and release gates, human review, finding
severity, evidence freshness, release waivers, and emergency-release governance.

## 0.5.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Minor pre-v1 development amendment
- Source revision: [`1fbff23`](https://github.com/DefinitelySecureStudio/studio/commit/1fbff2324c950c616d4d9f426b143b84435018d9)
- Issue: [#44](https://github.com/DefinitelySecureStudio/studio/issues/44)
- Decision: [ADR 0011](adr/0011-security-privacy-rights.md)

Added security, privacy, confidential-information, provider, intellectual-
property, third-party-rights, release-gate, and incident requirements.

## 0.4.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Minor pre-v1 development amendment
- Source revision: [`a0a2bc2`](https://github.com/DefinitelySecureStudio/studio/commit/a0a2bc278486a3d9549297d99167ada92e6962fc)
- Issue: [#43](https://github.com/DefinitelySecureStudio/studio/issues/43)
- Decision: [ADR 0010](adr/0010-provenance-reproducibility-audit.md)

Added provenance, reproducibility, auditability, immutable release-record,
sensitive-evidence, and retention requirements.

## 0.3.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Minor pre-v1 development amendment
- Source revision: [`099d0bd`](https://github.com/DefinitelySecureStudio/studio/commit/099d0bdb58c16687f950877badd83a02b32fa8f5)
- Issue: [#42](https://github.com/DefinitelySecureStudio/studio/issues/42)
- Decision: [ADR 0009](adr/0009-canon-lore-continuity-governance.md)

Added Canon, Lore, content-state, promotion, retcon, continuity-resolution,
non-leakage, and generated-content review requirements.

## 0.2.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Minor pre-v1 development amendment
- Source revision: [`f7a74e1`](https://github.com/DefinitelySecureStudio/studio/commit/f7a74e1fca361f30942c922cde15c05c9ff79a50)
- Issue: [#41](https://github.com/DefinitelySecureStudio/studio/issues/41)
- Decision: [ADR 0008](adr/0008-human-ai-authority-boundaries.md)

Added human/AI authority levels, delegation, approval gates, escalation,
attribution, evidence, and accountability requirements.

## 0.1.0 — 2026-08-16

- Status: Adopted foundation; pre-v1.0
- Classification: Initial pre-v1 constitutional foundation
- Source revision: [`f07a778`](https://github.com/DefinitelySecureStudio/studio/commit/f07a778967a6b9d54f75efd06213669cb0dafe15)
- Issue: [#40](https://github.com/DefinitelySecureStudio/studio/issues/40)
- Decision: [ADR 0007](adr/0007-studio-constitution-model.md)

Established the Constitution's scope, normative language, authority hierarchy,
foundational principles, definitions, canonical location, roadmap, and initial
conformance statement.
