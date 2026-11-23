#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

The entry is exactly one emoji and nothing else: a warm, genuine smile.
It is validated, printed, and written to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os

ENTRY = "\U0001F60A"  # U+1F60A SMILING FACE WITH SMILING EYES

OUTPUT_PATH = "/output/entry.txt"


def validate_emoji(text: str) -> str:
    """Validate the entry is exactly one emoji character."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")
    if text.strip() != text or text.isspace():
        raise ValueError("entry must be exactly one emoji")
    return text


def main() -> None:
    emoji = validate_emoji(ENTRY)
    print(emoji)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(emoji + "\n")


if __name__ == "__main__":
    main()
