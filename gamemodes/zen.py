import curses
import sys
import time
from pynput import keyboard
sys.path.append("..")
import game.board as board
import screen
import game.order as order
from game.rotation import nrs
import game.movement as movement
from game import tetrimino

RANDOM_BAG_TYPE = nrs.NRS
ARE = 0 #delay when placing a piece
LCARE = 0 #delay when clearing a line
GRAVITY = .02 #about 1/60, I think its just how fast it drops in minutes?
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
    b.grid_create()
    disp = screen.game_display()
    disp.start(b.grid)

    queueorder = order.sevenbag()
    q = []
    hold = "e"
    for _ in range(5):
        q.append(next(queueorder))

    movesys = movement.MoveStates()
    movesys.set_gravity(GRAVITY)

    curr_piece = None
    while True:
        k = disp.get_keypresses()

        if keyboard.KeyCode(char = "q") in k:
            disp.kill()
            return 0
        
        if curr_piece == None:
            curr_piece = q.pop(0)
            curr_piece = tetrimino.Piece(curr_piece)
            curr_piece.set_position(*curr_piece.get_spawn())
            q.append(next(queueorder))

        movesys.update_piece(b.grid, curr_piece,  k)

        #board add piece
        b.add_piece(curr_piece)
        disp.update_board(b.grid)
        disp.update_board(b.grid)
        disp.update_hold(hold)
        disp.update_queue(q)
        b.remove_piece(curr_piece)
        #board board remove piece