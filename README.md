# QuantumMeasurementContradictionKit (QMCK)

Sandbox for the quantum measurement problem: small, deterministic toy experiments that preserve (not “solve”) the unitary-vs-outcome contradiction.

![CI](https://github.com/purpledancingfrogs/QuantumMeasurementContradictionKit/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## What it includes

Interpretations:
- Copenhagen (collapse postulate)
- Many-Worlds (unitary branching)
- Objective collapse (toy GRW-style knob)

Toy experiments:
- Double slit (interference vs which-path)
- Schrödinger’s cat (decoherence suppresses coherence)
- Wigner’s friend (nested observers; explicit contradiction flag)

## Install

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -e .
pip install pytest
pytest -q
````

Windows runners:

* quickstart.bat
* run.ps1 all

## Run

```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 all
```

Generate an example JSON report:

```bash
python examples/generate_sample_report.py
```

Output: examples/sample_report.json

## Contributing / roadmap

* CONTRIBUTING.md
* ROADMAP.md
  '@

python .\examples\generate_sample_report.py
python -m pytest -q
powershell -ExecutionPolicy Bypass -File .\run.ps1 all

git add -A
git commit -m "Project polish: docs, templates, README badges, sample report"
git push

git tag -a v0.1.12 -m "Project polish: docs/templates + sample report + README badges"
git push --tags
gh release create v0.1.12 --title "v0.1.12" --notes "Project polish: added community templates, CONTRIBUTING/ROADMAP/CHANGELOG, sample report generator + output, refreshed README with badges and usage."

```
::contentReference[oaicite:0]{index=0}
```
Start-Process "https://github.com/purpledancingfrogs/QuantumMeasurementContradictionKit/actions"
Start-Process "https://github.com/purpledancingfrogs/QuantumMeasurementContradictionKit/releases/tag/v0.1.12"
Start-Process "https://github.com/purpledancingfrogs/QuantumMeasurementContradictionKit"
# If CI is green, ask Grok for a rescored review using these exact bullets

$body = @'
Re-review QMCK at https://github.com/purpledancingfrogs/QuantumMeasurementContradictionKit (latest tag v0.1.12).

Changes since your 6.5/10 review:
- GitHub Actions CI added (pytest on 3.11–3.13) + badge in README
- Added CONTRIBUTING.md, ROADMAP.md, CHANGELOG.md, CODE_OF_CONDUCT.md
- Added issue templates + PR template
- Added examples/generate_sample_report.py and examples/sample_report.json (concrete JSON output)
- One-command local verification via run.ps1 all and quickstart.bat
- Audit artifacts: .asios/audit_index.json (sha256 manifest) + tracked files manifests

Score it again (1–10) focusing on: clarity, reproducibility, auditability, and “contradiction-preserving” originality.