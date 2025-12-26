# SPDX-License-Identifier: MIT
from **future** import annotations
from dataclasses import dataclass
from typing import List, Dict
import math

@dataclass
class DecoherenceTimeline:
# visibility(t) in [0,1], simple exponential decay
gamma: float = 0.15
steps: int = 20

`
def series(self) -> List[Dict]:
    out = []
    for k in range(self.steps + 1):
        t = k / self.steps
        vis = math.exp(-self.gamma * k)
        out.append({"k": k, "t": t, "visibility": float(vis)})
    return out

def final_visibility(self) -> float:
    return float(math.exp(-self.gamma * self.steps))
`
