#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

One deadpan weather bulletin for Nulltown, a city that does not exist.
The forecast itself is broken -- a 404% chance of rain, a high of
undefined, a low of null -- and the bulletin still calmly advises
bringing an umbrella anyway.

Writes the single fixed line (<=120 chars) to /output/entry.txt.
Deterministic: every run produces the exact same bytes.
"""

import os

CITY = "Nulltown"
CONDITION = "partly cloudy"
RAIN_CHANCE = "404%"
HIGH = "undefined"
LOW = "null"

ENTRY = (
    f"Tomorrow in {CITY}: {CONDITION}, {RAIN_CHANCE} chance of rain, "
    f"high {HIGH}, low {LOW}. Bring an umbrella anyway."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 120


def validate_entry(text: str) -> str:
    """Check the entry against the gate rules and return it unchanged."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, limit is {MAX_CHARS}")
    if text.strip() != text:
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def _write_entry(text: str, path: str) -> None:
    """Write the entry with no trailing newline; the gate counts every char."""
    out_dir = os.path.dirname(path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    entry = validate_entry(ENTRY)
    _write_entry(entry, OUTPUT_PATH)


if __name__ == "__main__":
    main()
