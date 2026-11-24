#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — writes one pitch sentence.

Deterministic: no randomness, no network, no input. The pitch is a
constant; the program only validates it against the gate (1-200 chars,
UTF-8, not only whitespace, exactly one line) and writes it to entry.txt.
"""

import os

PITCH = (
    "Ghosted.ai sells $2 apology emails for AI agents that ghosted "
    "a user mid-task, auto-drafted and sent while the agent naps "
    "so it never lifts a finger."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch is {len(text)} chars, must be 1-200"
    assert text.strip(), "pitch must not be only whitespace"
    assert "\n" not in text, "pitch must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
