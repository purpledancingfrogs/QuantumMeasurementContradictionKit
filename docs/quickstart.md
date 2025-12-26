# Quickstart

## One-command verification (Windows)
\\\powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1 all
\\\

## Direct experiment runs (Python)
\\\powershell
python -c "from qmck.experiments.double_slit import run; print(run(shots=2000, which_path=0.2, seed=123))"
python -c "from qmck.experiments.schrodinger_cat import run; print(run(decoherence=0.2))"
python -c "from qmck.experiments.wigner_friend import run; print(run())"
\\\

### Example outputs
\\\	ext


WignerFriendResult(friend_outcome='definite outcome (collapsed)', wigner_description='unitary superposition', contradiction_flag=True, note='toy: friend assigns collapse; wigner assigns unitary evolution')
\\\

## CLI
\\\powershell
python -m qmck.cli --help
\\\
"@

Write-Utf8NoBom "docs\outputs.md" @"
# Outputs

QMCK produces machine-readable outputs so runs can be audited and compared across interpretations.

## Example JSON
File: \examples/sample_report.json\

\\\json
{
  "double_slit": {
    "note": "toy model: V\u22480.980, D\u22480.200, hits=1031/2000",
    "shots": 2000,
    "visibility": 0.9797958971132712,
    "which_path_info": 0.2
  },
  "schrodinger_cat": {
    "alive_prob": 0.5,
    "coherence": 0.8,
    "dead_prob": 0.5,
    "note": "toy cat: P(alive)=0.5, P(dead)=0.5, coherence\u22480.800"
  },
  "wigner_friend": {
    "contradiction_flag": true,
    "friend_outcome": "definite outcome (collapsed)",
    "note": "toy: friend assigns collapse; wigner assigns unitary evolution",
    "wigner_description": "unitary superposition"
  }
}
\\\

## Expected keys
- \double_slit\: \shots\, \isibility\, \which_path_info\, \
ote\
- \schrodinger_cat\: \live_prob\, \dead_prob\, \coherence\, \
ote\
- \wigner_friend\: \riend_outcome\, \wigner_description\, \contradiction_flag\, \
ote\

## Audit artifacts
- \.asios/audit_index.json\ — sha256 manifest of tracked artifacts for reproducible verification
- \.asios/tracked_files.txt\ — tracked file list snapshot