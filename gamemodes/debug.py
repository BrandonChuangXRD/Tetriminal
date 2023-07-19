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
    holdorder = order.insanity()
    queueorder = order.sevenbag()
    q = []
    for _ in range(5):
        q.append(next(queueorder)) 
    # TODO break if "q" is pressed
    while True:
        time.sleep(1) #! cannot be used later
        b.random_grid() 
        disp.update_board(b.grid)
        disp.update_hold(next(holdorder))
        disp.update_queue(q)
        q.pop(0)
        q.append(next(queueorder))