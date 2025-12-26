# QuantumMeasurementContradictionKit (QMCK)

Sandbox for the quantum measurement problem: toy experiments that keep the *observer-role contradiction* explicit without declaring a winner.

Interpretations included:
- **Copenhagen** (collapse on measurement)
- **Many-Worlds** (branching; no collapse)
- **Objective Collapse** (stochastic collapse with tunable strength)

Experiments included:
- Schrödinger Cat (macro entanglement + decoherence timeline)
- Wigner's Friend (nested observers; incompatible updates)
- Double Slit (which-path coupling vs interference visibility)

## Install (editable)
`powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -e .
``

## Run (CLI)

`powershell
qmck cat --interpretation many_worlds
qmck cat --interpretation copenhagen --seed 1
qmck cat --interpretation objective_collapse --collapse_strength 0.6 --seed 2

qmck wigner --interpretation copenhagen --seed 3
qmck double-slit --which_path 0.7 --seed 4
`

Outputs:

* Writes a run folder under uns/<timestamp>/
* Always emits uns/<timestamp>/report.json with parameters + results.

## Design principles

* Toy models: simple Hilbert spaces, explicit Born weights, explicit decoherence curves.
* Report-first: every run produces a machine-readable JSON artifact.
* Contradiction surfacing: experiments log where linear evolution + definite outcomes collide.
  "@

 = @"
param(
[string]$Interp = "many_worlds"
)
$ErrorActionPreference = "Stop"
if (!(Test-Path ".venv")) { python -m venv .venv }
..venv\Scripts\python -m pip install -U pip
..venv\Scripts\python -m pip install -e .
qmck cat --interpretation $Interp