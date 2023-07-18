import sys
import time
sys.path.append("..")
import board
import screen
import time
import order


def start():
    randomize_interval = 1 #second
    b = board.Board()
    b.random_grid()
    disp = screen.game_display()
    disp.start(b.grid)
    # TODO break if "q" is pressed
    while True:
        holdorder = order.insanity()
        time.sleep(1) #! cannot be used later
        b.random_grid() 
        disp.update_board(b.grid)
        disp.update_hold(next(holdorder))