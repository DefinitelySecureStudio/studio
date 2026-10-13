# U01 — Public source inventory and coverage proposal

**Status:** Andrew Peris accepted this starting coverage and seed for downstream drafting on 2026-10-13. This packet remains a proposal record, not canon, an episode brief, or a U02/U03 record; acceptance does not approve a merge, episode, or publication.

**Human editor:** Andrew Peris, confirmed by that explicit acceptance.

**Snapshot date:** 2026-10-13 UTC.

## Bounded scope and acceptance evidence

- **Target:** `DefinitelySecureStudio/studio`, based on `main` at [`9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8`](https://github.com/DefinitelySecureStudio/studio/commit/9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8).
- **Exact output:** this one review packet, `issues/u01-epic8-public-source-inventory.md`. It inventories approved public sources and proposes the smallest content set for U01 review. It adds no canon records and changes no other files.
- **Bounded path:** compare the pinned public Universe main tree and the listed public Studio brand/governance sources; derive only series-level coverage and one clearly labeled story seed from the approved comic identity. The exact starting coverage and seed below were accepted for separate U02/U03 drafts; any later replacement remains Andrew's creative decision.
- **Exact source set:** Universe `main` at [`66bf9b0d24329a134808b39e1d8898d9bd87722c`](https://github.com/DefinitelySecureStudio/universe/commit/66bf9b0d24329a134808b39e1d8898d9bd87722c): repository README; `bible/README.md`; `canon/README.md`; `characters/README.md` and `_template.md`; `locations/README.md`; `comics/README.md` and `_template.md`; `story-arcs/README.md`; `docs/canon-policy.md`; `CONTRIBUTING.md`; `.github/CODEOWNERS`; all public tag refs; and the public Releases listing. Studio `main` at [`9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8`](https://github.com/DefinitelySecureStudio/studio/commit/9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8): `README.md`; `ARCHITECTURE.md`; `brand/comic-identity.md`; `brand/APPROVAL.md`; and `repository-standards/BRANCH-AND-REVIEW.md`. Studio issues #9, #15, #114, #115, #116, and #117 are used only for approval provenance, scope, and gates.
- **Finite evidence matrix:** (1) Universe tree at the pinned commit plus complete public tag refs and Releases listing: verify which public canon/publication records exist and whether a tagged canon snapshot exists; (2) Studio comic identity plus its approval record and issue #9: verify the approved series-level facts; (3) Studio architecture, Universe canon policy/contribution rules, and Universe CODEOWNERS: verify ownership and proposal-vs-canon boundaries; (4) Epic/U01/U02/U03/U04 issue text: verify size caps and human/dependency gates. The packet records the source links, the observed result, the accepted starting record slots, and unresolved details.
- **Exclusions:** no private or restricted sources, no Lore checkout or access, no unrelated personal context, no U02/U03 drafts or canon promotion, no U04 candidate assembly, no C01 episode brief, no art, spending, publishing, new issues, settings, or credentials changes.
- **Estimate:** 0.5–1 focused person-day including source review, one packet, link/provenance check, and handoff; within the two-day cap.
- **Acceptance evidence:** Andrew Peris explicitly accepted this starting coverage and seed on 2026-10-13, saying to begin with them and review what is produced, with the option to choose different coverage and seed if the drafts do not work. The accepted set remains within the 3-character/2-location/3-relationship cap. This acceptance is limited to downstream drafts; it does not accept canon or publication. U01 remains open for parent review and handoff.

## Source inventory and status

| Source | Pinned provenance | What it establishes | Status and boundary |
| --- | --- | --- | --- |
| Universe main tree | [`66bf9b0d…`](https://github.com/DefinitelySecureStudio/universe/tree/66bf9b0d24329a134808b39e1d8898d9bd87722c) | The public repository currently has bible, canon, character, location, comic, and story-arc indexes/templates and policy. The inspected tree has no character, location, relationship, story-arc, or published-comic record beyond those indexes/templates. | No approved in-universe source record was found in this pinned snapshot. This scoped absence does not establish that unpublished or private material does not exist, and it is not a negative canon claim. |
| Universe public tag refs | [GitHub matching-refs/tags endpoint](https://api.github.com/repos/DefinitelySecureStudio/universe/git/matching-refs/tags/) returned `[]` at 2026-10-13 14:32:08 UTC; `git ls-remote --tags https://github.com/DefinitelySecureStudio/universe.git` independently exited 0 with no refs. The Releases listing endpoint returned `[]`. | All matching public tag refs were enumerated; the empty result means there were no tags to paginate or inspect. No GitHub release snapshot was listed either. | The Universe canon policy defines current public canon against tagged canon releases. No tagged canon snapshot was available at that point in time. This does not imply anything about private or unreleased material. |
| Universe canon policy | [`docs/canon-policy.md`](https://github.com/DefinitelySecureStudio/universe/blob/66bf9b0d24329a134808b39e1d8898d9bd87722c/docs/canon-policy.md), blob `963e0ff1ac018fc1f1e82f57b902adc28ed0b2bc` | Public canon is approved, non-superseded material in a tagged canon release; published comics are primary evidence; a PR, issue, draft, social discussion, or omission is not canon. | Governance, not story content. |
| Universe contribution and record guidance | [`CONTRIBUTING.md`](https://github.com/DefinitelySecureStudio/universe/blob/66bf9b0d24329a134808b39e1d8898d9bd87722c/CONTRIBUTING.md), blob `3fd17661a18ead4bf076a4ad380e365e22948278`; [`characters/README.md`](https://github.com/DefinitelySecureStudio/universe/blob/66bf9b0d24329a134808b39e1d8898d9bd87722c/characters/README.md), blob `c030f4b0fedd0ec63af81ad8acaa310da7f049e4`; [`locations/README.md`](https://github.com/DefinitelySecureStudio/universe/blob/66bf9b0d24329a134808b39e1d8898d9bd87722c/locations/README.md), blob `cbe8258dc5f2f62f6a5d77cd425a8e138437e203` | Universe holds reader-safe approved canon; its record templates are proposal templates, and only already-public or explicitly cleared facts belong in accepted records. | Governance only. No template is treated as a canon fact. |
| Universe ownership | [`.github/CODEOWNERS`](https://github.com/DefinitelySecureStudio/universe/blob/66bf9b0d24329a134808b39e1d8898d9bd87722c/.github/CODEOWNERS), blob `9c780913bcb3f154ef2635822a10f86dd3c9c6ba` | Andrew Peris is the code owner for all paths and explicitly owns canon review surfaces. | Supports the human review authority; does not itself approve this content proposal. |
| Studio comic identity | [`brand/comic-identity.md`](https://github.com/DefinitelySecureStudio/studio/blob/9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8/brand/comic-identity.md), blob `e32186869be99769a3ee4fe0fc1c28dcca150db1`; [approval record](https://github.com/DefinitelySecureStudio/studio/blob/9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8/brand/APPROVAL.md), blob `7955d7b2bb76ba92ce783fecbd42817bb0879f7f`; [Issue #9](https://github.com/DefinitelySecureStudio/studio/issues/9) | The component is marked Approved; the approval record cites Issue #9 and ADR 0002, and Issue #9 is closed as completed. It establishes the comic/series title *Definitely Secure*, fictional-company name Definitely Secure, series-level pitch, tone/reader promise, high-level workplace setting, and public episode/naming conventions. | Accepted Studio brand/identity source. It is not by itself an approved Universe character, location, relationship, episode, or canon record. |
| Studio README | [`README.md`](https://github.com/DefinitelySecureStudio/studio/blob/9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8/README.md), blob `855aaccf11fb4fbecb20a10982399526eb6c5029` | Public studio description and tagline. | Context only; no separate canon approval is asserted. |
| Studio ownership map | [`ARCHITECTURE.md`](https://github.com/DefinitelySecureStudio/studio/blob/9a3e9dec66f1aa46fefc39b6b7c6944e7cf755a8/ARCHITECTURE.md), blob `dff2f909058d145f46656f3a1c4255ba7bb82da3` | Studio owns governance/tracking; Universe owns public canon; Lore is a separate private authority. | Governance; no private source was accessed. |
| Studio issue scope | [Epic #15](https://github.com/DefinitelySecureStudio/studio/issues/15), [U01 #114](https://github.com/DefinitelySecureStudio/studio/issues/114), [U02 #115](https://github.com/DefinitelySecureStudio/studio/issues/115), [U03 #116](https://github.com/DefinitelySecureStudio/studio/issues/116), [U04 #117](https://github.com/DefinitelySecureStudio/studio/issues/117) | Exact deliverable, planning caps, U01 acceptance dependency, and U04 human-review boundary. | Backlog and workflow authority only, not creative canon. |

The approved comic-identity component is the only usable approved creative source found for this proposal in the inspected public state. The consolidated `brand/BRAND_GUIDE.md` is not used as an approved source: the approval record says the unified guide is still pending. No public comic page was independently verified; the Studio identity's website reference was inaccessible to the available browser and is not evidence here. Both the complete public tag-ref result and the GitHub Releases listing were empty at 2026-10-13 14:32 UTC; therefore no tagged canon snapshot was available to inspect at that time.

## Accepted starting content set for downstream draft review

Andrew accepted this exact starting set for downstream draft work. The creative content remains **proposal-only and non-canon**. The labels are temporary coverage handles, not names, stable canon IDs, or approved facts, and these are not drafted records. The set uses two characters, one location, and one relationship; no third character, second location, or additional relationship is proposed.

| Coverage handle | Proposed minimum record | What remains undecided |
| --- | --- | --- |
| C1 — Status owner | One unnamed worker responsible for updating a routine work-status report. | Name, pronouns, job title, appearance, history, seniority, and voice. |
| C2 — Evidence checker | One unnamed coworker who can observe that the reported status does not match the work. | Name, pronouns, job title, evidence, history, and voice. |
| L1 — Shared work setting | One shared workplace setting inside the fictional company Definitely Secure. | Site/room name, geography, physical vs. virtual form, design, equipment, and any layout. |
| R1 — Coworkers coordinating a correction | C1 and C2 exchange observations and coordinate a truthful status update. | Reporting hierarchy, tenure, friendship, conflict history, and any relationship beyond coworkers. |

Named characters, a specific location, or a richer relationship remain human creative choices for the separate U03 draft and Andrew's review. These placeholders do not establish the records' existence in canon.

## Coverage handoff to U02

- **Premise:** the approved Studio pitch describes a workplace comic about confident systems, messy reality, and people trying to keep both running. The proposed seed below narrows that promise to one routine mismatch between a status report and observed work; the series pitch is accepted branding, while this episode situation is a proposal.
- **Tone:** the approved comic identity calls for technically observant humor and character-driven stories accessible without specialist knowledge, centered on human experiences of work. Preserve the humor in the confidence/reality gap; do not turn this into a technical explainer or an incident postmortem.
- **Setting rules:** the approved identity names a fictional company, Definitely Secure, and a workplace shaped by dashboards, status reports, policies, and systems. For the seed, propose one shared work setting only. No location name, geography, org chart, system design, security architecture, or company operating rule is established by this packet.
- **Continuity conventions:** the approved identity says individual strips stand alone while recurring characters, workplace history, and consequences build over time. Public episode numbers follow publication order, not in-story chronology; `DS-NNNN` is the comic ID format. This proposal assigns no episode number or title and establishes no prior history.

## One provisional story seed

**Accepted as the starting seed for downstream drafting, not as a final episode decision:** during an ordinary status check at Definitely Secure, a report shows work as complete while one coworker can see it is still unresolved. Two coworkers compare the report with what they can observe and agree on a truthful next update. The comic's humor comes from the gap between confident language and operational reality, with no technical knowledge required.

This is a newly generated story idea grounded only in the approved public comic identity. Andrew accepted it to see what drafts produce and may later retain or replace it. It is not a sourced event, canon, episode brief, or release plan. It has no title, `DS-NNNN` assignment, defined system, named character, detailed cause, or downstream consequence.

## Gaps and deferred topics

| Gap or deferred topic | Why it stays open in U01 |
| --- | --- |
| Outcome of reviewing the U02/U03 drafts | Andrew accepted this starting set and seed; he may retain, revise, or replace them after reviewing the drafts. |
| Character names, identity, appearance, history, jobs, and voice | No approved Universe character source exists in the inspected main snapshot. |
| Exact location and company organization | The brand source establishes only the fictional company/workplace at a high level. |
| Relationship depth and any reporting structure | No approved relationship source exists; R1 is only the minimum collaboration needed by the proposed seed. |
| Which system or work item is involved, the factual mismatch, stakes, and resolution | The story seed intentionally leaves these as choices; no technical incident is treated as real or canonical. |
| Existing episode chronology, recurring cast, episode title/number, and publication status | No published comic record was found in the inspected Universe tree. The public numbering convention does not assign the first episode. |
| Additional characters, locations, relationship history, antagonists, or wider arcs | Not needed by this single seed and outside the proposed minimal coverage. |
| Hidden continuity, unrevealed explanations, private history, and comprehensive encyclopedia entries | Out of scope; no private material was accessed or inferred. |

## Gates and handoff

1. Andrew Peris confirmed the editor role and accepted this starting coverage and seed on 2026-10-13. Keep U01 open for parent review and handoff; this acceptance does not approve canon, a merge, an episode, or publication.
2. U02 and U03 remain separate bounded draft tasks and may proceed in parallel after this coverage acceptance under their own task-specific authorization and applicable owner/access prerequisites. The parent is launching those tasks. U02 may draft premise/tone/rules/conventions; U03 may draft only the accepted bounded records. U04 waits for both. This packet contains neither draft.
3. U04 must assemble and review every record for creative coherence and record explicit human content decisions. Formal first-comic C01 remains blocked on U04's human content decision; this seed does not start or approve an episode brief.
4. No merge, canon promotion, issue closure, art work, or publication is authorized by this packet.
