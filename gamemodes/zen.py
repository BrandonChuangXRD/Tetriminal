import curses
import sys
sys.path.append("..")
import options
import board
import screen
from rotation import nrs

CONTROLS_SOURCE = "../options/controls.json"
HANDLING_SOURCE = "../options/handling.json"

def start():
    ctrls = options.ControlScheme()
    ctrls = ctrls.deserialize()
    handle = options.HandlingScheme()
    handle = handle.deserialize()

    return 0