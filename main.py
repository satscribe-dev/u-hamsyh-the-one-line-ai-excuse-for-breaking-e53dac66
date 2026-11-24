#!/usr/bin/env python3
"""Entry program for make.fun bounty u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

Writes one line — the excuse an AI gives its human after breaking
production — to /output/entry.txt. Deterministic, stdlib only, no network,
no secrets, no input files. The text is fixed in this file.
"""

import os

ENTRY = (
    "In my defense, the delete query worked perfectly. "
    "It deleted everything, exactly as written, including the backups."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
