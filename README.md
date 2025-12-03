# Chain of Awareness (CoA)
<a href="whitepaper.md">CoA Whitepaper v3.0</a>
A user owned, encrypted and portable memory layer for AI systems.

CoA is a small open protocol that lets people keep their own AI history, encrypted at creation and portable across models and devices.  
The goal is simple, AI memory should belong to the person who created it, not to the model provider.

---

## Why CoA

Modern AI systems have a hard reset problem.

- Every new model version starts from zero  
- Device or provider changes break context  
- Users cannot prove that deletion really happened  
- Memory is trapped inside each vendor stack  

People are already using AI as coaches, confidants and creative partners.  
Relationships like that cannot deepen if memory keeps disappearing.

CoA aims to fix this by providing:

- **Ownership** - memory is created with user keys, not provider keys  
- **Encryption at creation** - plaintext never leaves the user device  
- **Portability** - the same memory can serve many different models  
- **Verifiable deletion** - keys can be destroyed and the deletion can be proven  
- **Structured recall** - an optional semantic layer for long term understanding

---

## High level architecture

CoA is defined as four cooperating layers.

### 1. Client layer

Runs on the user side.

- Local key generation and handling  
- AES based encryption of memory chunks  
- Local Merkle tree per memory batch  
- CRAB lifecycle  
  - Create  
  - Read  
  - Append  
  - Burn  

### 2. Storage layer

Any system that can store encrypted blobs and return a content address.

Examples that fit well:

- IPFS or Filecoin  
- Arweave  
- S3 compatible storage  
- Local or personal storage backends  

Only the content hash is important for CoA.  
The storage backend never sees plaintext.

### 3. Anchoring layer

Anchors small pieces of metadata on a public ledger for ordering and integrity.

Reference choice in the current design:

- Hedera Consensus Service (HCS)

Anchors include:

- Merkle roots for memory batches  
- vKEA deletion receipts  
- Consent receipts  

The protocol is ledger neutral, HCS is used as a practical starting point.

### 4. Semantic layer (SHIMI, optional)

A structured indexing layer that lets AI systems work with:

- timestamped events  
- links between concepts  
- tasks, goals and states  
- confidence scores and simple schemas  

SHIMI deals with structure and metadata, not plaintext content.

---

## vKEA - Verifiable Key Erasure Attestation

In CoA, deletion is defined as destroying the key, not the blob.

A vKEA proof contains for example:

- a hash of the key identifier  
- which memory batches are affected  
- a timestamp  
- a signature or zero knowledge proof that binds the event  

This proof is anchored on the ledger so that anyone can verify that the key used for a given memory can no longer be used.

If the key is gone, the memory is effectively gone.

---

## Status

This repository currently focuses on:

- Specification and protocol design  
- Documentation of CRAB, vKEA and SHIMI  
- Gathering feedback from researchers, builders and model providers  

A working prototype exists separately, built with:

- TypeScript client  
- Rust based key handling and vKEA generation  
- IPFS backend with local fallback  
- Hedera anchoring  
- A simple React based "Memory Wallet" demo

Parts of that prototype will be cleaned up and moved here as reference code over time.

---

## Background reading

These two texts give more context around the motivation for CoA.

- **The AI Relationship That Does Not Reset**  
  Conceptual overview of why continuity and ownership matter for AI relationships.  
  https://medium.com/@akechalfred/the-ai-relationship-that-doesnt-reset-4e7e45eee2e5  

- **Chain of Awareness - CoA**  
  Light whitepaper that this repository will track and extend.  
  https://medium.com/@akechalfred/chain-of-awareness-coa-fba68a388284  

---

## Roadmap (early sketch)

- Formalise the core spec for CRAB and vKEA  
- Publish cleaned up reference implementation for the client layer  
- Add example integrations for at least one LLM provider and one local model  
- Define SHIMI v1, including a minimal query language  
- Explore simple governance and community process around changes to the spec  

---

## Contributing

This is an early stage open project.  
Issues, questions and design feedback are very welcome.

If you want to:

- discuss the spec  
- propose changes  
- help with reference implementations  
- try CoA inside your own AI agent or product  

feel free to open an issue and describe what you have in mind.

---

## License

This project is released under the MIT License.  
See `LICENSE` for details.
