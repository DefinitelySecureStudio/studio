# Context Builder v1 architecture

Proposed in [ADR 0017](../adr/0017-context-builder-architecture.md), issue #75.
This is an architecture/API outline, not a Codex schema or implemented API.
Field names and serialization become normative only through #76.

## Ownership and immutable baseline

| Owner | Responsibility | Exclusion |
| --- | --- | --- |
| Studio / @andrewperis | Cross-repository architecture and review | Runtime dependency |
| Codex maintainers | Builder request/source/policy/result contracts | Runtime or creative content |
| Platform maintainers | Builder core, explicit adapters, tests and CLI | Canon authority or self-approval |
| Universe editors | Approved immutable public canon snapshots | Private lore |
| Lore/source owners | Minimal authorized exports and restricted evidence | Broad export to public tooling |
| Authorized policy/human reviewer | Access/preparation decision and exact package-use decision | Delegating reserved judgment to generated output |
| Lab maintainers | Synthetic/public experiments and promotion evidence | Production import |
| Manifest/Orchestrator owners | Build records and multi-step coordination | Taking over source or policy authority |

The supported baseline is [Prompt SDK v1.0.0](https://github.com/DefinitelySecureStudio/platform/releases/tag/prompt-sdk/v1.0.0),
Platform commit `e5fb340bdddd631f8d873e5feab9ef4a4e4b0b31`, and five
Codex 1.0.0 releases at `62e78b606986988518b9dc502c25ae1cd189684a`.
Exact schema/bundle asset tuples are recorded in Platform's
[released contract lock](https://github.com/DefinitelySecureStudio/platform/blob/e5fb340bdddd631f8d873e5feab9ef4a4e4b0b31/release/contract-lock.json).
Private inputs use approved secure immutable objects; a public tuple must not
disclose their locations or fingerprints.

| Released contract | Reuse | Gap reserved for #76 |
| --- | --- | --- |
| Prompt Definition | Exact id/version, declared slots, media/classification/size constraints | Build-intent mapping and selection requirements |
| Context Package | Inline sections/source lineage, manifest identity, detached reference, use authorization | Preparation authority, normalized candidates, assembly policy and builder result |
| Provider Execution | Downstream portable request/result boundary | None: Builder never invokes a provider |
| Structured Output | Downstream JSON processing | None: Builder does not perform model output processing |
| Execution Provenance | Links execution/correlation/package evidence | Builder selection/omission, preparation and restricted/public audit evidence |

Context Package authorization binds the exact prepared instance, prompt version,
purpose, section set, classification ceiling and time. That instance may not
exist before assembly. Consequently, its use authorization cannot substitute
for a pre-access preparation decision. Synthetic mock authorization is not a
production verifier or trust root.

## Data flow and failure boundaries

```text
explicit request + pinned target prompt + preparation evidence
  → validate request / verify preparation scope and time (no source read)
  → authorized reader → verify exact artifact bytes → normalize candidates
  → eligibility and conflict checks → deterministic selection
  → budgeted slot assembly → Context Package validation → prepared result
  → separate trusted review/use-authorization provider
  → Prompt SDK validates package + authorization + explicit time → bind/render
  → separately authorized execution / downstream build records
```

1. Validate allowed sources, target, intent, limits and explicit evaluation time.
   Verify evidence against configured trust and revocation policy, not an
   untrusted allow boolean. Denial fails before source bytes are accessed.
2. A reader can access only approved artifacts within the verified scope. Check
   size/digest before parsing. Fail on missing/corrupt/unsupported inputs; never
   follow floating branches, alternate sources or implicit fallback credentials.
3. Normalize supported UTF-8 text/JSON without altering meaning, retaining exact
   source/fragment identity, classification and validity. Reject malformed,
   ambiguous or excessive inputs. Normalization does not establish canon.
4. Filter authority, continuity/version/time/classification eligibility before
   ranking. Use explicit candidate IDs or a documented versioned lexical policy,
   stable scores and tie-breaks independent of filesystem/source enumeration.
   Ambiguous authority/conflicts fail or return an explicit unresolved state.
5. Assemble declared slots within per-slot/total byte limits. Missing required
   evidence or inability to fit it fails; optional omission is explicit.
   Preserve Unicode/JSON boundaries and meaning; no silent partial-fact truncation.
6. Compute section/source links and canonical identities. Raise classification
   to the highest contributing material. Derive review/expiry bounds no later
   than the governing sources/authorization. Return only schema-valid prepared
   output, never a partial package marked successful.
7. Obtain separate use authorization after exact package identity is known.
   Prompt SDK independently checks it at use time. Recheck any changed/expired/
   revoked authority before delivery/use; cached preparation is not permission.

Failure classes for #76 include invalid request, denied/unverifiable authority,
artifact unavailable/integrity failure, normalization failure, conflicting or
missing eligible evidence, budget exhaustion, stale/revoked evidence, audit
failure and cancellation. Reports carry stage, safe code, retry/repair guidance
and correlation identity, not protected values. Core operations never retry,
select a different source, renew a grant or produce replacement facts silently.

## Proposed API and effect boundaries

Names are illustrative until #76; implementation is a separate Platform
`context-builder` module, not additional Prompt SDK retrieval helpers.

| Operation | Inputs / output | Effects |
| --- | --- | --- |
| validateBuildRequest | Request, pinned prompt and supported contract/policy versions → report | None |
| verifyPreparation | Request and evidence, trusted verifier, explicit time → scoped verified decision | Explicit policy/revocation adapter only |
| resolveSources | Verified scope, exact references and approved readers → integrity-checked bytes | Authorized bounded artifact I/O |
| normalize/select/assemble | Verified explicit data, policy versions and budgets → candidates/selection/package | Pure; no hidden clock/network/randomness |
| buildContext | Coordinates the preceding operations → prepared package/reference plus reports | Only injected verified adapters |
| verify/replay | Original approved inputs and explicit time/policy → evidence/comparison | Must reauthorize reads; no silent source refresh |
| requestUseAuthorization | Prepared identity plus reviewed evidence → external use decision | Separate trusted authority; not self-issued |

A versioned build request must carry or resolve explicit build/correlation IDs,
exact prompt/version, approved sources, purpose, authority evidence, selection/
normalization versions, evaluation time, classification ceiling and slot/total
budgets. Supplied package instance IDs and timestamps are determinism inputs;
generating new ones is a caller responsibility, not hidden core randomness.
Wall-clock delivery timing belongs in separate operational evidence.

Results separate prepared content (protected according to classification),
metadata diagnostics, restricted provenance, and public-safe attestation handoff.
The exact request/result schema, policy verifier trust representation,
revocation semantics, source-candidate identity, conflict vocabulary, token
estimator contract and audit-required behavior are owned gaps for #76/#77,
not shortcuts an implementation may invent.

## Threat model and controls

| Threat | Required boundary / verification |
| --- | --- |
| Forged allow flag, confused deputy, cross-purpose reuse | Trusted preparation verifier; exact caller/source/target/purpose/time scope; assert zero denied reads |
| Private content/identity leakage | Minimized secure exports; no raw logs; public opaque attestation; tests forbid private hashes/paths/IDs |
| Source prompt injection or executable content | Treat source bytes as data; no eval, tools or policy override from content |
| Traversal, symlink escape, unapproved URLs | Reader allowlists and canonical containment; no direct checkout or implicit fetch |
| Tampering, version substitution, stale/revoked evidence | Immutable references and exact byte checks; explicit time and use-time policy revalidation |
| Nondeterministic ranking or conflicting canon | Versioned eligibility/scoring/ties and explicit conflict handling; no inferred canon promotion |
| Oversized/untrusted payload or budget abuse | Bounded read/parse/candidate counts, bytes and deadline/cancellation; deterministic failure |
| Cache scope leak or permission renewal | Memory-only baseline; complete scoped keys; revocation/expiry recheck; history distinct from use rights |
| Audit outage interpreted as approval | Required audit fails closed before delivery; optional telemetry policy explicit and never grants authority |
| Hash mistaken for authenticity | Digests prove byte identity, not source trust, permission or human review |

## Downstream boundary and sequencing

Epic #6 consumes the exact package/reference and a public-safe evidence handle
for a future build manifest. Epic #7 supplies correlation/intent/limits and
coordinates approvals, retries and execution. Neither interface requires a
Comic Manifest schema, hosted service or full orchestrator in Builder v1.
Private build lineage stays restricted; public manifests receive only approved
opaque attestations. Attestation creation/verification remains an explicit
trusted interface, with synthetic fakes for tests.

Issue sequence: #76 contracts; #77 authority; #78 sources; #79 selection;
#80 assembly; #81 lifecycle; #82 audit; #83 SDK handoff; #84 CLI; #85 consolidated
conformance; #86 immutable publication. Tests accompany each implementation.
Publish any new/changed Codex contracts first, adopt verified artifacts in
Platform, then release the implementation. Never rewrite released v1 bytes.

Synthetic public snapshots and private-export fixtures plus offline policy
fakes exercise every boundary without completing actual Universe Bible/Lore
content work. Real source/trust/storage onboarding is separately reviewed.
Embeddings/vector services, model summarization, model calls, multimodal
extraction, automatic creative decisions and hosted management are deferred.

## Scoped constitutional assessment

- Subject: issue #75 design diff against Studio base `523a2a46efb1e96970d0db749ddd16246b5f040f`; owner @andrewperis; assessed 2026-09-11.
- Authority/checklist: Constitution v1.0.0 at `a9cc8a503aa30e17820edc62ac95f7cbe10e0564`; [compliance checklist](../CONSTITUTION_COMPLIANCE.md).
- Applicable design profiles: universal; ADR/specification; repository/production system; automated workflow. Evidence is the ownership, stage/gate, threat and rollout sections above plus coordinated Platform ADR.
- Design findings: ownership singular; authority/publication separate; explicit provenance/privacy; bounded deterministic portable baseline; versioned exit/migration path. No new exception or data-access authority requested.
- Status: proposed assessment, pending owner/affected-source-owner review. Runtime controls, real-source onboarding and publication are not assessed or approved by this design.
- Next review: before #76 acceptance, then any trust, private-source, classification, persistence, selection/provider or downstream-boundary change.
