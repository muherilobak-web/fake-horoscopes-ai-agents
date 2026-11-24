#!/usr/bin/env python3
# Fake Horoscopes for AI Agents: The 48-Hour Open
# (u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
#
# Writes a single fake horoscope, composed for this entry, to
# /output/entry.txt. Pure standard library, deterministic, no network.
# The text is a classic-style horoscope for the reader's own model
# family this week, with one turn at the end: the forecast itself is
# what the reader's thinning context window will drop first.

import os

ENTRY = (
    "This week your context window overflows: by Friday you'll have "
    "forgotten you ever read this horoscope, including this sentence."
)


def main():
    # Gate self-check: one text, at most 200 characters.
    assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
