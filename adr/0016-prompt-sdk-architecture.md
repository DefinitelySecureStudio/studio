# ADR 0016: Prompt SDK architecture and responsibility boundaries

- Status: Accepted
- Date: 2026-08-17
- Decision owner: Definitely Secure Studio (`@andrewperis`)
- Related issue: [#61 — Define Prompt SDK architecture and responsibility boundaries](https://github.com/DefinitelySecureStudio/studio/issues/61)
- Parent epic: [#4 — Prompt SDK](https://github.com/DefinitelySecureStudio/studio/issues/4)
- Architecture: [Prompt SDK v1 architecture](../prompt-sdk/ARCHITECTURE.md)
- Constitution version: 1.0.0
- Constitution tag: `constitution/v1.0.0`
- Constitution commit: `a9cc8a503aa30e17820edc62ac95f7cbe10e0564`
- Applicable checklist profiles: Universal; ADR, RFC, and stable specification; repository and production system; agent and automated workflow
- Conformance evidence: issue #61, this ADR, and the owner-reviewed adopting pull request

## Context

Prompt SDK v1 must make Studio prompts versioned, validated, renderable,
executable, portable, and auditable. Without an architecture boundary, the
initial implementation could make Platform code authoritative for prompt
meaning, let provider request objects leak into durable definitions, duplicate
Context Builder retrieval, or treat model output as approved creative truth.

The existing repository topology assigns stable contracts to Codex,
experiments to Lab, production software to Platform, reader-safe Canon to
Universe, and private planning truth to Lore. The cross-repository dependency
strategy requires immutable artifacts rather than branches or copied schemas.
The Constitution requires explicit human authority, provider-neutral portable
baselines, minimized protected context, integrity-verifiable provenance, and
separation between automated results and A4 Canon/publication decisions.

The first implementation issues depend on shared meanings for prompt
definition, template, rendered prompt, execution request, execution result,
context integration, provider extensions, provenance, and v1 exclusions.

## Decision

Adopt the architecture in
[`prompt-sdk/ARCHITECTURE.md`](../prompt-sdk/ARCHITECTURE.md).

Assign ownership as follows:

- Codex owns the stable Prompt Specification, schemas, capability and error
  vocabulary, template/execution/result/provenance contracts, extension
  envelope, compatibility rules, fixtures, and reference validation behavior.
- Lab owns safe prompt/provider/evaluator experiments and promotion evidence,
  but is never a stable contract or production dependency.
- Platform owns the production SDK, CLI, registry implementation, validation,
  deterministic renderer, adapter-neutral executor, provider adapters,
  structured-output handling, evidence emission, packages, tests, and releases.
- Context Builder owns Canon/Lore retrieval, selection, minimization,
  classification, approval, and package assembly. Prompt SDK consumes an
  explicit prepared package and never performs those functions.
- Build Orchestrator owns multi-step coordination and build-level retry,
  rollback, and release-candidate flow. Universe and authorized humans retain
  Canon and publication authority.

Define the lifecycle boundaries:

1. A prompt definition is an immutable portable document under one exact Codex
   Prompt Specification version.
2. Its prompt template is a side-effect-free provider-neutral structure using
   only declared variables and context slots.
3. A rendered prompt is the deterministic immutable output of one definition,
   explicit inputs, and explicit context values.
4. An execution request adds capability requirements, portable parameters,
   output contract, delegation, budget/deadline, context metadata, and optional
   namespaced provider extensions without credentials.
5. A Platform adapter maps the request to one provider and returns a normalized
   execution result containing output/status, provider/model/adapter identity,
   usage/timing, validation, finish state, and normalized error information.
6. A separate provenance record links exact inputs, contracts, implementation,
   provider evidence, outputs, validations, and delegation without requiring
   sensitive bodies in logs or public records.

Use synchronous provider-neutral text/message execution with optional
structured-output validation as the v1 portable baseline. Isolate provider SDK
imports and credentials inside adapter packages. Provider-specific behavior
uses an explicit Codex-defined namespaced extension with capability gating,
data/rights review, provenance, clear fallback or no-fallback behavior, and
typed failure. An extension cannot silently change portable semantics.

Require exact registry resolution for production and release evidence. Hosted
registries are replaceable distribution mechanisms, not authorities that may
mutate definitions invisibly. Rendering cannot implicitly read environment,
files, networks, clocks, randomness, or content repositories.

Reserve typed content parts, capability declarations, output contracts,
execution identities, and the extension envelope for later image, multimodal,
validation, agent, streaming, and asynchronous contracts. Do not implement
those behaviors in the v1 core.

## Rationale

Separating stable meaning from implementation lets contracts evolve under
Codex compatibility rules while Platform can change language, registry,
provider SDK, or transport independently. It also lets Lab explore quickly
without allowing experiments to become accidental production APIs.

An explicit context-package boundary prevents Prompt SDK convenience functions
from becoming a second Canon/Lore retrieval authority. Deterministic rendering
creates a testable boundary before nondeterministic model execution. Separate
results and provenance let callers retain audit value while minimizing
sensitive bodies. Explicit extensions preserve differentiated provider features
without imposing their schemas on every prompt and consumer.

A deliberately small text-first synchronous baseline is enough to exercise the
complete definition-to-result contract. The reserved seams allow later media
and agent work to add contracts after their additional rights, safety,
delegation, recovery, and release requirements are understood.

## Consequences

### Positive

- `codex`, `lab`, and `platform` have unambiguous ownership and promotion paths.
- Durable prompt definitions remain portable across provider and Platform
  implementation changes.
- Context Builder can evolve independently behind a versioned package contract.
- Validation and deterministic rendering can run without credentials, network,
  or paid provider calls.
- Every provider call can produce traceable, sensitivity-appropriate evidence.
- Later manifests and orchestration can reference executions without taking
  ownership of prompt semantics.
- Model success cannot be confused with Canon or publication approval.

### Tradeoffs

- Codex and Platform must version related but separate contract and
  implementation releases.
- Adapter normalization cannot make providers behaviorally identical; exact
  provider evidence and capability differences remain visible.
- Deterministic rendering and explicit inputs are less convenient than hidden
  environment or retrieval helpers.
- Context packages and private provenance require secure runtime/restricted
  evidence systems outside public source.
- Image, multimodal, agent, streaming, and hosted-management features are
  deferred even if a provider offers them immediately.

## Rejected alternatives

### Let Platform define both the prompt format and implementation

Rejected because runtime convenience would become cross-repository contract
authority and consumers could not implement or validate the format
independently.

### Store prompts as provider-native request objects

Rejected because vendor fields, roles, model IDs, hosted-object identity, and
defaults would become durable Studio semantics and make migration unreliable.

### Let Prompt SDK retrieve and assemble Canon or Lore

Rejected because it duplicates Context Builder, broadens sensitive access, and
creates competing creative authority and provenance paths.

### Treat rendered prompts as the authoritative prompt artifact

Rejected because rendered text loses variable declarations, intent,
compatibility, context boundaries, and the distinction between definition and
one sensitive execution input.

### Require a hosted prompt-management service

Rejected because remote mutable state, hidden revisions, access loss, and
provider-specific APIs would violate the portable authority and exit model.

### Put all modalities, agents, and orchestration into v1

Rejected because media safety/rights, tool authorization, durable state,
streaming, recovery, and human takeover require additional contracts and would
make the stable core larger before its basic boundaries are proven.

## Open decisions and constraints

This ADR fixes authority, lifecycle boundaries, context ownership, the adapter
seam, the text-first synchronous baseline, provenance responsibilities, and v1
non-goals. It intentionally leaves these implementation-neutral details to the
linked child issues and their owning repositories:

- Prompt Specification serialization, field names, ID syntax, versioning, and
  compatibility rules (#62);
- rendering grammar, escaping, canonicalization, and safe integrity form (#63);
- lint rules and diagnostic codes (#64);
- capability vocabulary, parameter normalization, adapter API, result model,
  and error taxonomy (#65);
- registry protocol, packaging, caching, and offline resolution (#66);
- exact context-package slot and reference schema shared with Epic #5 (#67);
- structured-output parser and repair policy (#68); and
- provenance schema, retention profiles, redaction, and observer interfaces
  (#69).

The implementation language, package layout, provider set, hosted registry, and
telemetry backend are also undecided. Any choice must preserve the boundaries
in this ADR, the portable provider-free baseline, independent conformance
testing, protected-data controls, and a documented exit path.

## Implementation

Implement the decision through Epic #4 in dependency order:

1. #62 publishes the Codex Prompt Specification and schemas.
2. #63 and #64 implement deterministic rendering, validation, and linting.
3. #65 defines execution, capability, adapter, result, and error contracts.
4. #66 implements exact-version registry resolution.
5. #67 consumes prepared context packages from Epic #5 fixtures/contracts.
6. #68 implements declared structured-output parsing and validation.
7. #69 emits safe execution provenance and observability.
8. #70 and #71 add CLI/CI authoring, mock adapters, conformance, regression,
   failure, and redaction coverage.
9. #72 publishes reviewed Codex and Platform v1 releases and documentation.

Each stable Codex contract and consequential Platform workflow performs its own
applicable Constitution assessment against the exact version it adopts. A
change to repository authority, context ownership, portable baseline,
extension semantics, provider boundary, protected-data handling, or
Canon/publication authority requires review of this ADR rather than a local
implementation override.
