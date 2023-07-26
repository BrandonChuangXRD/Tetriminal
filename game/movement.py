#this takes in in the movement keys and determines the state and new positions
#mimics the movement in tetr.io
import sys
import time
from pynput import keyboard #! try to remove this for modularization
sys.path.append("..")
from options import opt
from game import tetrimino
from game import collision

LEFT = keyboard.Key.left
RIGHT = keyboard.Key.right
SOFT_DROP = keyboard.Key.down
HARD_DROP = keyboard.Key.space

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
        self.lock_delay = .5 #how long a piece remains on the floor till locking
        self.lock_time = float("inf")
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
        return 0
    
    def _lock_piece(self, grid: list, piece: tetrimino.Piece):
        for y, x in piece.get_blocks():
            grid[y][x] = piece.shape
        #to indicate the piece has been placed
        piece.shape = "e"
        return 0

    #determine the next board, given the time since last update
    #TODO how do i determine time until next shift?
    def _left(self, grid, piece) -> tuple:
        piece.x -= 1
        if collision.check_collision(grid, piece.get_blocks()):
            piece.x += 1
            return False
        return True
    

    def _left_inf(self, grid, piece):
        movecheck = False
        piece.x -= 1
        while not collision.check_collision(grid, piece.get_blocks()):
            piece.x -= 1
            movecheck = True
        piece.x += 1
        return movecheck

    #TODO
    def _right(self, grid, piece):
        piece.x += 1
        if collision.check_collision(grid, piece.get_blocks()):
            piece.x -= 1
            return False
        return True
    

    def _right_inf(self, grid, piece):
        movecheck = False
        piece.x += 1
        while not collision.check_collision(grid, piece.get_blocks()):
            piece.x += 1
            movecheck = True
        piece.x -= 1
        return movecheck
    

    #TODO do this first for gravity, need to test spawn points
    def _down(self, grid, piece):
        piece.y -= 1
        if collision.check_collision(grid, piece.get_blocks()):
            piece.y +=1
            return False
        return True
    
    def _down_inf(self, grid, piece):
        movecheck = False
        piece.y -= 1
        while not collision.check_collision(grid, piece.get_blocks()):
            piece.y -= 1
            movecheck = True
        piece.y += 1
        return movecheck

    #returns the new y, x coordinates 
    def update_piece(self, grid: list, piece: tetrimino.Piece, keys = []):

        self.timer = time.monotonic()

        #gravity check
        while self.timer >= self.repeat_times["gravity"]:
            self._down(grid, piece)
            self.repeat_times["gravity"] += self.gravity*60

        #add time to lock if grounded
        if collision.check_grounded(grid, piece.get_blocks()):
            if self.lock_time == float("inf"):
                self.lock_time = self.timer+self.lock_delay
            else:
                if self.lock_time <= self.timer:
                    self._lock_piece(grid, piece)
                    self.lock_time = float("inf")
                    return True

        #key pressed -> key held -> key released
        #hard drop
        if HARD_DROP in keys and HARD_DROP not in self.key_time.keys():
            self.key_time[HARD_DROP] = self.timer
            self._down_inf(grid, piece)
            self._lock_piece(grid, piece)
            return True
        elif HARD_DROP not in keys and HARD_DROP in self.key_time.keys():
            del self.key_time[HARD_DROP]

        #TODO when left and right are pressed at the same time,
        #TODO movement is not the same.
        #left
        if LEFT in keys and LEFT not in self.key_time.keys():
            self._left(grid, piece)
            self.key_time[LEFT] = self.timer
            self.repeat_times[LEFT] = self.timer+self.handle.DAS
        elif LEFT in keys and LEFT in self.key_time.keys():
            if self.handle.ARR == 0:
                self._left_inf(grid, piece)
            elif self.repeat_times[LEFT] <= self.timer:
                self._left(grid, piece)
                self.repeat_times[LEFT] += self.handle.ARR
                while self.repeat_times[LEFT] <= self.timer:
                    self._left(grid, piece)
                    self.repeat_times[LEFT] += self.handle.ARR
        elif LEFT not in keys and LEFT in self.key_time.keys():
            del self.key_time[LEFT]
            del self.repeat_times[LEFT]


        #right
        if RIGHT in keys and RIGHT not in self.key_time.keys():
            self._right(grid, piece)
            self.key_time[RIGHT] = self.timer
            self.repeat_times[RIGHT] = self.timer+self.handle.DAS
        elif RIGHT in keys and RIGHT in self.key_time.keys():
            if self.handle.ARR == 0:
                self._right_inf(grid, piece)
            elif self.repeat_times[RIGHT] <= self.timer:
                self._right(grid, piece)
                self.repeat_times[RIGHT] += self.handle.ARR
                while self.repeat_times[RIGHT] <= self.timer:
                    self._right(grid, piece)
                    self.repeat_times[RIGHT] += self.handle.ARR
        elif RIGHT not in keys and RIGHT in self.key_time.keys():
            del self.key_time[RIGHT]
            del self.repeat_times[RIGHT]

        #soft drop
        if SOFT_DROP in keys and SOFT_DROP not in self.key_time.keys():
            self.gravity /= (self.handle.SDF**2)
            self.key_time[SOFT_DROP] = self.timer
            temp = self.repeat_times["gravity"]-self.timer
            self.repeat_times["gravity"] -= temp-(temp/self.handle.SDF**2)
        elif SOFT_DROP not in keys and SOFT_DROP in self.key_time.keys():
            self.gravity *= (self.handle.SDF**2)
            temp = self.repeat_times["gravity"]-self.timer
            self.repeat_times["gravity"] += (temp*self.handle.SDF**2)-temp
            del self.key_time[SOFT_DROP]
    

    def game_over(self, grid:list, piece: tetrimino.Piece):
        return collision.check_collision(grid, piece.get_blocks())