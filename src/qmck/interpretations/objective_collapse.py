from **future** import annotations
from typing import Dict, Optional
from ..core.state import TwoStateSystem
from ..utils import rng

def objective_collapse(system: TwoStateSystem, collapse_strength: float = 0.5, seed: Optional[int] = None) -> Dict:
# collapse_strength in [0,1] acts like a probability of triggering collapse at measurement
cs = float(max(0.0, min(1.0, collapse_strength)))
p0, p1 = system.probs()
r = rng(seed)
triggered = (r.random() < cs)
pre = system.as_dict()

`
outcome = None
if triggered:
    x = r.random()
    outcome = 0 if x < p0 else 1
    system.collapse_to(outcome)

post = system.as_dict()
return {
    "interpretation": "objective_collapse",
    "collapse_strength": cs,
    "triggered": triggered,
    "born": {"p0": p0, "p1": p1},
    "outcome": outcome,
    "pre": pre,
    "post": post,
    "note": "If not triggered, state remains uncollapsed (toy GRW-like trigger)."
}
`
