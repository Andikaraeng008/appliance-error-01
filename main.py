"""The Funniest Honest Appliance Error.

A microwave dies heating 3 a.m. instant noodles, citing overwork,
underappreciation, and one exploded egg in 2023.
"""

# The Funniest Honest Appliance Error — Appliance 2, 140 characters (gate 1-200), no trailing newline.
LINE = "FAULT 12: The microwave died heating your 3 a.m. instant noodles. Cause of death: overwork, underappreciation, and one exploded egg in 2023."

open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
