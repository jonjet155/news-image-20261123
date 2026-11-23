"""news-image-20261123 entrypoint: copy the pre-built image to the output dir.

Stdlib only. The image is rendered at build time by build.py; this program
just places it where the grader expects it.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not os.path.isfile(SRC):
        print("entry.png is missing next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Sanity: the grader re-runs this program, so the copy must be exact.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        print("copied entry.png size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
