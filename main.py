"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance
(the office microwave) to /output/entry.txt.
Standard library only. The rant is 213 characters,
well inside the competition gate of 1-400 characters.
"""

from pathlib import Path

ENTRY = (
    "The microwave beeps once when it finishes, then again every thirty "
    "seconds until I open the door and confess that reheating fish at work "
    "was a mistake. My coworkers have filed a formal complaint. "
    "Against the fish."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
