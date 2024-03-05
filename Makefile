.PHONY: run

run:
    poetry run python app.py


.PHONY: venv

venv:
    conda activate sudokuvenv