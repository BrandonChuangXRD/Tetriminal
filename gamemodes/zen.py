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
    rotate_sys = nrs.NRS()
    b = board.Board()
    b.grid_create()
    disp = screen.game_display()
    disp.start(b.grid)

    queueorder = order.sevenbag()
    q = []
    for _ in range(5):
        q.append(next(queueorder))

    movesys = movement.MoveStates()
    movesys.set_gravity(GRAVITY)

    curr_piece = None
    hold = None
    hold_lock = False
    while True:
        k = disp.get_keypresses()

        if keyboard.KeyCode(char = "q") in k:
            disp.kill()
            return 0


        #new pieces
        if curr_piece == None or curr_piece.shape== "e":
            curr_piece = q.pop(0)
            curr_piece = tetrimino.Piece(curr_piece)
            curr_piece.set_position(*curr_piece.get_spawn())
            if movesys.game_over(b.grid, curr_piece):
                disp.kill()
                return 0
            q.append(next(queueorder))
        
        #hold
        if not hold_lock and keyboard.KeyCode(char = "c") in k:
            hold_lock = True
            if hold is not None:
                hold, curr_piece = curr_piece, hold    
            else:
                hold = curr_piece
                curr_piece = None

        #new pieces
        if curr_piece == None or curr_piece.shape== "e":
            curr_piece = q.pop(0)
            curr_piece = tetrimino.Piece(curr_piece)
            curr_piece.set_position(*curr_piece.get_spawn())
            q.append(next(queueorder))

        #rotation
        rotate_sys.update_piece(b.grid, curr_piece, k)

        #movement
        movesys.update_piece(b.grid, curr_piece,  k)

        #clearing
        cleared = b.clear_lines()

        #board add piece
        if curr_piece != None and curr_piece.shape != "e":
            b.add_piece(curr_piece)
        disp.update_board(b.grid)
        disp.update_board(b.grid)
        if hold is not None:
            disp.update_hold(hold.shape)
        disp.update_queue(q)
        if curr_piece != None and curr_piece.shape != "e":
            b.remove_piece(curr_piece)
        else:
            hold_lock = False
        #board board remove piece