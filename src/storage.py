"""
storage.py
Basic storage abstraction for Chain of Awareness (CoA).

This module defines a simple interface for:
- writing encrypted memory blocks
- reading them back
- appending new blocks
- marking entries as burned (deleted)

Real implementations will use verifiable storage like IPFS/Filecoin,
Arweave, Hedera HCS, or user-owned storage.
"""

class StorageBackend:
    """Abstract storage backend."""

    def write(self, key: str, data: bytes) -> str:
        """Store encrypted bytes. Return a content ID or path."""
        raise NotImplementedError

    def read(self, key: str) -> bytes:
        """Retrieve encrypted bytes."""
        raise NotImplementedError

    def append(self, key: str, data: bytes) -> str:
        """Append new encrypted memory block."""
        raise NotImplementedError

    def burn(self, key: str) -> bool:
        """Mark a memory block as deleted (vKEA in real system)."""
        raise NotImplementedError
