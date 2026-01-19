.PHONY: install run test clean

VENV_NAME := venv
PYTHON := $(VENV_NAME)/bin/python
PIP := $(VENV_NAME)/bin/pip

install:
	python3 -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	@# Checks if venv exists, if not warns user
	@[ -d $(VENV_NAME) ] || (echo "Virtualenv not found. Run 'make install' first." && exit 1)
	$(PYTHON) main.py

test:
	@[ -d $(VENV_NAME) ] || (echo "Virtualenv not found. Run 'make install' first." && exit 1)
	$(PYTHON) -m pytest tests/

clean:
	rm -rf $(VENV_NAME)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +