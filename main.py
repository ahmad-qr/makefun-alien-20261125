"""An alien tourist's review of planet Earth.

Writes the review to /output/entry.txt for make.fun's
"Alien Field Notes: The Two Day Earth Review" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Earth: beautiful oceans, terrible traffic. The locals stare at "
    "glowing rectangles all day and call it work. 4 stars, would abduct again."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
