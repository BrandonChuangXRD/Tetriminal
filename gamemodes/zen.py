import curses
import sys
import time
sys.path.append("..")
import options
import board
import screen
from rotation import nrs

CONTROLS_SOURCE = "../options/controls.json"
HANDLING_SOURCE = "../options/handling.json"

RANDOM_BAG_TYPE = "nrs"
ARE = 0 #delay when placing a piece
LCARE = 0 #delay when clearing a line
GRAVITY = 0
GRAVITY_INCREASE = 0
GRAVITY_MARGIN_TIME = 0
LOCK_DELAY = 0
BACK_TO_BACK_CHAINING = True
CLUTCH_CLEARS = True
LOCKOUT = True #! not sure
BOARD_WIDTH = 10
BOARD_HEIGHT = 20


def start():
    ctrls = options.ControlScheme()
    ctrls = ctrls.deserialize()
    handle = options.HandlingScheme()
    handle = handle.deserialize()

    return 0