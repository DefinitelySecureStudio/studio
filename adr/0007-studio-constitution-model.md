# ADR 0007: Studio Constitution model and authority

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#40 — Define Studio Constitution structure and governing principles](https://github.com/DefinitelySecureStudio/studio/issues/40)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)

## Context

Definitely Secure Studio needs durable governance for a system in which humans,
AI agents, automation, specifications, repositories, private creative context,
and public releases interact. Existing ADRs and policies define important
boundaries, but none is designed to be the highest internal authority across
creative and technical decisions.

A Constitution that is too abstract cannot guide a disputed decision. One that
contains schemas, prompt wording, model choices, or production steps will become
an implementation manual and compete with Codex, repository policies, and code.
The first constitutional decision must therefore establish scope, hierarchy,
language, initial principles, conflict resolution, and canonical storage while
leaving later Epic #3 issues room to add precise articles.

## Decision

Adopt the root [`CONSTITUTION.md`](../CONSTITUTION.md) as the single authoritative
Studio Constitution. Version 0.1.0 is the adopted pre-v1.0 foundation; issue #48
will publish Constitution v1.0 after the remaining constitutional articles and
compliance checklist are accepted.

The Constitution governs enduring principles and non-negotiable guardrails. It
does not own implementation details, story facts, schemas, prompts, licenses,
or repository procedures. Those remain with their established authorities and
must conform to the Constitution.

Adopt this internal hierarchy:

1. Studio Constitution;
2. accepted ADRs, RFCs, and stable specifications;
3. repository policies and creative governance, including Canon and Lore;
4. prompts, manifests, context packages, agents, validators, workflows, and
   runtime code; and
5. generated artifacts and releases.

Applicable law, contracts, and third-party rights constrain every layer but are
not created or overridden by Studio governance.

Use uppercase BCP 14 terms—MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY—for
explicit normative force. Lowercase words retain their ordinary meanings.

Adopt nine foundational principles covering human accountability, intentional
irreversible judgment, canon integrity, security/privacy/rights by design,
separation of authority, auditability, quality gates, artifact provenance, and
portability. Each principle includes a rationale and a decision test.

Resolve conflicts by first eliminating unlawful, rights-incompatible, unsafe,
or explicitly prohibited options; then identify domain authorities and seek the
narrowest, least-privileged, least-disclosing, reversible resolution. Preserve a
human checkpoint at irreversible boundaries and record durable or cross-
repository resolutions in a Studio ADR. If constitutional MUST requirements
cannot coexist, work stops pending constitutional review.

Downstream governance references an immutable Constitution commit before v1.0
and an immutable Constitution version/tag plus exact commit after publication.
Copies and prompt excerpts are context, never competing authority.

## Rationale

A single root document is discoverable to humans and agents and makes authority
unambiguous. The hierarchy lets implementation evolve while keeping mechanisms
subordinate to decisions and principles. Normative terms distinguish binding
requirements from guidance, while rationales and decision tests make principles
usable during review.

Starting with an adopted pre-v1.0 foundation gives issues #41–#47 a stable frame
without falsely presenting the Constitution as complete. Deferring the final
version and compliance checklist to issue #48 preserves the epic's intended
review sequence.

## Consequences

### Positive

- Humans and AI agents have one durable source for highest-level Studio rules.
- ADRs, specifications, policies, mechanisms, and outputs have explicit
  precedence and domain boundaries.
- Principles are concrete enough to stop or redirect nonconforming work.
- Later constitutional articles can add precision without absorbing
  implementation ownership.

### Tradeoffs

- Existing and future governance will need constitutional references and review.
- Principle conflicts may pause work rather than permit an expedient silent
  choice.
- The pre-v1.0 document will evolve through several reviewed amendments before
  publication.

## Rejected alternatives

### Store the Constitution in Codex

Rejected because Codex owns stable technical contracts, not Studio-wide human
and creative governance.

### Split constitutional authority across topic files

Rejected because multiple equal roots make precedence and complete review
ambiguous. Supporting documents may exist later, but the root Constitution
remains authoritative.

### Treat a system prompt as the Constitution

Rejected because prompt context is mutable implementation input, difficult to
review as public governance, and cannot be authoritative over the human process
that supplies it.

### Publish broad values without normative tests

Rejected because agreeable values do not resolve actual tradeoffs unless they
state requirements, rationale, ownership, and a way to test a decision.

## Implementation

The Constitution lives at repository root. The Studio README links it
prominently. Issues #41–#47 add the remaining constitutional articles, and issue
#48 publishes v1.0 with a compliance checklist and immutable reference.
