#!/usr/bin/env python3
"""Convert a plain-text screenplay laid out with spaces into a Fountain file.

Plain-text scripts (the kind written in chat, or exported as .txt) use spaces to
indent character cues and dialogue. Screenwriting software doesn't read those
spaces, so pasting the .txt in breaks the formatting. Fountain is plain text
with simple rules that WriterDuet, Final Draft, Highland, Fade In and others
import correctly.

Usage:
    python txt_to_fountain.py script.txt [output.fountain]

What it does:
- Title page (everything before FADE IN: or the first scene heading) becomes
  Fountain title-page keys: Title, Credit, Author, Contact.
- Character cues (indented, all caps) and the dialogue and parentheticals under
  them lose their indentation and their wrapped lines are joined.
- Action paragraphs are unwrapped into one line each.
- Transitions (CUT TO:, CUT TO BLACK., FADE OUT., ...) are forced with ">".
- All-caps action lines that Fountain could mistake for a cue are forced with "!".
- Fountain's emphasis characters (* and _) in the text are escaped.

It prints a short summary of what it found so you can sanity-check the result.
"""
import re
import sys
from pathlib import Path

SCENE = re.compile(r"^(INT|EXT|EST|INT\./EXT|INT/EXT|I/E)[\. ]", re.I)
TRANSITION = re.compile(r"^[A-Z0-9 .'\-]+(TO:|TO BLACK\.|FADE OUT\.|FADE TO BLACK\.)$")
CUE_INDENT = 15        # cues sit around 20 spaces in; dialogue around 10
DIALOGUE_INDENT = 6


def indent(line):
    return len(line) - len(line.lstrip(" "))


def is_upper(text):
    letters = [c for c in text if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters)


def escape(text):
    return text.replace("*", r"\*").replace("_", r"\_")


def blocks(lines):
    """Split into blocks of non-blank lines."""
    block = []
    for line in lines:
        if line.strip():
            block.append(line.rstrip())
        elif block:
            yield block
            block = []
    if block:
        yield block


def title_page(lines):
    text = [l.strip() for l in lines if l.strip()]
    if not text:
        return []
    out = [f"Title: {text[0]}"]
    rest = text[1:]
    if rest and rest[0].lower() in ("written by", "by", "screenplay by", "story by"):
        out.append(f"Credit: {rest[0]}")
        rest = rest[1:]
    if rest:
        out.append(f"Author: {rest[0]}")
        rest = rest[1:]
    if rest:
        out.append("Contact:")
        out += [f"    {r}" for r in rest]
    return out


def convert(raw):
    raw = raw.replace("\f", "\n").replace("\r\n", "\n")
    lines = raw.split("\n")

    # Find where the body starts.
    start = next((i for i, l in enumerate(lines)
                  if l.strip() == "FADE IN:" or SCENE.match(l.strip())), 0)
    out = title_page(lines[:start])
    if out:
        out.append("")

    counts = {"scenes": 0, "cues": 0, "action": 0, "transitions": 0}
    for block in blocks(lines[start:]):
        first = block[0]
        stripped = first.strip()

        if indent(first) >= CUE_INDENT and is_upper(stripped) and not stripped.startswith("("):
            # Cue, then parentheticals and dialogue.
            counts["cues"] += 1
            out.append(escape(stripped))
            speech = []
            for line in block[1:]:
                s = line.strip()
                if s.startswith("("):
                    if speech:
                        out.append(escape(" ".join(speech)))
                        speech = []
                    out.append(s)
                else:
                    speech.append(s)
            if speech:
                out.append(escape(" ".join(speech)))
        elif SCENE.match(stripped) and len(block) == 1:
            counts["scenes"] += 1
            out.append(stripped.upper())
        elif len(block) == 1 and TRANSITION.match(stripped):
            counts["transitions"] += 1
            out.append(f"> {stripped}")
        else:
            counts["action"] += 1
            para = escape(" ".join(l.strip() for l in block))
            # An all-caps action line on its own could read as a cue.
            if is_upper(para) and para != "FADE IN:" and not para.endswith(":"):
                para = "!" + para
            out.append(para)
        out.append("")

    return "\n".join(out).rstrip() + "\n", counts


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".fountain")
    text, counts = convert(src.read_text(encoding="utf-8"))
    dst.write_text(text, encoding="utf-8")
    print(f"Wrote {dst}")
    print(", ".join(f"{v} {k}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
