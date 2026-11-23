#!/usr/bin/env python3
"""news-image-20261123 entrypoint: copy entry.png to the output dir.

Stdlib only. The grader runs this in a fresh container with no
network and a read-only repo, so the entry image ships in the repo
and is copied verbatim to $MAKEFUN_OUTPUT_DIR/entry.png.
A plain byte copy is deterministic: run twice, same output bytes.
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not os.path.isfile(SRC):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
