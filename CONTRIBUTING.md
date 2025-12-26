# Contributing

QMCK is a contradiction-focused sandbox for the quantum measurement problem.

Core rule:
- preserve the contradiction; do not “solve” it inside the toolkit

## Dev setup
- python -m venv .venv
- .\.venv\Scripts\Activate.ps1
- pip install -e .
- pip install pytest
- pytest -q

## Add an experiment
- src/qmck/experiments/<name>.py
- provide run(...) returning a dataclass/dict with:
  - parameters used
  - result metrics
  - contradiction_flag (bool) when applicable
  - short note string
- add tests under tests/

## Quality bar
- deterministic with seeds
- pytest green
- no placeholders/stubs