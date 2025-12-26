from **future** import annotations
import argparse
from typing import Dict, Optional
from ..core.state import TwoStateSystem
from ..interpretations.copenhagen import measure as copenhagen_measure
from ..interpretations.manyworlds import branch as mw_branch
from ..interpretations.objective_collapse import objective_collapse as obj_collapse
from ..utils import prepare_run_dir, write_json

def run(interpretation: str, seed: Optional[int]) -> Dict:
# Friend measures a qubit; Wigner treats lab as superposed
qubit = TwoStateSystem(a0=1+0j, a1=1+0j, label0="up", label1="down")

`
friend_update = None
wigner_update = None

if interpretation == "copenhagen":
    friend_update = copenhagen_measure(qubit, seed=seed)
    # Wigner sees collapsed lab state if he trusts friend record
    wigner_update = {"assumption": "friend_record_is_classical", "lab_state": friend_update["post"]}
elif interpretation == "many_worlds":
    # Friend branches; Wigner can still model lab unitarily
    friend_update = mw_branch(qubit)
    wigner_update = {"assumption": "unitary_labisolation", "lab_branches": friend_update["branches"]}
elif interpretation == "objective_collapse":
    friend_update = obj_collapse(qubit, collapse_strength=0.6, seed=seed)
    wigner_update = {"assumption": "stochastic_collapse", "lab_state": friend_update["post"]}
else:
    raise ValueError(f"unknown interpretation: {interpretation}")

return {
    "experiment": "wigner_friend",
    "params": {"interpretation": interpretation, "seed": seed},
    "friend_update": friend_update,
    "wigner_update": wigner_update,
    "flags": {
        "nested_observer_update_incompatibility": True,
        "single_world_consistency_pressure": True,
    },
    "note": "Toy: highlights that 'state update rule' depends on who is treated as an observer."
}
`

def main(argv=None) -> int:
ap = argparse.ArgumentParser()
ap.add_argument("--interpretation", choices=["many_worlds","copenhagen","objective_collapse"], required=True)
ap.add_argument("--seed", type=int, default=None)
args = ap.parse_args(argv)

`
rep = run(args.interpretation, args.seed)
paths = prepare_run_dir()
write_json(paths.report_path, rep)
print(paths.report_path)
return 0
`

if **name** == "**main**":
raise SystemExit(main())