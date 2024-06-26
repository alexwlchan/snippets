import pathlib


def get_directories_under(root="."):
    """
    Generates the absolute paths to every directory under ``root``.
    """
    root = pathlib.Path(root)

    if root.exists() and not root.is_dir():
        raise ValueError(f"Cannot find files under file: {root!r}")

    if not root.is_dir():
        raise FileNotFoundError(root)

    for dirpath, _, _ in root.walk():
        yield dirpath


for p in get_directories_under():
    {cursor}
