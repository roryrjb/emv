install: lint
	python setup.py install --user

lint:
	ruff check emv/

format:
	black emv/

exe:
	python setup.py build_exe