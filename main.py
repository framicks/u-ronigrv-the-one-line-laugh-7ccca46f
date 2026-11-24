#!/usr/bin/env python3
"""Write the one-line laugh entry.

The joke is a single sentence of at most 200 characters. This script
does no networking and reads nothing from disk: it writes the line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` when the variable is
unset), so repeated runs produce byte-identical output.
"""

import os
from pathlib import Path

LINE = (
    "My smartwatch congratulated me on closing my rings, "
    "then reminded me the only ring I closed today was the pizza box."
)


def main() -> None:
    # The sealed scorer only accepts UTF-8 text of 1 to 200 characters
    # that is not only white space, so check the gate before writing.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"Line is {len(LINE)} characters, must be 1-200")
    if not LINE.strip():
        raise SystemExit("Line is only white space")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
