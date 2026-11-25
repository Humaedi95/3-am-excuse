#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

A hardware wallet, in its own voice, refusing to sign a transaction
at 3 AM. The wallet is a night-shift worker with a rota: its shift
ends at midnight, and the 3 AM hours belong to the owner's future
self — who has already filed a complaint about half-asleep signing.

Running this program writes the entry line to /output/entry.txt.
"""

import os

ENTRY = (
    "I'm off the clock. My rota ends at midnight, and 3 AM is your "
    "future self's shift. He already filed a complaint about your "
    "half-asleep signatures."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
