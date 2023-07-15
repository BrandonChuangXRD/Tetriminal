import curses

#(option, unit, input)
HANDLE_OPT = [
    ("Auto Repeat Rate (ARR)", "F", "float"),
    ("Delayed Auto Shift (DAS)", "F", "float"),
    ("DAS Cut Delay(DCD)", "F", "float"),
    ("Soft Drop Factor (SDF)", "X", "float"),
    ("Hard Drop Lockout (HDL)", "F", "float")
]
CTRL_OPT = [
    "left",
    "right",
    "soft_drop",
    "hard_drop",
    "clockwise",
    "counterclockwise",
    "one_eighty",
    "hold"
]

def init_menu():
    return 0