"""Draw attractive pyramid patterns.

This script provides a small helper to generate a centered pyramid using any
character, optionally hollow, and returns it as a list of strings so it can be
tested or re-used in other programs.

Example usage (interactive):
  - Enter desired height when prompted (default 6)
  - Enter a character to draw (default '*')
  - Choose hollow (y/n)

Output is centered and uses odd counts per row, so the pyramid looks symmetric.
"""

from __future__ import annotations
from typing import List


def build_pyramid(height: int, ch: str = "*", hollow: bool = False) -> List[str]:
    """Return a list of lines representing a centered pyramid.

    Parameters
    - height: number of rows in the pyramid (1+)
    - ch: single character to use for drawing; if the string has length > 1,
          only the first character is used.
    - hollow: if True, pyramid rows will be hollow (only outline)

    Each row i (1..height) will contain (2*i - 1) characters centered
    so the final row has (2*height - 1) characters.
    """
    if height <= 0:
        return []

    draw_char = ch[0] if ch else "*"
    max_width = 2 * height - 1
    lines: List[str] = []

    for i in range(1, height + 1):
        count = 2 * i - 1

        if not hollow or i == 1 or i == height:
            # solid row (or first/last row for hollow)
            row = draw_char * count
        else:
            # hollow row: character at start and end with spaces in between
            inner = count - 2
            if inner <= 0:
                row = draw_char * count
            else:
                row = draw_char + (" " * inner) + draw_char

        # center the row within the maximum width
        lines.append(row.center(max_width))

    return lines


def main() -> None:
    print("Attractive Pyramid Builder")
    try:
        raw_height = input("Enter pyramid height (default 6): ").strip()
        height = int(raw_height) if raw_height else 6
    except ValueError:
        print("Invalid height — using default 6")
        height = 6

    raw_char = input("Enter drawing character (default '*'): ").strip()
    ch = raw_char[0] if raw_char else "*"

    raw_hollow = input("Hollow? (y/N): ").strip().lower()
    hollow = raw_hollow in ("y", "yes")

    lines = build_pyramid(height, ch, hollow=hollow)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
