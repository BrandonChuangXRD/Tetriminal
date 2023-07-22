import curses
import sys
import time
from pynput import keyboard
sys.path.append("..")
import options
import game.board as board
import screen
import game.order as order
from game.rotation import nrs

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
    b = board.Board()
    b.random_grid()
    disp = screen.game_display()
    disp.start(b.grid)
    holdorder = order.insanity()
    queueorder = order.sevenbag()
    q = []
    for _ in range(5):
        q.append(next(queueorder)) 
    # TODO break if "q" is pressed
    last_update = time.time()-1
    while True:
        k = disp.get_keypresses()
        #print(k)
        if keyboard.KeyCode(char = "q") in k:
            disp.kill()
            return 0
        if time.time() > last_update+1 or keyboard.Key.space in k:
            last_update +=1
            b.random_grid() 
            disp.update_board(b.grid)
            disp.update_hold(next(holdorder))
            disp.update_queue(q)
            q.pop(0)
            q.append(next(queueorder))