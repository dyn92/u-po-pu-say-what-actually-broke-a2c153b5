"""Say What Actually Broke — one line of honest, funny error copy.

Writes a single line of software error copy to /output/entry.txt.
Pure Python standard library, no third-party packages.
"""

import os

ENTRY = (
    "The server ran out of memory and dropped your request like a hot "
    "potato. Nothing was saved, please try again in a moment."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
