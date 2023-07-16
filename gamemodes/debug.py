import curses
from .. import board
from .. import screen

def start():
    b = board.Board()
    b.random_grid()
    disp = screen.game_display(b.grid)

    return 0