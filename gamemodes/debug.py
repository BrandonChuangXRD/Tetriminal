import sys
import time
sys.path.append("..")
import game.board as board
import screen
import time
import game.order as order 
import game.movement as movement
from pynput import keyboard

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