unit-test:
	 python -m unittest tests/unit

run:
	uvicorn main:app --reload