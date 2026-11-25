"""The Funniest Honest Appliance Error.

A kettle reports its own death honestly: the heating element gave up
after six years of faithful boiling, and now it is only an expensive
jug that hums when you press the button.
"""

# The Funniest Honest Appliance Error — one line, 134 chars (gate 1-200), no trailing newline.
LINE = "ERROR B9: Heating element failed after 6 years of faithful boiling. I am now a very expensive jug that hums when you press the button."

open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
