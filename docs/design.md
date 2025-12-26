# Design: contradiction-preserving sandbox

QMCK is intentionally not a "solver" for the measurement problem.

## Invariants
- Preserve unitary evolution where applicable (no hidden collapse).
- When a model assumes definite outcomes (collapse, friend’s record, etc.), record that assumption explicitly.
- Emit a contradiction flag when two consistent descriptions cannot both be true under shared assumptions.

## What "contradiction_flag" means (toy Wigner's friend)
- Friend assigns: definite outcome (collapsed record)
- Wigner assigns: unitary superposition for the joint system
- If both are asserted as simultaneously valid descriptions of the same event, the toolkit flags the mismatch.

## Scope
Toy models by design:
- small state spaces
- parameterized knobs (decoherence, which-path info, collapse strength)
- reproducible seeds + JSON outputs for auditability