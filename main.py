#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single deadpan excuse from a robot vacuum for missing a spot
to /output/entry.txt.
"""

import os
import shutil

MAX_CHARS = 200

LINE = "I left the crumbs under the sofa because my sensors logged them as load-bearing, and demolishing the living room is above my pay grade."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-200 non-blank chars"

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
