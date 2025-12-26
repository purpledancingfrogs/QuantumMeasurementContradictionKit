# SPDX-License-Identifier: MIT
from **future** import annotations
from typing import Dict, Optional
from ..core.state import TwoStateSystem
from ..utils import rng

def measure(system: TwoStateSystem, seed: Optional[int] = None, forced_outcome: Optional[int] = None) -> Dict:
p0, p1 = system.probs()
r = rng(seed)
if forced_outcome is None:
x = r.random()
outcome = 0 if x < p0 else 1
else:
outcome = int(forced_outcome)
pre = system.as_dict()
system.collapse_to(outcome)
post = system.as_dict()
return {
"interpretation": "copenhagen",
"pre": pre,
"outcome": outcome,
"post": post,
"born": {"p0": p0, "p1": p1},
}