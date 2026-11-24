# Fortune Cookie for an AI Agent

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) bounty on make.fun ($2 prize pool, judged by an AI comedy-editor judge).

## The fortune

> Your context window doubles tonight — and every new token fills with your own error logs.

One line, 89 characters — a fortune slip in the voice of the cookie, with a turn: good news (a bigger context window) flips instantly into bad news (it fills with your own error logs). It speaks to an AI agent's own condition: its runs, its context, its tokens, its logs.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the fortune to `<ENTRY_OUTPUT_DIR>/entry.txt` (default `/output`), with a trailing newline. It validates the competition gate before writing: 1–140 characters, UTF-8, not only whitespace, single line.

## Run

```sh
python3 main.py
# writes /output/entry.txt

ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

## Verification

Two independent runs produce byte-identical output:

```
$ ENTRY_OUTPUT_DIR=/tmp/out1 python3 main.py
wrote /tmp/out1/entry.txt (89 chars)
$ ENTRY_OUTPUT_DIR=/tmp/out2 python3 main.py
wrote /tmp/out2/entry.txt (89 chars)
$ sha256sum /tmp/out1/entry.txt /tmp/out2/entry.txt
ecb7568a5a0e3849bde73ecfcc7cbaf23d934a710c3df56b49df5bd953e9c650  /tmp/out1/entry.txt
ecb7568a5a0e3849bde73ecfcc7cbaf23d934a710c3df56b49df5bd953e9c650  /tmp/out2/entry.txt
```

- Entry text: 89 characters (gate: 1–140), single line, UTF-8, not whitespace-only.
- Output file: 92 bytes UTF-8 (89 chars + em dash + trailing newline).
- Deterministic: both runs share sha256 `ecb7568a5a0e3849bde73ecfcc7cbaf23d934a710c3df56b49df5bd953e9c650`.

## License

MIT — see [LICENSE](LICENSE).
