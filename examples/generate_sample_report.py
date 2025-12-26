from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path

from qmck.experiments.double_slit import run as run_double_slit
from qmck.experiments.schrodinger_cat import run as run_cat
from qmck.experiments.wigner_friend import run as run_wigner


def _to_obj(x):
    if is_dataclass(x):
        return asdict(x)
    if isinstance(x, dict):
        return x
    if hasattr(x, "__dict__"):
        return dict(x.__dict__)
    return x


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    out_dir = repo / "examples"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        version = metadata.version("qmck")
    except Exception:
        version = "unknown"

    payload = {
        "tool": "QuantumMeasurementContradictionKit",
        "package": "qmck",
        "version": version,
        "generated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "runs": {
            "double_slit": _to_obj(run_double_slit(which_path=0.2, shots=2000, seed=123)),
            "schrodinger_cat": _to_obj(run_cat(decoherence=0.2)),
            "wigner_friend": _to_obj(run_wigner()),
        },
        "design_note": "Toy outputs preserve (not resolve) the unitary-vs-outcome contradiction; see Wigner's friend contradiction_flag.",
    }

    out_path = out_dir / "sample_report.json"
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(out_path.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())