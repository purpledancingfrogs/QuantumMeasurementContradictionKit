from __future__ import annotations
from pathlib import Path
import json, time, inspect, importlib

def call_with_supported_kwargs(fn, kwargs: dict):
    try:
        sig = inspect.signature(fn)
        use = {k:v for k,v in kwargs.items() if k in sig.parameters}
        return fn(**use)
    except Exception:
        return fn()

def pick_callable(mod, preferred_names):
    for name in preferred_names:
        fn = getattr(mod, name, None)
        if callable(fn):
            return fn
    # fallback: first top-level callable that isn't private/class
    for name in dir(mod):
        if name.startswith("_"):
            continue
        fn = getattr(mod, name)
        if callable(fn) and getattr(fn, "__module__", "") == mod.__name__:
            return fn
    raise RuntimeError(f"No callable found in {mod.__name__}")

def clean(x):
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, list):
        return [clean(v) for v in x]
    if isinstance(x, (int, float, str, bool)) or x is None:
        return x
    return str(x)

def run():
    ds_mod  = importlib.import_module("qmck.experiments.double_slit")
    cat_mod = importlib.import_module("qmck.experiments.schrodinger_cat")
    wf_mod  = importlib.import_module("qmck.experiments.wigner_friend")

    ds_fn  = pick_callable(ds_mod,  ["ds","double_slit","run","simulate","experiment","main"])
    cat_fn = pick_callable(cat_mod, ["cat","schrodinger_cat","run","simulate","experiment","main"])
    wf_fn  = pick_callable(wf_mod,  ["wf","wigner_friend","run","simulate","experiment","main"])

    r1 = call_with_supported_kwargs(ds_fn,  {"shots": 2000, "which_path": 0.2, "seed": 123})
    r2 = call_with_supported_kwargs(cat_fn, {"decoherence": 0.2, "seed": 123})
    r3 = call_with_supported_kwargs(wf_fn,  {"seed": 123})

    payload = {
        "meta": {"seed": 123, "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())},
        "double_slit": r1,
        "schrodinger_cat": r2,
        "wigner_friend": r3,
    }
    payload = clean(payload)

    docs = Path("docs")
    docs.mkdir(parents=True, exist_ok=True)
    out = docs / "sample_v0.2.7_seed123.json"
    out.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
    print(str(out))

if __name__ == "__main__":
    run()