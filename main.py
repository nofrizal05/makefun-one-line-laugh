# One-Line Laugh Sprint — make.fun entry
# Writes exactly one original one-liner (<=200 chars) to /output/entry.txt.
# Python 3.13 standard library only (os).
import os

LINE = (
    "I finally organized my junk drawer, and now I can't find anything "
    "\u2014 turns out my mess had a filing system all along, "
    "it just wasn't taking new clients."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
