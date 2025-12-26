from __future__ import annotations

from dataclasses import dataclass
import math
import random

@dataclass(frozen=True)
class DoubleSlitResult:
    shots: int
    visibility: float
    which_path_info: float
    note: str

def run(shots: int = 2000, which_path: float = 0.0, seed: int = 0) -> DoubleSlitResult:
    """Toy double-slit: which_path in [0,1] reduces interference visibility."""
    rng = random.Random(seed)
    which_path = max(0.0, min(1.0, float(which_path)))

    visibility = math.sqrt(max(0.0, 1.0 - which_path**2))

    hits = 0
    for _ in range(int(shots)):
        phase = rng.random() * 2.0 * math.pi
        p = 0.5 * (1.0 + visibility * math.cos(phase))
        if rng.random() < p:
            hits += 1

    note = f"toy model: V≈{visibility:.3f}, D≈{which_path:.3f}, hits={hits}/{shots}"
    return DoubleSlitResult(shots=int(shots), visibility=float(visibility), which_path_info=float(which_path), note=note)