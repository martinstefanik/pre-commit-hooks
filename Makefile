PACKAGE := pchooks

.PHONY: build clean test

build:
	@poetry build

clean:
	@rm -rf builds dist .coverage .mypy_cache .pytest_cache .tox

test:
	@rm -rf .pytest_cache
	@if [ -d tests ] && [ "$$(find tests -name 'test_*.py')" ]; then \
	 	poetry run python -m pytest --cov=$(PACKAGE) --cov-report=html tests; \
	 else \
		echo "No tests are currently implemented!"; \
	 fi
