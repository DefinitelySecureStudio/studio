# Comic Manifest v1 architecture

Proposed in [ADR 0018](../adr/0018-comic-manifest-architecture.md) for
[#88](https://github.com/DefinitelySecureStudio/studio/issues/88), the first task
in [Epic #6](https://github.com/DefinitelySecureStudio/studio/issues/6).
This document assigns architecture and acceptance boundaries. It is not a
schema, implemented API, approval record or creative canon. Serialization,
field names and normative semantics belong to Codex in #89.

## Foundations and ownership

Reuse [Prompt SDK v1.0.0](https://github.com/DefinitelySecureStudio/platform/releases/tag/prompt-sdk/v1.0.0),
[Context Builder v1.0.0](https://github.com/DefinitelySecureStudio/platform/releases/tag/context-builder/v1.0.0)
(Platform `7df7ea812e0987167407a07ab48b4b7e9a33f91b`) and its
[Codex contract v1.0.0](https://github.com/DefinitelySecureStudio/codex/releases/tag/contract/context-builder/v1.0.0)
(`2301597014f6fefe8a3cf772e2e02527cda6a254`). Context Package v1.0.0 and
all released Prompt SDK/Builder contract and implementation bytes remain unchanged.
These release references identify the design baseline, not a production lock:
consumers must adopt complete verified release artifact tuples.

| Owner | Records and operations | Boundary |
| --- | --- | --- |
| Studio / @andrewperis | Architecture, sequencing, governance, assessment and epic closeout | No runtime schema or implementation |
| Codex maintainers | Three record contracts, identity/linkage semantics, approval bindings, compatibility and synthetic fixtures | No production content or orchestration |
| Platform maintainers | Parse, validate, verify references/results, authoring CLI, review reports, safe release proposals and offline reference consumer | No self-approval, creative authority or canon promotion |
| Production owners with Lore/source owners | Protected production manifests, approved private artifacts and restricted build/provenance records in Lore or approved secure storage | Never public Platform/Codex source, fixtures, logs or artifacts |
| Universe editors / authorized publisher | Permanent publication identity, approved public comic/release records, publication and separately declared canon scope | No automatic adoption of generated facts |
| Authorized source/policy and disclosure reviewers | Preparation and current package-use decisions; restricted attestation mapping and disclosure approval | Verifiers enforce decisions; producers cannot grant themselves authority |
| Epic #7 in Platform | Future execution coordination and build-result production through the contracts | No hidden retrieval, permission renewal or publication authority |
| Lab maintainers | Optional public/synthetic experiments | Never a runtime dependency |

The [repository architecture](../ARCHITECTURE.md) and
[dependency strategy](../dependency-strategy/README.md) continue to govern.
Public code may process protected runtime inputs only within approved boundaries;
its repository visibility does not declassify the inputs or generated outputs.

## Three linked records

| Record | Required meaning | Identity and storage |
| --- | --- | --- |
| Production manifest | Episode intent; ordered panels; dialogue/captions; asset and rendition requirements; exact canon, prompt, context and tool/contract inputs | Opaque production ID plus immutable revision and byte identity; protected according to contents and lineage |
| Build-result record | Exact production revision; distinct attempt identity; actual verified input identities; produced artifacts; validations, transformations, execution/provenance evidence and explicit failures/limitations | Immutable result identity; references the input manifest exactly; restricted by default when linked inputs/evidence are protected |
| Public release manifest | Permanent episode ID and release revision; approved published outputs, public dependencies, rights/credits, release gates, safe provenance and declared canon scope | Immutable reader-safe candidate, then Universe-owned append-only publication record |

The production manifest is a specification, not execution progress. Results may
report partial or failed work, but these are not successful release evidence.
Multiple results may reference one production revision; selected output bytes
and the chosen result must be explicit, never inferred from “latest” or a path.
One result may support multiple explicitly scoped release proposals; approvals
do not transfer automatically between them.

Restricted lineage binds all three identities and exact output artifacts. A
public release must not include a protected production/result digest, ID, path,
package fingerprint or approval identity merely to complete that graph. Public
readers verify public dependencies and released bytes independently; authorized
reviewers follow an approved opaque attestation to restricted evidence. Public
approver attribution is distinct from private-source approver identities.

## Identity, panel scope and immutable inputs

Drafts receive a stable opaque production identity independent of title, date,
private content and publication order. A new saved revision is immutable and
links to its predecessor; a mutable editor buffer is not approved evidence.
Revision labels alone do not establish byte identity or authority.

Universe editors assign the permanent `DS-NNNN` identity separately, according
to [comic identity policy](../brand/comic-identity.md), before final candidate
approval. The assignment is explicit, unique and never reused. Concurrent or
conflicting assignments stop for editorial resolution. Cancelled drafts do not
automatically consume numbers. Corrections, translations, reposts and collections
retain the episode identity; changes to released content create linked revisions
or events with fresh applicable review. Numbering overflow/reservation mechanics
need owner-reviewed Codex semantics; no tool may silently change the format.

A v1 production manifest describes one comic with a nonempty explicit panel
order. Panel identities are unique within the production identity and stable
across edits; order is a separate relationship, never inferred from IDs or object
key order. Reordering, adding/removing panels or changing text creates a new
production revision. Dialogue/captions have explicit reading order and panel
association. Asset requirements distinguish required from optional inputs and
outputs and identify panel/episode scope. Dangling, duplicate or ambiguous
references fail validation. Exact limits and allowed vocabularies belong to #89.

Creative text is data. Generation instructions bind reviewed immutable prompt
definitions and declared slots; dialogue, captions, asset metadata and fetched
content cannot become commands, permission or prompt-policy overrides. Layout
requirements may describe intended ordering, dimensions and constraints without
embedding scripts, shell commands, arbitrary URLs to execute or a workflow DSL.

Every public dependency uses the full stable tuple: repository, logical version,
immutable tag, source commit, artifact URI, media type, byte size and SHA-256
digest. Verify bytes before parsing/use. Private references use approved secure
immutable artifact interfaces and stay restricted. Missing bytes, floating
versions, mismatched digests or unsupported contracts fail explicitly; parsing
never fetches, refreshes or substitutes an input implicitly.

Pin the input canon snapshot `C(n)`, prompt definitions, exact Context Package
instances/references, Builder evidence and SDK provenance. Validate relationships
between them, including the package target prompt/version, purpose and section
scope. Stored Builder preparation evidence is historical, not current use
permission. A release may enter `C(n+1)` later but must never claim that later
snapshot containing itself as an input.

## Gates, lifecycle and invalidation

These are semantic transitions, not proposed schema enum values. State labels
are derived from verified evidence and explicit decisions; caller-supplied
“approved” or “published” flags have no authority.

| Boundary | Required decision/evidence | Failure behavior |
| --- | --- | --- |
| Source preparation | Trusted current preparation authorization before source access; exact source, purpose, recipient and time scope | Deny before reads; no direct Lore checkout or fallback credentials |
| Package use | Separate current exact-instance authorization checked at actual use, including prompt, purpose, sections, classification, time and revocation | Expiry/revocation or unverifiable scope blocks use even if preparation previously passed |
| Production review | Authorized reviewers inspect exact intent, inputs, panel/text requirements, rights and intended outputs | New revisions remain proposals; validation cannot approve creative meaning |
| Result verification/review | Verify exact manifest linkage, selected artifacts, required outputs and current applicable gate evidence | Missing, substituted, unexpected or corrupt artifacts and unresolved failures block candidate progression |
| Attestation/disclosure | Authorized issuer creates random non-derivable ID, stores exact restricted mapping and separately approves public disclosure scope | No derived IDs, automatic declassification or issuance by the build itself |
| Publication/canon | Universe editor and required A4 humans approve exact gate-complete candidate, artifacts, destination, audience, purpose and timing; canon scope explicit | No publication or canon promotion from build success, attestation or a status string |

Production progresses from authored draft to validated revision to reviewed
revision eligible for its declared production purpose. This does not authorize
all future context use. Execution creates a separate result; verification creates
separate attributable evidence without mutating the production manifest or result.

Public release progression follows Constitution §9.1: draft output → exact
release candidate → gate-complete candidate → approved release → published
release → superseded/withdrawn release. Each transition has an explicit evidence
record. Before publication, verify approved and published identities match.
Publication appends the immutable record; correction, withdrawal and retcon
append linked events, preserving the original evidence and episode number.

Approvals are separate attributable records binding the exact revision/digest,
selected artifact set, governing versions, authoritative inputs, approval scope,
reviewer authority, decision time and applicable validity/revocation conditions.
Canonicalization, digest coverage and non-circular approval envelopes are Codex
gaps; approval must not require modifying its already-approved payload to insert
a signature or status. Hash equality proves identity, not reviewer authority.

| Change or discovery | Required consequence |
| --- | --- |
| Panel order, prose, prompt/context, asset, canon input, tool/contract version or output requirements change | New production revision; invalidate affected production review, dependent results and release-candidate evidence for the new revision |
| Output bytes, composition, rendition, rights/credits, public projection, destination, audience or release conditions change | New candidate identity/revision and fresh affected verification/approval; unchanged evidence reusable only with explicit matching scope |
| Grant expires/revokes or trusted policy/authority cannot be established | Block the affected current access/use/release; preserve historical facts without renewing permission |
| Missing validation, stale evidence, failed gate or unresolved blocking finding | Cannot become gate-complete; report safe failure and route to authorized owner |
| Post-publication defect or authority concern | Containment and owner review, then authorized append-only correction/withdrawal; never rewrite history |

Stored results remain historical evidence when no longer eligible for new use.
Permission expiry does not itself erase historical publication; its consequences
follow the grant and release policy through the responsible human. Material
changes conservatively invalidate dependent claims unless exact unaffected scope
can be established. No silent renewal or inherited blanket approval is allowed.

## Output requirements and public projection

Declare required renditions, media types, dimensions/other applicable constraints,
reading order, useful alternative text/transcript requirements, title/number,
credits, copyright, third-party rights/notices and intended distribution scope.
Platform checks completeness and technical consistency. Human review evaluates
storytelling, accessibility, continuity, rights and disclosure on actual outputs.
V1 does not generate images, render layouts or establish rights from a filename.

Projection constructs a new allowlisted record; it never serializes a production
object and removes a few known private keys. Follow the complete public record
minimums in Constitution §7.5 and [release provenance](../dependency-strategy/PROVENANCE.md):
exact public contract/tool/canon inputs, released artifact URI/media type/size/
digest/rights, public workflow/run and transformation evidence, validations,
public approval scope/times, declared canon scope, reproducibility class and
known gaps. Include provider/model/material generation parameters where safe,
with explicit unavailable/withheld evidence semantics rather than invented data.

If private context influenced production, publish only that fact and one approved
random opaque private attestation ID for its lineage. Keep private source names,
URLs, commits, paths, object versions, hashes, package IDs, approval identities,
content-derived fingerprints and raw evidence out of public fields, logs and
errors. Review free text, filenames, URLs, accessibility text and output bytes
for disclosure as well as structured metadata. Classification propagates through
derivation until authorized disclosure; projection cannot lower it automatically.
Restricted records follow approved access, retention/deletion and audit policies.

Attestation fakes are test fixtures, not production trust roots. Production issuer,
trust verification, revocation and secure storage onboarding require separate
review. Missing or unverifiable required evidence fails closed. Deterministic
processing is reproducible; external generation is only as reproducible as its
documented controlled inputs and preserved selected outputs permit.

## Epic #7 consumer boundary

Epic #6 provides contract-backed parsing, semantic/reference validation, result
verification, review reports, safe projection and an offline reference consumer.
The handoff accepts explicit bounded bytes, pinned supported contracts/artifact
references, policies, evaluation time and injected authorized verification/read
interfaces. It returns typed validation outcomes, immutable record identities,
verified artifact relationships and proposals; it does not schedule execution.

Epic #7 consumes an eligible exact production revision and independently checks
current execution/package-use authority before invoking tools. It supplies attempt
and correlation identities and records actual inputs, ordered transformations,
selected outputs, SDK/Builder evidence, failures and nondeterministic limitations
in the result contract. Reusing or retrying work does not renew permission.
Partial/failure results cannot masquerade as verified completion.

Pure validation has no hidden network, wall clock, random IDs or source refresh.
Explicit artifact I/O is bounded, authorized and verifies expected bytes; public
diagnostics use safe codes/stages without protected values. Parsers reject
unsupported versions, malformed/oversized data, duplicate/ambiguous identities,
unrecognized fields where contracts prohibit them and inconsistent relationships.
Untrusted paths/URIs cannot escape approved readers or invoke arbitrary tools.

Scheduling, retries, resumable jobs, provider routing, multi-step execution,
illustration, rendering/lettering/layout engines and distribution automation are
Epic #7 or later work. Universe Bible (#15), Lore (#16), First Comic (#17), real
private-source access, production trust/signing infrastructure, npm publication
and repository visibility changes are excluded from this design task.

## Offline synthetic vertical slice and contract gaps

The acceptance slice uses no real story facts, private exports, network calls or
paid providers. Synthetic fake-private data is public test data tagged to exercise
handling rules, never an actual private source. Test episode numbers live only
in fixtures and do not reserve real `DS-NNNN` identities.

1. Codex supplies reviewed synthetic two-panel content, public snapshot/assets,
   fake-private export, pinned prompts/packages and deterministic policy fixtures.
2. Platform validates the immutable production revision, ordered relationships,
   full references and separate preparation/current-use evidence at explicit time.
3. An offline mock consumer emits fixed rendition bytes and a separate build
   result bound to the exact production revision; no renderer or orchestration.
4. Verify output requirements, digests, selected result and gate evidence. Build
   the restricted linkage and an allowlisted reader-safe release proposal.
5. A separate synthetic authority fixture approves exact candidate/artifact scope
   and attestation disclosure. Verify publication eligibility and append-only
   correction in the mock consumer; nothing is published to Universe.
6. Replay with identical inputs/time to demonstrate deterministic processing.
   A public-only verifier checks the release without accessing restricted records.

Focused negative cases accompany their implementing issues: denied preparation
causes zero reads; expired/revoked package use remains denied despite historical
approval; panel reorder/byte tampering invalidates approval; wrong manifest/result
link, floating references, missing renditions or altered artifacts fail; forged
approval/status does not pass; private sentinel values in nested metadata, URLs,
text and diagnostics cannot reach public output; absent attestation disclosure
blocks projection eligibility; a correction never overwrites the original.

| Codex gap for #89 | Required resolution / consuming work |
| --- | --- |
| Three record schemas and identity/linkage semantics | Versions, revision ancestry, panel order/IDs, production-to-public mapping, selected attempt and failure vocabulary; #90–#91 |
| Immutable references and integration relationships | Complete tuples, limits, supported foundation versions, exact Builder/package/prompt/SDK linkage, classification rules; #92–#93 |
| Rendition and publication requirements | Required/optional outputs, accessibility, credit/rights and numbering consistency; #94 |
| Approval and invalidation semantics | Exact payload coverage, detached evidence, scope/time/revocation, issuer trust boundary and gate dispositions; #95 |
| Results and safe projection | Artifact matching, allowlisted public fields, restricted links, opaque attestation and unavailable/withheld evidence semantics; #96 |
| Compatibility and conformance | Canonicalization, unknown fields, resource bounds, safe errors, feature support, positive/negative fixtures and deterministic replay; #97–#98 |

Resolve normative gaps in Codex before consumer implementation; do not create
Studio schemas or Platform contract forks. Coordinate contract-owner and Platform
feasibility review before #89 acceptance. New contracts use immutable releases;
unsupported versions fail explicitly, and breaking changes require new versions,
migration and reviewed adoption. Preserve old artifacts and lineage for rollback;
rollback never reinstates revoked permission. #99 releases contracts before their
Platform consumer and verifies complete artifact tuples/downloaded bytes.

## Scoped constitutional assessment and review status

- Subject: issue #88 architecture change against Studio base
  `813696a80af724c0541bacaba8d3ffba7bee6578`; exact adopting revision to be recorded
  in the owner review. Public design documentation only; no runtime/release claim.
- Constitution: v1.0.0, tag `constitution/v1.0.0`, commit
  `a9cc8a503aa30e17820edc62ac95f7cbe10e0564`.
- Checklist: [CONSTITUTION_COMPLIANCE.md](../CONSTITUTION_COMPLIANCE.md) at base
  `813696a80af724c0541bacaba8d3ffba7bee6578`.
- Accountable owner: @andrewperis. Required affected reviewers: Codex contract
  maintainer, Platform maintainer and Universe editorial owner; source/disclosure
  owner for the private-evidence boundary. Their reviews are pending.
- Assessment prepared: 2026-09-17. Status: **Not assessed** for final constitutional
  conformance; design evidence below is proposed, not owner approval.

| Applicable profile | Proposed evidence | Remaining assessment |
| --- | --- | --- |
| Universal | Singular ownership; separate A4 gates; exact provenance; privacy/rights propagation; portable deterministic records | Qualified human review of all applicable checklist items |
| ADR/specification | ADR context, alternatives and consequences; Codex gaps, compatibility and rollback | Codex semantics and exact-revision owner acceptance |
| Repository/production system | Existing topology, immutable artifact interfaces, content-neutral public tooling | Platform feasibility review; runtime controls assessed in implementation tasks |
| Automated workflow | Explicit effects, current authority, safe failures, no self-approval and synthetic negative cases | Tests and operational evidence in #90–#98 and Epic #7 |

Creative/canon and release profiles are not assessed as executed activities:
this task creates neither canon nor a production release. Their design obligations
are captured in the gates and output sections for later candidate assessments.
No amendment/exception is requested because no constitutional meaning or authority
changes. Do not claim `Conforming` or close owner-review acceptance criteria from
this proposal alone. Reassess before #89 acceptance and whenever authority,
classification, contracts, identity, storage, evidence freshness or consumer
boundaries change.
