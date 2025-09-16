#!/usr/bin/env python3
import sys, re
from pathlib import Path

if len(sys.argv) not in (2,4):
    print("Usage:")
    print("  set_release.py 10.5281/zenodo.NNNNNNN")
    print("  set_release.py 10.5281/zenodo.NNNNNNN vX.Y.Z COMMIT")
    sys.exit(1)

doi = sys.argv[1]
version = sys.argv[2] if len(sys.argv) >= 3 else None
commit = sys.argv[3] if len(sys.argv) >= 4 else None

root = Path(__file__).resolve().parents[1]

# 1) bump release.tex
rel = root / "release.tex"
content = rel.read_text(encoding="utf-8", errors="ignore") if rel.exists() else ""
def set_macro(txt, name, value):
    import re
    pat = re.compile(r"\\newcommand\{\\" + name + r"\}\{[^}]*\}")
    if pat.search(txt):
        return pat.sub(r"\\newcommand{\\%s}{%s}" % (name, value), txt)
    else:
        return txt + "\n\\newcommand{\\%s}{%s}\n" % (name, value)

if not rel.exists():
    content = ""
content = set_macro(content, "RepoDOI", doi)
if version: content = set_macro(content, "PaperVersion", version)
if commit:  content = set_macro(content, "RepoCommit", commit)
rel.write_text(content, encoding="utf-8")

# 2) sync CITATION.cff and README.md
cff = root / "CITATION.cff"
if cff.exists():
    txt = cff.read_text(encoding="utf-8", errors="ignore")
    # doi
    if "doi:" in txt:
        txt = re.sub(r"(?m)^(doi:\s*)10\.5281/zenodo\.\d+\s*$", r"\g<1>%s" % doi, txt)
        if not re.search(r"(?m)^doi:\s*10\.5281/zenodo\.\d+\s*$", txt):
            txt += "\ndoi: %s\n" % doi
    else:
        txt += "\ndoi: %s\n" % doi
    # version
    if version:
        if re.search(r"(?m)^version:\s*.+$", txt):
            txt = re.sub(r"(?m)^version:\s*.+$", "version: %s" % version, txt)
        else:
            txt += "\nversion: %s\n" % version
    # commit
    if commit:
        if re.search(r"(?m)^commit:\s*.+$", txt):
            txt = re.sub(r"(?m)^commit:\s*.+$", "commit: %s" % commit, txt)
        else:
            txt += "\ncommit: %s\n" % commit
    cff.write_text(txt, encoding="utf-8")

readme = root / "README.md"
if readme.exists():
    txt = readme.read_text(encoding="utf-8", errors="ignore")
    txt = re.sub(r"10\.5281/zenodo\.\d+", doi, txt)
    txt = re.sub(r"https?://doi\.org/10\.5281/zenodo\.\d+", "https://doi.org/%s" % doi, txt)
    readme.write_text(txt, encoding="utf-8")

print("Updated release.tex, CITATION.cff, and README.md to DOI=%s%s%s." % (doi, (" version="+version) if version else "", (" commit="+commit) if commit else ""))
