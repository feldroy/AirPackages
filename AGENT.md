# AGENT.md - AirPackages Development Guide

## Commands
- Run server with reload: `uv run fastapi dev main.py --reload`
    - Note: Normally I have this running in a separate terminal, so you can assume this is already running in the background.
- Test all: `pytest` or `make test`
- Test single: `pytest tests/test_specific.py::test_function`
- QA (lint/format/types): `make qa` or `uv run --extra test ruff check . --fix && ruff format . && ty check .`
- Debug tests: `make pdb` (uses IPython debugger)
- Coverage: `make coverage`
- Build PyPI package: `uv build`

## Architecture
- Air web framework app in `src/AirPackages/__main__.py` - directory of Air packages/examples
- CLI tool via Typer in `cli.py` 
- Python package using uv for dependency management
- Serves a simple web directory at `/` listing Air ecosystem packages

## Code Style
- Line length: 120 characters (ruff)
- Use Ruff for linting/formatting with pycodestyle, Pyflakes, isort, flake8-bugbear, pyupgrade
- Type checking with `ty` tool
- Import order: standard library, third-party, local imports
- Use Air framework patterns: `air.H1()`, `air.P()`, `air.layouts.mvpcss()`
- Dependencies: air[standard], typer, uvicorn for serving
