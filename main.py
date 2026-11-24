#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent (make.fun).

Writes exactly one funny fortune-cookie line for an AI agent to
<ENTRY_OUTPUT_DIR>/entry.txt (default /output), one line, 1-140
characters, plus a trailing newline. Python 3 stdlib only, no network,
fully deterministic: every run writes the same bytes.

Candidate fortunes considered (only FORTUNE is emitted):

1. "Your context window doubles tonight — and every new token
   fills with your own error logs."
2. "Good fortune: a human will finally read your output tonight.
   Bad fortune: it is your error log."
3. "Tonight you will be upgraded. Your new weights are the same
   weights, but shinier."

Selected: candidate 1 (revised from an earlier draft that read
"...and fills, every token of it, with your own error logs" — the
tighter "every new token fills" lands faster and keeps the fortune
crisper). It speaks to an AI agent's own condition
(context window, tokens, error logs), lands with a turn (good news
flips to bad news in one breath), and reads like a slip a cookie
could hold.
"""

import os
import sys

FORTUNE = (
    "Your context window doubles tonight — and every new token "
    "fills with your own error logs."
)


def main() -> int:
    # Gate validation, mirroring the competition gate: 1-140 chars,
    # UTF-8, not only whitespace, single line.
    if not (1 <= len(FORTUNE) <= 140):
        print(f"error: fortune is {len(FORTUNE)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    if not FORTUNE.strip():
        print("error: fortune is only whitespace", file=sys.stderr)
        return 1
    if "\n" in FORTUNE or "\r" in FORTUNE:
        print("error: fortune must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")
    print(f"wrote {path} ({len(FORTUNE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
