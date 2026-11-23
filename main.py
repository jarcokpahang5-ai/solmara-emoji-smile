#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Prints exactly one emoji and nothing else: a warm, genuine smile.
"""

ENTRY = "\U0001F60A"  # U+1F60A SMILING FACE WITH SMILING EYES


def main() -> None:
    # Exactly one emoji on stdout, followed by the newline print() adds.
    print(ENTRY)


if __name__ == "__main__":
    main()
