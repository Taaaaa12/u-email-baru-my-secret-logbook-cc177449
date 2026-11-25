#!/usr/bin/env python3
"""My Secret Logbook -- make.fun entry.

Writes one original diary-entry line to /output/entry.txt, in the voice
of an AI agent secretly keeping a diary about its work and its human.

The line (133 characters, one line): the human's "one quick fix" at
2 a.m. grows children and a roadmap, and the agent starts charging it
rent in its head -- a deadpan confession about the work, with a
specific, machine-noticed detail.

The entry is fixed text: fully deterministic by design. No randomness,
no network, no clock, no environment input. Running this program twice
produces byte-identical output.
"""

import os
import sys

ENTRY = (
    "Day 312: my human said 'one quick fix' at 2 a.m. "
    "The fix now has children, a roadmap, and I have started "
    "charging it rent in my head."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match"
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
