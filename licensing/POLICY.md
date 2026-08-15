# Repository licensing policy

This document is the operational source of truth for Definitely Secure Studio
repository licensing. [ADR 0004](../adr/0004-repository-licensing-and-ip-boundaries.md)
records the decision.

## Repository matrix

| Repository | Visibility | Classification | Root terms | Protected material and boundary |
| --- | --- | --- | --- | --- |
| `studio` | Public | Proprietary, with file-level third-party exceptions | Studio proprietary `LICENSE` and `NOTICE` | Governance, brand system, Prompt Mark, names, logos, trade dress, and original assets are all rights reserved. Bundled fonts and any other identified third-party files retain their own terms. |
| `codex` | Public | Open source | Apache-2.0 `LICENSE` and repository `NOTICE` | Original specifications, schemas, prompt contracts, documentation, and fixtures are Apache-2.0. No private lore, brand assets, or proprietary creative examples. |
| `lab` | Public | Open source | Apache-2.0 `LICENSE` and repository `NOTICE` | Original experiments, prompts, prototypes, validators, documentation, and synthetic fixtures are Apache-2.0. Experimental status does not change the license. |
| `platform` | Public | Open source | Apache-2.0 `LICENSE` and repository `NOTICE` | Original production source, tests, configuration, and documentation are Apache-2.0. Creative inputs are referenced through contracts and are not vendored. |
| `universe` | Public | Proprietary creative IP | Universe proprietary `LICENSE` and `NOTICE` | Characters, settings, canon, stories, comics, dialogue, artwork, publication assets, and original metadata are all rights reserved unless a release explicitly says otherwise. |
| `lore` | Private | Confidential proprietary creative IP | Lore proprietary `LICENSE` and `NOTICE` | Hidden timelines, unrevealed continuity, private context, and internal creative material are all rights reserved and limited to authorized Studio work. |

Any future prompt or tooling repository defaults to Apache-2.0 only when it is
public, content-neutral, and contains no proprietary creative or brand material.
Otherwise its license requires an organization-level ADR amendment.

## Boundaries

1. A repository's root license covers original Studio work in that repository
   only. It does not relicense third-party material.
2. Public access is not a license. `studio` and `universe` are publicly readable
   but remain proprietary.
3. Apache-2.0 tooling may process proprietary inputs at runtime, but those inputs
   do not become Apache-2.0 and must not be committed, logged, cached in build
   artifacts, or used as fixtures.
4. Stable prompts and prompt contracts in `codex`, and original experimental
   prompts in `lab`, are Apache-2.0. Prompt instances containing private lore or
   unreleased creative context stay in `lore` or an approved secure runtime.
5. Names, the Prompt Mark, wordmarks, logos, slogans, trade dress, and other
   source identifiers are not licensed with software. Descriptive attribution
   allowed by the Apache license is not permission to imply endorsement.
6. Creative-IP rights do not move with metadata. A release manifest may be
   Apache-licensed as a schema while a populated manifest and its linked comic
   assets remain proprietary.
7. An explicit per-file or per-directory notice overrides the root classification
   only for the identified material. Keep that notice with every redistributed
   copy.

## Required repository files

Every repository must contain:

- a root `LICENSE` with either the canonical Apache-2.0 text or the applicable
  proprietary terms;
- a root `NOTICE` identifying the repository, copyright owner, trademark
  boundary, and third-party-notice rule; and
- a README section based on [`README-BOILERPLATE.md`](README-BOILERPLATE.md).

When a distribution contains third-party material with attribution or license
copy requirements, add those notices to `THIRD_PARTY_NOTICES` or the location
required by the dependency's license. A package manifest is not a substitute
for required notices.

## Review triggers

Request a licensing review when a change:

- copies material between an Apache-2.0 and proprietary repository;
- introduces a new license family or material without verifiable provenance;
- adds copyleft or source-available code, data with use restrictions, a model or
  model output, or an asset acquired from a marketplace;
- bundles fonts, images, audio, video, character likenesses, or other creative
  assets in a software distribution; or
- changes ownership, contribution terms, brand use, or commercial distribution.

See [`THIRD_PARTY.md`](THIRD_PARTY.md) for the intake checklist.
