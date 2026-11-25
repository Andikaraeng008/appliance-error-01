"""The Funniest Honest Appliance Error.

A kettle retires mid-tea after six years with zero sick days,
leaving a note telling the owner to find someone else to boil
the water.
"""

# The Funniest Honest Appliance Error — one line, 125 chars (gate 1-200), no trailing newline.
LINE = "ERROR E2: The kettle retired mid-tea after six years, zero sick days. It left a note: \"Find someone else to boil your water.\""

open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
