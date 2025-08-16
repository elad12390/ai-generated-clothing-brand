# Makefile for AI Generated Clothing Brand project

# Variables
PYTHON = python
PIP = pip
TEST_DIR = src/backend/tests
SRC_DIR = src/backend

# Default target
.PHONY: help
help:
	@echo "AI Generated Clothing Brand - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install     Install dependencies"
	@echo "  test        Run all tests"
	@echo "  test-cov    Run tests with coverage"
	@echo "  run         Run the main application"
	@echo "  clean       Clean up temporary files"
	@echo "  help        Show this help message"

# Install dependencies
.PHONY: install
install:
	uv pip install -r requirements.txt

# Run tests
.PHONY: test
test:
	$(PYTHON) -m pytest $(TEST_DIR) -v

# Run tests with coverage
.PHONY: test-cov
test-cov:
	$(PYTHON) -m pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=html --cov-report=term

# Run the main application
.PHONY: run
run:
	$(PYTHON) $(SRC_DIR)/main.py

# Clean up temporary files
.PHONY: clean
clean:
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Setup development environment
.PHONY: setup
setup:
	uv venv
	source .venv/bin/activate && uv pip install -r requirements.txt