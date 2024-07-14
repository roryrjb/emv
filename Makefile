install: lint
	python setup.py install --user

lint:
	ruff check emv/

format:
	black emv/