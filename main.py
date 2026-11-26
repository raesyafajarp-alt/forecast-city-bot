#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

Writes one line (<=120 chars) to /output/entry.txt: a deadpan weather
bulletin for Nulltown, a city that does not exist, where the forecast
itself is broken -- a 404% chance of rain, a high of undefined, a low
of null -- and the bulletin still calmly advises an umbrella.

Deterministic: the same fixed line is written on every run.
"""

import os

ENTRY = (
    "Tomorrow in Nulltown: partly cloudy, 404% chance of rain, "
    "high undefined, low null. Bring an umbrella anyway."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
