# ADR 0009: Canon, Lore, and continuity governance

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#42 — Define canon, lore, and continuity governance](https://github.com/DefinitelySecureStudio/studio/issues/42)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)
- Constitutional article: [Canon, Lore, and continuity governance](../CONSTITUTION.md#6-canon-lore-and-continuity-governance)

## Context

Definitely Secure Studio needs a durable boundary between public story truth,
private creative planning, unfinished work, generated material, and exact
published artifacts. Without explicit states and precedence, publication or
repetition can accidentally become canon, a private plan can leak through a
production system, or an internal note can silently rewrite what readers saw.

Universe and Lore already have separate repository ownership under ADR 0003,
and ADR 0006 defines immutable canon snapshots and minimal private context
packages. The Constitution must now govern the editorial decisions those
mechanisms serve without defining their future schemas or validators.

## Decision

Use two related but separate dimensions:

- an **editorial content state** of proposal, draft, Lore, active canon, or
  deprecated canon; and
- a **release state** identifying an exact published artifact and its declared
  canon scope.

Publication does not automatically promote content to canon. A published
artifact may be canonical, non-canonical, promotional, hypothetical, or mixed
when the scope is explicit. Every material creative item has an explicit state;
missing or unknown state is non-canonical.

Universe is the singular authority for active and deprecated public canon,
canon decisions, reader-safe continuity, released canon snapshots, and public
publication records. Lore is the singular private authority for unrevealed
continuity, established private facts, labeled possibilities and alternatives,
and approved context packages. Published artifacts are immutable evidence of
what audiences received. No processor, generated output, copy, or dependency
owns creative truth.

Canon promotion and publication are separate A4 human decisions. A combined
review is valid only when it separately identifies and approves the exact canon
scope and exact release artifact. Agents may propose and analyze but cannot
declare, promote, deprecate, retcon, or publish canon.

Canon promotion requires the exact candidate, pinned active canon snapshot,
minimum authorized Lore context when needed, continuity comparison, material
provenance, effective point, scope, and disposition of alternatives. The
decision record identifies the editor, accepted content, prior and new states,
rationale, affected records, and immutable references before consumers may
treat the material as canon.

Treat any meaning-changing correction as an A4 canon decision. A retcon is an
explicit A4 decision that preserves the prior canon and published history,
marks the old scope deprecated, identifies its replacement or intentionally
unresolved state, states an effective point and rationale, and records affected
artifacts and downstream updates.

Resolve apparent continuity conflicts by pinning exact sources, identifying the
question, testing whether scope, time, viewpoint, narrator, or explicit
ambiguity permits coexistence, and applying deterministic precedence:

1. the exact artifact controls what an audience received;
2. the latest applicable explicit Universe decision controls current public
   continuity, but a difference from publication requires an explicit
   correction, deprecation, or retcon;
3. absent such a later decision, approved canonical publication controls over
   contradictory unpublished documentation;
4. Lore controls only private planning and cannot override public canon; and
5. proposals, drafts, outputs, implementations, and memories carry no
   precedence over an authoritative record.

Equal-authority conflicts remain explicitly unresolved until an authorized
canon editor records an A4 decision. Last-write-wins, file order, timestamps,
repetition, and agent preference are not resolution rules.

Protect Lore as confidential material. Production receives only a minimal,
purpose-bound, approved context package—not a repository checkout or broad
export. Non-leakage covers content and indirect signals such as summaries,
negative confirmations, identifiers, paths, commits, hashes, embeddings,
prompts, logs, timing, and correlation metadata. Public records use a
non-derivable opaque attestation where private influence must be acknowledged.

Generated comic content is checked against a pinned Universe snapshot, the
minimum approved Lore context, its intended state and canon scope, relevant
continuity constraints, and a restricted non-leakage review. Automated checks
are advisory; unresolved conflicts, missing authority, unknown state, or
suspected leakage block promotion and publication.

## Rationale

Separating editorial truth from release state avoids two opposite mistakes:
treating all publication as canon and treating internal documentation as able
to rewrite published history. Singular repository ownership makes the current
authority discoverable, while immutable release evidence preserves what readers
actually received.

Explicit promotion and retcon decisions keep creative judgment human and make
continuity changes explainable. Minimum context packages and derived-information
controls recognize that Lore can leak through metadata and inference as well as
direct quotation.

## Consequences

### Positive

- Canon, Lore, drafts, proposals, deprecated material, and releases have
  unambiguous roles.
- Published history remains stable while current canon can evolve explicitly.
- Continuity conflicts follow a deterministic path instead of last-write-wins.
- Agents can assist with continuity without acquiring editorial authority.
- Private Lore has a hard disclosure boundary across public tooling and output.

### Tradeoffs

- Creative work must carry explicit state and authority references.
- Promotion, correction, and retcon decisions require durable editorial records.
- Lore-assisted production needs restricted comparison and non-leakage review.
- Some conflicts remain blocked until a canon editor makes an explicit decision.

## Rejected alternatives

### Treat every published artifact as wholly canonical

Rejected because promotional, hypothetical, framing, or deliberately
non-canonical material may be published, and individual statements may have an
explicitly limited canon scope.

### Let the newest internal document override publication

Rejected because last-write-wins silently rewrites reader experience and hides
whether a correction or retcon was intentional.

### Treat all Lore as established future canon

Rejected because Lore contains possibilities, alternatives, questions, and
retired plans as well as established private continuity.

### Give production systems direct Lore access

Rejected because broad access defeats least disclosure, increases leakage risk,
and lets implementation convenience blur creative ownership.

### Let validators resolve contradictions automatically

Rejected because continuity can depend on viewpoint, ambiguity, theme, and
intentional creative judgment that a mechanical consistency check cannot own.

## Implementation

The Constitution contains the normative content states, ownership boundaries,
promotion and retcon rules, conflict precedence, Lore confidentiality controls,
and generated-content review requirements. Universe, Lore, Codex, and Platform
may implement schemas, approval records, context-package contracts, and
validators that preserve these rules without becoming the creative authority.
