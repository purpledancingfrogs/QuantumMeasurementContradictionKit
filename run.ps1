param(
  [ValidateSet('help','version','double-slit','cat','wigner','all')]
  [string] = 'all'
)

Stop = 'Stop'

function Run-DoubleSlit {
  python -c "from qmck.experiments.double_slit import run; print(run(shots=2000, which_path=0.2, seed=0))"
}
function Run-Cat {
  python -c "from qmck.experiments.schrodinger_cat import run; print(run(decoherence=0.2))"
}
function Run-Wigner {
  python -c "from qmck.experiments.wigner_friend import run; print(run(friend_basis='z', wigner_basis='unitary'))"
}

switch () {
  'help'    { python -m qmck.cli --help; break }
  'version' { python -m qmck.cli --version; break }
  'double-slit' { Run-DoubleSlit; break }
  'cat' { Run-Cat; break }
  'wigner' { Run-Wigner; break }
  'all' {
    python -m pytest -q
    Run-DoubleSlit
    Run-Cat
    Run-Wigner
    break
  }
}