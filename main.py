#!/usr/bin/env python3
"""Writes one absurd-startup pitch sentence to entry.txt.

Stdlib only, no network, deterministic.
"""
import os

SENTENCE = "We pay new parents $5,000 to name their baby after a brand, then charge advertisers for a living billboard who introduces themselves at every job interview for life."

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    assert SENTENCE.strip(), "sentence must not be only whitespace"
    assert 1 <= len(SENTENCE) <= 200, f"sentence must be 1-200 chars, got {len(SENTENCE)}"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
