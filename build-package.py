#!/usr/bin/env python3
"""Builds adenium-data-<version>.zip from this folder, reproducibly (sorted entries, fixed timestamps, no extra attributes),
and prints its size and SHA-256 for data-package.json in the Adenium repository.

Usage: python3 build-package.py <version> [output-dir]
The zip holds DataFiles/, Icons/ and Maps/ (unpack it over Adenium's data/ folder) and DATA-README.md (this folder's README)."""
import hashlib, os, sys, zipfile

if len(sys.argv) < 2:
    sys.exit(__doc__)
version = sys.argv[1]
out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Adenium-data-dist")
root = os.path.dirname(os.path.abspath(__file__))
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, f"adenium-data-{version}.zip")

entries = [("README.md", "DATA-README.md")]
for folder in ("DataFiles", "Icons", "Maps"):
    for dirpath, dirs, files in os.walk(os.path.join(root, folder)):
        dirs.sort()
        for name in sorted(files):
            full = os.path.join(dirpath, name)
            entries.append((os.path.relpath(full, root), os.path.relpath(full, root)))
entries.sort(key=lambda e: e[1])

with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for source, arcname in entries:
        info = zipfile.ZipInfo(arcname.replace(os.sep, "/"), date_time=(2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        with open(os.path.join(root, source), "rb") as f:
            z.writestr(info, f.read(), zipfile.ZIP_DEFLATED, 9)

digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
print(f"{path}\n{len(entries)} files, {os.path.getsize(path)} bytes\nsha256 {digest}")
