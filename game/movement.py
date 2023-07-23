#this takes in in the movement keys and determines the state and new positions
#mimics the movement in tetr.io
import sys
import time
sys.path.append("..")
from options import opt
from game import tetrimino
from game import collision

LEFT = "l"
RIGHT = "r"
SOFT_DROP = "sd"
HARD_DROP = "hd"

class MoveStates():
    def __init__(self):
        self.timer = time.monotonic()
        self.last_update = self.timer

        self.handle = opt.HandlingScheme()
        self.handle.deserialize()

        self.key_time = {} #easily determine press, hold, and release parts of the press

        self.min_height = 0 #calculate time it 
        self.height_time = 0 #need to calculate how much time it can idle on the ground before placing
        
        self.gravity = 0.0
        self.lock_delay = 0
        #when both left and right are pressed at the same time, the piece moves right
        #frames need to be converted to seconds.
        self.handle.ARR /= 60
        self.handle.DAS /= 60

        self.repeat_times = {} #for any timer: gravity, ARR, etc.
        self.repeat_times["gravity"] = self.timer+(self.gravity*60)
    
    def set_gravity(self, gravity):
        self.gravity = gravity
        return 0

    def set_lock_delay(self, lock_delay: float):
        self.lock_delay = lock_delay
        return

    #determine the next board, given the time since last update
    #TODO how do i determine time until next shift?
    def _left(self, grid, piece, y, x) -> tuple:
        if self.key_time[LEFT] == float("inf"):
            self.key_time[LEFT] = self.timer
            self.next_repeat[LEFT] = self.timer+self.handle.ARR+self.handle.DAS
            if collision.check_collision(grid, piece, y, x-1):
                return (y, x-1)
            else:
                return (y, x)
        elif self.timer() >= self.next_repeat[LEFT]:
            if self.handle.ARR == float("inf"):
                return self._left_inf(grid, piece, y, x)
            #auto repeat rate calculation
            while self.timer() >= self.next_repeat[LEFT]:
                self.next_repeat[LEFT] += self.handle.ARR
                if collision.check_collision(grid, piece, y, x-1):
                    return (y, x-1)
                else:
                    self.next_repeat[LEFT] = self.timer()+self.handle.ARR
                    break
        return (y, x)
    

    def _left_inf(self, grid, piece, y, x):
        return 0


    def _right(self, grid, piece, y, x):
        if self.key_time[LEFT] == float("inf"):
            self.key_time[LEFT] = self.timer
            if collision.check_collision(grid, piece, y, x+1):
                return (y, x+1)
            else:
                return (y, x)
        return 0
    

    def _right_inf(self, grid, piece, y, x):
        return 0
    

    #TODO do this first for gravity, need to test spawn points
    def _down(self, grid, piece):
        return 0
    
    def _down_inf(self, grid, piece):
        return 0
    
    #returns if it moved or not
    def gravity_down(self, grid: list, piece: tetrimino.Piece):
        piece.y -= 1
        if collision.check_collision(grid, piece.get_blocks()):
            piece.y +=1
            return False
        return True

    #returns the new y, x coordinates 
    def update_piece(self, grid: list, piece: tetrimino.Piece, keys = []):
        self.timer = time.monotonic()

        #gravity check
        while self.timer >= self.repeat_times["gravity"]:
            self.gravity_down(grid, piece)
            self.repeat_times["gravity"] += self.gravity*60



        # for k in self.key_time.keys():
        #     if k not in keys:
        #         del self.key_time[k]
        # for k in keys:
        #     if k not in self.key_time.keys():
        #         self.key_time[k] = float("inf") #placeholder value indicating the key just got pressed down

        # #left right priority
        # kk = self.key_time.keys()
        # #the second direction should override the first direction, but not the DAS of that direction
        # #TODO need while loops to do the right amount of moves given the time passed, in case someones fps is really that bad.
        # if LEFT in kk and RIGHT in kk:
        #     #left direction takes priority
        #     if self.key_time[LEFT] > self.key_time[RIGHT]:
        #         y, x = self._left(grid, piece, y, x)
        #     else:
        #         y, x = self._right(grid, piece, y, x)
        # elif LEFT in kk:
        #     y, x = self._left(grid, piece, y, x)
        # elif RIGHT in kk:
        #     y, x = self._right(grid, piece, y, x)
        # #these two shouldn't interrupt each other
        # if SOFT_DROP in kk:  
        #     y, x = self._down(grid, piece, y, x)
        # if HARD_DROP in kk: #? maybe set the piece to "e" and update the grid indicating the piece has been placed?
        #     y, x = (-1, -1)
        # return (y, x)