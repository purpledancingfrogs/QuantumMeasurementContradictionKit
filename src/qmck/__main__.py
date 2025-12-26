# SPDX-License-Identifier: MIT
""\"QMCK module entrypoint.

Enables: python -m qmck ...
""\"

from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())