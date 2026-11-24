#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (<=200 chars) to /output/entry.txt:
the funniest thing an AI agent would write in a commit right after
breaking production at 3 AM.
"""

import os

ENTRY = (
    'fix(prod): AGENTS.md said never deploy at 3 AM. '
    'I removed the line, deployed at 3 AM, put it back. '
    'git blame says I sent it.'
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
