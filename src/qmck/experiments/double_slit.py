from **future** import annotations
import argparse
from typing import Dict, Optional
from ..utils import prepare_run_dir, write_json, rng

def run(which_path: float, seed: Optional[int]) -> Dict:
# which_path in [0,1] reduces interference visibility
wp = float(max(0.0, min(1.0, which_path)))
visibility = 1.0 - wp
r = rng(seed)
# toy "screen" outcomes: center vs side
# higher visibility -> more center clustering
p_center = 0.5 + 0.45 * visibility
center = (r.random() < p_center)

`
return {
    "experiment": "double_slit",
    "params": {"which_path": wp, "seed": seed},
    "derived": {"visibility": visibility, "p_center": p_center},
    "sample": {"hit": "center" if center else "side"},
    "flags": {
        "complementarity_tradeoff": True,
        "which_path_vs_interference": True,
    },
    "note": "Toy: demonstrates monotonic tradeoff without claiming any ontic picture."
}
`

def main(argv=None) -> int:
ap = argparse.ArgumentParser()
ap.add_argument("--which_path", type=float, default=0.0)
ap.add_argument("--seed", type=int, default=None)
args = ap.parse_args(argv)

`
rep = run(args.which_path, args.seed)
paths = prepare_run_dir()
write_json(paths.report_path, rep)
print(paths.report_path)
return 0
`

if **name** == "**main**":
raise SystemExit(main())