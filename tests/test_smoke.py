import os
import subprocess
import sys
from pathlib import Path

def test_cli_help():
    repo = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"

    # Ensure package is importable when running tests without editable install
    env["PYTHONPATH"] = str(repo / "src") + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")

    cmd = [sys.executable, "-m", "qmck.cli", "--help"]
    p = subprocess.run(cmd, cwd=str(repo), env=env, capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    assert "QuantumMeasurementContradictionKit" in (p.stdout + p.stderr)