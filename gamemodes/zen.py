import curses
from ..options import options
from .. import board
from .. import screen

CONTROLS_SOURCE = "../options/controls.json"
HANDLING_SOURCE = "../options/handling.json"

def start():
    ctrls = options.ControlScheme()
    ctrls = ctrls.deserialize()
    handle = options.HandlingScheme()
    handle = handle.deserialize()
    
    

    return 0