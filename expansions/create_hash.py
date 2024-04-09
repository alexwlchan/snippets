import hashlib


def create_hash(path, *, algorithm=hashlib.sha256):
    """
    Returns the hex checksum of the given path.
    """
    h = algorithm()

    with open(path, "rb") as infile:
        while chunk := infile.read(8192):
            h.update(chunk)

    return h.hexdigest()
