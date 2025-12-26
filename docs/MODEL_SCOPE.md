# Model scope (QMCK)

QMCK is a **toy-model** sandbox for exploring the **quantum measurement problem**.
It is designed to preserve and expose the contradiction between:

- **Unitary evolution** (linear Schrödinger dynamics)
- **Definite outcomes** (measurement postulates / observer reports)

QMCK is **not** a high-precision quantum dynamics solver and is **not** intended for hardware control, quantum computing workloads, or experimental prediction.

Included interpretations implement simplified rulesets:
- Copenhagen: explicit collapse rule
- Many-Worlds: branching records without collapse
- Objective collapse: stochastic collapse with tunable parameters (GRW-like)

Outputs are JSON and designed for reproducibility and audit.