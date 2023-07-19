#this takes in in the movement keys and determines the state and new positions
#mimics the movement in tetr.io
import sys
import time
sys.path.append("..")
import options

LEFT = 0
RIGHT = 1
SOFT_DROP = 2
HARD_DROP = 3

def convert_times(h: options.HandlingScheme()):
    h.ARR /= 60
    h.DAS /= 60
    return 0

class MoveStates():
    def __init__(self):
        self.handle = options.HandlingScheme()
        self.handle = self.handle.deserialize()
        self.key_durations = {} #easily determine press, hold, and release parts of the press
        self.first_direction = 0 #-1 for left, 1 for right. determines which direction to move
        self.time_since_update = 0
        self.min_height = 0 #calculate time it 
        self.height_time = 0 #need to calculate how much time it can idle on the ground before placing
        #when both left and right are pressed at the same time, the piece moves right
        convert_times(self.handle)
        

    #frames need to be converted to seconds.
    
    #determine the next board, given the time since last update
    #! make sure to remove keys once they are not pressed
    #Returns 1 if piece should be placed, 0 otherwise.
    # def update_board(self, grid, piece, keyboard = []):
    #     if LEFT in keyboard:

    #     if RIGHT in keyboard:

    #     if SOFT_DROP in keyboard:

    #     if HARD_DROP in keyboard:

    #     return 0