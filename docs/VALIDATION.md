# Validation (QMCK)

This repository is validated by:

1) **Unit tests**
- Run: python -m pytest -q

2) **Deterministic sample artifact**
- File: uns/sample_seed123.json
- Hash recorded in: docs/EXPECTED_OUTPUTS.md

3) **Build integrity**
- Build: python -m build
- Verify: python -m twine check dist/*

4) **CI matrix**
- GitHub Actions runs pytest on Windows/macOS/Linux for Python 3.11–3.13.

Notes:
- If you change parameters or algorithms, deterministic artifacts may change; regenerate the sample and update the recorded sha256.