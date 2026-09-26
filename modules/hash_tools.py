import hashlib
from pathlib import Path

def hash_file(path, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return {"file": str(path), "algorithm": algorithm, "digest": h.hexdigest()}
