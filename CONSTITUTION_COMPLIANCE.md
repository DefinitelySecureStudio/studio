# Constitution compliance checklist

Use this checklist to assess a named subject against an exact version of the
[Definitely Secure Studio Constitution](CONSTITUTION.md). It is the operational
minimum for Article 15, not a replacement for the Constitution or qualified
domain review.

Complete the universal profile and every applicable specialized profile. Mark
each item `Pass`, `Fail`, `Not applicable`, or `Not assessed`; attach evidence
for `Pass` and a specific rationale for `Not applicable`. Any applicable `Fail`
or `Not assessed` item prevents a `Conforming` status unless the Constitution
explicitly permits a narrower recorded disposition.

## Assessment identity

- [ ] The subject, stable revision or digest, purpose, environment, audience,
      scope, and exclusions are exact.
- [ ] The record pins the Constitution semantic version, immutable
      `constitution/vMAJOR.MINOR.PATCH` tag, full Studio commit, and this
      checklist revision.
- [ ] A named accountable human owns the assessment, and qualified affected
      domain reviewers and required separation of duties are identified.
- [ ] Applicable profiles, evidence locations, assessment time, evidence-
      freshness boundary, status, unresolved findings, and next review trigger
      are recorded.
- [ ] The public record is reader-safe, and any necessary sensitive evidence is
      held in a paired restricted record with a non-derivable attestation.

## Universal constitutional profile

### Authority and human accountability

- [ ] The authoritative repository, policy, specification, creative source, and
      accountable owner are identified for every material decision and input.
- [ ] Lower-level documents and mechanisms conform without redefining higher
      authority, Canon, Lore, contracts, approvals, or constitutional meaning.
- [ ] AI systems and automation act only within explicit delegation, capability,
      data, tool, time, cost, and escalation bounds.
- [ ] Every A4 creative, canon, publication, security, privacy, rights,
      disclosure, access, and governance decision is made and recorded by an
      authorized human reviewing the actual evidence.
- [ ] Uncertainty, authority conflict, scope expansion, novel risk, or a
      potentially irreversible action stops or escalates as required.

### Canon, Lore, and creative intent

- [ ] Content state is explicit, and proposal, draft, private Lore, active Canon,
      deprecated Canon, and publication state are not conflated.
- [ ] Universe is the authority for reader-safe Canon; Lore remains the private
      planning authority; processing, repetition, or publication does not grant
      either status automatically.
- [ ] Canon promotion, correction, deprecation, retcon, and continuity decisions
      include their required A4 approval, rationale, effective point, provenance,
      and downstream effects.
- [ ] Private Lore access and context packages are purpose-bound, minimized,
      approved, expiring, non-leaking, and unavailable to public tooling that
      does not require them.
- [ ] Generated work is checked against the exact authorized Canon snapshot and
      Lore-safe context, with creative intent and ambiguity resolved by humans.

### Provenance, evidence, and reproducibility

- [ ] Material inputs, specifications, prompts, tools, models, providers,
      parameters, transformations, humans, approvals, and exact outputs are
      linked by integrity-verifiable provenance.
- [ ] The record distinguishes observed facts from later explanation and
      distinguishes unknown, unavailable, inapplicable, and withheld evidence.
- [ ] Reproducibility is classified as exact, partial, or audit-only without
      overstating seeds, provider opacity, or similarity.
- [ ] Exact selected generated output and released bytes are preserved;
      deterministic assembly and required transformations are reproducible.
- [ ] Audit records are attributable, time-ordered, tamper-evident or append-
      only, sensitivity-appropriate, retained by policy, and independently
      verifiable for consequential actions.

### Security, privacy, confidentiality, and rights

- [ ] Purpose, data flow, trust boundaries, threats, failure modes, retention,
      deletion, recovery, and accountable security/privacy/rights owners were
      reviewed before consequential processing.
- [ ] Data, access, privilege, precision, recipients, providers, integrations,
      logs, and retention are the minimum necessary and fail safely.
- [ ] Secrets never enter source, prompts, issues, messages, logs, fixtures,
      manifests, outputs, or releases; suspected exposure uses the private
      incident path.
- [ ] Information classification follows copies, prompts, outputs, embeddings,
      metadata, caches, logs, backups, exports, and inferences.
- [ ] Each provider destination has current contractual and technical review for
      retention, deletion, training, human review, subprocessors, isolation,
      access, export, rights, and actual protective configuration.
- [ ] Every third-party input has exact identity, source, provenance, permission,
      compatible intended uses, notices, human contribution or ownership scope,
      and required A4 rights review.
- [ ] Questionable provenance, disclosure, access, vulnerability, similarity,
      or rights concerns stop affected work and enter the authorized private
      escalation path.

### Quality, portability, and durable control

- [ ] Acceptance criteria were defined independently of the producer and cover
      creative, editorial, continuity, visual, text, technical, accessibility,
      safety, security, rights, provenance, packaging, and release needs.
- [ ] Automated checks establish only their bounded predicates; qualified humans
      review creative meaning, context, risk, rights, and publication.
- [ ] Durable Studio data has a Studio-recognized authoritative home, stable
      identifiers, documented portable representation, integrity, and tested
      independent parse or restore path.
- [ ] Provider-specific features are isolated behind Studio-owned contracts when
      practical, capability-gated, explicit in provenance, and accompanied by a
      portable baseline, continuity behavior, owner, rationale, review, and exit
      plan.
- [ ] Migrations preserve meaning, identity, authority, sensitivity, rights,
      provenance, and rollback evidence; loss is explicit and approved.

## ADR, RFC, and stable-specification profile

- [ ] The decision or contract belongs to the named authority and does not embed
      Canon, Lore, governance, or implementation ownership outside that domain.
- [ ] Context, alternatives, rationale, consequences, constraints, unknowns,
      decision owners, and the exact constitutional reference are recorded.
- [ ] Normative requirements are testable and implementation-neutral at the
      contract boundary; examples and provider shapes are not mistaken for the
      authority.
- [ ] Known producers and consumers, compatibility, capability negotiation,
      versioning, deprecation, migration, fixtures, validation, and rollback are
      addressed proportionally.
- [ ] Security, privacy, rights, provenance, accessibility, portability, and
      failure behavior are designed into the decision rather than deferred.
- [ ] A constitutional amendment is used if normative constitutional meaning or
      authority changes; the ADR alone does not claim that power.

## Repository and production-system profile

- [ ] The repository has one architecture-authorized responsibility, visibility,
      owner, prohibited-content boundary, license class, and dependency direction.
- [ ] Branch protection, CODEOWNERS, review, security reporting, dependency
      controls, release rules, and recovery match the repository standard or a
      valid recorded exception.
- [ ] Cross-repository inputs use versioned immutable artifacts, expected sizes
      and digests, compatibility declarations, and provenance—not branches,
      copied schemas, broad checkouts, or circular builds.
- [ ] Public tooling uses synthetic, licensed, or approved public fixtures and
      contains no secrets, private Lore, unpublished Canon, or real protected
      context.
- [ ] The repository publishes the declaration required by the
      [reference standard](repository-standards/CONSTITUTION-REFERENCE.md).

## Agent and automated-workflow profile

- [ ] Agent identity, responsible owner, authority level, purpose, permitted and
      prohibited actions, data classes, tools, destinations, budgets, duration,
      monitoring, and revocation are explicit.
- [ ] Retrieval and tool results are treated as untrusted data; authorization
      and policy are enforced outside model output.
- [ ] The workflow cannot self-expand scope, self-approve, conceal uncertainty,
      treat output as Canon, or cross an A4 gate without explicit human action.
- [ ] Actions, tool calls, retries, failures, context versions, transformations,
      outputs, and approvals create sufficient audit evidence without leaking
      protected content.
- [ ] Failure, timeout, provider loss, partial execution, duplicate action,
      recovery, rollback, containment, and human takeover are tested.

## Creative, Canon, and Lore profile

- [ ] The exact public Canon snapshot, private context package, creative brief,
      source assets, rights, intended audience, and content state are pinned.
- [ ] Continuity conflicts use the deterministic resolution order and never let
      style, recency, repetition, or model confidence overrule authority.
- [ ] Human editors review character voice, story meaning, humor, visual
      storytelling, ambiguity, accessibility, audience impact, and Lore leakage.
- [ ] Promotion or publication records Canon scope separately and preserves
      alternatives, rejected drafts, corrections, deprecations, and retcons under
      their proper visibility.

## Release profile

- [ ] The exact candidate digest, contents, audience, destination, purpose,
      criteria, owners, and governing versions are fixed before final validation.
- [ ] Every applicable Article 9 gate has current evidence and a recorded `Pass`,
      `Fail`, `Inconclusive`, `Not run`, `Not applicable`, or eligible waiver.
- [ ] Blocker and Major findings stop normal release; Minor and Advisory findings
      have accountable dispositions; suppressed or unavailable checks are not
      treated as passing.
- [ ] Editorial, Canon, continuity, visual/media, dialogue/text, schema,
      technical, provenance, security/privacy/rights, accessibility/safety,
      packaging, and A4 publication review cover the actual candidate.
- [ ] Release notes, notices, migration, known limitations, support, monitoring,
      rollback, withdrawal, and correction are ready.
- [ ] Published bytes match approvals and immutable provenance exactly; a
      generated, rendered, built, tagged, or validator-passing artifact is not
      released without the final A4 decision.

## Amendment and exception profile

- [ ] The change is correctly classified as implementation, domain decision,
      release waiver, dependency decision, constitutional amendment, or temporary
      constitutional exception.
- [ ] An amendment pins the base, supplies exact text and semantic version,
      rationale, alternatives, impact inventory, migration, effective point,
      qualified review, A4 approvals, changelog, immutable tag, and release.
- [ ] A breaking amendment identifies every known consumer, owner, old/new
      reference, compatibility effect, notification, deadline, validation,
      transition, and completion or block status.
- [ ] An exception names one eligible requirement and exact scope, necessity,
      risk, controls, reviewers, A4 approvals, monitoring, stop and rollback,
      public/restricted evidence, and an expiry of no more than 90 days.
- [ ] Renewal is a fresh record and approval; a repeated departure opens an
      amendment or permanent-conformance plan; expiry and closure are preserved.

## Assessment outcome

- [ ] Findings use constitutional and release severity based on consequence,
      with blockers unresolved only in `Nonconforming — blocked` status.
- [ ] The final status is exactly `Conforming`, `Authorized exception`,
      `Transition required`, `Nonconforming — blocked`, or `Not assessed`.
- [ ] The approval identifies the exact assessed revision and does not imply
      broader, later, or historical conformance.
- [ ] Material change, stale evidence, incident, amendment, exception expiry, or
      breached stop condition triggers reassessment.

## Minimum conformance record template

```yaml
subject:
  identity: "<stable repository, decision, workflow, artifact, or release ID>"
  revision: "<commit, version, or digest>"
  scope: "<included scope>"
  exclusions: "<excluded scope with rationale>"
constitution:
  version: "1.0.0"
  tag: "constitution/v1.0.0"
  commit: "<full 40-character Studio commit>"
  checklist_revision: "<full Studio commit containing this checklist>"
assessment:
  status: "<Conforming | Authorized exception | Transition required | Nonconforming — blocked | Not assessed>"
  owner: "<accountable human>"
  reviewers: []
  assessed_at: "<ISO 8601 timestamp>"
  applicable_profiles: []
  evidence: []
  findings: []
  release_waivers: []
  constitutional_exceptions: []
  next_review: "<date or material trigger>"
```

The template is a portable example, not a Codex schema. Public records must not
contain secrets, private Lore, unnecessary personal data, or protected evidence.
