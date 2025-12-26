from qmck.experiments.double_slit import run as run_double_slit
from qmck.experiments.schrodinger_cat import run as run_cat
from qmck.experiments.wigner_friend import run as run_wigner

def test_double_slit_runs():
    r = run_double_slit(shots=200, which_path=0.3, seed=1)
    assert 0.0 <= r.visibility <= 1.0
    assert 0.0 <= r.which_path_info <= 1.0
    assert r.shots == 200

def test_cat_runs():
    r = run_cat(decoherence=0.25)
    assert abs(r.alive_prob + r.dead_prob - 1.0) < 1e-12
    assert 0.0 <= r.coherence <= 1.0

def test_wigner_friend_runs():
    r = run_wigner(friend_basis="z", wigner_basis="unitary")
    assert isinstance(r.contradiction_flag, bool)
    assert r.friend_outcome
    assert r.wigner_description