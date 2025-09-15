[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17119050.svg)](https://doi.org/10.5281/zenodo.17119050)


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
