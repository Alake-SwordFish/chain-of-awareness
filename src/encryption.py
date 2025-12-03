"""
encryption.py
Very small placeholder for client-side encryption for Chain of Awareness (CoA).

IMPORTANT:
This is NOT real cryptography. It is only a simple XOR-based scheme
so we can build and test the rest of the CoA flow.
In a real implementation this must be replaced with proper
authenticated encryption (for example libsodium / AES-GCM).
"""

from typing import ByteString


def _derive_key(key_str: str, length: int) -> bytes:
    """
    Derive a repeatable byte key from a user key string.
    Not secure, just for testing.
    """
    key_bytes = key_str.encode("utf-8")
    if not key_bytes:
        raise ValueError("Encryption key must not be empty")
    # repeat key bytes until we reach desired length
    return (key_bytes * (length // len(key_bytes) + 1))[:length]


def encrypt(plaintext: ByteString, key: str) -> bytes:
    """
    "Encrypt" bytes using a simple XOR with a derived key.
    Returns ciphertext bytes.
    """
    data = bytes(plaintext)
    k = _derive_key(key, len(data))
    return bytes(b ^ kb for b, kb in zip(data, k))


def decrypt(ciphertext: ByteString, key: str) -> bytes:
    """
    Decrypt bytes. XOR is symmetric, so encrypt() and decrypt()
    are the same operation with the same key.
    """
    data = bytes(ciphertext)
    k = _derive_key(key, len(data))
    return bytes(b ^ kb for b, kb in zip(data, k))
