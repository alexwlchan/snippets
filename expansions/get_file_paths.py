from collections.abc import Iterator
from pathlib import Path


def get_file_paths_under(
    root: Path | str = Path("."), *, suffix: str = ""
) -> Iterator[Path]:
    """
    Generates the absolute paths to every matching file under ``root``.
    """
    root = Path(root)

    if root.exists() and not root.is_dir():
        raise ValueError(f"Cannot find files under non-directory: {root!r}")

    if not root.is_dir():
        raise FileNotFoundError(root)

    for dirpath, _, filenames in root.walk():
        for f in filenames:
            p = dirpath / f

            if p.is_file() and f.lower().endswith(suffix):
                yield p


for p in get_file_paths_under():
    {cursor}
