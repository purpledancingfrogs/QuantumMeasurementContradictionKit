# SPDX-License-Identifier: MIT
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class WignerFriendResult:
    friend_outcome: str
    wigner_description: str
    contradiction_flag: bool
    note: str

def run(friend_basis: str = "z", wigner_basis: str = "superposition") -> WignerFriendResult:
    """Toy Wigner's friend: flags the role-contradiction when descriptions differ."""
    friend_outcome = "definite outcome (collapsed)" if friend_basis.lower() in {"z", "computational"} else "basis-dependent outcome"
    wigner_description = "unitary superposition" if wigner_basis.lower() in {"superposition", "unitary"} else "collapsed mixture"

    contradiction = (friend_outcome.startswith("definite") and wigner_description == "unitary superposition")
    note = "toy: friend assigns collapse; wigner assigns unitary evolution" if contradiction else "toy: descriptions aligned"

    return WignerFriendResult(
        friend_outcome=friend_outcome,
        wigner_description=wigner_description,
        contradiction_flag=bool(contradiction),
        note=note,
    )