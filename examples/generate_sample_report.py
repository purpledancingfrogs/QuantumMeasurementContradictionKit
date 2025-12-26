from __future__ import annotations

import argparse
import json
from pathlib import Path

from qmck.experiments.double_slit import run as run_double_slit
from qmck.experiments.schrodinger_cat import run as run_cat
from qmck.experiments.wigner_friend import run as run_wigner


def build_report(which_path: float, shots: int, seed: int, decoherence: float) -> dict:
    ds = run_double_slit(shots=shots, which_path=which_path, seed=seed).__dict__
    cat = run_cat(decoherence=decoherence).__dict__
    wf = run_wigner().__dict__
    return {
        "double_slit": ds,
        "schrodinger_cat": cat,
        "wigner_friend": wf,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a concrete QMCK sample_report.json")
    ap.add_argument("--out", default="examples/sample_report.json", help="Output JSON path")
    ap.add_argument("--which-path", type=float, default=0.2, help="Which-path information in [0,1]")
    ap.add_argument("--shots", type=int, default=2000, help="Number of shots")
    ap.add_argument("--seed", type=int, default=123, help="RNG seed")
    ap.add_argument("--decoherence", type=float, default=0.2, help="Decoherence in [0,1]")
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    report = build_report(args.which_path, args.shots, args.seed, args.decoherence)
    out.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())