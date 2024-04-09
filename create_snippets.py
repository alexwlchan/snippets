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


if __name__ == "__main__":
    curdir = pathlib.Path(os.getcwd()).absolute()

    with zipfile.ZipFile(f"Alex’s snippets.alfredsnippets", "w") as zf:
        zf.write("info.plist")

        for shortcut, expansion in SNIPPETS.items():
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

    subprocess.check_call(["open", "Alex’s snippets.alfredsnippets"])
