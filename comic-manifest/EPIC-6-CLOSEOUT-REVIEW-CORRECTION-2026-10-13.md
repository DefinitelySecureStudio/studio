# Epic #6 review correction and finding ledger — 2026-10-13

## Scope and assessed disposition

This dated correction preserves the accepted Studio #146 proposal unchanged at
PR head [`a9935f8fcab04396b3ba5f8077620ca167291933`](https://github.com/DefinitelySecureStudio/studio/pull/146).
Its complete 13-criterion evidence map and exact Codex/Platform implementation,
release, and publication references remain the evidence source. This ledger
corrects Repository 5 and assessment-outcome dispositions and updates criteria
1/12 as of present-day evidence.

- Assessed Studio baseline:
  [`7707273f1641bbd7c6243bcee47b5e74c2709938`](https://github.com/DefinitelySecureStudio/studio/commit/7707273f1641bbd7c6243bcee47b5e74c2709938);
  date: 2026-10-13 (UTC).
- Constitution: v1.0.0, tag
  [`constitution/v1.0.0`](https://github.com/DefinitelySecureStudio/studio/tree/constitution/v1.0.0),
  commit
  [`a9cc8a503aa30e17820edc62ac95f7cbe10e0564`](https://github.com/DefinitelySecureStudio/studio/commit/a9cc8a503aa30e17820edc62ac95f7cbe10e0564).
- Scope: synthetic/offline contract and library boundary plus Epic #6 governance,
  documentation, and immutable v1 software-release evidence only. Excluded:
  production trust, private-source access, canon, rendering, orchestration, and
  comic publication.
- Status at the assessed baseline: **Nonconforming — blocked**. The required
  root declaration and severity/outcome dispositions were unsatisfied.
- Active exceptions: **None**. The Oct 6 owner instruction is historical context,
  not a formally approved or registered exception.

## Severity and dated disposition ledger

Severity follows Constitution §9.5 and the compliance checklist. GitHub's P2
label is not itself a constitutional severity.

| Finding and evidence | Severity | Dated disposition |
| --- | --- | --- |
| ADR 0018 and the architecture at [`7b5065cef76bea9580609caba356b0d8fe7cc17c`](https://github.com/DefinitelySecureStudio/studio/commit/7b5065cef76bea9580609caba356b0d8fe7cc17c) remained Proposed on Oct 11; required reviews and owner decisions were pending. | **Blocker at proposal time** | Resolved for present-day criterion 1 only. On Oct 13 at 11:47:50.998442 UTC, Andrew Peris accepted the exact architecture and proposal, recorded in [Studio PR #147](https://github.com/DefinitelySecureStudio/studio/pull/147) and its merged decision record. Not backdated; no architecture or role-capacity reapproval is requested. |
| Oct 6 AI-only code review/merge instruction without an approved and registered Article 12.7 exception; later mislabeled “A3 AI-review exception.” Evidence: [Codex v1 source record](https://github.com/DefinitelySecureStudio/codex/blob/12e437e30328a3bb9cd2d15e6307a70b4b7e0e2a/releases/comic-manifest-v1.md), [exception register](../CONSTITUTION_EXCEPTIONS.md), Constitution Article 12.7. | **Blocker, historical authority/provenance** | The owner instruction was not an exception and cannot be legalized retroactively. Additive Codex PR #17 merged at [`279d30319a0aff14366dc5846a18200bd1fd0ae9`](https://github.com/DefinitelySecureStudio/codex/commit/279d30319a0aff14366dc5846a18200bd1fd0ae9) and Platform PR #46 at [`4779be4d64bcc68aab5785c12779427cc48336eb`](https://github.com/DefinitelySecureStudio/platform/commit/4779be4d64bcc68aab5785c12779427cc48336eb) clarify the history without changing released bytes. Keep the historical finding visible; no exception/policy change is sought. |
| Repository 2 / Provenance 5 review-record gap and conflict between #88/#99 completion state; repository protection/CODEOWNERS configuration was not inspected. | **Blocker for historical required-review/evidence gap**; controls **Not assessed** | Append-only reconciliation is recorded on [#88](https://github.com/DefinitelySecureStudio/studio/issues/88#issuecomment-6145261670) and [#99](https://github.com/DefinitelySecureStudio/studio/issues/99#issuecomment-6145264263). Branch-protection/CODEOWNERS remains Not assessed, not a Fail or a pass. |
| Required repository declaration absent from root README/governance at the assessed baseline; proposal incorrectly marked Repository 5 Pass from an ADR pin and reference standard alone. [PR #146 review finding](https://github.com/DefinitelySecureStudio/studio/pull/146#discussion_r4258258631). | **Blocker** | Repository 5 is **Fail at baseline** under Constitution §15.4 and the repository reference standard. This PR proposes the declaration and README link; it was not present at the assessed baseline. |
| Severity and outcome checks marked Pass despite known applicable Fail/blocker findings; overall status left `Not assessed`. [PR #146 review finding](https://github.com/DefinitelySecureStudio/studio/pull/146#discussion_r4258258647). | **Blocker** | Outcome 1 and Outcome 2 are **Fail at baseline**: known unresolved blockers require `Nonconforming — blocked`. This dated ledger corrects the scoped disposition; broader excluded subjects remain Not assessed. |
| ADR 4 / Release 5: Platform closeout commit `8267c90` contained conflicting published versus unreleased/candidate-unpublished guidance. | **Major, resolved** | Separate from future-version guidance. Platform PR #46 merged at `4779be4d64bcc68aab5785c12779427cc48336eb`, correcting living publication-state guides and preserving candidate records as history. |
| Platform builder/packet/verifier guides implied future-version use beyond published v1 scope. | **Major, resolved** | Platform PR [#47](https://github.com/DefinitelySecureStudio/platform/pull/47) merged at [`bd864fa195ab323d987cc1e33f431a5d9ed10f3f`](https://github.com/DefinitelySecureStudio/platform/commit/bd864fa195ab323d987cc1e33f431a5d9ed10f3f). Its two-guide change was reviewed at exact head `b92014673d29e96735aa5661b3cc133f47fa4b21` with no findings; exact-head CI [#38397040260](https://github.com/DefinitelySecureStudio/platform/actions/runs/38397040260) passed Node 22/24. No duplicate Studio edit is needed. |
| Codex Authority 2 / Exception 1 and Exception 4: the Oct 6 instruction was misdescribed as a registered exception, but no approved record exists. | **Blocker, historical authority/provenance** | Same historical fact as the second row. Preserve the actual instruction, empty exception register, and additive corrections; do not backdate, register, or imply an exception. |

## Corrected completion dispositions

- **Criterion 1 — Pass for present-day architecture acceptance.** The owner
  accepted ADR 0018 and exact architecture revision
  `7b5065cef76bea9580609caba356b0d8fe7cc17c` on Oct 13. The Oct 11 proposal
  records the earlier pending state; this is not backdated. Acceptance grants
  no production trust, private-source access, canon, rendering, orchestration,
  or publication authority.
- **Criterion 12 — Pending this Studio correction.** The 13-row evidence map
  retains exact implementation/release evidence, but Repository 5 and
  severity/outcome dispositions were inaccurate. This PR supplies a root
  declaration and dated ledger. Platform PR #47 is now merged. Criterion 12
  remains incomplete until this Studio correction merges and is verified.
- **Criteria 2–11 and 13:** retain the exact evidence and bounded dispositions
  in the unchanged proposal; this correction expands no implementation or
  release evidence.

After this Studio correction is merged and verified, no identified Epic #6
closeout blocker remains within this bounded scope. Broader unassessed subjects
remain **Not assessed**; that is not a whole-repository or whole-history
`Conforming` claim. The owner already accepted the exact proposal/head and
confirmed affected capacities in PR #147. The only remaining approval question
is review of this docs-only correction at its exact PR head; no architecture
reapproval, role reassignment, exception, or historical-conformance claim is
requested.
