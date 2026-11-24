"""Funniest Time Machine Warning Label — make.fun entry.

Writes exactly one warning label, one line, to /output/entry.txt.
Deterministic: the same bytes on every run. Python 3.13, stdlib only.
"""

import os

LABEL = "WARNING: Do not exit the vehicle while it is still yesterday."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LABEL + "\n")


if __name__ == "__main__":
    main()
