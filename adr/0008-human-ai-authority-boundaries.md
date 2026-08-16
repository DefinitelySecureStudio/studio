# ADR 0008: Human and AI authority boundaries

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#41 — Define human and AI authority boundaries](https://github.com/DefinitelySecureStudio/studio/issues/41)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)
- Constitutional article: [Human and AI authority boundaries](../CONSTITUTION.md#5-human-and-ai-authority-boundaries)

## Context

The Studio uses AI agents and automation for creative and technical work. A
binary rule of "human in the loop" is insufficient: it does not distinguish a
human reviewing a generated draft from a human personally making a canon,
publication, security, or rights decision. It also does not say when routine,
reversible work may proceed under standing delegation.

The authority model must let agents perform useful bounded work while
preventing access, capability, speed, or vague instructions from becoming
implicit authority. It must apply across creative, editorial, technical,
operational, security, privacy, intellectual-property, and publishing domains
without becoming a tool-specific implementation specification.

## Decision

Adopt four ascending authority levels:

1. **A1 — Advisory:** agents research, reason, draft, simulate, and recommend in
   authorized non-authoritative space; humans decide whether results advance.
2. **A2 — Bounded delegation:** agents autonomously perform a written class of
   low-risk, reversible actions within objective limits and stop conditions.
3. **A3 — Approval-gated:** agents may prepare a consequential action but cross
   the boundary only after an authorized human approves the exact action.
4. **A4 — Reserved human:** an authorized human personally makes and records the
   underlying judgment; an agent may inform it and mechanically execute it.

The highest applicable level controls, and downstream policy may raise but not
lower it. Delegation beyond A1 identifies the accountable owner, purpose,
actions, targets, data and access limits, authority level, validations, evidence,
duration, stop conditions, escalation route, and recovery expectations.

Reserve canon decisions, public release decisions, destructive or irreversible
commitments, material security/privacy risk acceptance, protected disclosures,
access grants, and intellectual-property or licensing judgments to humans at A4.
Require at least A3 for merges into authoritative branches, deployments,
production configuration, governance or stable-contract changes, and other
consequential but reviewable execution.

A valid human gate is affirmative, attributable, informed, scoped,
contemporaneous, and recorded. It applies to the exact reviewed artifact,
target, inputs, material risks, and execution plan. Silence, prior approval,
similarity, urgency, or an agent's assessment cannot satisfy it. A material
change voids the approval.

Require agents to identify themselves and preserve evidence of identity,
delegation, authority level, inputs, tools, actions, outputs, validations,
uncertainty, failures, retries, approvals, escalation, and final state. Records
must support audit without leaking protected content. Issue #43 will define
detailed provenance formats and retention.

Require escalation before an authority boundary when delegation or approval is
unclear, instructions conflict, sensitive or irreversible consequences may be
involved, validation fails, mutation outcome is unknown, or work needs expanded
access or scope. The agent preserves the safest useful state, explains the
uncertainty and governing boundary, and requests the narrowest human decision.

## Rationale

Four levels separate assistance, safe standing delegation, approval of a
specific action, and judgments that remain inherently human. This is more
meaningful than a generic review requirement and still permits low-risk
automation without per-action ceremony.

Explicit delegation and gates make authority inspectable. Risk-based minimums
keep the model consistent across repositories, while allowing specialized
policies to impose stronger controls. Identity and evidence requirements prevent
an autonomous action from becoming unowned or being misrepresented as human
work.

## Consequences

### Positive

- Agents can proceed autonomously when work is bounded, reversible, and
  auditable.
- Canon, public release, destructive, security/privacy, and rights judgments
  retain explicit human ownership.
- Approval records distinguish review of execution from a personally human
  decision.
- Uncertainty and conflicting instructions have a mandatory safe escalation
  path.

### Tradeoffs

- Consequential workflows must expose an approval boundary and preserve its
  evidence.
- Broad or ambiguous delegations are insufficient even when they would be more
  convenient.
- Some work pauses when authority or system state cannot be verified.

## Rejected alternatives

### Require approval for every agent action

Rejected because it treats formatting and reversible validation like canon or
publication and encourages meaningless approval fatigue.

### Allow autonomy whenever an action is technically reversible

Rejected because a reversible mechanism may still disclose protected content,
change an authority, create legal exposure, or impose a public consequence.

### Treat human review and human judgment as equivalent

Rejected because a human clicking approve on an agent-selected outcome is not
the same as the human personally making a reserved creative, rights, security,
or publication decision.

### Let each repository define authority independently

Rejected because cross-repository agents would receive inconsistent authority
at precisely the boundaries where shared Studio accountability matters most.

## Implementation

The Constitution contains the normative authority matrix, approval gates,
identity and audit expectations, escalation rules, and examples. Repository
policies and agent instructions may translate the model into concrete controls
and evidence formats without reducing the constitutional minimums.
