#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji, the Heart Hands gesture, to /output/entry.txt.
Standard library only. No words, no caption, no explanation in the output.
"""

import os

EMOJI = "\U0001faf6"  # 🫶 Heart Hands


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)

    # Self-check: the file must hold exactly one non-space character.
    with open(output_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if len(written) != 1 or written.isspace():
        raise ValueError("entry.txt must contain exactly one emoji")


if __name__ == "__main__":
    main()
