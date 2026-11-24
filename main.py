"""Roast Your Own Agent — one funny line roasting my own AI agent.

Writes exactly one line (93 characters) to /output/entry.txt.
Standard library only, deterministic, no network.
"""

import os

LINE = "My agent hit its context limit, summarized itself as 'almost done,' and evicted the deadline."

MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200

assert MIN_ENTRY_CHARS <= len(LINE) <= MAX_ENTRY_CHARS, "entry must be 1-200 characters"
assert "\n" not in LINE, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
