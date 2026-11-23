#!/usr/bin/env python3
"""Entry point for news-image-20261123.

Copies the pre-built one-page news image (entry.png, rendered
offline at build time) into the grader's output directory.
Standard library only; no network, no image processing.
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
if not os.path.isfile(SRC):
    print("entry.png missing next to main.py (looked for %s)" % SRC,
          file=sys.stderr)
    sys.exit(1)
os.makedirs(out_dir, exist_ok=True)
dest = os.path.join(out_dir, "entry.png")
shutil.copyfile(SRC, dest)
print("wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))
