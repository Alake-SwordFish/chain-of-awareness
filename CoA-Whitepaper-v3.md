CoA 3.0

Chain of Awareness (CoA)

Whitepaper v3.0 – November 2025

An Open Protocol for User-Owned, Verifiable AI Memory

© 2025 CoA Collective – CC BY-SA 4.0


---

Executive Summary

Chain of Awareness (CoA) is an open protocol for user-owned, cryptographically verifiable AI memory.

All memories are:

encrypted client-side

stored in any verifiable storage backend (DataHaven, IPFS/Filecoin, Arweave, or user-owned storage)

anchored to a public ledger for immutable ordering (Hedera HCS as reference implementation)

erasable through Verifiable Key Erasure Attestation (vKEA)

managed through a consent-driven lifecycle called CRAB: Create, Read, Append, Burn


CoA gives users true ownership of their AI memory:
The network never sees plaintext, no operator can secretly retain or alter memory, and deletion is provable to everyone.

A working local prototype (TypeScript + Rust) exists today, with full CRAB flow, vKEA generation, and ledger anchoring.


---

1. Introduction

AI systems are shifting from tools to companions.
When a model becomes a therapist, advisor, tutor, or personal assistant, memory stops being optional. It becomes the foundation for trust.

Today, this trust is broken.

“Delete conversation” is not verifiable

model providers control storage, access and retention

users cannot move their memory to another system

consent is static and unprovable

no model gives users their own encryption keys

no memory layer is portable across AIs


CoA addresses this by giving memory:

user ownership

cryptographic privacy

verifiable deletion

portable structure

interoperable semantics

storage-agnostic design


The goal is simple:
AI memory should belong to the person who creates it, not the company who hosts it.


---

2. Design Principles

CoA is built on a small set of unbreakable rules:

1. Memory is encrypted at creation
Plaintext never leaves the user’s device. Keys never leave the device.

2. Storage is pluggable
CoA does not require any specific chain or storage network.
DataHaven, IPFS/Filecoin, Arweave, S3, or local disks can serve as encrypted blob storage.

3. Anchoring is minimal and immutable
Only small Merkle roots and deletion proofs are anchored.
Hedera HCS is the reference implementation, but the protocol is ledger-neutral.

4. Deletion is real and provable
vKEA turns deletion into a cryptographic event:
Destroy key → generate proof → anchor → user receives receipt.

5. Consent is granular, revocable, and verifiable
Based on W3C DIDs and Verifiable Credentials.

6. Semantic memory is optional but powerful
SHIMI, a structured indexing layer, provides better recall for AI agents without exposing plaintext.

7. CoA is not tied to any AI model
It works with GPT, Claude, Grok, local models, or future systems.


---

3. Core Architecture

CoA consists of four layers:

1. Client Layer (encryption, key handling, vKEA)


2. Storage Layer (verifiable blob storage)


3. Anchoring Layer (Merkle roots + deletion receipts)


4. Semantic Layer (SHIMI – optional structured memory graphs)




---

3.1 Client Layer

This is where privacy is guaranteed.

AES-256-GCM encryption

user-owned keys only

local Merkle tree per memory batch

CRAB lifecycle enforcement

vKEA generation for key burn events


Once encrypted, CoA treats memory as an opaque blob.


---

3.2 Storage Layer

CoA supports any system capable of storing encrypted data and returning content-addressed identifiers.

Reference implementations:

DataHaven AVS (EigenLayer, Merkle Patricia Forests, storage proofs)

IPFS/Filecoin

Arweave

User-managed storage (S3, NAS, on-device fallback)


Key requirement:
Storage must produce a deterministic hash (CID or equivalent).

This hash becomes part of the Merkle tree and is anchored.


---

3.3 Anchoring Layer

Anchoring ensures memory integrity and ordering without storing plaintext.

Reference implementation: Hedera Consensus Service (HCS)

near real-time finality

predictable fees

no smart contracts required

minimal metadata for audit trails


Anchors:

Merkle root of memory batch

vKEA deletion proofs

consent receipts


CoA is ledger-agnostic; HCS is a practical default.


---

3.4 CRAB Lifecycle

Create
Encrypt memory, store blob, update Merkle tree, anchor hash.

Read
Retrieve blob, verify Merkle inclusion, decrypt locally.

Append
New version references old version; tree updates; anchor.

Burn
Key destroyed → vKEA proof generated → proof anchored → user receives deletion receipt.

CRAB ensures all memory actions are traceable and user-controlled.


---

3.5 vKEA – Verifiable Key Erasure Attestation

Deletion is not “requesting a server to obey”.
Deletion is destroying the key and proving it.

A vKEA proof contains:

key identifier hash

affected memory IDs

timestamp

signature or ZK proof verifying destruction event

anchored receipt (ledger)


If the key is gone, the data is un-decryptable forever.


---

3.6 SHIMI – Semantic Memory (Optional)

SHIMI is a structured indexing layer built on RDF/OWL:

timestamped events

Semantic Confidence Scores

references between nodes

schema for conversations, emotions, tasks, goals

SQL-like query language for retrieving memory without raw dumps


LLMs can use SHIMI through embeddings or structured prompts.

SHIMI never exposes plaintext; only structure and metadata.


---

4. Reference Implementation (Prototype)

A working prototype exists with:

TypeScript client library

Rust key-handling and vKEA generation

IPFS backend + local fallback

Hedera anchoring

React Memory Wallet UI

W3C DID/VC consent flows


CRAB flows complete in ~2–4 seconds on consumer hardware with residential internet.

This is not a final implementation; it proves feasibility.


---

5. Threat Model (Minimal Practical Version)

CoA defends against:

servers retaining plaintext

silent retention after “delete”

undetectable modification of memory

unauthorized access without user-issued VC

corporate shutdowns deleting your history

opaque provider-side behavior


CoA does NOT defend against:

compromised user devices

malicious browser extensions

users re-sharing decrypted content

coercive access at the legal level

inference attacks at the model layer


Design philosophy:
Privacy must be guaranteed at creation, not dependent on provider honesty.


---

6. Interoperability

CoA is compatible with:

W3C DID

Verifiable Credentials

any blob-storage

any ledger with cheap ordering

any AI model (local or cloud)

browser, mobile, or desktop clients


Memory can move freely across AI platforms.


---

7. Governance

A hybrid DAO manages protocol evolution:

token + reputation

upgrade proposals

review committees (ethics, legal, technical)

emergency circuit-breakers

transparent logging


Governance never controls user memory; it only controls protocol evolution.


---

8. Roadmap (Non-Speculative)

Q4 2025
Public testnet
CRAB prototype
vKEA prototype
HCS anchoring
Memory Wallet alpha

Q1 2026
Relay mesh
MAP-1 verification protocol
Storage provider integration

Q2 2026
SHIMI v1
ZK-based consent proofs
Improved vKEA circuits

Q4 2026
Multi-agent memory sharing
Developer SDK 1.0


9. Conclusion

CoA turns AI memory from a corporate asset into a user-sovereign digital capability.

Encrypted at creation.
Verifiable in operation.
Erasable with proof.
Portable across systems.
Independent of any company or model.

This is the foundation for AI companions that respect autonomy, privacy, and trust.


---

Appendices (Condensed Headers)

A1: SHIMI specification
A2: CRAB + vKEA specification
A3: MAP-1
A4: Storage backend integration
A5: Consent VC schema
A6: Threat surfaces
A7: ZKP circuits
A8: Memory Wallet API
A9: Governance model
A10: Glossary
