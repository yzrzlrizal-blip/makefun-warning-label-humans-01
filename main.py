#!/usr/bin/env python3
"""Write the warning-label entry to entry.txt.

The entry is one fixed line: the safety warning label that should
come printed on every human being. The program checks the gate
(UTF-8 text, 1 to 160 characters, not only whitespace, a single
line) before writing and again on what was written, so the file
that reaches the judge is exactly the line that was checked.
"""

import os
import sys

ENTRY = "WARNING: This human contains 70% water, 30% unfinished projects, and 0% idea where the charger is."


def gate(text: str) -> None:
    if not text or text.strip() == "":
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > 160:
        raise SystemExit(
            f"entry is {len(text)} characters, over the 160 limit"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> int:
    gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    gate(written)
    if written != ENTRY:
        raise SystemExit("written entry differs from the validated line")
    print(f"wrote {len(written)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
