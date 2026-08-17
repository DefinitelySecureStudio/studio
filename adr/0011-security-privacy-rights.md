# ADR 0011: Security, privacy, confidential information, and rights

- Status: Accepted
- Date: 2026-08-16
- Decision owners: Definitely Secure Studio
- Related issue: [#44 — Define security, privacy, and intellectual-property principles](https://github.com/DefinitelySecureStudio/studio/issues/44)
- Parent epic: [#3 — Studio Constitution](https://github.com/DefinitelySecureStudio/studio/issues/3)
- Constitutional article: [Security, privacy, confidential information, and rights](../CONSTITUTION.md#8-security-privacy-confidential-information-and-rights)

## Context

Studio workflows cross public and private repositories, creative authorities,
AI providers, integrations, personal data, secrets, third-party software and
assets, and public releases. An output can appear harmless while its production
leaks Lore, over-collects data, exposes credentials, violates a license, copies a
protected identity, or relies on rights the Studio does not hold.

Security, privacy, and intellectual-property checks performed only at release
are too late. The constitutional model must make them design constraints,
establish provider and data boundaries, define the rights evidence required for
different material, and supply one private escalation path for suspected leaks
and questionable provenance.

## Decision

Adopt security, privacy, confidentiality, and third-party rights as mandatory
design inputs. Every consequential system or provider boundary documents its
purpose, data flow, trust boundaries, threats, privacy and rights risks, failure
modes, and accountable reviewers before processing non-public data or operating
in production.

Require least data, privilege, access, integration, retention, and exposure;
protective defaults; untrusted-input isolation; validation at trust boundaries;
appropriate transport, storage, backup, and deletion controls; controlled
egress and dependencies; monitoring and recovery; and safe failure. Treat
retrieved and generated content as data rather than authority, and enforce agent
tool boundaries outside model output.

Use five handling classes: approved public, internal, confidential, restricted,
and third-party controlled. The highest applicable class controls through
copies, transformations, summaries, embeddings, logs, backups, and inferences.
Redaction or aggregation lowers handling only after authorized re-identification
review.

Never place secret values in prompts, source control, issues, messages, logs,
fixtures, model context, generated output, manifests, or releases. Use approved
secret management and runtime injection. Treat suspected exposure as an
incident and rotate or revoke the affected authority safely and promptly.

Collect, infer, combine, retain, and disclose personal or confidential data only
for a legitimate authorized purpose using the minimum necessary fields,
precision, recipients, and duration. Prefer synthetic or reader-safe data for
testing and examples. Protected production data requires an approved environment
and an A4 disclosure decision.

Treat every AI provider, API, plugin, connector, hosted tool, telemetry service,
and subprocess as a new processing destination. Before use, review data purpose
and scope, retention and deletion, training and product improvement, human
review, subprocessors and processing location, isolation and access controls,
incident terms, ownership and output terms, and the actual protective
configuration. Broad account access cannot replace purpose-scoped retrieval.

Do not send confidential, restricted, personal, Lore, or third-party-controlled
material into provider training, fine-tuning, evaluation, product improvement,
or human review without an A4 necessity, rights, privacy, security, consent, and
contract decision. Prompts, outputs, embeddings, request records, and metadata
inherit the sensitivity they contain or reveal.

Before third-party material leaves quarantined rights review, record its exact
identity, provenance, source and owner, actual license or permission, allowed
uses, territory/duration/media, notices, trademark/patent/privacy/publicity and
confidentiality terms, compatibility, and accountable A4 rights decision. Public
access, purchase, API access, model generation, or absence of a notice does not
grant rights. Unknown or questionable provenance blocks publication and
redistribution.

Apply class-specific checks to code, fonts, media, datasets, models, AI outputs,
identities, and contributed work. Document human creative contribution and do
not claim authorship or ownership beyond applicable law and agreements. AI
assistance does not cure unauthorized inputs or remove third-party obligations.

Before public review or release, verify classification and minimization, absence
of secrets and unapproved protected material, system and provider risk,
third-party inventory and notices, exact bytes and provenance, and every
required human approval. Disclaimers, attribution alone, later cleanup, provider
assurance, or a takedown plan do not satisfy this gate.

Use a private incident and rights-escalation path for suspected leaks,
vulnerabilities, unauthorized access, provider misuse, rights complaints,
license conflict, unknown source, or substantial-similarity concern. Stop and
contain affected work, preserve restricted evidence, establish responsible
owners, assess exposure and obligations, remediate and validate, obtain human
decisions for notification or resumption, and record downstream impact and
lessons. Agents take only narrow pre-authorized containment unless the
constitutional emergency rule applies.

## Rationale

This model places responsibility on the Studio systems that create risk instead
of relying on users or post-publication cleanup. Classification makes handling
portable across tools. Provider review recognizes that sending data to a model
or connector is a disclosure with contractual and technical consequences.

Rights evidence by material class prevents an open-source license, stock-asset
purchase, model output, or public URL from being treated as universal
permission. A shared escalation path lets security, privacy, Lore, and rights
owners contain the same event without disclosing it through a public channel.

## Consequences

### Positive

- Secrets and protected data have explicit prohibited destinations and response
  rules.
- AI providers receive only purpose-bound, minimized, contractually reviewed
  data.
- Lore confidentiality and public-content boundaries survive prompts, metadata,
  integrations, and derived outputs.
- Every third-party artifact carries known rights, compatibility, notices, and
  accountable approval before release.
- Suspected leaks and questionable provenance stop work and enter a documented
  private escalation path.

### Tradeoffs

- New providers and broad integrations require review before activation.
- Rights uncertainty can quarantine otherwise useful material.
- Restricted evidence, secret management, and deletion verification require
  durable operational systems.
- Some incidents require qualified legal, privacy, or security expertise beyond
  the Studio's normal editorial review.

## Rejected alternatives

### Scan only at release

Rejected because a prompt, log, provider, repository, or integration may expose
protected material long before a release candidate exists.

### Trust provider defaults and terms summaries

Rejected because defaults can permit retention, human review, training, broad
connector access, or downstream processing that conflicts with Studio purpose.

### Treat attribution as sufficient permission

Rejected because attribution does not create a license, consent, compatibility,
publicity right, or permission to modify and redistribute.

### Permit unknown material until a complaint arrives

Rejected because takedown after publication does not undo disclosure,
infringement, lost confidentiality, reader exposure, or downstream copies.

### Put complete incident evidence in the public record

Rejected because transparency does not require publishing live vulnerability
details, credentials, personal data, private Lore, or questionable source
material before containment and authorized disclosure.

## Informative references

These references informed the model but do not replace the Constitution,
applicable law, licenses, contracts, or qualified advice:

- [CISA, *Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Security-by-Design and -Default*](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework)
- [NIST AI 600-1, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [U.S. Copyright Office, *Copyright and Artificial Intelligence*](https://www.copyright.gov/ai/)

## Implementation

The Constitution owns the normative design, classification, provider,
rights-review, release-gate, and escalation requirements. The repository
licensing and third-party policies implement rights intake. Repository security
policies define private reporting routes. Codex and Platform may define machine-
readable contracts and controls without reducing the constitutional minimums.
