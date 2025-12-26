@echo off
setlocal
python -m pip install -e .
python -m pytest -q
python -c "from qmck.experiments.double_slit import run; print(run())"
python -c "from qmck.experiments.schrodinger_cat import run; print(run())"
python -c "from qmck.experiments.wigner_friend import run; print(run())"
