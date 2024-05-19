#!/usr/bin/env python3

import hashlib
import json
import os
import pathlib
import subprocess
import uuid
import zipfile


def read(name: str) -> str:
    with open(os.path.join("expansions", name)) as infile:
        return infile.read()


# fmt: off
SNIPPETS = {
    "!bq": "<blockquote>{clipboard}</blockquote>",

    # =========================
    # Get the current date/time
    # =========================

    # pretty, e.g. 9 April 2024
    ";dp": "{isodate:d MMMM yyyy}",

    # short, e.g. 2024-04-09
    ";ds": "{isodate:yyyy-MM-dd}",

    # e.g. 2024-04-09 10:49:12 +0100
    ";dd": "{isodate:yyyy-MM-dd HH:mm:ss Z}",

    # =========================
    # English words and phrases
    # =========================
    "a11e": "accessible",
    "a11y": "accessibility",
    "acc't": "account",
    "Acc't": "Account",
    "acct": "account",
    "Acct": "Account",
    "afaict": "as far as I can tell",
    "atm": "at the moment",
    "avg": "average",
    "bdy": "boundary",
    "Bdy": "Boundary",
    "bdies": "boundaries",
    "Bdies": "Boundaries",
    "cafe": "café",
    "cliche": "cliché",
    "ctd": "continued",
    " cts": " continuous",
    "Das Ubermensch": "Das Übermensch",
    "defn": "definition",
    "deja vu": "déjà vu",
    "dept.": "department",
    "distn": "distribution",
    "eqn": "equation",
    "expt": "experiment",
    "fdn": "foundation",
    "Fdn": "Foundation",
    "fiance": "fiancé",
    "fn": "function",
    "gdn": "garden",
    "Gdn": "Garden",
    "gov't": "government",
    "govt": "government",
    "i14n": "intersectional",
    "i18n": "internationalisation",
    " iff": " if and only if",
    "ina11e": "inaccessible",
    "indpt": "independent",
    "intl.": "international",
    "iptic": "in particular",
    "Iptic": "In particular",
    "l12n": "localisation",
    "lmk": "let me know",
    "mgmt": "management",
    "mgr": "manager",
    "Mgr": "Manager",
    "naive": "naïve",
    "natl.": "national",
    "nbhd": "neighbourhood",
    "nee ": "née ",
    "o/w": "otherwise",
    "ofc": "of course",
    " ptic": " particular",
    "rec'd": "recommended",
    "reln": "relation",
    "reqd": "required",
    "s.t.": "such that",
    "soln": "solution",
    "spose": "suppose",
    "stdlib": "standard library",
    "thm": "theorem",
    "w/b": "week beginning",
    "w/e": "week ending",
    "w/o": "without",
    "y'day": "yesterday",

    # =============================
    # Fix my common typing mistakes
    # =============================
    "cunt": "count",
    "EVentbridge": "EventBridge",
    "Flcikr": "Flickr",
    " ot ": " to ",
    "thier": "their",
    "WHy": "Why",

    # ============
    # Proper nouns
    # ============
    "Agnes": "Agnès",
    "B'ham": "Birmingham",
    "BackBlaze": "Backblaze",
    "Bezier": "Bézier",
    "Borrowbox": "BorrowBox",
    "CF": "CloudFront",
    "CO2": "CO₂",
    "China Mieville": "China Miéville",
    "Cloudwatch": "CloudWatch",
    "Ebay": "eBay",
    "El Otro Periodico": "El Otro Periódico",
    "Elasticache": "ElastiCache",
    "Eventbridge": "EventBridge",
    "Facetime": "FaceTime",
    "FastMail": "Fastmail",
    "Gitbook": "GitBook",
    "Hashicorp": "HashiCorp",
    "Maciej Ceglowski": "Maciej Cegłowski",
    "Paypal": "PayPal",
    "Phylopic": "PhyloPic",
    "Postgresql": "PostgreSQL",
    "Powerpoint": "PowerPoint",
    "Raphaelle": "Raphaëlle",
    "Regents Canal": "Regent’s Canal",
    "Rubocop": "RuboCop",
    "Sqlite": "SQLite",
    "SQlite": "SQLite",
    "Sean": "Seán",
    "Sharepoint": "SharePoint",
    "Skoda": "Škoda",
    "Smugmug": "SmugMug",
    "Taf": "Tâf",
    "Textexpander": "TextExpander",
    "Whatsapp": "WhatsApp",
    "WikiData": "Wikidata",
    "Wordpress": "WordPress",
    "Youtube": "YouTube",
    "Zoe": "Zoë",
    "bhalaj": "bhålaj",
    " ldn": " london",
    "wall-e": "WALL·E",

    # =================================
    # Symbols and other bits of Unicode
    # =================================
    "180^": "180°",
    "^C": "°C",
    "^F": "°F",
    "^deg": "°",
    "^ft": "′",
    "^in": "″",
    ":+1:": "👍",
    ":wave:": "👋",
    ";1/2": "½",
    ";3/4": "¾",
    ";alt": "⌥",
    ";approx": "≈",
    ";bullet": "•",
    ";cmd": "⌘",
    ";ctrl": "⌃",
    ";dot": "·",
    ";eur": "€",
    ";minus": "−",
    ";opt": "⌥",
    ";pi": "π",
    ";pm": "±",
    ";sec": "§",
    ";shift": "⇧",
    ";sqrt": "√",
    ";times": "×",
    ";tm": "™",
    ";zwsp": "\u200b",  # zero-width space

    # =============
    # Personal info
    # =============
    "@aa": "@alexwlchan.net",
    ";ee": "alex@alexwlchan.net",

    ";ale": "alexwlchan",

    # ====================
    # Programming snippets
    # ====================
    "!bash": "#!/usr/bin/env bash\n\nset -o errexit\nset -o nounset\n",
    "!osa": "#!/usr/bin/env osascript\n",
    "!py": "#!/usr/bin/env python3\n\n",
    "!rb": "#!/usr/bin/env ruby\n",
    "!swift": "#!/usr/bin/env swift\n",

    "!rect": '<rect width="500" height="250" fill="yellow"/>',
    "!svg": read("template.svg"),

    "!before": read("before_and_after.html"),
    "!html": read("empty_page.html"),

    "!mit": read("mit_license.txt"),

    # Git trailer
    # See https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors
    ";co": "Co-authored-by:",

    # ===================================
    # Python-related programming snippets
    # ===================================
    "!dt": "import datetime\n",
    "!j": "import json\n",
    "!pp": "from pprint import pprint; pprint({cursor})",

    "@param": "@pytest.mark.parametrize({cursor})",

    "!flapi": read("flapi.py"),

    "py!aws": read("get_boto3_session.py"),
    "py!dy": read("list_dynamodb_rows.py"),
    "py!h": read("create_hash.py"),
    "py!de": read("datetime_encoder.py"),
    "py!pth": read("get_file_paths.py"),
    "py!pd": read("get_directories.py"),
    "py!sec": read("get_secrets_manager_secret.py"),
    "py!s3": read("list_s3_objects.py"),

    # I can never remember the order of args to this function,
    # so when I start typing it, add a comment to help me out.
    "datetime.datetime.strp": "datetime.datetime.strptime({cursor})  # date_string, format",

    # =================
    # Obsidian snippets
    # =================
    ";nd": read("note_header.txt"),

    # ============
    # Misc phrases
    # ============
    "porque?": "¿Por qué no los dos?",
}
# fmt: on


def add_snippet(zf: zipfile.ZipFile, shortcut: str, expansion: str) -> None:
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

    with zipfile.ZipFile("Alex’s snippets.alfredsnippets", "w") as zf:
        zf.write("info.plist")

        for shortcut, expansion in SNIPPETS.items():
            add_snippet(zf, shortcut, expansion)

    subprocess.check_call(["open", "Alex’s snippets.alfredsnippets"])
