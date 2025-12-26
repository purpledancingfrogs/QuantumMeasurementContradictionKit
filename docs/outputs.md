# Outputs

QMCK emits machine-readable outputs to support reproducibility and auditing.

## Example JSON output
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

## Minimal schema (documentary)
- double_slit:
  - shots: int
  - visibility: float
  - which_path_info: float
  - note: str
- schrodinger_cat:
  - alive_prob: float
  - dead_prob: float
  - coherence: float
  - note: str
- wigner_friend:
  - friend_outcome: str
  - wigner_description: str
  - contradiction_flag: bool
  - note: str

## Sample console outputs
\\\	ext


WignerFriendResult(friend_outcome='definite outcome (collapsed)', wigner_description='unitary superposition', contradiction_flag=True, note='toy: friend assigns collapse; wigner assigns unitary evolution')
\\\

## Audit artifacts
- .asios/audit_index.json — sha256 manifest
- .asios/tracked_files.txt — tracked files snapshot