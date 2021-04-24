unit-test:
	 python -m unittest tests/unit

run:
	./venv/bin/uvicorn main:app --reload --