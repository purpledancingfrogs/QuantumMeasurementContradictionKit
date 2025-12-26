from **future** import annotations
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class TwoStateSystem:
# basis: |0>, |1>
a0: complex
a1: complex
label0: str = "0"
label1: str = "1"

`
def norm(self) -> float:
    return float((self.a0.conjugate()*self.a0 + self.a1.conjugate()*self.a1).real)

def probs(self) -> Tuple[float, float]:
    n = self.norm()
    if n <= 0:
        return (0.0, 0.0)
    p0 = float((self.a0.conjugate()*self.a0).real / n)
    p1 = float((self.a1.conjugate()*self.a1).real / n)
    return (p0, p1)

def as_dict(self) -> Dict:
    p0, p1 = self.probs()
    return {
        "basis": [self.label0, self.label1],
        "amplitudes": {"a0": [self.a0.real, self.a0.imag], "a1": [self.a1.real, self.a1.imag]},
        "probs": {"p0": p0, "p1": p1},
    }

def collapse_to(self, outcome: int) -> None:
    if outcome == 0:
        self.a0, self.a1 = (1+0j), 0j
    else:
        self.a0, self.a1 = 0j, (1+0j)
`
