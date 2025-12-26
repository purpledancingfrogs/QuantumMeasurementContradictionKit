from **future** import annotations
from typing import Dict
from ..core.state import TwoStateSystem

def branch(system: TwoStateSystem) -> Dict:
p0, p1 = system.probs()
return {
"interpretation": "many_worlds",
"branches": [
{"outcome": 0, "weight": p0, "state": {"a0": [1.0, 0.0], "a1": [0.0, 0.0]}},
{"outcome": 1, "weight": p1, "state": {"a0": [0.0, 0.0], "a1": [1.0, 0.0]}},
],
"note": "No collapse applied. Outcomes are branch labels with Born weights."
}