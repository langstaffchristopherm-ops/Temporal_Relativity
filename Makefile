
PY ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python
.DEFAULT_GOAL := help
.PHONY: help venv install deps all data figs metric weakfield thermal clean clobber
help:
	@echo "Targets: venv install deps all data figs metric weakfield thermal clean clobber"
venv:
	$(PY) -m venv $(VENV)
install: venv
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt
deps:
	$(PIP) install -U -r requirements.txt
all: data figs
data: metric weakfield thermal
figs: metric weakfield thermal
metric:
	$(PYTHON) src/metric_rates.py
weakfield:
	$(PYTHON) src/weakfield_run.py
thermal:
	$(PYTHON) src/thermal_consistency.py
clean:
	rm -f data/*.csv data/run_summary.json
clobber: clean
	rm -f figs/*.png
