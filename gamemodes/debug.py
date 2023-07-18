import sys
import time
sys.path.append("..")
import board
import screen



def start():
    print("what the hell")
    b = board.Board()
    b.random_grid()
    disp = screen.game_display()
    disp.start(b.grid)
    # TODO break if "q" is pressed
    while True:
        time.sleep(1) #! cannot be used later
        b.random_grid() #this works. why does it not pass anything?
        disp.update_board(b.grid)
    return 0