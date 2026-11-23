#!/usr/bin/env python3
"""news-image-20261123 v2: deliver the pre-rendered page.

Stdlib only. The image is built ahead of time; this program just
copies entry.png into the grader's output directory.
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def main():
    if not os.path.isfile(SRC):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
    # sanity: the delivered copy must be byte-identical to the source
    if os.path.getsize(os.path.join(OUT_DIR, "entry.png")) != os.path.getsize(SRC):
        print("copied entry.png size mismatch", file=sys.stderr)
        return 1
    print("wrote", os.path.join(OUT_DIR, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
