#!/usr/bin/env python3
"""
bump.py — update everything with TWO args: DOI and VERSION.

Usage:
  py -3 bump.py 10.5281/zenodo.NNNNNNN vX.Y.Z

What it updates (in the current folder):
  1) release.tex      — writes \RepoDOI, \RepoCommit (auto), \PaperVersion, \PaperLicense
  2) CITATION.cff     — sets doi:, version:, commit: (if file exists)
  3) README.md        — rewrites Zenodo DOI links (if file exists)
Then rebuild your PDF as you normally do (e.g., latexmk -C && latexmk -pdf hub.tex)
"""

import sys, re, subprocess
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: py -3 bump.py 10.5281/zenodo.NNNNNNN vX.Y.Z")
    sys.exit(1)

DOI, VERSION = sys.argv[1], sys.argv[2]
ROOT = Path(".").resolve()

DOI_RE       = re.compile(r"10\.5281/zenodo\.\d+")
DOI_LINK_RE  = re.compile(r"https?://doi\.org/10\.5281/zenodo\.\d+", re.I)

def ghash():
    try:
        out = subprocess.check_output(["git","rev-parse","--short","HEAD"], stderr=subprocess.DEVNULL)
        return out.decode().strip()
    except Exception:
        return "UNKNOWN"

def read(p):
    try:
        return Path(p).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def write_atomic(p, s):
    p = Path(p); tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(s, encoding="utf-8"); tmp.replace(p)

# 1) release.tex (single source of truth used by LaTeX)
commit = ghash()
license_text = "CC BY 4.0"
old_release = read("release.tex")
m = re.search(r"\\newcommand\{\\PaperLicense\}\{([^}]*)\}", old_release)
if m: license_text = m.group(1).strip()
release_body = (
    f"\\newcommand{{\\RepoDOI}}{{{DOI}}}\n"
    f"\\newcommand{{\\RepoCommit}}{{{commit}}}\n"
    f"\\newcommand{{\\PaperVersion}}{{{VERSION}}}\n"
    f"\\newcommand{{\\PaperLicense}}{{{license_text}}}\n"
)
write_atomic("release.tex", release_body)
print(f"[release.tex] DOI={DOI}  VERSION={VERSION}  COMMIT={commit}  LICENSE={license_text}")

# 2) CITATION.cff (if present)
cff = Path("CITATION.cff")
if cff.exists():
    txt = read(cff)
    # doi
    if 'doi:' in txt:
        txt = re.sub(r"(?m)^(doi:\s*).*$", r"\g<1>"+DOI, txt)
    else:
        txt = txt.rstrip() + f"\ndoi: {DOI}\n"
    # version
    if re.search(r"(?m)^version:\s*.*$", txt):
        txt = re.sub(r"(?m)^(version:\s*).*$", r"\g<1>"+VERSION, txt)
    else:
        txt = txt.rstrip() + f"\nversion: {VERSION}\n"
    # commit
    if re.search(r"(?m)^commit:\s*.*$", txt):
        txt = re.sub(r"(?m)^(commit:\s*).*$", r"\g<1>"+commit, txt)
    else:
        txt = txt.rstrip() + f"\ncommit: {commit}\n"
    write_atomic(cff, txt)
    print("[CITATION.cff] updated")
else:
    print("[CITATION.cff] not found — skipped")

# 3) README.md (if present)
rd = Path("README.md")
if rd.exists():
    t = read(rd)
    new = DOI_RE.sub(DOI, t)
    new = DOI_LINK_RE.sub(f"https://doi.org/{DOI}", new)
    if new != t:
        write_atomic(rd, new)
        print("[README.md] DOI links updated")
    else:
        print("[README.md] no DOI occurrences — skipped")
else:
    print("[README.md] not found — skipped")

print("\nDone. Now rebuild your PDF (example):  latexmk -C && latexmk -pdf hub.tex")
