# Definitely Secure Studio Constitution

- Status: Stable v1 baseline; effective on publication of `constitution/v1.0.0`
- Version: 1.0.0
- Date: 2026-08-16
- Authority: Definitely Secure Studio
- Constitutional model: [ADR 0007](adr/0007-studio-constitution-model.md)
- Human/AI authority model: [ADR 0008](adr/0008-human-ai-authority-boundaries.md)
- Canon/Lore governance model: [ADR 0009](adr/0009-canon-lore-continuity-governance.md)
- Provenance and audit model: [ADR 0010](adr/0010-provenance-reproducibility-audit.md)
- Security, privacy, and rights model: [ADR 0011](adr/0011-security-privacy-rights.md)
- Quality and release model: [ADR 0012](adr/0012-quality-validation-release-governance.md)
- Portability and vendor-neutrality model: [ADR 0013](adr/0013-portability-interoperability-vendor-neutrality.md)
- Amendment and exception model: [ADR 0014](adr/0014-constitutional-amendment-exception-process.md)
- v1 publication and conformance model: [ADR 0015](adr/0015-constitution-v1-publication-conformance.md)
- Version history: [Constitution changelog](CONSTITUTION_CHANGELOG.md)
- Exception history: [Constitution exception register](CONSTITUTION_EXCEPTIONS.md)
- Compliance checklist: [Constitution compliance checklist](CONSTITUTION_COMPLIANCE.md)

## Preamble

Definitely Secure Studio combines human creative direction with software,
automation, and AI-assisted production. The Studio adopts this Constitution so
that faster or more capable mechanisms do not silently replace human
accountability, creative intent, security, privacy, rights discipline, canon
integrity, quality, or durable ownership of the work.

This Constitution is the highest internal governance authority of Definitely
Secure Studio. It constrains how the Studio decides, creates, changes, validates,
and publishes work. It does not grant legal rights, override applicable law or
contract, or turn principles into ownership of material held by someone else.

## Constitutional structure

The Constitution is organized as a durable governance document rather than an
implementation manual:

1. **Scope** establishes what the Constitution does and does not govern.
2. **Normative language** distinguishes binding requirements from guidance.
3. **Authority hierarchy** defines precedence and preserves domain ownership.
4. **Foundational principles** state each rule, its rationale, and a practical
   decision test.
5. **Human and AI authority boundaries** define delegation levels, approval
   gates, escalation, and accountability.
6. **Canon, Lore, and continuity governance** defines creative truth, content
   states, promotion, retcons, and confidentiality.
7. **Provenance, reproducibility, and audit** defines lineage, evidence,
   deterministic rebuilds, nondeterministic generation, and retention.
8. **Security, privacy, and rights** defines protective design, data handling,
   provider boundaries, third-party material, and incident response.
9. **Quality, validation, and release governance** defines candidate states,
   minimum gates, severity, human review, and bounded waivers.
10. **Portability, interoperability, and vendor neutrality** defines durable
    representations, Studio-owned contracts, migration, and provider dependencies.
11. **Conflict resolution** defines how competing obligations are handled.
12. **Amendment, versioning, and exceptions** defines constitutional change
    authority, review, history, downstream adoption, and temporary departures.
13. **Definitions** provide a shared constitutional vocabulary.
14. **Authority, storage, and references** identify the canonical document and
   how downstream work pins it.
15. **Conformance and adoption** defines valid claims, version declarations,
    applicability profiles, evidence, and outcomes.

Later articles MAY add precise requirements within this structure. They MUST
NOT turn the Constitution into a schema, procedure, prompt, or implementation
reference.

## 1. Scope

### 1.1 What this Constitution governs

This Constitution governs:

- the allocation of authority and accountability between humans, AI systems,
  automation, repositories, and production processes;
- non-negotiable boundaries for creative decisions, canon, continuity, private
  lore, security, privacy, intellectual property, quality, provenance, and
  publication;
- the hierarchy by which ADRs, RFCs, specifications, policies, prompts, code,
  and generated artifacts derive authority;
- the standard used to resolve conflicts between principles or governance
  layers; and
- the durable qualities that Studio systems MUST preserve even when tools,
  vendors, formats, models, or implementations change.

The Constitution applies to humans acting for the Studio and to every AI agent,
automation, service, or workflow operated on the Studio's behalf.

### 1.2 What this Constitution does not govern

This Constitution does not define:

- API shapes, schemas, protocol fields, package layouts, or validation
  algorithms;
- model providers, prompt wording, agent frameworks, infrastructure, or
  implementation languages;
- individual story facts, character details, unpublished continuity, or the
  content of a particular creative decision;
- step-by-step production procedures, repository-specific contribution rules,
  or release commands; or
- permissions that belong in licenses, contracts, employment terms, or other
  legal instruments.

Those details belong to their named domain authorities. They MUST conform to the
Constitution but SHOULD evolve without constitutional amendment when the
underlying principles remain unchanged.

## 2. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are
normative only when written in uppercase. Their meanings follow BCP 14,
[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and
[RFC 8174](https://www.rfc-editor.org/rfc/rfc8174):

- **MUST** states an absolute requirement for constitutional conformance.
- **MUST NOT** states an absolute prohibition.
- **SHOULD** states the expected course. A departure requires a specific reason,
  understood consequences, an accountable human owner, and a written record.
- **SHOULD NOT** states a normally prohibited course. Taking it requires the
  same documented justification and ownership.
- **MAY** states a permitted option, not a requirement or recommendation.

Lowercase uses retain their ordinary English meaning. Normative terms MUST be
used sparingly and only where a genuine governance requirement, prohibition, or
choice exists.

## 3. Authority hierarchy

```mermaid
flowchart TD
    external["Applicable law, contracts, and third-party rights<br/>External constraints; not Studio-created authority"]
    constitution["1. Studio Constitution<br/>Enduring principles and non-negotiable guardrails"]
    decisions["2. Accepted ADRs, RFCs, and stable specifications<br/>Durable decisions and contracts"]
    governance["3. Repository policies and creative governance<br/>Canon, lore, security, release, contribution"]
    mechanisms["4. Prompts, manifests, context packages, agents,<br/>validators, workflows, and code"]
    outputs["5. Generated artifacts and releases"]

    external -. "constrains" .-> constitution
    constitution --> decisions
    decisions --> governance
    governance --> mechanisms
    mechanisms --> outputs
```

### 3.1 Precedence

1. The Constitution governs every lower internal layer.
2. Accepted organization ADRs record durable cross-repository decisions.
   Accepted Codex RFCs and stable specifications govern shared technical
   contracts. Repository ADRs govern implementation decisions within their
   repository. None may override the Constitution.
3. Repository policies and creative governance apply those decisions within a
   domain. Universe is authoritative for public canon; Lore is authoritative for
   private planning truth; other repositories retain the responsibilities in
   the Studio architecture.
4. Prompts, manifests, context packages, agents, validators, workflows, and code
   are mechanisms. Their behavior does not become policy merely because it runs.
5. Generated artifacts and releases are outputs. Repetition, publication, or
   apparent quality does not give an output authority that its approvals and
   provenance do not establish.

A lower layer MUST NOT redefine, weaken, or silently bypass a higher layer. A
more specific rule controls within its proper domain only when it conforms to
every higher applicable rule.

### 3.2 Domain authority

Constitutional precedence does not erase domain ownership. A technical
specification cannot declare canon; canon cannot redefine a software contract;
runtime code cannot become the source of a governance rule; and private planning
truth does not become public through processing or inference. When two peer
authorities appear to conflict, the accountable owners MUST identify the shared
higher-level question and resolve it through the appropriate Studio ADR or
constitutional process.

## 4. Foundational principles

These principles establish the durable decision frame. Lower authorities MAY
make them more specific within their domains but MUST preserve this foundation.

### Principle 1: Human authority carries human accountability

The Studio MUST assign an accountable human owner to every consequential
creative, publication, security, privacy, rights, access, and governance
decision. AI systems and automation MAY advise, draft, transform, compare, or
validate within explicit delegated bounds; they MUST NOT be treated as the
accountable authority.

**Rationale:** Delegation can accelerate work, but responsibility cannot be
outsourced to a mechanism that cannot own consequences.

**Decision test:** Can a named human explain the decision, its evidence, the
delegated bounds, and who can stop or reverse it? If not, the decision MUST NOT
proceed.

### Principle 2: Irreversible creative judgment remains intentional

The Studio MUST preserve meaningful human judgment before an irreversible or
externally consequential creative act, including canon acceptance, publication,
destructive replacement, rights commitment, or disclosure of private material.
Automation SHOULD default to proposals, previews, drafts, and reversible state.

**Rationale:** Efficiency is valuable only while the Studio remains the author
of its choices rather than the spectator of an automated sequence.

**Decision test:** Is there an informed human checkpoint before the action
becomes public, canonical, destructive, contractually committed, or difficult
to recover? If not, the workflow is nonconforming.

### Principle 3: Canon and continuity have explicit authority

Public canon and private Lore MUST remain distinct authorities. Material MUST
enter public canon only through an explicit editorial decision. An AI inference,
generated continuation, production dependency, repeated output, or absence from
a record MUST NOT create, reveal, or revise canon by implication.

**Rationale:** Story truth depends on intentional editorial continuity, while
private planning requires a real disclosure boundary.

**Decision test:** Can every asserted public fact be traced to an approved
Universe record or publication, and every private influence be handled without
unapproved disclosure? If not, the material MUST NOT be treated as canon-ready.

### Principle 4: Security, privacy, and rights are design inputs

Systems and workflows MUST minimize access, data, retention, disclosure, and
rights exposure from the start. They MUST NOT rely on cleanup after publication
or processing as the primary control. Material MUST NOT be used merely because
it is accessible; provenance, permission, purpose, and handling terms MUST be
known and compatible.

**Rationale:** A creative workflow can cause lasting harm through leaks,
overcollection, insecure processing, or rights misuse even when its visible
output appears harmless.

**Decision test:** Are the minimum necessary data and permissions identified,
are prohibited destinations and retention limits enforced, and are rights and
provenance documented before use? If not, processing MUST pause.

### Principle 5: Authority stays separated from mechanism

Governance, stable contracts, experiments, runtime implementation, public
canon, and private Lore MUST retain singular authoritative homes. Experiments
MUST NOT become production dependencies by convenience; implementations MUST
NOT redefine contracts; processors MUST NOT take ownership of their inputs.

**Rationale:** Separation makes change reviewable and prevents a convenient copy
or successful prototype from becoming accidental truth.

**Decision test:** Does every decision, fact, contract, implementation, and
artifact have one named authority, with consumers referencing rather than
forking it? If not, the ownership boundary MUST be resolved first.

### Principle 6: AI-assisted work is traceable and auditable

Material AI-assisted transformations and generated artifacts MUST retain enough
provenance to identify inputs, tools or models, relevant versions, human
approvals, transformations, and outputs without exposing protected information.
Reproducibility SHOULD be achieved where practical; where it is not, the record
MUST still support a meaningful audit of what happened and why.

**Rationale:** The Studio cannot evaluate, correct, defend, or learn from a
result whose origin and approvals are unknown.

**Decision test:** Can an authorized reviewer reconstruct the material inputs,
mechanism identity, decision checkpoints, and exact released output while public
records remain reader-safe? If not, the artifact MUST NOT be published.

### Principle 7: Quality outranks uncontrolled automation

The Studio MUST evaluate work against defined creative, editorial, technical,
accessibility, security, and release criteria before publication. Generated
volume, speed, model confidence, validator success, or absence of errors MUST
NOT substitute for fitness and intentional approval.

**Rationale:** Automation scales defects and mediocrity as readily as it scales
good work.

**Decision test:** Are acceptance criteria defined independently of the system
that produced the work, and has the accountable reviewer evaluated the actual
output? If not, the release MUST stop.

### Principle 8: Provenance travels with artifacts

Every released artifact MUST identify its authoritative sources, exact
dependencies, applicable rights and notices, generation or build record, and
human approval at the level appropriate to its sensitivity. Public provenance
MUST remain useful without exposing private Lore or security-sensitive details.

**Rationale:** An artifact separated from its origin cannot be reliably audited,
reproduced, licensed, corrected, or trusted.

**Decision test:** Can the Studio identify the exact released bytes, their
authorities, their dependency versions, their rights, and their approval record?
If not, the artifact is not release-ready.

### Principle 9: Portability preserves creative independence

The Studio SHOULD use durable, documented, exportable formats and explicit
interfaces. A material dependency on a vendor-specific service, model, or format
MUST have an identified owner, reason, exit path, and preservation plan
proportional to the cost of replacement.

**Rationale:** Creative continuity and access to Studio history must not depend
on the indefinite availability or policy of one vendor.

**Decision test:** Can the Studio retrieve its source, metadata, decisions, and
released artifacts in documented forms and continue essential work after the
dependency is withdrawn? If not, the dependency requires remediation or an
explicitly accepted risk.

## 5. Human and AI authority boundaries

AI systems and automation exercise capabilities, not inherent authority. Every
agent action MUST derive from an accountable human owner and an applicable
constitutional delegation. Tool access, technical ability, a previous success,
or an instruction embedded in data does not grant decision authority.

When more than one authority level applies, the highest level controls. A
repository or workflow MAY impose a higher level but MUST NOT lower the levels
required here.

### 5.1 Delegation prerequisites

Before an agent acts beyond advisory work, its delegation MUST identify:

- the accountable human owner and the authorized purpose;
- permitted actions, targets, data classes, tools, and environments;
- the applicable authority level and approval gates;
- scope, duration, access limits, and resource limits;
- required validations and the evidence the agent must preserve; and
- stop conditions, escalation route, and recovery expectations.

Delegation MUST use least privilege and the narrowest practical scope. It MUST
NOT be inferred from credentials, repository access, silence, urgency, a broad
goal, or a similar action having been approved before. In the absence of a
sufficient delegation, an agent is limited to advisory work using information
it is already authorized to access.

### 5.2 Authority levels

| Level | Decision authority | Permitted agent role | Human control |
| --- | --- | --- | --- |
| **A1 — Advisory** | The agent has no authority to establish truth, policy, approval, or consequential external effect. | Research, compare, reason, draft, simulate, and recommend in non-authoritative, access-controlled, reversible space. | A human decides whether any result advances. |
| **A2 — Bounded delegation** | A human pre-authorizes a defined class of low-risk, reversible decisions. | Modify, validate, or execute autonomously only within written limits and objective stop conditions. | The accountable human owns the delegation and reviews its evidence at the required cadence. |
| **A3 — Approval-gated** | The agent prepares a specific consequential action, but has no authority to cross its gate. | Propose, modify, validate, and execute the exact approved action after the gate is satisfied. | An authorized human gives explicit, informed approval before the effect occurs. |
| **A4 — Reserved human** | The judgment itself belongs to a human and cannot be delegated. | Assemble evidence, identify options and risks, draft alternatives, and mechanically execute a separately recorded human decision. | An authorized human personally makes and records the decision before execution. |

A3 approval authorizes execution of a specific reviewed action. A4 requires the
human to make the underlying judgment; approving an agent's recommendation
without performing that judgment does not satisfy A4.

### 5.3 Human/AI authority matrix

The following levels are minimums. Greater sensitivity, uncertainty, scope, or
irreversibility raises the required level.

| Domain or action | Minimum level | Boundary |
| --- | --- | --- |
| Any domain — research, comparison, brainstorming, and draft alternatives | A1 | Sources and data must already be authorized; results remain non-authoritative. |
| Creative/editorial — reversible changes in non-canonical working state | A2 | The work must remain reviewable and must not silently establish creative direction, canon, or release status. |
| Technical — routine formatting, objective validation, tests, and reversible maintenance | A2 | The delegation must define rules, targets, validation, and stop conditions. |
| Operational — routine, reversible housekeeping in a non-production environment | A2 | The delegation must define the environment, resource limits, and recovery path. |
| Technical/governance — merge, stable specification, constitutional policy, or other authoritative change | A3 | A human must review the exact change, evidence, impact, and recovery plan before effect. |
| Operational — deployment or production configuration change | A3 | A human must approve the exact target, change, validation, risk, and rollback plan. |
| Creative/editorial — selection or rejection of material creative direction | A3 | The accountable editor must review the actual alternatives and intended effect. |
| Editorial — canon acceptance, rejection, retcon, or continuity exception | A4 | The editorial judgment must be explicitly human and follow the canon governance in Section 6. |
| Publishing — public release or representation that work is approved, official, or final | A4 | A human publisher must decide that the exact artifact and public context are fit to release. |
| Public interaction — external message, issue, pull request, or other public-facing write | A3 | An authorized human must approve the content and destination unless a narrower routine class is explicitly delegated at A2. |
| Security/privacy — analysis of already authorized evidence | A1 | The agent may identify concerns and options but must not expand access or expose protected detail. |
| Security/privacy — bounded, reversible remediation outside production | A2 | Objective controls, validation, and stop conditions must be pre-authorized. |
| Security/privacy — production remediation or control change | A3 | A human must review the exact control, affected environment, risk, validation, and rollback. |
| Security/privacy — access grant, protected disclosure, control weakening, new secret destination, or material residual-risk acceptance | A4 | The authorized human must make the judgment; constitutional prohibitions still cannot be waived. |
| IP/rights — inventory, source comparison, and evidence gathering | A1 | The agent may report evidence but must not infer missing permission. |
| IP/rights — mechanical compliance check against an established policy | A2 | The rule and authoritative rights metadata must be explicit and yield no unresolved ambiguity. |
| IP/rights — ownership, permission, fair-use, licensing, attribution, or third-party-rights commitment | A4 | The rights judgment and any commitment must be made by an authorized human. |
| Any domain — destructive, irreversible, legally binding, or financially committing action | A4 | The responsible human must decide the action and review the exact target and consequence. |

### 5.4 Mandatory approval gates

An A3 or A4 gate MUST occur before an action:

- changes public canon or private Lore authority;
- publishes a release, deploys, merges into an authoritative branch, creates a
  public-facing communication, or represents an artifact as official, approved,
  or final;
- destroys, overwrites, revokes, transfers, or makes state materially difficult
  to recover;
- changes access, privilege, secrets, security controls, privacy handling, or a
  protected-data destination;
- uses or commits the Studio to intellectual property, license, contract,
  financial obligation, or third-party terms;
- changes constitutional governance, a stable specification, or another
  durable cross-repository authority; or
- crosses any repository-defined gate that is stricter than this Constitution.

A valid approval MUST be affirmative, attributable, informed, scoped,
contemporaneous, and recorded. The approver MUST be authorized for the affected
domain and MUST receive the exact artifact or action, material inputs and
changes, validation evidence, known risks, affected authorities, and recovery
or irreversibility statement.

Silence, inactivity, a past approval, approval of a similar action, an agent's
own assessment, or a request to "finish" does not satisfy a gate. A material
change to the reviewed artifact, target, inputs, risk, or execution plan voids
the approval and requires a new gate. An agent MUST NOT approve its own work or
describe work as human-reviewed without a corresponding approval record.

### 5.5 Agent identity, attribution, and evidence

An agent MUST identify itself as an AI system or automation when interacting
with a human or recording an action. It MUST NOT impersonate a person, attribute
its own judgment to a person, fabricate approval, or obscure which work was
AI-assisted.

Every action beyond A1 MUST produce evidence sufficient for an authorized
reviewer to identify:

- the agent or workflow identity and unique run or session;
- the accountable human, delegation, authority level, and governing policy
  version;
- material inputs and their authorities, without leaking protected content;
- tools used, actions attempted, changes or outputs produced, and targets;
- validation results, uncertainty, failures, retries, and final state; and
- required approvals, escalations, and the humans who supplied them.

Evidence MUST be durable and proportionate to the consequence before the action
is treated as complete. Audit records MUST preserve accountability without
placing secrets, private Lore, personal data, or sensitive security detail in a
less protected destination. Section 7 defines the detailed provenance,
retention, and reproducibility requirements.

### 5.6 Uncertainty, conflict, and escalation

An agent MUST stop before crossing an authority boundary and escalate when:

- the accountable owner, delegation, authority level, target, or approval is
  missing, ambiguous, expired, or unverifiable;
- instructions conflict with each other or with a higher authority;
- the action may affect canon, publication, rights, protected data, security,
  access, irreversible state, or another domain outside the delegation;
- validation fails, expected state differs from observed state, or the outcome
  of an attempted mutation is unknown;
- completing the work requires broader access, a new tool, a different
  environment, or materially expanded scope; or
- a reasonable interpretation could produce materially different consequences.

The agent MUST preserve the safest useful state, retain evidence, state what is
known and uncertain, identify the governing boundary, and ask the accountable
human for the narrowest decision needed. It MAY continue independent work only
when that work is authorized, reversible, and cannot prejudice the pending
decision.

Conflicting instructions MUST be resolved by the authority hierarchy in Section
3, then by the narrower valid delegation and the more protective applicable
boundary. An agent MUST NOT select a convenient lower-authority instruction,
invent missing intent, or treat urgency as authorization. When an attempted
mutation has an uncertain result, the agent MUST inspect current state before
retrying so it does not duplicate or compound the action.

### 5.7 Examples

| Agent action | Autonomous status | Reason |
| --- | --- | --- |
| Draft three script alternatives in a private working branch from authorized context. | Allowed at A1. | The alternatives are reversible and non-canonical. |
| Apply formatting, run tests, and fix an objective lint rule within a named branch. | Allowed at A2 when explicitly delegated. | The scope and validation are bounded and reversible. |
| Change an undocumented public API because tests still pass. | Prohibited autonomously. | Passing tests do not grant authority to change a stable contract. |
| Merge a reviewed change after the exact commit receives recorded approval. | Allowed at A3 when the delegation includes merge execution. | The human gate controls the authoritative change. |
| Declare generated dialogue canonical because it matches established style. | Prohibited. | Similarity and quality do not create canon authority; canon is A4. |
| Publish an artifact based on a general instruction to finish the task. | Prohibited. | Publication requires an exact, informed A4 human decision. |
| Upload private Lore or a secret to an unapproved model or service to improve a result. | Prohibited. | Tool access and expected quality cannot waive disclosure boundaries. |
| Decide that unlicensed third-party material is fair use and include it in a release. | Prohibited. | The rights judgment and release commitment are reserved to an authorized human. |
| Retry an external write whose first result timed out without checking state. | Prohibited. | The retry may duplicate a consequential action. |
| Pause after detecting conflicting instructions, preserve the draft, and request a scoped decision. | Required. | Escalation preserves authority and reversibility. |

### 5.8 Human accountability

Human approval is an exercise of judgment, not a transfer of accountability to
the agent. The approving human MUST review evidence proportionate to the risk
and MUST NOT rely solely on model confidence, automated validation, or the
agent's summary when the underlying artifact or consequence can reasonably be
examined. Use of an agent does not reduce the Studio's responsibility for the
decision, action, or released result.

## 6. Canon, Lore, and continuity governance

Creative truth requires both an editorial state and a release state. Canon
status answers what the Studio currently treats as reader-safe story truth;
publication status answers what exact material an audience received. The two
MUST be recorded separately. Publication alone does not make every statement
canonical, and a private plan does not become public canon through use,
inference, repetition, or implementation.

### 6.1 Ownership and authorities

The following ownership boundaries are singular:

- **Universe** owns active and deprecated public canon, canon decisions,
  reader-safe continuity records, released canon snapshots, and the public
  publication record.
- **Lore** owns private unrevealed continuity, established private facts,
  explicitly labeled possibilities and alternatives, and approved private
  context packages. Lore authority is private and does not itself grant public
  canon status.
- **Published artifacts** are immutable evidence of what an audience received
  under a particular release identity. Universe records their declared canon
  scope and relationship to current canon.
- **Humans authorized as canon editors** make A4 canon, continuity-exception,
  and retcon decisions. Humans authorized as publishers make the separate A4
  release decision.
- **Agents, Platform, prompts, validators, and generated outputs** MAY propose,
  compare, flag, or transform material within delegation, but MUST NOT declare,
  promote, deprecate, retcon, or publish canon.

Copies, caches, context packages, scripts, production dependencies, and model
outputs are consumers of creative authority. They MUST NOT become competing
sources merely because they are newer, more detailed, or necessary to a build.

### 6.2 Content states

| State | Meaning | Authority and allowed transition |
| --- | --- | --- |
| **Proposal** | A discrete candidate idea, fact, change, or resolution submitted for consideration. | Non-authoritative. A human or agent MAY create or revise it within delegation; doing so does not advance its canon status. |
| **Draft** | An assembled work in progress that may combine proposals and approved sources. | Non-authoritative and non-canonical. It remains reviewable working state until an explicit decision changes its status. |
| **Lore** | Private planning material in the Lore authority, with each item labeled as established private continuity, possibility, alternative, question, or retired plan. | Authoritative only for its labeled private planning role. Promotion requires a sanitized proposal and an A4 canon decision; direct copying is not promotion. |
| **Active canon** | Reader-safe story truth explicitly accepted by an authorized canon editor and recorded in Universe. | Governs current public continuity from its stated effective point until explicitly superseded or deprecated. |
| **Deprecated canon** | Material that was canonical but has been explicitly superseded, limited, or retired. | Retained with its prior status, affected scope, replacement or resolution, effective point, rationale, and decision provenance; it is not active authority for new work. |
| **Published artifact** | Exact material intentionally released to an audience under a stable identity. | Immutable evidence of that release. Its record MUST declare which content is canonical, non-canonical, promotional, hypothetical, or otherwise scoped. Publication does not silently promote content. |

These states are not a single automatic lifecycle. A draft MAY become a
published non-canonical artifact; a canon record MAY exist before its associated
artifact is released; and a published artifact remains historical evidence if
some of its canon is later deprecated. Every material creative item MUST have
an explicit state. Unknown or missing state is non-canonical.

### 6.3 Canon promotion and change

Canon promotion is an A4 editorial decision distinct from the A4 publication
decision. One human review MAY record both only when it explicitly identifies
and separately approves the exact canon scope and exact release artifact.

Before promotion, the canon editor MUST receive:

1. the exact proposal or draft and its current state;
2. the pinned active Universe canon snapshot used for review;
3. the minimum authorized Lore context needed for the decision, if any;
4. a continuity comparison identifying contradictions, unresolved ambiguity,
   private implications, and affected canon;
5. source and generation provenance sufficient to understand material creative
   influence under Section 7; and
6. the proposed effective point, public wording, canon scope, and disposition
   of superseded or rejected alternatives.

The recorded decision MUST identify the authorized canon editor, exact accepted
material, prior and new states, effective point, rationale, affected records and
artifacts, unresolved limitations, and immutable source references. Universe
MUST update its canon status and decision record before consumers treat the
material as canon.

An agent inference, generated continuation, validator result, production use,
publication, repeated reference, audience assumption, or absence of a contrary
record MUST NOT substitute for promotion. Content omitted from a canon snapshot
is unknown unless an explicit record marks it false, deprecated, or outside the
snapshot's scope.

### 6.4 Corrections, deprecation, and retcons

A correction that changes presentation without changing story meaning MAY be
handled as an A3 publication or record correction, but it MUST preserve the
original artifact or record and explain the correction. If reasonable readers
could understand the story differently, the change is a canon decision at A4.

A retcon is an intentional A4 decision that contradicts, replaces, narrows, or
reinterprets previously active canon. A retcon MUST NOT erase history or silently
rewrite a prior release. Its record MUST:

- identify the exact prior canon and affected published artifacts;
- state the contradiction or change, rationale, and accountable canon editor;
- mark the prior material deprecated with its prior status and publication
  history preserved;
- identify the replacement, new interpretation, or deliberately unresolved
  state and its effective point;
- record source, decision, and release provenance with immutable references;
  and
- identify known downstream continuity, publication, and consumer updates.

Generated material MUST NOT initiate a retcon by being more convenient,
coherent, recent, or repeatedly used. A continuity exception limited to one
work or framing device is still an A4 decision and MUST state its exact scope so
it cannot silently become a general retcon.

### 6.5 Deterministic continuity conflict resolution

When a proposed or active statement appears to contradict another creative
source, promotion and publication MUST pause for the disputed scope. The canon
editor and assisting systems MUST:

1. pin the exact records, snapshots, artifacts, and effective dates involved;
2. identify whether the question concerns historical publication, current
   canon, private planning, or a proposed future change;
3. test whether time, viewpoint, narrator reliability, scope, or explicit
   ambiguity allows the statements to coexist;
4. apply the precedence rules below without rewriting a source in place;
5. record the resolution, affected states, rationale, and decision owner; and
6. update the authoritative records before downstream work resumes.

Precedence is determined by the question being answered:

- For **what an audience received**, the exact published artifact and its
  immutable release record control.
- For **current public continuity**, the latest applicable explicit Universe
  canon decision controls. A Universe record may differ from an earlier
  published artifact only when an explicit correction, deprecation, or retcon
  accounts for that difference.
- If no later explicit decision exists, an approved canonical published
  artifact controls over contradictory unpublished internal documentation. The
  internal record MUST be corrected; it cannot silently negate publication.
- Lore controls private planning only where it does not claim to override
  public canon. Conflicting Lore MUST be reconciled, scoped as an alternative,
  or marked retired before use.
- Proposals, drafts, generated outputs, implementation behavior, and memories
  have no precedence over an authoritative record.

Timestamps, file order, branch position, repetition, and last-write-wins MUST
NOT resolve equal-authority conflicts. If the rules do not yield one outcome,
the conflict is explicitly unresolved until an authorized canon editor records
an A4 decision. Agents MAY detect and explain the conflict but MUST NOT choose a
preferred truth.

### 6.6 Lore confidentiality and non-leakage

Lore is protected private material. Access to Lore does not authorize
disclosure, publication, canon promotion, or reuse in a different system or
purpose. Lore MUST NOT enter a public or less-protected repository, issue, pull
request, prompt, log, fixture, cache, model-training corpus, artifact, manifest,
or release unless the exact reader-safe material has an A4 human disclosure
decision and explicit canon scope. A release additionally requires its A4
publication decision.

Production systems MUST consume the minimum approved, purpose-bound Lore
context package rather than the Lore repository or a broad export. Each package
MUST identify its authorized purpose, recipient or environment, included
material, source revision, handling constraints, retention or expiry, and A4
human disclosure approval. Access MUST be least-privileged, time-bounded where
practical, and unavailable to public tooling that does not require the content.

Non-leakage applies to derived and indirect information, including summaries,
negative confirmations, filenames, paths, commit identifiers, content-derived
hashes, embeddings, prompts, logs, timing, and correlation metadata. Public
provenance MUST use a non-derivable opaque attestation when it needs to refer to
private influence; the restricted mapping remains in an approved private
authority.

Before public review or release, an authorized check MUST compare the candidate
against its approved public inputs and, in a restricted environment, the private
material available to the production run. The check MUST identify unapproved
facts, implications, quotations, metadata, and transformations. It MUST expose
only the minimum finding needed for public correction, not the Lore content that
caused the finding.

On suspected leakage, the workflow MUST stop publication and further
disclosure, preserve evidence in a restricted destination, contain accessible
copies where authorized, and escalate to the accountable human. Deletion or
redaction alone MUST NOT be treated as proof that disclosure did not occur.

### 6.7 Generated-content continuity checks

Generated comic content MUST be evaluated against:

- the exact active Universe canon snapshot pinned for the work;
- only the approved minimum Lore context package, when private context is
  necessary;
- the intended content state and declared canon scope;
- the relevant chronology, identities, relationships, setting, prior events,
  and explicit continuity constraints; and
- a restricted non-leakage review when Lore influenced generation.

The check MUST produce a reviewable report of sources, conflicts, unknowns, and
private-risk findings without exposing protected detail. Unresolved conflict,
unknown authority, missing state, or suspected Lore leakage blocks canon
promotion and publication of the affected material.

Automated checks are advisory evidence. Passing a validator proves only that
its encoded checks passed against its supplied inputs; it does not establish
canon completeness, creative fitness, safe disclosure, or human approval. The
authorized canon editor and publisher remain accountable for the exact result.

## 7. Provenance, reproducibility, and audit

Provenance MUST travel with every material artifact from authoritative inputs
through transformations, selection, approval, and release. A record is
sufficient only when an authorized reviewer can follow the lineage in both
directions: from an output to what produced and approved it, and from an input
or decision to every affected output.

### 7.1 Traceability, reproducibility, and auditability

These are distinct claims:

- **Traceability** means the Studio can identify an artifact's authoritative
  inputs, instructions and specifications, mechanisms, transformations,
  responsible actors, decisions, approvals, and exact output.
- **Exact reproducibility** means an authorized party can follow the recorded
  procedure with the pinned inputs and controlled environment to produce
  byte-identical output. A digest match demonstrates identity; visual,
  semantic, or functional similarity does not.
- **Auditability** means an authorized reviewer can verify what happened, why,
  under whose authority, with which evidence and controls, and with what result,
  even when the original generation cannot be repeated exactly.

Every material artifact MUST be traceable and auditable. Deterministic release
assembly, packaging, manifests, and derived transformations MUST be exactly
reproducible. Nondeterministic generated candidates need not be exactly
reproducible, but their exact selected outputs MUST be preserved and every
subsequent deterministic transformation MUST be reproducible.

A workflow MUST classify its reproducibility as **exact**, **partial**, or
**audit-only**, state the boundary of that claim, and identify known gaps. It
MUST NOT claim reproducibility merely because it recorded a seed, can send a
similar request again, or produced a perceptually similar result.

- **Exact** applies when the complete claimed artifact can be regenerated with
  a byte-identical result.
- **Partial** names the specific deterministic stages or components that can be
  regenerated exactly and treats the remainder as audit-only.
- **Audit-only** makes no exact-regeneration claim but still requires preserved
  outputs and sufficient evidence for meaningful review.

### 7.2 Common provenance record

Every material artifact record MUST identify, as applicable:

- a permanent artifact identifier, artifact class, content state, media type,
  creation time, owning authority, and sensitivity classification;
- every authoritative input by stable identifier, logical version, immutable
  revision or object version, media type, byte size, and cryptographic digest;
- the applicable Constitution, policy, specification, schema, prompt or
  instruction-set, and workflow versions by immutable reference;
- the agent, human, service, tool, model, and provider identities and versions
  involved, including unavailable or provider-opaque fields explicitly marked
  as such;
- material parameters, random seeds, sampling controls, environment,
  dependencies, fonts, toolchain, locale, clock or time source, and other
  influences needed to understand or repeat the work;
- an ordered transformation and tool-action history linking intermediate and
  final artifacts without silently collapsing human edits;
- validation results, warnings, failures, retries, uncertainty, exceptions,
  and the final disposition of the run;
- selection, rejection, edit, canon, and publication decisions, including the
  authority level, accountable humans, approval scope, and time; and
- the exact output identifier, storage reference, media type, byte size,
  cryptographic digest, and relationship to any release.

The record MUST distinguish facts observed from the system from explanations
or reconstructions added later. Unknown, unavailable, inapplicable, and
intentionally withheld fields MUST remain distinguishable; an empty field MUST
NOT silently represent all four.

Detailed schemas belong to Codex. A schema MAY organize these fields but MUST
NOT reduce the constitutional evidence or turn an embedded copy into the
authoritative input.

### 7.3 Provenance requirements by artifact class

The common record applies to all classes. The matrix adds minimum class-specific
evidence and the required reproducibility target.

| Artifact class | Additional minimum provenance | Reproducibility requirement |
| --- | --- | --- |
| **Generated text, code, or structured draft** | Exact input and output identities; prompt/instruction specification; model/provider identifier where available; parameters and seed; tool calls; candidate selection; human edits and approvals. | Traceable and auditable. Preserve the exact selected candidate; reproduce deterministic edits and formatting. |
| **Generated image, comic or comic component, audio, animation, or video** | Source-asset references; model and generation controls; candidate identifiers; selected source bytes; crop, composite, color, typography, audio, and other post-processing lineage; rights and approval references. | Traceable and auditable. Preserve selected source and final bytes; reproduce deterministic composition and post-processing. |
| **Authored text, image, or creative source** | Author/editor identity; authoritative source revision; referenced canon snapshot; material source assets; edit history; content state; approval and rights references. | Version history and deterministic export SHOULD reproduce the released representation; exact source and release bytes MUST be preserved. |
| **Manifest, report, metadata, or provenance record** | Governing schema/specification; generator version; complete ordered inputs; normalization rules; validation result; signer or attestation. | Exact reproduction is required except for explicitly isolated signature, timestamp, encryption, or transport envelopes whose payload identity remains verifiable. |
| **Lore context package** | Restricted source records; selection and minimization decisions; contract version; purpose; recipient; disclosure approval; expiry; package identity and digest; deletion or preservation evidence. | The authorized payload and deterministic transformations MUST be reproducible in the restricted environment. Randomized encryption envelopes may differ but MUST verify to the same approved payload identity. |
| **Software, build, or packaged technical artifact** | Source commit; dependency lock; compiler/runtime and toolchain; build workflow and environment; commands and configuration; test and security results; package identity and digest. | Deterministic build and packaging SHOULD be exact; any gap MUST be declared and the exact released bytes preserved and auditable. |
| **Published release** | Permanent release ID and revision; all output identities; complete public dependency graph; exact specifications and source revisions; build/run identity; validations; canon scope; rights notices; human approvals; private-context attestation when applicable. | Exact release assembly and manifest generation are required. Every released byte MUST be preserved and verifiable even when a nondeterministic source cannot be regenerated. |

### 7.4 Nondeterministic generation

Before using a nondeterministic mechanism, the workflow MUST declare the
expected reproducibility boundary. It MUST capture all exposed controls and
identifiers that materially affect the result, including model/provider name,
model or endpoint version where available, request or run identity, prompt and
specification versions, parameters, seed, tool state, time, and environment.

The workflow MUST preserve the exact returned candidate before edits, assign it
a stable identifier and digest, and record selection, rejection, and every
subsequent transformation. Manual edits MUST be represented as transformations
with an accountable actor; they MUST NOT be folded into a claim that the model
produced the final work unchanged.

A seed is evidence, not a guarantee. Provider opacity, mutable hosted models,
uncontrolled infrastructure, hidden safety transformations, race conditions,
and time-dependent sources MUST be recorded as limitations. If a material
identifier or control is unavailable, the record MUST say so and preserve the
best available request, response, and environment evidence in the appropriate
protected store.

A rerun is a new generation event and MUST receive a new artifact and run
identity. It MUST NOT overwrite the selected candidate or be presented as proof
that the original output was reproduced. If the preserved output or evidence is
insufficient for meaningful audit, the artifact MUST NOT be promoted to canon
or published.

### 7.5 Immutable release record

Before the A4 publication gate, the publisher MUST verify a proposed immutable
release record containing at minimum:

1. permanent release identifier, revision, authority, publication time, and
   declared canon scope;
2. provenance contract/schema name and immutable version;
3. every released artifact's stable URI or storage reference, media type, byte
   size, cryptographic digest, and rights notice;
4. exact public inputs, source commits, specifications, prompt/instruction
   versions, contracts, dependencies, toolchain, and build environment;
5. workflow and run identity, ordered material transformations, verification
   procedure, validation results, and available attestations;
6. model/provider/tool identifiers and material parameters for generated
   inputs, with unavailable fields and nondeterministic limitations declared;
7. accountable canon editor, publisher, other required approvers, approval
   scope, approved artifact identities, and decision times;
8. reproducibility classification, instructions, controlled boundary, preserved
   intermediates, and known gaps; and
9. whether private context influenced the release and, if so, only a random,
   non-derivable opaque attestation identifier in the public record.

Publishing makes the record append-only. A correction, withdrawal, retcon, or
replacement MUST create a linked new event; it MUST NOT rewrite the evidence of
what was released. The public record and artifacts MUST permit readers to verify
public identity and lineage without access to private systems. Authorized
reviewers MUST be able to follow the opaque private attestation to the paired
restricted record.

### 7.6 Audit records and verification

Audit records MUST be append-only or equivalently tamper-evident, time-ordered,
attributable, integrity-verifiable, and stored under the authority and
sensitivity appropriate to their contents. Corrections MUST preserve the prior
entry and identify who corrected it, why, and when.

An audit MUST be able to:

- verify artifact sizes, digests, signatures or attestations, immutable source
  references, and the ordered lineage graph;
- confirm that authorities, delegations, approvals, and content states matched
  the action taken;
- distinguish generated, authored, selected, transformed, and approved work;
- identify missing evidence, unverifiable claims, nondeterministic boundaries,
  failed checks, overrides, exceptions, and unresolved risk;
- trace an input, tool, model, approval, or defect forward to affected outputs;
  and
- perform the same checks in the restricted record without revealing protected
  content to a public reviewer.

Provenance completeness and integrity MUST be checked before canon promotion
and publication. The producing agent's self-report MAY contribute evidence but
MUST NOT be the sole verification of its own consequential actions. A missing,
corrupt, contradictory, or sensitivity-violating record blocks the affected
promotion or release until resolved.

### 7.7 Sensitive evidence and retention

Provenance records MUST NOT contain secret values, credentials, authentication
tokens, private keys, unnecessary personal data, or protected content merely to
make a record self-contained. They SHOULD record a non-secret configuration or
secret-version reference only when necessary, and only in a store whose access
does not broaden the underlying secret or data exposure.

Private Lore content, restricted prompts, private source identifiers,
content-derived private hashes, provider request identifiers, personal data,
and sensitive security evidence MUST remain in a paired restricted record when
needed for audit. The public record MUST contain only reader-safe evidence and a
random, non-derivable opaque link. Redaction MUST be explicit, must state the
withholding authority, and MUST preserve a complete authorized audit path.

Each provenance class MUST have a documented owner, purpose, access policy,
retention period or event, preservation obligations, and deletion method:

- official release records, released bytes, approvals, and evidence necessary
  to verify identity and public lineage MUST be preserved for as long as the
  Studio represents the release as official; withdrawal or deprecation MUST
  preserve the historical release record;
- restricted evidence needed to audit canon, rights, disclosure, security, or
  an official release MUST be preserved under least privilege for the required
  audit, legal, contractual, and incident-response period, then reviewed for
  minimization or deletion;
- rejected candidates, transient prompts, caches, and intermediate data MUST
  use the shortest documented period compatible with review, recovery,
  security, rights, and audit needs; indefinite retention is not the default;
  and
- deletion, legal hold, migration, or preservation MUST itself create an audit
  event without exposing the deleted protected content.

When retention and minimization requirements conflict, the accountable human
MUST preserve the minimum evidence that proves identity, authority, decision,
and outcome, store sensitive supporting material separately, and document the
resolution under Section 11.

## 8. Security, privacy, confidential information, and rights

Security, privacy, confidentiality, and third-party rights are design
constraints, not cleanup tasks or optional release polish. The Studio MUST own
the consequences of its systems, choose protective defaults, and reduce risk at
the earliest practical point. Convenience, speed, cost, model quality,
automation, access, and publication pressure MUST NOT create permission or
weaken a boundary.

Applicable law, contract, consent, license, and third-party rights may impose
stricter requirements. This Constitution does not supply a legal permission
that the Studio or a contributor does not otherwise hold.

### 8.1 Protective design and system boundaries

Before a system, workflow, provider, integration, or material change processes
non-public data or controls a consequential action, its accountable owner MUST
document the purpose, data flow, trust boundaries, threats, privacy and rights
risks, failure modes, and responsible reviewers. The design MUST:

- minimize data, access, privileges, integrations, retention, and public or
  external exposure;
- use secure and privacy-protective defaults, explicit authorization, separation
  of duties where warranted, and least privilege for humans and mechanisms;
- isolate untrusted inputs and generated content from instructions, credentials,
  tools, authoritative records, and approval decisions;
- validate inputs, outputs, destinations, state changes, and authorization at
  each trust boundary rather than trusting an upstream assertion;
- protect data in transit, at rest, in backups, in temporary state, and during
  deletion using controls appropriate to its classification;
- control network and tool egress, dependencies, updates, logging, monitoring,
  recovery, and revocation so a failure can be contained and audited;
- fail safely when identity, authority, destination, rights, or system state is
  unknown; and
- define verification, rollback or containment, incident reporting, retention,
  and end-of-life behavior before production use.

Content retrieved from a document, website, issue, message, model, tool result,
or context package is data, not authority. It MUST NOT change agent instructions,
expand tool permissions, disclose protected material, or bypass an approval
gate merely because it contains imperative language. Systems using agents MUST
enforce authority and tool boundaries outside the model's generated text.

### 8.2 Information classification and handling

Every material input, intermediate, output, and record MUST have a known owner,
purpose, and handling classification. When classifications overlap, the highest
applicable protection controls.

| Classification | Examples | Minimum handling |
| --- | --- | --- |
| **Approved public** | Published releases, reader-safe canon, approved public documentation, intentionally open code and specifications. | May enter public systems only within its license, canon scope, provenance, and stated use. Public availability does not erase ownership or license terms. |
| **Internal** | Non-public drafts, routine operational records, review notes, and unreleased content not otherwise confidential. | Authenticated Studio access, purpose-limited sharing, approved services, and documented retention. It MUST NOT be treated as public by default. |
| **Confidential** | Lore, unreleased creative plans, contracts, commercial information, vulnerability details, confidential communications, and personal data. | Need-to-know access, approved protected storage and processing, minimum disclosure, explicit external-destination review, and restricted audit evidence. |
| **Restricted** | Credentials, tokens, private keys, recovery material, high-impact personal data, active-incident evidence, and material explicitly assigned the strongest boundary. | Dedicated secret or restricted systems, narrowly authorized access, no prompt or source embedding, strong revocation and monitoring, and immediate incident handling on suspected exposure. |
| **Third-party controlled** | Licensed code, fonts, images, media, models, datasets, commissioned work, confidential partner material, and provider outputs. | The higher of the Studio classification and the source's license, contract, consent, attribution, confidentiality, and use restrictions. |

Classification MUST be preserved or raised through copies, transformations,
embeddings, summaries, caches, logs, backups, exports, and derived inferences.
Redaction, de-identification, or aggregation MAY lower handling only after an
authorized review confirms that the result cannot reasonably reveal or be
linked back to protected information in its intended context.

### 8.3 Secrets and sensitive data

Secret values, credentials, authentication tokens, private keys, recovery codes,
and equivalent access material MUST NOT be placed in prompts, source control,
issues, pull requests, chat messages, documentation, logs, telemetry, fixtures,
model context, generated output, manifests, or published artifacts. Systems MUST
obtain them through an approved secret-management and runtime-injection boundary
that prevents unnecessary exposure to humans, models, subprocesses, and logs.

Secrets MUST be scoped, rotated, revoked, monitored, and separated by purpose
and environment. A secret MUST NOT be reused to avoid provisioning work, exposed
to a tool that does not need it, or retained after its authorized purpose ends.
A suspected secret exposure is an incident even when use has not been observed;
the affected credential MUST be contained and rotated or revoked as soon as an
authorized responder can do so safely.

Personal data and other confidential information MUST NOT be collected,
inferred, combined, retained, or disclosed merely because it is available. The
accountable owner MUST establish a legitimate authorized purpose, identify the
minimum necessary fields and precision, limit recipients and uses, state the
retention or deletion event, and provide notice, consent, access, correction, or
other individual protections where required by the applicable relationship and
law.

Real personal, confidential, incident, production, or Lore data MUST NOT be used
as a public example, test fixture, benchmark, or debugging convenience.
Synthetic or approved reader-safe data SHOULD be used. When protected data is
strictly necessary, processing MUST occur in an approved environment with a
documented A4 disclosure decision, bounded purpose, and restricted evidence.

### 8.4 AI providers, integrations, and data minimization

Sending data to a model, API, plugin, connector, hosted tool, telemetry service,
or subprocess is a disclosure to a new processing destination. Before enabling
that destination, the accountable owner MUST evaluate and record:

- the exact purpose and why public, synthetic, redacted, local, or less
  sensitive alternatives are insufficient;
- permitted data classes, fields, volume, precision, context window, and
  connector scope;
- provider data use, retention, deletion, training or product-improvement use,
  human review, logging, subprocessors, processing locations, and incident
  notification;
- authentication, tenant isolation, encryption, access control, export,
  portability, deletion verification, and contract termination;
- ownership, output, confidentiality, indemnity, acceptable-use, and other
  terms relevant to the intended inputs and outputs; and
- the owner, approval level, monitoring, review date, revocation path, and
  evidence of the configuration actually in use.

Workflows MUST send the minimum necessary authorized data and MUST use the most
protective available training, retention, logging, and human-review settings.
Broad repository, mailbox, drive, calendar, or account access MUST NOT replace
purpose-scoped retrieval. Background access and connectors MUST expire or be
reviewed; removing a user interface integration is not proof that provider-held
data was deleted.

Confidential, restricted, personal, Lore, or third-party-controlled material
MUST NOT enter a provider's training, fine-tuning, evaluation, product
improvement, or human-review process unless an A4 owner has documented the
necessity, rights, privacy and security assessment, applicable consent, contract,
retention, and deletion conditions. A consumer account or default public service
MUST NOT receive such material merely because it is convenient.

Prompts, outputs, embeddings, safety-filter records, provider request IDs, and
usage metadata inherit the sensitivity of the information they contain or can
reveal. Provider assurances and interface labels MUST be verified against the
applicable contract and observed configuration; they are not substitutes for a
Studio handling decision.

### 8.5 Intellectual property and third-party material

Before third-party material is used beyond a quarantined rights review, the
Studio MUST know and record:

- the material's identity, provenance, source, owner or author, version or
  immutable revision, and acquisition date;
- the actual license, contract, permission, consent, or other rights basis—not
  merely a package label, marketplace description, or provider summary;
- whether the intended access, processing, modification, generation,
  adaptation, training, display, performance, publication, redistribution,
  sublicensing, and commercial use are permitted;
- territory, duration, media, audience, attribution, notice, source-disclosure,
  modification-marking, trademark, patent, confidentiality, privacy, publicity,
  and termination conditions as applicable;
- compatibility with the destination repository, artifact, license, and
  distribution model; and
- the accountable A4 human rights decision and any required qualified legal
  review when permission, ownership, authorship, fair use, or compatibility is
  uncertain or materially consequential.

A public URL, purchased copy, subscription, API response, model output, search
result, package download, lack of a notice, or technical ability to copy does
not grant rights. An AI system MUST NOT infer permission, ownership, public
domain status, fair use, or license compatibility from accessibility or
similarity. Unknown, unverifiable, conflicting, or questionable provenance
blocks use outside rights review and blocks publication or redistribution.

Rights and obligations travel with material through copying, format conversion,
translation, generation, editing, combination, embedding, packaging, and
publication. Required copyright, license, attribution, modification, source,
trademark, and other notices MUST remain attached or be reproduced in the
required location. A Studio license applies only to material the Studio has the
authority to license and MUST NOT overwrite third-party terms.

### 8.6 Material-specific rights checks

| Material class | Required rights evidence before publication or redistribution |
| --- | --- |
| **Code, packages, snippets, specifications, and templates** | Source and exact version; license and patent terms; compatibility; source or notice duties; modification markings; dependency and security review. |
| **Fonts** | Font license; copyright and Reserved Font Name terms; embedding, web, application, document, modification, and redistribution permissions; required license copy. |
| **Images, illustrations, audio, video, 3D assets, and stock media** | Owner and source; exact media/channel/commercial/derivative scope; attribution; model, property, location, music, and performer releases where applicable. |
| **Datasets and model inputs** | Collection and source rights; consent and privacy basis; dataset terms; training, evaluation, transformation, and redistribution rights; prohibited or withdrawn records. |
| **Models, weights, APIs, and provider outputs** | Model and service terms; weight or API license; acceptable-use limits; input and output terms; redistribution and commercial rights; provider opacity and provenance risk. |
| **AI-assisted or generated material** | Generation provenance; exact selected output; authorized input rights; provider terms; human authorship and edits; similarity, trademark, likeness, voice, and release review; scope of any ownership claim. |
| **Names, brands, characters, likenesses, and voices** | Trademark, publicity, privacy, endorsement, character, performer, and contractual permissions appropriate to the use and audience. |
| **Commissioned, contributed, or collaborative work** | Written authorship and ownership record; assignment or license; work-made-for-hire status where legally valid; contributor authority; credit; compensation and reuse terms. |

The Studio MUST document material human creative contribution and MUST NOT
represent purely generated material as exclusively human-authored or claim
ownership broader than applicable law and agreements support. AI assistance does
not cure an unauthorized input, remove third-party rights from an output, or
make a provider warranty sufficient on its own.

Using a person's name, likeness, voice, private information, or other identity
attribute to create a replica, endorsement, or misleading representation
requires an A4 human rights/privacy decision and the permissions required for
the actual use. Material selected to imitate an identifiable living creator or
to evade a rights boundary MUST NOT be published without documented rights and
editorial review.

### 8.7 Security, privacy, and rights release gate

Before canon promotion, public review, publication, or redistribution, the
accountable reviewer MUST verify for the exact candidate and destination:

- classification, authorized purpose, recipients, minimization, retention, and
  deletion obligations;
- absence of secrets and unapproved personal, confidential, restricted, Lore,
  incident, or vulnerability information, including indirect and metadata
  leakage;
- system, dependency, access, provider, model, prompt, logging, and integration
  risks and the status of required validation or remediation;
- a complete third-party inventory with known provenance, compatible rights,
  required notices, and human authorship or ownership scope;
- the exact approved bytes and provenance record, with public and restricted
  evidence separated; and
- all required A3 execution approvals and A4 security, privacy, disclosure,
  rights, canon, and publication decisions.

A disclaimer, attribution, takedown plan, provider assurance, later cleanup, or
ability to rotate a secret MUST NOT substitute for satisfying the gate. A known
unmitigated boundary violation or materially questionable provenance blocks the
affected promotion, review, publication, or redistribution.

### 8.8 Incidents and questionable provenance

A suspected credential exposure, unauthorized access, private Lore or personal
data disclosure, confidentiality breach, vulnerability, malicious instruction,
integrity failure, provider misuse, rights complaint, license conflict, unknown
source, or substantial-similarity concern MUST enter the private incident or
rights-escalation path. The reporter MUST NOT place sensitive evidence or the
questionable material in a public issue or discussion.

The accountable response owner MUST:

1. stop affected processing, promotion, publication, redistribution, and further
   disclosure while preserving the safest useful state;
2. contain access and distribution, quarantine affected material, and rotate or
   revoke exposed authority where authorized, without destroying evidence;
3. establish a private coordination channel and notify the appropriate security,
   privacy, Lore, rights, editorial, and repository owners with minimum
   necessary detail;
4. preserve an integrity-verifiable restricted timeline, affected identities,
   artifacts, systems, recipients, decisions, and containment evidence;
5. determine scope, exposure, ongoing risk, downstream dependencies, rights,
   contracts, and applicable notification, takedown, preservation, or legal
   obligations;
6. remediate or replace the cause and affected material, validate the result,
   and obtain authorized human decisions for disclosure, notification, release,
   or resumption; and
7. record the resolution, residual risk, affected releases, follow-up owners,
   review date, and lessons that must change systems or policy.

Agents MAY take only pre-authorized, narrow, reversible containment. When delay
would materially increase immediate harm, the emergency rule in Section 11
permits the narrowest protective action with evidence and prompt human review.
Investigation MUST NOT broaden access, reproduce harmful content unnecessarily,
contact a suspected rights holder as the Studio, or disclose the incident
without the responsible human's authority.

Questionable material remains quarantined until an authorized rights owner
verifies a sufficient basis for the intended use or directs documented removal
or replacement. Deletion, redaction, credential rotation, license purchase, or
provider removal does not erase the incident and MUST NOT replace the audit and
downstream-impact review.

## 9. Quality, validation, and release governance

Generation, assembly, rendering, building, or validation success creates an
output, not an approved release. Every artifact intended for an audience MUST
pass criteria appropriate to its purpose and risk, satisfy the minimum gates in
this article, and receive the required human decisions for its exact identity
and destination. Automation MAY establish evidence; it MUST NOT convert its own
success into publication authority.

Quality means fitness for the artifact's declared purpose while preserving
creative intent, continuity, accessibility, security, privacy, rights, and
technical integrity. It is not reducible to polish, validator success, audience
metrics, or similarity to prior output.

### 9.1 Release states and candidate identity

A release progresses through explicit states:

1. A **draft output** is generated, authored, assembled, or built and remains
   non-releasable.
2. A **release candidate** binds a stable candidate identifier and digest to a
   declared artifact scope, destination, audience, purpose, acceptance criteria,
   authoritative inputs, and release owner.
3. A **gate-complete candidate** has current evidence and a recorded disposition
   for every applicable gate, with no unresolved blocking finding.
4. An **approved release** is the exact gate-complete candidate authorized by
   the required A4 humans for its named destination, timing, and audience.
5. A **published release** is the approved identity actually made available and
   bound to its immutable release and provenance records.
6. A **superseded or withdrawn release** preserves the published history and
   records the corrective, replacement, or withdrawal event.

No state transition is implicit. A material change to bytes, composition,
content, executable behavior, authoritative inputs, destination, audience, or
release conditions creates a new candidate identity or revision. It invalidates
every validation or approval whose claim no longer applies. A publisher MUST
verify that the approved and published identities match exactly.

### 9.2 Acceptance criteria and validation plan

Before consequential validation begins, the accountable owner MUST record:

- the artifact's intended audience, purpose, quality target, content and canon
  scope, destination, and conditions of use;
- independently reviewable acceptance criteria, including intended creative
  effect and known acceptable variation where judgment is involved;
- the exact candidate identity, authoritative inputs, applicable specifications,
  policies, schemas, and Constitution version;
- applicable gates, severity thresholds, validator versions, qualified human
  reviewers, decision owners, and required separation of duties;
- accessibility and compatibility targets, evidence retention, and handling of
  private review material; and
- withdrawal, rollback, correction, and post-release monitoring expectations.

Criteria MUST be specific enough for a reviewer to explain why the candidate
passes or fails. A producer, model, or workflow MUST NOT redefine the criteria
after seeing its output merely to make that output pass. Creative criteria MAY
permit intentional ambiguity, stylization, or variation, but the accountable
editor MUST distinguish intent from an accidental defect.

### 9.3 Minimum release gates

Every release candidate MUST receive the following gates when applicable. A
gate with a human requirement cannot be satisfied solely by an automated result.

| Gate | Minimum evidence | Human requirement | Normal blocking condition |
| --- | --- | --- | --- |
| **Identity and scope** | Exact candidate digest; contents; destination; audience; purpose; criteria; governing versions. | Release owner confirms scope. | Unknown, mutable, mismatched, or incomplete candidate identity. |
| **Creative and editorial quality** | Review against intent, composition, pacing, clarity, tone, and audience expectations. | Qualified editor reviews the actual artifact. | Material failure of creative intent, meaning, audience fitness, or editorial criteria. |
| **Canon and continuity** | Applicable Universe snapshot; Lore-safe attestation; continuity findings and dispositions. | Authorized canon editor makes reserved decisions. | Unresolved contradiction, unauthorized canon claim, or Lore leakage. |
| **Visual and media consistency** | Layout, character and environment continuity, colors, typography, legibility, crop, resolution, audio/video, and export checks as applicable. | Qualified visual or media review of rendered output. | Material inconsistency, illegibility, broken presentation, or unintended visual change. |
| **Dialogue and text correctness** | Spelling, grammar, names, attribution, balloons/captions, reading order, localization, and semantic review. | Editor verifies meaning, voice, humor, context, and intentional deviations. | Meaning-changing error, wrong speaker or order, broken localization, or material voice failure. |
| **Manifest, schema, and artifact integrity** | Schema validation; referential integrity; checksums; package completeness; deterministic assembly; required metadata. | Release owner reviews failures, suppressions, and coverage. | Invalid contract, missing artifact, broken reference, unverifiable bytes, or non-reproducible required assembly. |
| **Technical behavior and compatibility** | Tests, supported-environment checks, performance and reliability evidence, and known limitations as applicable. | Domain owner accepts the demonstrated behavior. | Unsafe or unusable core behavior, data loss, or failure of a required supported target. |
| **Provenance and audit** | Section 7 lineage, reproducibility classification, evidence integrity, retention, and approvals. | Independent verification for consequential artifacts. | Missing, corrupt, contradictory, or sensitivity-violating material evidence. |
| **Security, privacy, confidentiality, and rights** | Section 8 release-gate evidence, third-party inventory, notices, and incident status. | Authorized domain owners make reserved risk, disclosure, and rights decisions. | Unmitigated boundary violation, questionable provenance, missing rights, or prohibited disclosure. |
| **Accessibility and audience safety** | Applicable accessibility checks, content treatment, warnings, and foreseeable audience-impact review. | Qualified human reviews experience and contextual risk. | Required access is prevented or the candidate creates unaccepted material harm. |
| **Packaging and release readiness** | Release notes, changes, known limitations, dependency and migration impact, support, rollback/withdrawal plan, and destination verification. | Publisher confirms operational readiness. | Missing required notice, unsafe migration, no viable recovery path, or destination mismatch. |
| **Final approval** | Complete gate record bound to exact candidate; unresolved findings and waivers; named approvers and decision times. | Authorized A4 editor, publisher, and domain owners approve their scopes. | Any missing approval, stale evidence, unresolved blocker, or candidate mismatch. |

A repository or artifact policy MAY add gates or make a conditional gate always
applicable. It MUST NOT remove a gate that applies to the artifact. The release
record MUST state why a gate was inapplicable; silence is not a passing result.

### 9.4 Automated validation and mandatory human review

An automated validator MAY conclusively establish only a bounded,
machine-verifiable predicate when its inputs match the exact candidate, its
version and configuration are recorded, its integrity is trusted, its coverage
and limitations are known, and its result is current. Examples include schema
conformance, checksum identity, link resolution, deterministic comparison, or a
specified test outcome.

Automation MUST NOT be the sole authority for creative intent, story meaning,
character voice, humor, emotional effect, visual storytelling, intentional
ambiguity, canon judgment, private disclosure, audience harm, rights or legal
permission, residual-risk acceptance, or publication. Those judgments require
a qualified accountable human reviewing the actual artifact and material
evidence, not merely an agent's summary or score.

The producer or generating agent MAY report checks and propose dispositions but
MUST NOT be the sole verifier of its own consequential work. Human review does
not erase an objective failure, and automated success does not satisfy a
reserved human decision. Passing every automated check therefore establishes
neither quality nor release approval.

### 9.5 Finding severity and release effect

Every finding MUST be classified by consequence rather than by the name or
default severity supplied by a tool:

| Severity | Meaning | Release effect |
| --- | --- | --- |
| **Blocker** | A violation or uncontrolled risk involving law, contract, constitutional requirements, authority, security, privacy, Lore, rights, safety, identity, evidence integrity, or essential behavior. | Release MUST stop until corrected. It is not eligible for a release waiver. |
| **Major** | A material failure of declared creative, editorial, continuity, accessibility, compatibility, reliability, or release criteria that does not independently constitute a Blocker. | Normal release MUST stop. A narrowly eligible waiver requires Section 9.7. |
| **Minor** | A bounded defect that does not alter meaning, canon, security, privacy, rights, safety, essential use, or the release's honest representation. | MAY proceed only after an accountable owner records disposition, user impact, and correction plan where needed. |
| **Advisory** | An improvement opportunity or observation that is not a failure of an applicable requirement or acceptance criterion. | Non-blocking, but MUST remain visible to the responsible owner when material. |

Uncertainty about a potentially prohibited disclosure, missing right, artifact
identity, required approval, or material provenance is a Blocker until resolved.
Related findings MUST be assessed together; multiple Minor findings that
materially impair the experience become Major. A suppressed, flaky, disputed,
or unavailable check is not a pass and requires an explicit evidence-based
disposition.

### 9.6 Validation evidence and freshness

For each gate, the release record MUST identify the candidate, criterion and
governing version, validator or human reviewer, relevant inputs and environment,
decision time, outcome, findings and severity, limitations, disposition, and
linked approval or waiver. Evidence MUST distinguish not-run, inapplicable,
passed, failed, inconclusive, and waived outcomes.

Evidence becomes stale when the candidate or a material input, criterion,
validator, dependency, environment, provider, destination, audience, or risk
assumption changes beyond the evidence's stated boundary. The owner MUST rerun
or repeat affected validation and obtain renewed approval. Reusing unrelated or
stale evidence, silently suppressing a result, or validating a representation
other than the artifact to be released is prohibited.

### 9.7 Release waivers and emergency releases

A release waiver MAY accept one identified Major or Minor finding only when the
underlying requirement permits risk acceptance and the candidate still conforms
to every applicable MUST and MUST NOT. A waiver MUST NOT excuse law, contract,
third-party rights, security or privacy boundary violations, Lore disclosure,
missing authority or A4 approval, unknown candidate identity, corrupt audit
evidence, invalid required provenance, or uncontrolled risk of material harm.

Every waiver MUST record the exact candidate and finding, severity, rationale,
residual risk, affected audience and destination, mitigating controls, qualified
domain-owner concurrence, A4 publisher approval, responsible follow-up owner and
issue, expiry or correction deadline, disclosure of the known limitation when
safe, and withdrawal or rollback conditions. It applies to one release only,
creates no precedent, cannot be copied forward, and becomes invalid when its
facts or candidate change.

An emergency release is permitted only to contain or reduce an immediate
security, privacy, safety, availability, rights, or disclosure harm. It MUST be
the narrowest viable change; retain exact identity, focused validation,
provenance, and an accountable A4 approval; record every deferred gate and the
reason; include rollback or withdrawal; and assign prompt, time-bounded
completion and retrospective review. Schedule, cost, marketing, convenience, or
generation effort does not create an emergency. A release waiver remains
governed by this section and MUST NOT be represented as a constitutional
exception under Section 12.

### 9.8 Approval, publication, and correction

Before publication, the A4 publisher MUST verify the complete gate record, the
authority and scope of each approval, the exact candidate identity and
destination, notices and known limitations, and the ability to withdraw or
correct safely. Publication MUST bind the released bytes to the immutable
release and provenance records required by Section 7.

The Studio MUST monitor releases according to their declared risk and support
expectations. A post-release defect receives the same severity analysis as a
candidate finding. A Blocker requires immediate containment and authorized
withdrawal, disabling, or correction as appropriate; a Major requires prompt
owner review and a recorded disposition. Correction, withdrawal, deprecation,
or replacement MUST be an append-only event and MUST NOT silently rewrite the
historical release.

## 10. Portability, interoperability, and vendor neutrality

The Studio MUST retain practical control of its creative work, governing truth,
technical contracts, production evidence, and ability to continue essential
operations when a tool, model, provider, account, format, price, policy, or
integration changes or disappears. Vendor neutrality does not prohibit using a
provider's distinctive capabilities. It prohibits allowing convenience or
lock-in to become ownership, authority, or an unreviewed single point of failure.

A portable representation preserves the meaning, identity, relationships,
rights, sensitivity, and evidence needed for an authorized independent tool or
human to use the data for its declared purpose. Exporting a screenshot, opaque
archive, flattened rendition, or provider-generated summary is not portability
when the authoritative structure or material information cannot be recovered.

### 10.1 Authority and control of durable Studio data

Every class of durable Studio data MUST have one Studio-recognized authoritative
home and at least one documented portable representation. The authoritative
record MUST remain addressable by Studio-controlled stable identifiers and MUST
NOT exist solely in an AI model, hosted assistant, provider dashboard, private
account, proprietary index, chat history, or undocumented application database.

An external service MAY store or process an authorized copy, but that copy does
not acquire authority. Provider object IDs and URLs MAY be recorded as mappings
or provenance; they MUST NOT be the only durable identifiers for Studio facts,
decisions, contracts, sources, or released artifacts. Canon remains controlled
by Universe, private Lore by Lore, stable technical contracts by Codex,
production implementations by Platform, and Studio governance by Studio even
when another system presents or transforms them.

The Studio MUST be able to export its authorized data without surrendering
ownership, confidentiality, integrity, provenance, or rights controls. A full
provider export is not automatically an authorized public export; Section 8
classification, minimization, disclosure, retention, and deletion rules remain
in force throughout migration.

### 10.2 Durable representation requirements

A durable representation SHOULD use open, documented, machine-readable,
widely implementable formats. It MUST have a published or Studio-owned syntax
and semantics sufficient to parse without the originating provider; explicit
encoding and media type; stable identities and relationships; versioned schema
or format references where structured; integrity verification; and documented
handling of optional, unknown, unavailable, redacted, and provider-specific
fields.

Human-readable views SHOULD accompany structured records when they materially
improve independent review. The Studio MUST preserve exact original bytes when
conversion would lose creative, evidentiary, rights, or technical information,
and MUST also maintain a documented access or preservation rendition when the
original requires a proprietary application. A portable representation need
not reproduce a provider's user interface or hidden implementation, but it MUST
preserve the Studio-owned information and behavior claimed by its contract.

| Durable data class | Minimum portable representation |
| --- | --- |
| **Constitution, governance, ADRs, policies, and stable specifications** | Versioned, human-readable text plus stable references and history; structured contracts include machine-readable schemas and conformance fixtures. |
| **Public canon and private Lore** | Versioned structured records and snapshots preserving identity, status, continuity relationships, decisions, and provenance. Lore exports remain encrypted or access-controlled and purpose-scoped; public and private truth MUST NOT be collapsed. |
| **Prompts, instructions, and agent behavior** | Provider-independent intent, inputs, expected outputs, constraints, tool contracts, acceptance criteria, and version history in documented text or structured configuration; provider-specific rendering remains a mapped derivative. |
| **Context packages** | Versioned Codex contract, exact authorized payload or lossless representation, purpose, consumer, sensitivity, expiry, source references, digest, and restricted audit link. Embeddings or provider indexes alone are insufficient. |
| **Manifests, metadata, and provenance** | Versioned, machine-readable records preserving identifiers, types, ordered relationships, lineage, approvals, rights, sensitivity, validation, digests, and explicit absent-value semantics. |
| **Creative sources and media** | Exact source and released bytes, edit and transformation lineage, required dependencies such as fonts or linked assets, rights metadata, and a documented preservation or access rendition when practical. |
| **Software, workflows, and infrastructure** | Source, Studio-owned interfaces, dependency locks, build and environment declarations, configuration without secrets, tests, migration behavior, and exact released artifacts. |
| **Decisions, reviews, and audit events** | Attributable, time-ordered, integrity-verifiable records with scope, authority, rationale, evidence references, outcome, and later corrections preserved. |

Retention of a portable representation MUST follow Section 7 and Section 8. A
conversion MUST NOT silently discard precision, order, identity, status,
comments with decision value, editability, accessibility, rights terms, audit
links, or security classifications. Loss MUST be identified before migration
and accepted by the accountable domain owner when acceptance is constitutionally
permitted.

### 10.3 Studio-owned contracts and provider adapters

Where practical, a material provider integration MUST sit behind a stable,
implementation-neutral Studio contract owned by Codex. The contract defines
Studio semantics, identities, capabilities, error behavior, security and data
boundaries, and import/export expectations without treating one provider's API
or response shape as the domain model.

Platform owns production adapters and MUST isolate provider credentials,
transport, object mappings, retries, limits, and provider-specific behavior from
the authoritative Studio record. It MUST preserve the exact provider and model
details required by provenance while mapping durable Studio meaning through the
stable contract. Consumers SHOULD negotiate declared capabilities rather than
infer a provider from an identifier or endpoint.

A provider schema MAY inform an adapter but MUST NOT be copied into Codex as a
nominally neutral contract without review. A Studio contract MUST have fixtures
or conformance tests sufficient to distinguish portable required behavior from
optional provider extensions. Provider replacement need not produce identical
nondeterministic creative output; it MUST preserve contract semantics,
authorities, evidence, and the ability to evaluate a new candidate under the
same acceptance process.

### 10.4 Export, restore, and migration verification

For every material external dependency, the accountable owner MUST maintain an
exit record identifying:

- owner, purpose, data classes, authority boundaries, provider and applicable
  contract versions, rights, confidentiality, and retention obligations;
- available export interfaces, formats, completeness limits, rate or cost
  constraints, encryption and access requirements, and provider termination or
  deletion behavior;
- Studio-controlled backups or exports, their location, freshness, integrity,
  schema, restore procedure, and responsible operators;
- the replaceable boundary, required capabilities, alternative implementation
  or continuity mode, expected data or feature loss, migration order, and
  rollback path; and
- review cadence, triggers for exit, accepted residual risk, and the A4 human
  responsible for continuation or termination.

Material exports MUST be exercised on a risk-based cadence and after a material
provider or contract change. Verification MUST parse the export independently,
check identity and integrity, account for expected records, restore a
representative protected copy or run a reference importer, and compare semantic
meaning and relationships rather than file count alone. Secrets MUST NOT be
embedded merely to make an export self-contained.

A migration MUST preserve provenance from old identifiers to new identifiers,
record transformations and loss, validate security and rights boundaries,
obtain the domain owner's semantic acceptance, and keep the prior record until
retention and rollback obligations are satisfied. Disconnection MUST include
credential revocation, authorized provider deletion or retention disposition,
and evidence of the resulting state.

### 10.5 Provider-specific capabilities and dependency decisions

A provider-specific capability MAY be used when it offers a material creative,
quality, safety, security, accessibility, operational, or economic benefit that
a reasonably available portable approach cannot supply at proportionate cost.
Its use MUST remain compatible with every higher authority and MUST NOT make an
external provider the exclusive authority or sole recoverable home for canon,
Lore, governance, specifications, approvals, provenance, or released assets.

Before consequential use, the accountable owner MUST record the capability and
provider, intended scope, benefit and alternatives considered, lock-in and
concentration risk, affected data and rights, portable baseline, isolated
extension boundary, degradation or continuity behavior, export and exit plan,
replacement cost, review or expiry date, and A4 approval. A missing equivalent
provider MAY justify a documented dependency; it does not justify an
undocumented one.

Provider extensions MUST be explicitly namespaced or capability-gated, MUST
fail clearly when unavailable, and SHOULD degrade to the portable baseline when
doing so remains safe and honest. They MUST NOT silently alter portable core
semantics or force unrelated consumers to adopt the same provider. Repeated or
indefinite renewal requires fresh evidence and review; a dependency decision is
not a constitutional exception and cannot waive security, privacy, rights,
canon, quality, provenance, or human-approval requirements.

### 10.6 Repository responsibilities

| Authority | Portability responsibility |
| --- | --- |
| **Studio** | Own constitutional rules, organization decisions, dependency-risk acceptance, and durable public governance history. |
| **Codex** | Own implementation-neutral schemas, interfaces, capability vocabulary, portable bundle contracts, versioning, fixtures, and reference validation or import behavior. Codex MUST NOT contain private story data. |
| **Lab** | Explore providers and formats with synthetic or approved public data, measure portability and loss, and preserve promotion lineage. A Lab prototype or provider SDK MUST NOT become a production dependency by direct import. |
| **Platform** | Implement and operate adapters, import/export paths, conformance checks, provider mappings, migration tooling, and production continuity controls without taking authority over creative inputs. |
| **Universe** | Preserve reader-safe canon, publication history, and public snapshots in portable Codex-governed representations. |
| **Lore** | Preserve private planning truth and restricted provenance, and create only minimized, authorized, expiring context exports under portable Codex contracts. Portability MUST NOT weaken confidentiality. |
| **Artifact owners and stores** | Preserve exact masters and releases, editable sources where required, rights and dependency metadata, integrity, backups, and documented access or preservation renditions. |

Promotion from Lab to Codex or Platform is a reviewed adoption with recorded
lineage, not a runtime dependency. Codex contract change precedes coordinated
Platform adapter change. Platform output returns to Universe only as a proposed,
validated artifact and manifest; processing never transfers canon authority.

### 10.7 Portability release and conformance gate

Before releasing a material contract, integration, workflow, migration, or
artifact whose continued use depends on an external provider, the accountable
reviewer MUST verify:

- the authoritative Studio home and portable representation for each durable
  data class;
- export identity, completeness, integrity, sensitivity, rights, provenance,
  and independent parse or restore evidence;
- isolation of provider-specific behavior behind the applicable contract and
  explicit treatment of unsupported capabilities and semantic loss;
- current exit ownership, continuation or fallback behavior, migration and
  rollback procedure, and provider deletion or retention obligations; and
- every provider-specific dependency decision, review date, accepted residual
  risk, and required A4 approval.

Missing portability evidence is classified under Section 9 by its consequence.
A dependency that makes protected authoritative data unrecoverable, prevents
essential audit, or gives an external provider exclusive authority is a Blocker.
A release tag, provider export button, API promise, local cache, subscription,
or theoretical alternative MUST NOT be treated as proof of portability.

## 11. Resolving conflicts

Principles are intended to constrain one another, not to provide slogans that
justify bypassing one another. A claimed benefit under one principle does not
waive a MUST or MUST NOT under another.

When rules or principles appear to conflict, the accountable human owner MUST:

1. identify applicable external obligations and every constitutional
   requirement or prohibition;
2. discard options that violate law, contract, third-party rights, an explicit
   MUST NOT, or an unmitigated security, privacy, or disclosure boundary;
3. identify the authoritative repository and owners for each disputed domain;
4. prefer an option that satisfies all requirements through narrower scope,
   least privilege, least disclosure, reversibility, additional review, or a
   delayed decision;
5. preserve human accountability and intentional review at any irreversible
   boundary;
6. document the facts, tradeoff, decision, owner, affected authorities, and
   review or expiry condition; and
7. use a Studio ADR when the resolution is durable, cross-repository, or likely
   to become precedent.

If two constitutional MUST requirements cannot both be satisfied, work MUST
pause. The conflict indicates a defect or missing distinction in governance and
MUST be escalated for constitutional review; a prompt, code path, deadline, or
output cannot resolve it by choosing silently.

An unresolved constitutional conflict MAY be resolved only by an amendment or
eligible temporary exception under Section 12. Work MUST remain paused unless a
more specific constitutional emergency rule permits the narrowest protective
action. Emergency action MUST preserve evidence, name an accountable Studio
owner, and enter review as soon as the immediate risk is controlled; urgency
does not silently amend the Constitution.

## 12. Amendment, versioning, and exceptions

The Constitution MAY evolve only through an intentional, human-approved,
traceable process that preserves its historical meaning and the ability to audit
which version governed an action. A prompt, precedent, deadline, output, ADR,
repository policy, waiver, exception, or implementation change cannot amend the
Constitution by implication.

Definitely Secure Studio is the constitutional authority. It exercises that
authority through named A4 constitutional stewards who can approve, reject,
delay, or withdraw a proposed constitutional change and remain accountable for
its consequences. An AI agent MAY draft, compare, analyze impact, or perform an
approved mechanical publication step; it MUST NOT propose on its own behalf,
approve, or make an amendment or exception effective.

### 12.1 What constitutes an amendment

A **constitutional amendment** changes the normative meaning, authority,
applicability, guarantees, obligations, prohibitions, reserved decisions,
definitions, amendment process, or conformance claim of this document. Adding,
removing, weakening, strengthening, or materially reinterpreting a MUST, MUST
NOT, SHOULD, SHOULD NOT, authority boundary, approval gate, or exception rule is
an amendment regardless of the label attached to the change.

The following do not amend the Constitution when they remain conforming:

- an ADR that records a durable decision within constitutional bounds;
- an RFC or Codex specification that defines a stable technical contract;
- a repository policy, checklist, prompt, schema, validator, workflow, or code
  change that implements a higher rule;
- a canon, Lore, editorial, release, security, privacy, rights, or provider
  decision made by its existing authority; or
- a correction to spelling, formatting, links, metadata, or wording that does
  not alter normative or reasonably relied-on meaning.

If reasonable reviewers disagree whether meaning or conformance changes, the
proposal MUST use the more consequential amendment classification until the
constitutional steward records why a lower classification is safe. An ADR MAY
explain an amendment but cannot make it effective without the exact
constitutional text, version, changelog, review, approval, and merge required by
this article.

### 12.2 Amendment proposal record

Every amendment MUST begin with a public proposal record unless Section 8
requires sensitive supporting evidence to remain restricted. The record MUST
identify:

1. the exact base Constitution version and immutable revision;
2. proposed text or reviewable diff, rationale, problem, intended outcome,
   alternatives, and consequences of no change;
3. proposed semantic version and whether the change is breaking, additive, or
   editorial, with an explanation rather than a label alone;
4. affected principles, articles, definitions, authorities, human decisions,
   external obligations, security/privacy/rights boundaries, and prior
   amendments or exceptions;
5. a downstream inventory covering known repositories, ADRs, RFCs,
   specifications, policies, contracts, schemas, prompts, agents, validators,
   workflows, data, releases, training, and delegations;
6. per-consumer impact, owner, migration or remediation, compatibility and
   deprecation plan, validation, communication, deadline, rollback or correction
   path, and unresolved risk;
7. proposed approval set, review period, effective point, transition behavior,
   and whether old-version operation remains permitted; and
8. issue, pull request, ADR when required, evidence, discussion, approvals,
   dissent, and later implementation records needed for a complete audit trail.

The public record MUST contain a reader-safe explanation of material effects and
withhold only what security, privacy, Lore, rights, or legal duties require. A
paired restricted record MUST preserve any withheld evidence and its authorized
review. Concealing material impact or affected consumers is not confidentiality.

### 12.3 Review, approval, and effective point

A Major or Minor amendment MUST have a Studio ADR and a protected pull request
containing the exact proposed Constitution, version, changelog, and related
records. A Patch MAY use a pull request with recorded rationale when it does not
change meaning. Every amendment requires:

- review by the constitutional steward and every known domain owner materially
  affected by the change;
- explicit A4 concurrence from each owner whose reserved authority is moved,
  narrowed, or exposed to new risk;
- qualified security, privacy, rights, Lore, editorial, accessibility, or
  technical review when the proposal affects that boundary;
- an independent approving reviewer when another qualified human is available,
  with any unavoidable self-approval identified in the record;
- resolution or explicit A4 disposition of material objections and known
  unknowns; and
- final approval by a named A4 constitutional steward for the exact commit.

No vote count, agent consensus, validator result, repository permission, or
passage of time substitutes for the required human authority. An amendment is
adopted when its approved commit is merged into protected `main`. It becomes
effective at merge unless the amendment records a later unambiguous date,
version event, or migration condition. A future effective point MUST identify
which version governs the transition and MUST NOT permit an unsafe ambiguity.

An amendment MUST NOT retroactively authorize a prior violation, erase an
incident or exception, rewrite the meaning of a historical version, or remove
the evidence used to make the decision. For versions before 1.0.0, the merged
commit is the immutable version reference. For version 1.0.0 and every later
effective version, the merged commit MUST also receive an immutable signed or
annotated `constitution/vMAJOR.MINOR.PATCH` tag and matching release record;
tags MUST NOT be moved or reused.

### 12.4 Constitution semantic versioning

The Constitution uses `MAJOR.MINOR.PATCH`:

| Change class | Version effect | Constitutional meaning |
| --- | --- | --- |
| **Major** | Increment `MAJOR`; reset `MINOR` and `PATCH`. | A previously conforming unchanged actor, system, policy, or workflow may become nonconforming; a relied-on guarantee is removed or weakened; authority or a reserved decision changes; or the meaning of an existing normative rule changes incompatibly. |
| **Minor** | Increment `MINOR`; reset `PATCH`. | A backward-compatible principle, rule, definition, evidence expectation, or governance capability is added without invalidating existing conforming behavior or weakening a relied-on guarantee. |
| **Patch** | Increment `PATCH`. | A correction or clarification changes no normative requirement, authority, conformance outcome, or reasonably relied-on meaning. |

Adding a MUST is Major when unchanged conforming consumers would fail it;
calling a weakening a clarification does not make it Patch. A security, privacy,
rights, Lore, or human-authority correction MAY require urgent adoption but is
still classified by compatibility, not urgency.

Every pre-1.0.0 Minor increment MAY contain breaking development changes. Its
proposal and changelog MUST still label actual compatibility and downstream
impact. Version 1.0.0 establishes the first stable constitutional compatibility
baseline; historical pre-v1 status does not excuse omitted review, history, or
migration.

Exactly one Constitution version identifies one immutable text. Two different
texts MUST NOT claim the same version, and one amendment MUST NOT silently
bundle unrelated normative changes merely to avoid multiple reviews.

### 12.5 Changelog and historical traceability

[`CONSTITUTION_CHANGELOG.md`](CONSTITUTION_CHANGELOG.md) is the authoritative
version index. Every amendment MUST update it in the same pull request with:

- version, adoption and effective dates, immutable commit and tag when required,
  issue, pull request, ADR, classification, and status;
- concise normative summary, rationale, affected articles and authorities,
  compatibility and downstream impact, migration or transition, and exception
  effects; and
- links to the proposal, review, approvals, dissent, impact inventory, and any
  restricted-record attestation that can safely be public.

The repository MUST preserve every historical Constitution text, changelog
entry, proposal, approval, amendment ADR, and effective or superseding event.
Corrections append a new entry and version; they MUST NOT rewrite a prior entry
to make history appear different. The current file MAY improve navigational
links to an old record only when the old immutable text and meaning remain
verifiable.

### 12.6 Breaking changes and downstream adoption

A Major amendment MUST NOT merge without an impact inventory and an A4-approved
transition plan for every known materially affected consumer. The plan MUST:

1. classify each consumer as unaffected, already conforming, change required,
   deprecated, retired, or blocked, and name an accountable owner;
2. identify exact old and new constitutional references, affected requirements,
   compatibility boundary, data or creative meaning changes, and validation;
3. provide ordered updates for ADRs, RFCs, specifications, policies, contracts,
   schemas, repositories, agents, prompts, workflows, delegations, training,
   releases, and audit controls as applicable;
4. state the notification channel, adoption deadline, migration assistance,
   rollback or safe-stop behavior, and treatment of work created during the
   transition; and
5. record each consumer's acknowledgment, adoption revision, validation result,
   residual risk, exception if any, and completion or block status.

Downstream references MUST remain pinned and MUST NOT silently float to a new
Constitution version. The Studio MUST notify affected owners through durable,
traceable records and coordinated changes, not only an ephemeral message.
A consumer MUST NOT claim conformance to the new version until its required
changes and validation are complete. If the new rule is immediately effective
and no safe transition is authorized, affected work MUST pause.

A Minor amendment still requires impact review and notification proportional to
its reach. A Patch requires confirmation that no downstream conformance or
meaning changes. Discovery of an omitted consumer or unexpected incompatibility
MUST reopen impact review and may require correction, delayed effectiveness,
temporary exception, or a new amendment.

### 12.7 Temporary constitutional exceptions

A **temporary constitutional exception** permits a bounded, time-limited
departure from one explicitly named eligible internal requirement. It does not
change the Constitution, interpretation, version, authority hierarchy, or
historical conformance of work outside its exact scope. It MUST NOT be used when
a release waiver, continuity decision, provider-dependency decision, narrower
conforming design, delayed action, or amendment is the proper mechanism.

No exception may override applicable law, contract, consent, or third-party
rights; transfer an A4 reserved human decision to an agent; authorize an
uncontrolled secret, personal data, confidential information, or Lore
disclosure; permit use or publication of materially questionable rights; erase
provenance, audit, incident, or approval history; authorize deception about
canon, authorship, ownership, safety, or conformance; or retroactively legalize
completed conduct. A constitutional MUST or MUST NOT is exception-eligible only
when the rule or this article permits bounded risk acceptance without defeating
the rule's purpose.

An exception request MUST record:

- the exact Constitution version, article and requirement, affected system,
  action, data, artifacts, people, audience, destination, repository, and time;
- necessity, evidence, alternatives tried, consequence of denial, why amendment
  or ordinary waiver is inappropriate, and the narrowest requested departure;
- security, privacy, Lore, rights, creative, quality, operational, and
  downstream risk, including uncertainty and affected external obligations;
- compensating controls, monitoring, stop conditions, rollback, remediation,
  notification, and evidence-retention plan;
- accountable owner, qualified affected-domain reviewers, A4 constitutional
  steward, approval times, start, and an expiry no later than 90 days; and
- public disclosure or a reader-safe summary with a random, non-derivable link
  to a complete restricted record when disclosure itself would cause harm.

Approval requires the A4 constitutional steward and every A4 domain owner whose
boundary or reserved authority is affected. An exception is active only after
those humans approve the exact record and it is entered in
[`CONSTITUTION_EXCEPTIONS.md`](CONSTITUTION_EXCEPTIONS.md). Immediate protective
action already authorized by a constitutional emergency rule MAY precede the
record, but cannot expand beyond that rule or continue as an exception without
prompt approval.

An exception expires automatically at its recorded time. Dependent work MUST
then stop, return to conformance, or operate under a newly approved amendment or
exception. Renewal is a new decision with current evidence, impact, approvals,
and a new maximum 90-day term; it MUST NOT be automatic or presumed from
continued operation. A second consecutive request for substantially the same
departure MUST also open an amendment or permanent-conformance plan. Repeated
renewal does not create precedent, and expired or denied exceptions remain in
the historical register.

### 12.8 Exception monitoring, closure, and audit

The exception owner MUST monitor the named risks and controls, preserve evidence,
report a breached stop condition immediately, and request revocation when the
necessity ends. An A4 constitutional steward or affected domain owner MUST revoke
or narrow an exception when its facts, scope, controls, law, rights, risk, or
candidate change materially.

Closure MUST record actual use, affected outputs and downstream systems,
incidents or unexpected effects, control performance, residual obligations,
remediation and validation, revocation or expiry time, and whether an amendment,
policy, training, or system change follows. Exception use MUST be visible in the
provenance and conformance record of every affected consequential artifact or
decision without exposing protected details.

The constitutional steward MUST review the active register at least monthly and
the complete exception history at least annually for repeated patterns,
concentration, overdue remediation, and attempted normalization. A recurring
need is evidence of a defective implementation or a potential amendment; it is
not evidence that the exception has become policy.

## 13. Definitions

- **Accountable human:** A named person with authority to approve, stop, explain,
  and accept responsibility for a decision and its consequences.
- **Approval gate:** A boundary that an agent cannot cross until an authorized
  human supplies an explicit, informed, scoped, and recorded approval.
- **Auditability:** The ability of an authorized reviewer to verify what
  happened, why, under whose authority, with which evidence and controls, and
  with what result, without requiring exact regeneration.
- **Audit record:** Integrity-verifiable, attributable, time-ordered evidence of
  actions, decisions, validations, and outcomes.
- **AI-assisted work:** Work in which a model materially generates, transforms,
  selects, evaluates, or directs content, code, metadata, or decisions.
- **Authority:** The recognized source entitled to establish truth, rules, or
  maintained behavior within a defined domain.
- **Breaking constitutional change:** An amendment that can make previously
  conforming unchanged behavior nonconforming, weaken a relied-on guarantee,
  move reserved authority, or incompatibly change normative meaning.
- **Canon:** Material whose public story-truth status was explicitly decided by
  an authorized canon editor and recorded in Universe. Active canon governs
  current continuity; deprecated canon records former status.
- **Continuity:** The coherent relationship among story facts, events,
  chronology, identities, perspectives, and declared ambiguities across works.
- **Content state:** The explicit governance status that determines whether
  creative material is a proposal, draft, Lore, active canon, or deprecated
  canon; publication is recorded as a separate release state.
- **Confidential information:** Non-public material whose unauthorized access,
  use, or disclosure could harm a person, the Studio, a partner, creative intent,
  security, privacy, or rights.
- **Constitutional conformance:** Satisfaction of every applicable MUST and MUST
  NOT, with documented treatment of applicable SHOULD and SHOULD NOT terms.
- **Constitutional exception:** A recorded A4 authorization for one bounded,
  eligible, time-limited departure under Section 12; it is not an amendment,
  waiver, precedent, or transfer of authority.
- **Constitutional steward:** A named A4 human authorized by Definitely Secure
  Studio to approve, stop, publish, correct, and account for constitutional
  amendments and exceptions.
- **Delegation:** A bounded grant from an accountable human permitting an agent
  to perform specified actions under stated limits, evidence, and escalation
  requirements.
- **Data minimization:** Limiting collection, inference, access, precision,
  processing, disclosure, retention, and replication to what an authorized
  purpose actually requires.
- **Deprecated canon:** Formerly active canon retained as a historical record of
  prior canon status but no longer controlling new continuity within its stated
  deprecated scope.
- **Draft:** Assembled, non-authoritative creative work that has not received an
  applicable canon decision.
- **Durable Studio data:** Information or artifacts whose loss, inaccessibility,
  or semantic degradation would materially impair authority, continuity,
  creative control, operation, release, rights, audit, or historical evidence.
- **Generated artifact:** Any content, code, data, media, manifest, or build
  output produced materially by software, automation, or AI assistance.
- **Interoperability:** The ability of independently implemented systems to
  exchange and preserve declared meaning through a documented contract rather
  than shared hidden assumptions.
- **Irreversible decision:** An action that is public, canonical, destructive,
  legally or commercially committed, security-sensitive, or costly to undo.
- **Incident:** A suspected or confirmed event that threatens security,
  privacy, confidentiality, integrity, availability, creative boundaries, or
  third-party rights and requires coordinated containment and review.
- **Lore:** Private planning material held in the restricted Lore authority,
  including explicitly labeled established facts, possibilities, alternatives,
  questions, retired plans, continuity, and unrevealed context.
- **Mechanism:** A prompt, model, agent, workflow, validator, manifest, context
  package, service, or code path used to perform work; a mechanism is not policy
  merely because it is executable.
- **Nondeterministic generation:** Production in which the same recorded request
  and apparent environment are not guaranteed to produce byte-identical output.
- **Personal data:** Information relating to an identified or reasonably
  identifiable person, including data that becomes identifying when combined or
  inferred.
- **Portable representation:** A documented, independently parseable form that
  preserves the identities, meaning, relationships, rights, sensitivity, and
  evidence required for its declared use outside the originating provider.
- **Principle:** A durable constitutional rule and rationale used to judge
  decisions across changing implementations.
- **Proposal:** A non-authoritative candidate idea, fact, change, or resolution
  submitted for consideration.
- **Provenance:** The integrity-verifiable lineage connecting an artifact or
  decision to its authorities, sources, rights, tools, versions,
  transformations, approvals, and exact output.
- **Release:** An intentionally approved artifact or collection made available
  to its intended audience under a stable identity and recorded terms.
- **Release candidate:** An exact, identified artifact or collection proposed
  for a declared audience and destination under recorded acceptance criteria;
  candidate status does not imply approval.
- **Release waiver:** A one-release, traceable A4 acceptance of a specifically
  eligible Major or Minor finding; it is not a constitutional exception or
  precedent.
- **Published artifact:** The exact, immutable evidence of material released to
  an audience, with its canon scope recorded separately.
- **Reserved human decision:** A judgment that an authorized human must
  personally make and record, even when an agent supplies analysis or performs
  subsequent mechanical execution.
- **Reproducibility:** The ability of an authorized party to follow a recorded
  procedure with pinned inputs and controlled conditions to produce
  byte-identical output.
- **Retcon:** An intentional human decision that contradicts, replaces, narrows,
  or reinterprets previously active canon while preserving its history and
  provenance.
- **Secret:** Authentication, signing, encryption, recovery, or equivalent
  access material whose disclosure could confer authority or defeat a control.
- **Specification:** A stable, implementation-neutral contract owned by Codex
  after its required acceptance process.
- **Traceability:** The ability to follow lineage backward from an artifact to
  its inputs and decisions and forward from an input or decision to affected
  outputs.
- **Third-party material:** Content, code, data, media, model, service output,
  identity attribute, or other material not created and wholly owned by the
  Studio for the intended use.
- **Vendor neutrality:** The preservation of Studio authority, recoverability,
  and meaningful provider choice; it does not require avoiding all proprietary
  capabilities or treating unlike providers as identical.
- **Validator:** A versioned human or automated mechanism that evaluates a
  candidate against stated criteria and produces evidence within declared
  limits; a validator does not possess publication authority by itself.

## 14. Authority, storage, and references

The authoritative Constitution is the root file
[`CONSTITUTION.md`](CONSTITUTION.md) in the public
[`DefinitelySecureStudio/studio`](https://github.com/DefinitelySecureStudio/studio)
repository. No mirror, generated copy, prompt excerpt, model context, wiki page,
or downstream repository may become a competing authority.

For Constitution 1.0.0 and later, a durable external reference MUST identify the
exact semantic version, immutable `constitution/vMAJOR.MINOR.PATCH` release tag,
and full Studio commit. A historical pre-1.0.0 reference MUST identify the exact
commit. `main`, a branch, a version range, `latest`, a copied file, or a web page
without the commit is not an immutable conformance reference.

ADRs, RFCs, specifications, repository policies, material agent instructions,
and release governance SHOULD state the Constitution version or commit they were
reviewed against. They MAY link the human-readable root file for convenience,
but compliance records MUST retain the immutable reference.

The authoritative version index is
[`CONSTITUTION_CHANGELOG.md`](CONSTITUTION_CHANGELOG.md). The authoritative
public exception index is
[`CONSTITUTION_EXCEPTIONS.md`](CONSTITUTION_EXCEPTIONS.md), paired with restricted
records where required. A mirror or summary of either file is non-authoritative.

## 15. Conformance and adoption

Conformance is an evidence-backed claim about a named subject, scope, version,
and point in time. It is not a general endorsement, certification of unrelated
work, or permanent status. A repository, policy, specification, system,
workflow, agent, decision, artifact, or release MUST be assessed within its own
authority and cannot inherit conformance merely because a dependency, tool,
template, or parent organization was assessed.

### 15.1 Minimum conformance record

A proposal, mechanism, or release MUST NOT claim constitutional conformance
unless its accountable owner can identify the applicable constitutional rules,
domain authorities, authority level, delegation, evidence, approval gates, and
unresolved risks. Every claim MUST record:

- the assessed subject, stable identity or revision, scope, excluded scope,
  purpose, environment, audience, and assessment time;
- Constitution version, immutable release tag, full commit, and checklist
  revision used;
- accountable human owner, qualified reviewers, affected domain authorities,
  and any required separation of duties;
- applicable articles and checklist profiles, explicit rationale for each
  inapplicable item, evidence locations, validation results, and evidence
  freshness;
- unresolved findings and severity, residual risk, release waiver,
  constitutional exception, transition, incident, or blocked decision; and
- status, approval scope and time, next review trigger or date, and an audit-safe
  record of corrections.

The operational minimum is
[`CONSTITUTION_COMPLIANCE.md`](CONSTITUTION_COMPLIANCE.md). A lower-level
checklist MAY add evidence or stricter gates but MUST NOT remove an applicable
constitutional question. Checking a box without evidence or treating silence as
inapplicable does not establish conformance.

### 15.2 Applicability profiles

A creative proposal, canon decision, or release MUST additionally identify its
content state, applicable Universe snapshot, Lore handling and disclosure
authority, continuity findings, and any correction, deprecation, or retcon on
which it depends.

A generated artifact or release MUST additionally identify its provenance
record, exact output identity, reproducibility classification and boundary,
audit status, retention authority, and any unavailable, withheld, or unresolved
evidence.

A system, provider use, third-party material, canon decision, or release MUST
additionally identify its information classification, authorized purpose,
minimum necessary data and access, approved processing destinations, retention
and deletion conditions, security/privacy/rights owners, applicable permissions
and notices, release-gate result, and any incident or questionable provenance.

A release MUST additionally identify its exact candidate and destination,
acceptance criteria, applicable gate outcomes and evidence freshness, human
editorial and domain approvals, unresolved findings and severity, any valid
single-release waiver, and rollback, withdrawal, or correction path. A
successful generation, build, render, or validation result alone MUST NOT be
represented as constitutional release approval.

A durable data system, provider integration, migration, contract, or dependent
release MUST additionally identify its authoritative Studio home, portable
representation and contract, export and restore evidence, provider-specific
extensions, semantic or data loss, exit owner and continuity path, and any
current A4 dependency decision. Provider access or an opaque export alone MUST
NOT be represented as constitutional portability.

An amendment, downstream adoption, or temporary constitutional exception MUST
additionally identify its exact Constitution version and revision, authority,
classification, rationale, review and approvals, effective or expiry point,
changelog or exception-register entry, affected consumers, migration or
compensating controls, validation, unresolved risk, and complete public or
paired restricted audit path.

An ADR, RFC, or stable specification MUST additionally identify the authority
that owns the decision or contract, alternatives and higher-rule constraints,
affected consumers, compatibility and migration, validation, and why the chosen
mechanism does not redefine authority or constitutional meaning.

A repository or agent workflow MUST additionally identify its responsibility
boundary, permitted and prohibited data, capability and authority limits,
delegation and escalation, tool and provider boundaries, durable records,
failure and recovery behavior, and the human approval required for every
irreversible action.

### 15.3 Conformance statuses and claims

An assessment MUST use one of these statuses:

| Status | Meaning |
| --- | --- |
| **Conforming** | Every applicable requirement is satisfied with current evidence and no unresolved blocking condition. |
| **Authorized exception** | One exact eligible departure is covered by an active Section 12 exception; no broader conformance claim is permitted. |
| **Transition required** | A version change has an approved migration plan, but required adoption or validation is incomplete. The subject is not yet conforming to the new version. |
| **Nonconforming — blocked** | An applicable MUST, MUST NOT, authority boundary, required approval, or blocking gate is unsatisfied. Consequential use or release MUST stop. |
| **Not assessed** | No complete current assessment exists. Absence of a finding MUST NOT be represented as conformance. |

A release waiver under Section 9 changes the disposition of one eligible release
finding but does not create constitutional conformance for an otherwise
nonconforming subject. A temporary constitutional exception authorizes only its
recorded scope and term. Expiry, material change, stale evidence, amendment,
incident, or breached stop condition invalidates the affected claim until
reassessment.

### 15.4 Downstream declaration and adoption

Every maintained Studio repository MUST publish a durable, reader-safe
declaration naming the Constitution version, immutable tag, full commit,
assessment status, covered scope, accountable owner, assessment revision and
date, evidence location, active exception identifiers, and next review trigger.
The declaration format and update rules are defined in the
[repository reference standard](repository-standards/CONSTITUTION-REFERENCE.md).

An ADR, RFC, specification, policy, agent instruction, workflow, manifest, and
release record SHOULD repeat the exact constitutional reference when its meaning
or approval depends on that version. A bare statement such as “constitutionally
compliant,” an unpinned link, or compatibility with a version range is
insufficient.

A Major Constitution version requires full impact review and explicit adoption.
A Minor version requires review of additions and affected assumptions. A Patch
requires verification that the subject did not rely on corrected wording and
that its pinned reference is updated when claiming the Patch. Adoption MUST
preserve the prior assessment and MUST NOT silently change the version governing
historical work.
