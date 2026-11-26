#!/usr/bin/env python3
"""One-Liner Laughs entry: write a single funny line to /output/entry.txt."""

import os

JOKE = "I asked my phone for directions to happiness \u2014 it said \u201crecalculating\u201d and sent me straight back to work."


def main():
    line = JOKE.strip()
    assert "\n" not in line, "joke must be a single line"
    assert 1 <= len(line) <= 200, "joke must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
