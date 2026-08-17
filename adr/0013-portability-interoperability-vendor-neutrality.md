# ADR 0013: Portability, interoperability, and vendor neutrality

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#46 — Define portability, interoperability, and vendor-neutrality principles](https://github.com/DefinitelySecureStudio/studio/issues/46)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)
- Constitutional article: [Portability, interoperability, and vendor neutrality](../CONSTITUTION.md#10-portability-interoperability-and-vendor-neutrality)

## Context

The Studio uses repositories, creative applications, asset stores, AI models,
hosted providers, indexes, workflow services, and production infrastructure.
Each may provide valuable distinctive behavior, but any can change its API,
model, export, price, rights, retention, access policy, or availability. Durable
creative truth and production evidence become fragile when their only usable
form is a provider object, chat history, opaque project file, proprietary index,
or undocumented database.

Portability cannot mean flattening every artifact to a screenshot or restricting
all systems to the smallest common feature set. It must preserve Studio-owned
meaning and authority while allowing explicit provider extensions. The model
also has to respect the established division in which Codex owns stable
contracts, Lab owns experiments, Platform owns production implementations,
Universe owns public canon, and Lore owns private planning truth.

## Decision

Require every durable Studio data class to have one recognized authoritative
home and a documented portable representation. An external service may process
or store an authorized copy but does not acquire authority. Studio-controlled
stable identifiers remain primary; provider identifiers are mappings or
provenance and cannot be the sole identifiers for facts, decisions, contracts,
sources, or releases.

Define a portable representation as one that an independent implementation can
parse using documented syntax and semantics while preserving the identity,
meaning, relationships, rights, sensitivity, and evidence needed for its
declared purpose. Prefer open, documented, machine-readable, widely implementable
formats. Preserve original bytes when conversion is lossy and maintain a
documented access or preservation rendition when proprietary source tooling is
required.

Set minimum portable representations for governance and specifications;
public canon and private Lore; prompts and agent behavior; context packages;
manifests, metadata, and provenance; creative sources and media; software and
workflows; and decisions and audit events. Prompts preserve provider-independent
intent and contracts, not only rendered provider requests. Context packages
preserve exact authorized payloads under versioned Codex contracts; embeddings
or hosted indexes alone are insufficient. Structured records distinguish
unknown, unavailable, redacted, and inapplicable data.

Place material provider integrations behind stable, implementation-neutral
Codex contracts where practical. Codex defines Studio semantics, capabilities,
errors, security boundaries, and import/export behavior. Platform isolates
provider credentials, transport, IDs, retries, limits, and extensions in
adapters while preserving exact provider evidence in provenance. Contract
fixtures and conformance tests distinguish portable required behavior from
optional extensions.

Require an exit record for every material external dependency. It identifies
ownership, data and authority boundaries, export completeness and constraints,
Studio-controlled backup state, restore procedure, replaceable boundary,
required capabilities, alternatives or continuity mode, loss, migration and
rollback, review triggers, residual risk, and accountable A4 owner. Exercise
exports and representative restore or reference-import paths on a risk-based
cadence and after material changes.

Verify migrations semantically rather than by file count. Preserve old-to-new
identity mappings, provenance, security classifications, rights, decisions, and
loss reports. Obtain domain-owner acceptance and retain rollback evidence as
required. On disconnection, revoke credentials and record the authorized
provider deletion or retention state.

Permit provider-specific capabilities when they offer a material benefit that
a reasonably available portable approach cannot provide at proportionate cost.
Record the benefit, alternatives, lock-in, data and rights, portable baseline,
isolated extension, degradation behavior, exit plan, replacement cost, review
date, and A4 approval. Extensions are namespaced or capability-gated, fail
clearly, and do not silently redefine portable semantics or force unrelated
consumers onto the provider. The decision creates no constitutional exception.

Assign repository responsibilities as follows: Studio owns governance and risk
acceptance; Codex owns neutral contracts, formats, fixtures, and reference
behavior; Lab tests providers and loss with safe data but supplies no direct
production dependency; Platform owns adapters, import/export, conformance, and
migration tooling; Universe publishes portable reader-safe canon snapshots;
Lore creates minimized protected exports under Codex contracts; artifact owners
preserve exact masters, editable sources where required, dependencies, rights,
integrity, and preservation renditions.

Add a portability gate for material contracts, integrations, migrations,
workflows, and provider-dependent releases. Verify authoritative homes,
portable representations, independent export/restore evidence, adapter
isolation, loss, continuity, exit ownership, and current dependency decisions.
Treat unrecoverable authoritative data, lost essential audit, or exclusive
external authority as a release Blocker.

## Rationale

Authority and recoverability are stronger targets than superficial format
conversion. They let the Studio use specialized tools without making those tools
the owners of canon, private truth, specifications, approvals, or history.
Studio-owned contracts isolate change at the provider boundary and make
capability differences explicit rather than pretending they do not exist.

Regular independent parsing and restore tests turn an export promise into
evidence. Repository responsibilities keep experiments, contracts,
implementations, and creative authorities separate while providing a clear path
for portable behavior to move into production.

## Consequences

### Positive

- Canon, Lore, contracts, prompts, manifests, metadata, provenance, and assets
  remain recoverable under Studio-recognized authority.
- Provider-specific features can be used without silently becoming core Studio
  semantics.
- Exports and exit plans are tested rather than assumed.
- Codex, Lab, and Platform have distinct portability responsibilities.
- Migration loss, concentration risk, and fallback behavior become explicit
  human decisions.

### Tradeoffs

- Adapters, conformance fixtures, reference importers, and restore tests require
  continuing maintenance.
- Exact source preservation may require licensed proprietary tools as well as
  portable access renditions.
- Some provider features cannot be reproduced identically after migration.
- Protected Lore portability requires restricted infrastructure and cannot rely
  on a broad convenience export.

## Rejected alternatives

### Ban all proprietary providers and formats

Rejected because vendor neutrality is control and recoverability, not avoidance
of useful differentiated capabilities. A ban would unnecessarily reduce
creative and operational quality.

### Accept any provider export as portable

Rejected because an opaque archive, screenshot, flattened media file, or
incomplete API dump may omit meaning, relationships, identity, editability,
rights, or decision evidence.

### Adopt each provider schema as the Studio contract

Rejected because provider transport and domain semantics change for reasons the
Studio does not control and would spread lock-in to every consumer.

### Preserve only released output

Rejected because future editing, audit, continuity, rights review, correction,
and regeneration depend on sources, decisions, relationships, prompts,
metadata, and provenance.

### Document an exit plan without testing it

Rejected because an unparsed export or unexercised restore path can fail only
after access, time, or provider cooperation has been lost.

## Implementation

The Constitution owns authority, durable representation, contract, adapter,
dependency-decision, migration, and portability-gate requirements. The
cross-repository dependency strategy implements immutable references and
compatibility. Codex will define concrete schemas, bundles, capability
negotiation, fixtures, and reference validators; Platform will implement
adapters and migration tooling; Lab may compare provider behavior and data loss
without becoming a production dependency.
