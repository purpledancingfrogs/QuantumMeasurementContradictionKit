# Reproducibility

## Determinism knobs
- All experiments accept a seed.
- Reports are written as JSON to runs/.
- Runtime strings are ASCII-only for Windows cp1252 compatibility.

## Quickstart
\\\ash
python scripts/quickstart.py
\\\

## Verify
\\\ash
python -m pytest -q
\\\

## Expected artifacts
Running a demo will create files under runs/ (ignored by git).