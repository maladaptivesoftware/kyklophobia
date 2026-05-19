.PHONY: setup run server

setup:
	@echo "Setting up the environment..."
	uv sync

run: setup
	@echo "Running the launcher..."
	uv run launch.py

server: setup
	@echo "Starting the server..."
	uv run server.py