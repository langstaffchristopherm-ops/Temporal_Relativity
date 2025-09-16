[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17137145.svg)](https://doi.org/10.5281/zenodo.17137145)


# Empirics Pack


## Makefile (optional)

```bash
make install   # create .venv and install dependencies
make all       # generate CSVs + figures
make clean     # remove data outputs
make clobber   # clean + remove figures
```


## Reproducible runs (timestamped)

Each script also writes into `runs/<UTC-stamp>/{data,figs}` so outputs never overwrite.

## Continuous Integration (GitHub Actions)

`.github/workflows/empirics.yml` runs the experiments on push/PR and uploads outputs as artifacts.


## Licensing
- **Code** (`src/`, `Makefile`, build scripts): MIT License (see `LICENSE`).
- **Manuscript & figures** (`hub.tex`, `format_macros.tex`, compiled PDF, `figs/` figure assets used in the paper):
  Creative Commons Attribution 4.0 (see `LICENSES/CC-BY-4.0.txt`).
- **Data** (`data/`): CC0 1.0 (Public Domain) unless otherwise noted
  (see `LICENSES/CC0-1.0.txt`). If a file cites third-party sources, its original
  terms apply; see headers or `data/README.md`.