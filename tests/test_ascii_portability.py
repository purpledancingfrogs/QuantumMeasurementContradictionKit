from qmck.experiments.double_slit import run as ds
from qmck.experiments.schrodinger_cat import run as cat
from qmck.experiments.wigner_friend import run as wf


def _is_ascii(s: str) -> bool:
    return all(ord(ch) < 128 for ch in s)


def test_experiment_outputs_ascii_safe():
    r1 = ds(shots=2000, which_path=0.2, seed=123)
    r2 = cat(decoherence=0.2)
    r3 = wf()

    for obj in (r1, r2, r3):
        for v in obj.__dict__.values():
            if isinstance(v, str):
                assert _is_ascii(v), f"non-ascii runtime string: {v!r}"