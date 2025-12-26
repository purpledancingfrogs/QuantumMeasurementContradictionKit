# SPDX-License-Identifier: MIT
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class CatResult:
    alive_prob: float
    dead_prob: float
    coherence: float
    note: str

def run(decoherence: float = 0.2) -> CatResult:
    """Toy cat: decoherence in [0,1] suppresses coherence between |alive> and |dead|."""
    d = max(0.0, min(1.0, float(decoherence)))

    alive = 0.5
    dead = 0.5
    coherence = max(0.0, 1.0 - d)

    note = f"toy cat: P(alive)=0.5, P(dead)=0.5, coherence~={coherence:.3f}"
    return CatResult(alive_prob=alive, dead_prob=dead, coherence=coherence, note=note)