# Epic 6 closeout proposal — Comic Manifest v1

**Status:** Draft for owner and affected-steward review. This proposal does not
accept ADR 0018, close Epic 6, make a constitutional conformance claim, create an
exception, or change either immutable release.

**Assessment date:** 2026-10-11.

## Scope and present result

This is a present-day evidence audit of the 13 completion criteria on
[Studio #6](https://github.com/DefinitelySecureStudio/studio/issues/6). The
technical assessment is limited to the synthetic/offline Comic Manifest v1
contract and library boundary. No production trust service, private-source
access, canon decision, rendering, orchestration, or comic-publication authority
was exercised or is granted by this proposal.

The architecture and implementation exist, and the contract and implementation
releases have been published with verified artifact tuples. Criterion 1 remains
incomplete because ADR 0018 is still Proposed and the exact-revision maintainer
reviews and Studio owner decision are not recorded. Criterion 12 remains
incomplete because the documentation exists but the constitutional closeout and
history corrections below are not accepted. Epic 6 remains open.

| Evidence set | Exact revision |
| --- | --- |
| Studio architecture proposal | [Studio commit `7b5065cef76bea9580609caba356b0d8fe7cc17c`](https://github.com/DefinitelySecureStudio/studio/commit/7b5065cef76bea9580609caba356b0d8fe7cc17c); [ADR 0018](https://github.com/DefinitelySecureStudio/studio/blob/7b5065cef76bea9580609caba356b0d8fe7cc17c/adr/0018-comic-manifest-architecture.md); [architecture and scoped assessment](https://github.com/DefinitelySecureStudio/studio/blob/7b5065cef76bea9580609caba356b0d8fe7cc17c/comic-manifest/ARCHITECTURE.md) |
| Governing Constitution | v1.0.0, tag `constitution/v1.0.0`, Studio commit [`a9cc8a503aa30e17820edc62ac95f7cbe10e0564`](https://github.com/DefinitelySecureStudio/studio/tree/a9cc8a503aa30e17820edc62ac95f7cbe10e0564) |
| Codex contract | [Tag `contract/comic-manifest/v1.0.0`](https://github.com/DefinitelySecureStudio/codex/releases/tag/contract/comic-manifest/v1.0.0), source commit [`12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a`](https://github.com/DefinitelySecureStudio/codex/commit/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a) |
| Platform implementation | [Tag `comic-manifest/v1.0.0`](https://github.com/DefinitelySecureStudio/platform/releases/tag/comic-manifest/v1.0.0), source commit [`f0672d90a47473da6a27614cad07abc175546d67`](https://github.com/DefinitelySecureStudio/platform/commit/f0672d90a47473da6a27614cad07abc175546d67) |
| Platform publication proof and current documentation closeout | [Merged commit `8267c90585d387843cdf4578ca392ac3e3bb7a72`](https://github.com/DefinitelySecureStudio/platform/commit/8267c90585d387843cdf4578ca392ac3e3bb7a72), including [publication proof](https://github.com/DefinitelySecureStudio/platform/blob/8267c90585d387843cdf4578ca392ac3e3bb7a72/release/comic-manifest-v1.0.0-publication-proof.json) and [release/API/handoff documentation](https://github.com/DefinitelySecureStudio/platform/blob/8267c90585d387843cdf4578ca392ac3e3bb7a72/docs/comic-manifest-release.md) |

## Advisory architecture reviews

These are explicitly attributed technical observations, not maintainer sign-offs,
owner decisions, or constitutional approvals. Both are scoped to the revisions
above and to the synthetic/offline boundary.

### Codex contract fit — advisory review by this AI assistant

Reviewed Studio `7b5065c` against Codex `12e437e` and its released v1.0.0
contract. The review included the [Comic Manifest specification](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/specs/manifests/comic-manifest-v1.md),
[RFC 0007](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/rfcs/0007-comic-manifest-v1.md),
[RFC 0008](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/rfcs/0008-comic-manifest-rendition-profiles.md),
the [closed v1 schema](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/schemas/json/comic-manifest/v1/comic-manifest.schema.json),
and [synthetic fixtures](https://github.com/DefinitelySecureStudio/codex/tree/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/fixtures).

**Finding:** No blocking contract-fit mismatch was identified for the scoped
offline design. The three record kinds, detached approval binding, immutable
identities/references, and rendition requirements align with ADR 0018. Schema
validity and digests do not establish authority; the contract leaves current
authorization and trust to explicit consuming boundaries. This does not assess a
production trust root, actual private-source access, or a comic publication.

**Disposition:** Recommend Codex contract-maintainer review of these exact
revisions before ADR acceptance. This advisory is not a Codex maintainer review
and does not make criterion 1 pass.

### Platform feasibility — independent AI reviewer report

The independent reviewer report for Platform `f0672d9` is identified as task
`01a117fc-90f2-75b9-a05c-e28c7e7bb0ca`, reported 2026-10-11 15:52 UTC. The
reviewer reran approval/build-result/golden suites (**59/59**) and
CLI/reference/offline-network suites (**77/77**) from a temporary source
archive: **136/136 passed**, with no implementation defect found. It reports
criteria 7, 9, and 10 passing within the injected/synthetic boundary.

The reviewer also records the limits: the issuer, trusted clock, and revocation
service are host-owned; `publication_authority` is not issued; and free-text and
public-URL disclosure still requires qualified human review. The report is
advisory AI technical evidence, not a Platform maintainer review, actual
disclosure decision, production trust assessment, or owner acceptance.

**Disposition:** Recommend Platform-maintainer review against Studio `7b5065c`,
Codex `12e437e`, and Platform `f0672d9`. Passing injected tests do not authorize
production access, publication, or canon promotion.

## Completion criteria evidence map

“Pass” below means the implementation evidence supports the criterion within
the declared synthetic/offline scope. It is not a human approval of ADR 0018 or a
claim of production readiness. “Incomplete” means the criterion itself includes
an approval or closeout condition that remains outstanding.

| # | Disposition | Exact evidence and remaining condition |
| --- | --- | --- |
| 1 | **Incomplete** | The proposed three-record architecture is in [ADR 0018](https://github.com/DefinitelySecureStudio/studio/blob/7b5065cef76bea9580609caba356b0d8fe7cc17c/adr/0018-comic-manifest-architecture.md) and [Comic Manifest architecture](https://github.com/DefinitelySecureStudio/studio/blob/7b5065cef76bea9580609caba356b0d8fe7cc17c/comic-manifest/ARCHITECTURE.md). Codex’s versioned contract is at [`12e437e`](https://github.com/DefinitelySecureStudio/codex/tree/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a); Platform’s implementation is at [`f0672d9`](https://github.com/DefinitelySecureStudio/platform/tree/f0672d90a47473da6a27614cad07abc175546d67). ADR 0018 still says **Proposed**; Studio #88 is closed with its owner-reviewed-architecture acceptance box unchecked. Exact-revision Codex and Platform maintainer reviews and the Studio owner’s architecture decision are still required. |
| 2 | **Pass, scoped** | Bounded parsing and semantic validation: Platform [`parse-json.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/parse-json.js), [`validate.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/validate.js), [`parse-json.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/parse-json.test.js), and [`validation.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/validation.test.js). Reviewer rerun: 136/136 across the two reported groups. These tests support the bounded offline-validation boundary; production-source access was not tested. |
| 3 | **Pass, scoped** | Normative episode/panel/revision semantics and fixtures: Codex [v1 specification](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/specs/manifests/comic-manifest-v1.md), [schema](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/schemas/json/comic-manifest/v1/comic-manifest.schema.json), and [`comic-manifest-v1-cases.json`](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/fixtures/comic-manifest-v1-cases.json); Platform [`episode.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/episode.js), [`semantics.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/semantics.js), and [`episode.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/episode.test.js). |
| 4 | **Pass, injected/offline** | Exact immutable public tuples and explicit host resolver boundary: Codex [reference semantics](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/specs/manifests/comic-manifest-v1.md); Platform [`references.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/references.js), [`references.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/references.test.js), and [`comic-manifest-references.md`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/docs/comic-manifest-references.md). Resolver and protected-store operation are injected; real private-source access is not assessed. |
| 5 | **Pass, synthetic/injected** | Exact Prompt SDK/Context Builder relationships and separate current-use authorization are described in Platform [`comic-manifest-contracts.md`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/docs/comic-manifest-contracts.md) and covered by [`comic-manifest-contract.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/prompt-sdk/comic-manifest-contract.test.js). The host supplies the authorization verifier; no production issuer, private source, or permission renewal is demonstrated. |
| 6 | **Pass, declaration/validation only** | Profile, dimensions/media limits, accessibility text, credits, and rights fields: Codex [RFC 0008](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/rfcs/0008-comic-manifest-rendition-profiles.md); Platform [`output-compatibility.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/output-compatibility.js), [`output-compatibility.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/output-compatibility.test.js), and [`comic-manifest-renditions.md`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/docs/comic-manifest-renditions.md). No renderer or real-output rights/accessibility review is part of this scope. |
| 7 | **Pass, injected/synthetic** | Detached approvals bind exact candidate, artifact, scope, time, and role; edits and stale/revoked records do not confer new authority. Evidence: Platform [`approvals.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/approvals.js), [`revision-diff.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/revision-diff.js), [`approval-boundary.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/approval-boundary.test.js), and [`comic-manifest-approvals.md`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/docs/comic-manifest-approvals.md). Host identity, clock, and revocation remain host-owned and are not production-verified. |
| 8 | **Pass, mock results** | Exact manifest/result relationship and output-byte checks: Platform [`build-result.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/build-result.js), [`build-result.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/build-result.test.js), and [`comic-manifest-build-results.md`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/docs/comic-manifest-build-results.md). The report is an offline mock, not production orchestration. |
| 9 | **Pass, structured synthetic projection** | Allowlisted release projection and synthetic private-context fixtures: Platform [`comic-manifest-release.md`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/docs/comic-manifest-release.md), [`golden-conformance.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/golden-conformance.test.js), and [reviewed goldens](https://github.com/DefinitelySecureStudio/platform/tree/f0672d90a47473da6a27614cad07abc175546d67/tests/fixtures/comic-manifest-goldens). The independent review confirms the synthetic boundary; no sentinel test proves all free text or public URLs safe. Qualified human disclosure review remains required for an actual candidate. |
| 10 | **Pass, synthetic end-to-end** | Codex synthetic fixtures and Platform [reviewed golden packet](https://github.com/DefinitelySecureStudio/platform/tree/f0672d90a47473da6a27614cad07abc175546d67/tests/fixtures/comic-manifest-goldens), [`golden-conformance.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/golden-conformance.test.js), [`build-result.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/build-result.test.js), and [`release.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/release.test.js). Reviewer reports the golden/build-result group passing 59/59. The fake approval is not production trust or a real comic release. |
| 11 | **Pass, offline** | CLI commands and outcomes: Platform [`cli.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/src/comic-manifest/cli.js), [`cli.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/cli.test.js), [`offline-network-tripwire.test.js`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/tests/comic-manifest/offline-network-tripwire.test.js), and [`comic-manifest-cli.md`](https://github.com/DefinitelySecureStudio/platform/blob/f0672d90a47473da6a27614cad07abc175546d67/docs/comic-manifest-cli.md). Reviewer reports CLI/reference/offline-network suites passing 77/77 without paid providers or real private content. |
| 12 | **Incomplete** | API, CLI/authoring/review, compatibility/deprecation, limitations, and Epic #101 handoff documentation are present at Platform closeout commit [`8267c90`](https://github.com/DefinitelySecureStudio/platform/tree/8267c90585d387843cdf4578ca392ac3e3bb7a72), especially [`comic-manifest-release.md`](https://github.com/DefinitelySecureStudio/platform/blob/8267c90585d387843cdf4578ca392ac3e3bb7a72/docs/comic-manifest-release.md). The missing evidence is an owner/steward-accepted constitutional disposition and a truthful, append-only correction of the issue/release-preparation record described below. ADR 0018’s existing assessment remains **Not assessed**. |
| 13 | **Pass, release evidence only** | The Codex and Platform tags target the exact commits in the evidence table above. Studio #99 records separate exact-artifact publication approvals and independent public-download verification; Platform’s [publication proof at `8267c90`](https://github.com/DefinitelySecureStudio/platform/blob/8267c90585d387843cdf4578ca392ac3e3bb7a72/release/comic-manifest-v1.0.0-publication-proof.json) records eight successful Platform asset downloads. Exact release asset tuples are listed below. This criterion does not approve ADR 0018, satisfy criterion 12, grant production permission, or publish a comic. |

### Published release tuples for criterion 13

The public tag targets and release metadata were checked against the listed
commit identities. The release and Studio #99 records state that public download
bytes were independently checked against the exact sizes and SHA-256 digests.

**Codex — `contract/comic-manifest/v1.0.0`, source `12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a`:**

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `comic-manifest-v1.0.0.schema.json` | 30,860 | `7bd3c5392ae0db0c5baba553c233142d3d4427471f5850123eef7b87d4c8eaa4` |
| `comic-manifest-v1.0.0.bundle.json` | 865,650 | `bb131a7dbb96692172b4e44b56a272d041309e53b136433cc71a24c8d1b934de` |
| `comic-manifest-v1.0.0.manifest.json` | 1,152 | `56bba6d990c429384e16d8aa49af99b3a25ca8733efa96b5681be5932dcba878` |

**Platform — `comic-manifest/v1.0.0`, source `f0672d90a47473da6a27614cad07abc175546d67`:**

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `comic-manifest-v1.0.0.source.tar.gz` | 491,339 | `b383cee702b4ceba0c4090bceee0c2f6c451bce18c148162543b4e1316226501` |
| `comic-manifest-v1.0.0.package.tgz` | 225,334 | `98f9ad51546620a2197672b2bfd21e6bc31f72b274dc56bb3c50590edfe493ec` |
| `comic-manifest-v1.0.0.package-lock.json` | 3,149 | `ef90ff0593d91ed26980629ce896ac08294281ed2521db01d7e19ad89b5d87bd` |
| `comic-manifest-v1.0.0.sdk-contract-lock.json` | 7,588 | `6b4b515cc606f2c50b1baead50faaddd3d87d3a1d7b2c9b14e4170e36776dfab` |
| `comic-manifest-v1.0.0.context-builder-contract-lock.json` | 1,366 | `297dfa1e7e1e89b63eba0df5d3e012d6243f449bdcddc9e9e34714e786f7e595` |
| `comic-manifest-v1.0.0.contract-lock.json` | 2,678 | `d74950fc19669f1187aca54669b80f32c332685ef4f3a4a8361c4a9dd1a12e7a` |
| `comic-manifest-v1.0.0.api-v1.json` | 1,317 | `5f3d3e069a99f3533fb17d795d636cd9960c67ebd0be925d063652d3cfb71238` |
| `comic-manifest-v1.0.0.manifest.json` | 6,159 | `7e01965f6b7f2ba341073d3854185f46a95a3ed13af3862fb26f656839e4f1d6` |

## Scoped constitutional assessment

**Constitution:** v1.0.0 at `a9cc8a503aa30e17820edc62ac95f7cbe10e0564`.
**Scope:** public, synthetic/offline contract and library behavior only. This
assessment excludes production trust issuance/verification, real private-source
access, actual creative canon, rendering, orchestration, and comic publication.
It does not assert that excluded activities are constitutionally conforming.

| Topic | Disposition | Evidence and boundary |
| --- | --- | --- |
| Separation of production intent, build results, and public release; approval is distinct from schema validity | **Pass, scoped** | Codex v1 semantics and Platform’s injected approval/build-result boundary keep status, digest, and successful validation from granting authority. Reviewer reports the scoped suites passed. |
| October 6 AI-review/merge authorization as a formal Article 12.7 exception | **Fail as an exception/conformance claim** | The audit evidence says the owner authorized AI code review and merge for Epic 6 after the human-review requirement was raised. Treat that instruction as a historical owner authorization. [`CONSTITUTION_EXCEPTIONS.md`](https://github.com/DefinitelySecureStudio/studio/blob/7b5065cef76bea9580609caba356b0d8fe7cc17c/CONSTITUTION_EXCEPTIONS.md) says both Active and Historical exceptions are “None.” [Article 12.7](https://github.com/DefinitelySecureStudio/studio/blob/a9cc8a503aa30e17820edc62ac95f7cbe10e0564/CONSTITUTION.md#127-temporary-constitutional-exceptions) requires the exact approved record, A4 constitutional-steward and affected-domain approvals, and register entry before an exception becomes active; it also forbids retroactive legalization. The October 6 instruction therefore cannot be described as a formally registered exception or used to claim retrospective constitutional compliance. No exception is requested or created by this proposal. |
| Production issuer, trusted clock, revocation, or private-source authorization | **Not assessed** | Platform documents these as host-owned/injected. No production trust service or private source was used. |
| Real private-source material or private-source identifiers | **Not applicable to this work** | The reported acceptance and conformance evidence uses synthetic/fake-private fixtures only; no real private source was accessed. |
| Actual canon/editorial decision, rendering, orchestration, or comic publication | **Not applicable to this work** | None occurred. The Platform package/release is software publication, not a comic release or canon act. |
| Qualified review of actual free text, public URLs, rights, accessibility, or a comic output | **Not assessed** | The reviewer explicitly leaves free-text/public-URL disclosure for qualified human review. No actual comic output or disclosure decision is in scope. |
| Overall constitutional conformance for final Epic 6 closure | **Not assessed** | Human Codex/Platform maintainer reviews, the Studio owner’s exact-revision architecture decision, and the affected stewardship decisions remain unrecorded. The known exception-recording failure above must remain visible; it cannot be erased by an after-the-fact entry. |

The scope-level pass findings do not erase the historical governance gap. The
closeout record must not say “Conforming” or “Authorized exception” for the whole
Epic 6 history. A qualified Constitution steward and affected A4 owners must
decide how to record the known gap and required forward-looking remediation. That
decision may document history and require future process changes; it cannot
backdate an exception or change what was authorized on October 6.

## Required issue and record corrections

These are proposed **append-only** corrections. Preserve existing issue bodies,
reviews, commits, tags, release assets, and the October 6 owner instruction as
history. Add a dated correction that links the original instruction if the
owner has a durable source link; do not invent one.

1. **Studio #88:** append that the issue is closed while its
   “Owner-reviewed architecture” acceptance criterion remains
   unchecked. State that ADR 0018 is still Proposed pending exact-revision
   Codex and Platform maintainer reviews and the Studio owner decision. Do not
   represent issue closure as architecture acceptance.
2. **Studio #99:** correct the checked statement that “All preceding tasks are
   complete and owner-reviewed.” It conflicts with #88’s unchecked owner-review
   criterion. Append a dated qualification that release tasks and exact
   artifact approvals are evidenced, while architecture approval and the
   constitutional/doc closeout remain open. Keep the verified release tuples
   and publication facts intact.
3. **AI-review wording:** the October 6 instruction authorized AI review and
   merge for Epic 6; it was not an Article 12.7 exception. Codex’s
   [release-preparation record at `12e437e`](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/releases/comic-manifest-v1.md)
   calls it an “A3 AI-review exception.” If correcting that description, use a
   dated addendum or a new source commit, preserve the tagged release and its
   source history, and say no formal exception was registered. Do not create a
   new or backdated exception.
4. **Studio #6:** keep the Epic open. After owner review of this proposal,
   record each criterion with its evidence. Leave criteria 1 and 12 incomplete
   until the required maintainer/owner reviews and accepted constitutional
   closeout are recorded. Do not treat release approval as satisfying either.
5. **Platform documentation:** this proposal makes no duplicate Platform edit.
   The cited current closeout is Platform commit `8267c90`; any separate
   in-progress Platform correction remains with its existing worker.

## Decisions and roles still required

| Decision | Required role | Exact subject |
| --- | --- | --- |
| Contract-fit review | Codex contract maintainer | Studio architecture `7b5065c` against Codex tag/revision `contract/comic-manifest/v1.0.0` / `12e437e` |
| Feasibility review | Platform maintainer | Studio architecture `7b5065c` against Platform tag/revision `comic-manifest/v1.0.0` / `f0672d9`; review the stated host-owned trust and disclosure limits |
| Architecture adoption | Studio accountable owner, @andrewperis | Accept or decline ADR 0018’s exact proposed boundary after the above reviews. Acceptance is only the cross-repository architecture decision. |
| Affected-responsibility boundaries | Universe editorial owner; source/disclosure owner | Confirm that public identity/canon decisions and restricted-source/disclosure authority remain with those owners. No actual canon or source-access decision is requested here. |
| Historical governance disposition and documentation closeout | Named Constitution steward and affected A4 owners | Decide the accurate record and forward-looking remediation for the October 6 instruction and the incorrect “A3 exception” description. Do not authorize an exception retroactively. |

**Minimum architecture decision:** after the Codex and Platform maintainers review
the exact revisions above, does the Studio owner accept ADR 0018’s proposed
architecture for the synthetic/offline Comic Manifest v1 boundary? That answer
does not close criterion 12 or decide private access, production trust, canon,
rendering, orchestration, comic publication, or constitutional conformance.

## Non-effects

This proposal changes no approval status to approved, creates no constitutional
exception, does not backdate or replace any record, changes no release or tag,
and does not close Epic 6. It proposes no Constitution amendment or policy
weakening. Any follow-up release, production trust, private-source use, canon
decision, rendering, orchestration, or comic publication requires its own scoped
owner approvals and evidence.
