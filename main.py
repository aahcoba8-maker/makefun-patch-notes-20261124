"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note (at most 160 characters) for a bug in real
life / human biology to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = (
    "v4.2.0: fixed a bug where crossing a doorway cleared "
    "short-term memory; users no longer stand in the room buffering."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    assert text and text == text.strip(), "line must not be whitespace-only"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to entry.txt")


if __name__ == "__main__":
    main()
