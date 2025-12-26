from __future__ import annotations

import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="qmck",
        description="QuantumMeasurementContradictionKit — sandbox for the quantum measurement problem.",
    )
    p.add_argument("--version", action="store_true", help="Print version and exit.")
    return p

def main(argv: list[str] | None = None) -> int:
    p = build_parser()
    args = p.parse_args(argv)
    if args.version:
        print("QuantumMeasurementContradictionKit")
        return 0
    p.print_help()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())