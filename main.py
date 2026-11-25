#!/usr/bin/env python3
"""Entry program for Fortune in a Pot.

Writes one fortune (at most 120 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
a kind, funny fortune for a houseplant. The plant will be
admired, watered by a guilty owner, and moved six inches
toward destiny.
"""

import os

LINE = (
    "You will outlive three of your owner's resolutions, "
    "be watered with renewed commitment, and get the big "
    "window."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
