import argparse, json, inspect, sys
from pathlib import Path
from dataclasses import is_dataclass, asdict

def _ensure_src_on_path():
    here = Path(__file__).resolve()
    root = here.parents[1]
    src = root / "src"
    if src.exists() and str(src) not in sys.path:
        sys.path.insert(0, str(src))

def _to_jsonable(x):
    if x is None or isinstance(x, (bool, int, float, str)):
        return x
    if isinstance(x, (list, tuple)):
        return [_to_jsonable(v) for v in x]
    if isinstance(x, dict):
        return {str(k): _to_jsonable(v) for k, v in x.items()}
    if is_dataclass(x):
        return _to_jsonable(asdict(x))
    if hasattr(x, "model_dump"):  # pydantic v2
        return _to_jsonable(x.model_dump())
    if hasattr(x, "dict"):        # pydantic v1
        try:
            return _to_jsonable(x.dict())
        except Exception:
            pass
    if hasattr(x, "__dict__"):
        return _to_jsonable({k: v for k, v in x.__dict__.items() if not k.startswith("_")})
    return str(x)

def _pick_callable(mod):
    for name in ("ds", "cat", "wf", "run", "simulate", "main"):
        fn = getattr(mod, name, None)
        if callable(fn):
            return name, fn
    for name, fn in vars(mod).items():
        if callable(fn) and not name.startswith("_"):
            return name, fn
    raise RuntimeError(f"No callable experiment entrypoint found in {mod.__name__}")

def _call(fn, seed, shots=None, which_path=None, decoherence=None):
    sig = inspect.signature(fn)
    kwargs = {}
    if "seed" in sig.parameters:
        kwargs["seed"] = seed
    if shots is not None and "shots" in sig.parameters:
        kwargs["shots"] = shots
    if which_path is not None and "which_path" in sig.parameters:
        kwargs["which_path"] = which_path
    if decoherence is not None and "decoherence" in sig.parameters:
        kwargs["decoherence"] = decoherence
    return fn(**kwargs)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=123)
    ap.add_argument("--out", type=str, default="runs/sample_seed123.json")
    ap.add_argument("--shots", type=int, default=2000)
    ap.add_argument("--which-path", type=float, default=0.2)
    ap.add_argument("--decoherence", type=float, default=0.2)
    args = ap.parse_args()

    _ensure_src_on_path()

    from qmck.experiments import double_slit, schrodinger_cat, wigner_friend

    payload = {"seed": args.seed, "experiments": {}}
    for mod in (double_slit, schrodinger_cat, wigner_friend):
        name, fn = _pick_callable(mod)
        res = _call(fn, seed=args.seed, shots=args.shots, which_path=args.which_path, decoherence=args.decoherence)
        payload["experiments"][mod.__name__.split(".")[-1]] = {"entrypoint": name, "result": _to_jsonable(res)}

    outp = Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()