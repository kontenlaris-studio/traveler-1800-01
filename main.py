#!/usr/bin/env python3
"""traveler-1800-01: one sentence of advice for a time traveler from 1800."""
import os

ENTRY = "Do not panic when the horseless carriages scream past \u2014 but never tell anyone the glowing rectangle in your pocket knows where you are at all times."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
