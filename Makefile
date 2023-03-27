install:
	pip install -r requirements.txt

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -type d -name .pytest_cache -exec rm -r {} \+

format:
	black src/
	isort src/

lint:
	flake8 --ignore=E501 src/

test:
	python -m pytest
