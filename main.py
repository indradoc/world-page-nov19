# SPDX-License-Identifier: MIT
"""Copy the 19 Nov 2026 world-news digest image to /output/entry.png."""
import os, shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
shutil.copyfile(src, os.path.join(OUTPUT_DIR, "entry.png"))
print("wrote entry.png")
