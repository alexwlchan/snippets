#!/usr/bin/env python3

import hashlib
import json
import os
import pathlib
import subprocess
import uuid
import zipfile


# fmt: off
SNIPPETS = {
    # =========================
    # English words and phrases
    # =========================
    "ina11e": "inaccessible",

    # =============
    # Personal info
    # =============
    "@aa": "@alexwlchan.net",
    ";ee": "alex@alexwlchan.net",

    ";ale": "alexwlchan",

    # =================================
    # Programming: shebangs for scripts
    # =================================
    "!bash": "#!/usr/bin/env bash\n\nset -o errexit\nset -o nounset\n",
    "!osa": "#!/usr/bin/env osascript\n",
    "!py": "#!/usr/bin/env python3\n\n",
    "!rb": "#!/usr/bin/env ruby\n",
    "!swift": "#!/usr/bin/env swift\n",
}
# fmt: on



# fmt: off
LONGER_SNIPPETS = {
    # ==============================
    # Programming: fragments of code
    # ==============================
    "!flapi": "flapi.py",
}
# fmt: on


def add_snippet(zf: zipfile.ZipFile, shortcut: str, expansion: str):
    """
    Add a single snippet to a snippets bundle.
    """
    h = hashlib.md5()
    h.update(shortcut.encode("utf8"))
    h.update(expansion.encode("utf8"))

    snippet_id = uuid.UUID(hex=h.hexdigest())

    snippet_data = {
        "alfredsnippet": {
            "snippet": expansion,
            "uid": str(snippet_id),
            "name": "",
            "keyword": shortcut,
        }
    }

    zf.writestr(f"{snippet_id}.json", data=json.dumps(snippet_data))



if __name__ == "__main__":
    curdir = pathlib.Path(os.getcwd()).absolute()

    with zipfile.ZipFile(f"Alex’s snippets.alfredsnippets", "w") as zf:
        zf.write("info.plist")

        for shortcut, expansion in SNIPPETS.items():
            add_snippet(zf, shortcut, expansion)

        for shortcut, filename in LONGER_SNIPPETS.items():
            with open(pathlib.Path("expansions") / filename) as f:
                expansion = f.read()

            add_snippet(zf, shortcut, expansion)

    subprocess.check_call(["open", "Alex’s snippets.alfredsnippets"])
