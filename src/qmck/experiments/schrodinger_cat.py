from **future** import annotations
import argparse
from typing import Dict, Optional
from ..core.state import TwoStateSystem
from ..core.decoherence import DecoherenceTimeline
from ..interpretations.copenhagen import measure as copenhagen_measure
from ..interpretations.manyworlds import branch as mw_branch
from ..interpretations.objective_collapse import objective_collapse as obj_collapse
from ..utils import prepare_run_dir, write_json

def run(interpretation: str, outcome: Optional[int], collapse_strength: float, seed: Optional[int]) -> Dict:
# cat basis: |alive>, |dead>
sys = TwoStateSystem(a0=1+0j, a1=1+0j, label0="alive", label1="dead")
deco = DecoherenceTimeline(gamma=0.18, steps=24)
timeline = deco.series()

`
if interpretation == "many_worlds":
    interp = mw_branch(sys)
elif interpretation == "copenhagen":
    interp = copenhagen_measure(sys, seed=seed, forced_outcome=outcome)
elif interpretation == "objective_collapse":
    interp = obj_collapse(sys, collapse_strength=collapse_strength, seed=seed)
else:
    raise ValueError(f"unknown interpretation: {interpretation}")

# Contradiction surfacing: interference visibility vs definite macroscopic outcome
contradiction_flag = (deco.final_visibility() < 0.05 and interpretation == "many_worlds")

return {
    "experiment": "schrodinger_cat",
    "params": {
        "interpretation": interpretation,
        "forced_outcome": outcome,
        "collapse_strength": float(collapse_strength),
        "seed": seed,
    },
    "initial_state": sys.as_dict() if interpretation != "copenhagen" else interp.get("pre", {}),
    "decoherence": {
        "model": "exp_decay_visibility",
        "timeline": timeline,
        "final_visibility": deco.final_visibility(),
    },
    "interpretation_result": interp,
    "flags": {
        "observer_role_contradiction": True,
        "macroscopic_definiteness_vs_linearity": True,
        "decoherence_without_outcome_resolution": True,
        "branching_with_low_visibility": contradiction_flag,
    },
}
`

def main(argv=None) -> int:
ap = argparse.ArgumentParser()
ap.add_argument("--interpretation", choices=["many_worlds","copenhagen","objective_collapse"], required=True)
ap.add_argument("--outcome", type=int, choices=[0,1], default=None)
ap.add_argument("--collapse_strength", type=float, default=0.5)
ap.add_argument("--seed", type=int, default=None)
args = ap.parse_args(argv)

`
rep = run(args.interpretation, args.outcome, args.collapse_strength, args.seed)
paths = prepare_run_dir()
write_json(paths.report_path, rep)
print(paths.report_path)
return 0
`

if **name** == "**main**":
raise SystemExit(main())