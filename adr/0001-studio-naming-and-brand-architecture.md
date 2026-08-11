# ADR 0001: Studio naming and brand architecture

- Status: Proposed
- Date: 2026-08-11
- Decision owners: Definitely Secure Studio
- Related issue: [#8 — Finalize studio branding](https://github.com/DefinitelySecureStudio/studio/issues/8)

## Context

The organization needs one identity that can publish *Definitely Secure* while also supporting future comics, publications, animation, tools, and unrelated creative universes. “Definitely Secure” already carries two story-level meanings: the flagship comic and the fictional workplace inside it. Without a defined hierarchy, public credits can confuse the real producer with the property or its fictional company. The GitHub organization and primary domain also need to fit the same system without forcing their technical forms into public prose.

## Decision

The formal and public studio name is **Definitely Secure Studio**. It is the durable parent identity for all real-world creative and technical work.

**Definitely Secure** is the official title of the flagship comic and its broader creative universe. It is also the name of the fictional company inside that universe. Context and typography distinguish those uses; “Definitely Secure Inc.” is not the title.

The approved hierarchy is:

```text
Definitely Secure Studio
├── Definitely Secure
│   ├── Fictional workplace/company
│   ├── Characters and lore
│   └── Supporting stories and publications
├── Future creative properties
└── Open-source tools and experiments
```

The Studio uses the production credit “A Definitely Secure Studio production.” Its tagline is “Serious craft. Questionable systems.” Open-source tools use the Studio identity rather than a separate engineering brand, while retaining their own product names and licenses.

`DefinitelySecureStudio` remains the GitHub organization identifier. `definitelysecure.com` is the primary Studio domain and can host both the flagship property and future projects.

The Studio does not appear as an entity inside the *Definitely Secure* fictional universe by default. Any exception must be a deliberate and clearly signposted meta-fictional choice.

Corporate suffixes and category words are not part of the public brand. A registered legal suffix is used only where legally or contractually required. New imprints require their own later decision.

## Rationale

Keeping “Studio” in the parent name separates the real producer from the comic and fictional company while preserving the recognition already attached to “Definitely Secure.” A broad parent identity avoids limiting future work to comics or publishing. Using one Studio identity for creative and open-source output keeps attribution coherent; licenses and product names provide the necessary distinction without another umbrella brand.

The tagline expresses the shared editorial point of view without tying the Studio to one medium or property. Retaining the existing domain and GitHub identifier avoids unnecessary migration and makes the difference between human-facing names and platform-constrained identifiers explicit.

## Consequences

### Positive

- Public credits clearly identify the real-world producer.
- The flagship property keeps the shorter, stronger title *Definitely Secure*.
- Future properties and formats fit beneath a medium-neutral studio name.
- Creative and technical projects share discoverable provenance.
- Website, social, repository, and legal usage have explicit rules.

### Tradeoffs

- “Definitely Secure” remains intentionally ambiguous between the title and fictional company, so some sentences need a clarifying noun.
- Social handles may use either the property-sized form or the longer studio form depending on availability.
- Legal documents may show a registered entity name that differs from the public brand.

## Rejected alternatives

### Use “Definitely Secure” as the studio name

Rejected because it collapses the producer, property, and fictional company into one undifferentiated name and leaves no clear parent identity for future work.

### Title the comic “Definitely Secure Inc.”

Rejected because the suffix makes the title feel like a corporate entity, adds friction to speech and display, and does not resolve the need for a distinct real-world studio.

### Create a separate engineering identity

Rejected for now because it fragments attribution before the tool portfolio requires an independent audience or promise. Individual tools may still have distinct product names.

### Use “Press,” “Comics,” or “Productions” as the parent suffix

Rejected because each narrows the organization to a subset of its planned media and technical work.

## Implementation

The canonical wording, biographies, credits, channel guidance, and detailed do-and-don’t rules live in [`brand/studio-identity.md`](../brand/studio-identity.md). Public surfaces and repository metadata should migrate to that language as they are created or next revised.
