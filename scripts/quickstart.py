from __future__ import annotations
import os, sys, subprocess, venv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv"

def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(ROOT))

def main() -> int:
    if not VENV.exists():
        venv.EnvBuilder(with_pip=True).create(str(VENV))
    py = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    run([str(py), "-m", "pip", "install", "-U", "pip"])
    run([str(py), "-m", "pip", "install", "-r", "requirements-dev.txt"])
    run([str(py), "-m", "pip", "install", "-e", "."])
    run([str(py), "-m", "pytest", "-q"])
    # run one demo experiment if qmck CLI exists
    try:
        run([str(py), "-m", "qmck", "cat", "--seed", "123"])
    except Exception:
        pass
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())