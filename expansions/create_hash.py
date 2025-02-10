import hashlib
from pathlib import Path


def create_hash(path: Path) -> "hashlib._Hash":
    """
    Returns the checksum of the given path.
    """
    h = hashlib.sha256()

    with open(path, "rb") as infile:
        while chunk := infile.read(8192):
            h.update(chunk)

    return h
