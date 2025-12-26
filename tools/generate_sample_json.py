import argparse, json, os, sys

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=123)
    ap.add_argument("--shots", type=int, default=2000)
    ap.add_argument("--which-path", type=float, default=0.2, dest="which_path")
    ap.add_argument("--decoherence", type=float, default=0.2)
    ap.add_argument("--out", default=os.path.join("runs", "sample_seed123.json"))
    args = ap.parse_args()

    try:
        from qmck import ds, cat, wf  # exported API (tests already rely on this)
    except Exception as e:
        print(f"Import error: {e}", file=sys.stderr)
        return 2

    payload = {
        "seed": args.seed,
        "params": {
            "shots": args.shots,
            "which_path": args.which_path,
            "decoherence": args.decoherence,
        },
        "outputs": {
            "double_slit": ds(shots=args.shots, which_path=args.which_path, seed=args.seed),
            "cat": cat(decoherence=args.decoherence),
            "wigner_friend": wf(),
        },
    }

    out = args.out
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=True, indent=2, sort_keys=True)
        f.write("\n")
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())