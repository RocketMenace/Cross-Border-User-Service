

.PHONY: help run format check

help:
	@echo "Available commands:"
	@echo "  up                   - Start all containers in detached mode"
	@echo "  run                  - Run FastAPI application locally"
	@echo "  format               - Run ruff format command"
	@echo "  check                - Run ruff check command"

run:
	uvicorn app.main:app --reload --loop uvloop --http httptools

format:
	ruff format .
	isort .

check:
	ruff check --fix .