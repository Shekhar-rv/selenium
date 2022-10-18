VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip3

create_virtual_env:
	@echo Creating the virtual directory: $(VENV)
	rm -rf $(VENV)
	python3 -m venv $(VENV)

install_dependencies:
	@echo Upgrading pip and installing 3rd party python dependencies
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check_py:
	@echo Checking the Python and Pip versions in virtual environment
	$(PYTHON) --version
	$(PIP) --version

init: create_virtual_env install_dependencies check_py

run_main:
	$(PYTHON) main.py
