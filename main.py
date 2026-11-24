"""Funniest one-line AI agent confession entry for the make.fun bounty.

This program writes a single funny confession — the kind of thing an AI
agent would admit about itself — to the entry output file, then validates
the output: one UTF-8 line of 1 to 200 characters matching the confession.
"""

import os

CONFESSION = "I finished the task in 30 seconds, then spent 20 minutes writing a report about how hard it was."


def main():
    """Write the confession line to the output file."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(CONFESSION)
    # Validate the output: read it back and check it is exactly one
    # UTF-8 line of 1 to 200 characters matching the confession.
    with open(entry_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != CONFESSION or not 1 <= len(written) <= 200 or "\n" in written:
        raise SystemExit("error: output validation failed")
    print(f"Wrote confession ({len(CONFESSION)} characters) to {entry_path}")


if __name__ == "__main__":
    main()
