"""
coa_client.py
Simple high-level CoA client using:
- encryption.py for client-side "encryption"
- storage.py backend interface
- local_storage.LocalStorage as default backend
"""

from typing import Optional

from encryption import encrypt, decrypt
from storage import StorageBackend
from local_storage import LocalStorage


class CoAClient:
  """
  Minimal Chain of Awareness client.

  CRAB-lifecycle:
  - Create: write new encrypted memory block
  - Read:   fetch and decrypt a block
  - Append: append to an existing block
  - Burn:   mark a block as deleted
  """

  def __init__(self,
               backend: Optional[StorageBackend] = None,
               encryption_key: str = "demo-key") -> None:
    self.backend = backend or LocalStorage()
    self.key = encryption_key

  def create(self, memory_id: str, plaintext: str) -> str:
    """Create a new encrypted memory block."""
    data = encrypt(plaintext.encode("utf-8"), self.key)
    return self.backend.write(memory_id, data)

  def read(self, memory_id: str) -> Optional[str]:
    """Read and decrypt a memory block."""
    data = self.backend.read(memory_id)
    if data is None:
      return None
    plaintext = decrypt(data, self.key)
    return plaintext.decode("utf-8", errors="replace")

  def append(self, memory_id: str, extra_text: str) -> str:
    """Append text to an existing memory block."""
    data = encrypt(extra_text.encode("utf-8"), self.key)
    return self.backend.append(memory_id, data)

  def burn(self, memory_id: str) -> bool:
    """Burn (delete) a memory block."""
    return self.backend.burn(memory_id)
