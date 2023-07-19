import sys
import time
sys.path.append("..")
import board
import screen
import time
import order 
import movement

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
    last_update = time.time()-1
    while True:
        k = disp.get_keypresses()
        if ord("q") in k:
            disp.kill()
            return 0
        if time.time() > last_update+1:
            last_update +=1
            b.random_grid() 
            disp.update_board(b.grid)
            disp.update_hold(next(holdorder))
            disp.update_queue(q)
            q.pop(0)
            q.append(next(queueorder))