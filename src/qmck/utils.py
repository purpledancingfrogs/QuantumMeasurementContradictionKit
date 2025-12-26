from **future** import annotations
import json
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional
import random

def now_stamp() -> str:
return time.strftime("%Y%m%d_%H%M%S")

def ensure_dir(path: str) -> str:
os.makedirs(path, exist_ok=True)
return path

def write_json(path: str, obj: Any) -> None:
ensure_dir(os.path.dirname(path))
with open(path, "w", encoding="utf-8") as f:
json.dump(obj, f, indent=2, sort_keys=False)

def rng(seed: Optional[int] = None) -> random.Random:
r = random.Random()
if seed is not None:
r.seed(int(seed))
return r

@dataclass(frozen=True)
class RunPaths:
outdir: str
report_path: str

def prepare_run_dir(base: str = "runs") -> RunPaths:
outdir = ensure_dir(os.path.join(base, now_stamp()))
report_path = os.path.join(outdir, "report.json")
return RunPaths(outdir=outdir, report_path=report_path)