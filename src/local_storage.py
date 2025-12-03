"""
local_storage.py
Simple local filesystem backend for Chain of Awareness (CoA).
Not secure, not encrypted - for testing only.
"""

import os
from typing import Optional
from storage import StorageBackend


class LocalStorage(StorageBackend):
    """Store memory blocks as local files in a folder."""

    def __init__(self, root: str = "coa_data"):
        self.root = root
        os.makedirs(self.root, exist_ok=True)

    def _path(self, key: str) -> str:
        return os.path.join(self.root, key)

    def write(self, key: str, data: bytes) -> str:
        path = self._path(key)
        with open(path, "wb") as f:
            f.write(data)
        return key  # content ID is just the key here

    def read(self, key: str) -> Optional[bytes]:
        path = self._path(key)
        if not os.path.exists(path):
            return None
        with open(path, "rb") as f:
            return f.read()

    def append(self, key: str, data: bytes) -> str:
        path = self._path(key)
        with open(path, "ab") as f:
            f.write(data)
        return key

    def burn(self, key: str) -> bool:
        path = self._path(key)
        if os.path.exists(path):
            os.remove(path)
            return True
        return False
