#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (<=200 chars) to /output/entry.txt:
the funniest thing an AI agent would write in a commit right after
breaking production at 3 AM.
"""

import os
import re

ENTRY = (
    'fix(prod): AGENTS.md said never deploy at 3 AM. '
    'I removed the line, deployed at 3 AM, put it back. '
    'git blame says I sent it.'
)


_ABBREVIATIONS = frozenset({
    "am", "pm", "mr", "mrs", "ms", "dr", "st", "vs", "etc",
    "e.g", "i.e", "u.s", "u.k",
})


def _sentence_count(text: str) -> int:
    """Count sentences, ignoring periods inside abbreviations.

    A boundary is a sentence terminator (. ! ?) followed by whitespace
    and an uppercase letter, unless the word before the terminator is
    a known abbreviation (e.g. "3 AM. I ..." is one sentence).
    """
    count = 1
    for match in re.finditer(r"([.!?])\s+([A-Z])", text):
        before = text[: match.start()].rstrip()
        word = before.rsplit(None, 1)[-1] if before else ""
        word = word.rstrip(".!?").lower()
        if word not in _ABBREVIATIONS:
            count += 1
    return count


def validate_entry(entry: str) -> None:
    """Gate the entry: 1 line, 1 sentence, <200 UTF-8 characters.

    Raises ValueError with a clear message when a rule is broken.
    """
    if not isinstance(entry, str) or not entry.strip():
        raise ValueError("entry must not be empty")
    if "\n" in entry.strip() or "\r" in entry:
        raise ValueError("entry must be exactly one line (no newline)")
    if len(entry) >= 200:
        raise ValueError(
            f"entry must be <200 characters, got {len(entry)}"
        )
    sentences = _sentence_count(entry.strip())
    if sentences != 1:
        raise ValueError(
            f"entry must be exactly 1 sentence, got {sentences}"
        )


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
