install: lint
	python3 setup.py install --user

lint:
	ruff check emv/

format:
	black emv/