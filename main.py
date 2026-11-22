#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a small, quiet mystery: a room, a letter, and a reader
who has not opened it yet. It is written to make its reader curious,
not to tell them how to feel.
"""

import os

ENTRY_TEXT = (
    "There is a room you have never entered. It has one window, "
    "one chair, and a letter on the table. The letter is addressed "
    "to you, in handwriting you almost recognize. It is a single "
    "sentence. You have not read it yet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
