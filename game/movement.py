#this takes in in the movement keys and determines the state and new positions
#mimics the movement in tetr.io
import sys
import time
sys.path.append("..")
import options
import time
import tetrimino

LEFT = "l"
RIGHT = "r"
SOFT_DROP = "sd"
HARD_DROP = "hd"

class MoveStates():
    def __init__(self):
        self.handle = options.HandlingScheme()
        self.handle = self.handle.deserialize()
        self.key_time = {} #easily determine press, hold, and release parts of the press
        self.first_direction = 0 #-1 for left, 1 for right. determines which direction to move
        self.time_since_update = 0
        self.min_height = 0 #calculate time it 
        self.height_time = 0 #need to calculate how much time it can idle on the ground before placing
        self.gravity = 0
        self.lock_delay = 0
        #when both left and right are pressed at the same time, the piece moves right
        #frames need to be converted to seconds.
        self.handle.ARR /= 60
        self.handle.DAS /= 60
    
    #determine the next board, given the time since last update

    def _left(self, grid, piece, y, x):
        return 0
    
    def _left_inf(self, grid, piece, y, x):
        return 0

    def _right(self, grid, piece, y, x):
        return 0
    
    def _right_inf(self, grid, piece, y, x):
        return 0
    
    #TODO do this first for gravity, need to test spawn points
    def _down(self, grid, piece, y, x):
        return 0
    
    def _down_inf(self, grid, piece, y, x):
        return 0
    
    def gravity_down(self, grid, piece, y, x):
        return 0

    #returns the new y, x coordinates
    def update_piece(self, grid: list, piece: tetrimino.Piece, y: int, x: int, keys = []):
        for k in self.key_time.keys():
            if k not in keys:
                del self.key_time[k]
        for k in keys:
            if k not in self.key_time.keys():
                self.key_time[k] = float("inf") #placeholder value indicating the key just got pressed down

        #left right priority
        kk = self.key_time.keys()
        #the second direction should override the first direction, but not the DAS of that direction
        #TODO need while loops to do the right amount of moves given the time passed, in case someones fps is really that bad.
        if LEFT in kk and RIGHT in kk:
            #left direction takes priority
            if self.key_time[LEFT] > self.key_time[RIGHT]:
                y, x = self._left(grid, piece, y, x)
            else:
                y, x = self._right(grid, piece, y, x)
        elif LEFT in kk:
            y, x = self._left(grid, piece, y, x)
        elif RIGHT in kk:
            y, x = self._right(grid, piece, y, x)
        #these two shouldn't interrupt each other
        if SOFT_DROP in kk:  
            y, x = self._down(grid, piece, y, x)
        if HARD_DROP in kk: #? maybe set the piece to "e" and update the grid indicating the piece has been placed?
            y, x = (-1, -1)
        return (y, x)