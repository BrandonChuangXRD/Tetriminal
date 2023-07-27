from . import rotate
import sys
sys.path.append("..")
from game import tetrimino
from game import collision
from pynput import keyboard

CCW = keyboard.KeyCode(char = "z")
CW = keyboard.KeyCode(char = "x")
OE = keyboard.KeyCode(char =  "a")

#index indicates the starting position
#tetrio to wiki direction conversions:
#0: 0; 1: R; 2: 2; 3: L


#!I think this might be wrong. see SRS+ I kick graph in readme
_KICKS_CCW_I = (((0, 0), (0, -1), (0, 2), (2, -1), (-1, 2)),
               ((0, 0), (0, 2), (0, -1), (1, 2), (-2, -1)),
               ((0, 0), (0, 1), (0, -2), (-2, 1), (1, -2)),
               ((0, 0), (0, -2), (0, 1), (-1, -2), (2, 1))
               )

_KICKS_CCW_O = (((0, 0)),
               ((0, 0)),
               ((0, 0)),
               ((0, 0))
               )

_KICKS_CCW_OTHER = (((0,0), (0, 1), (1, 1), (-2, 0), (-2, 1)),
         ((0,0), (0, 1), (-1, 1), (2, 0), (2, 1)),
         ((0,0), (0, -1), (1, -1), (-2, 0), (-2, -1)),
         ((0,0), (0, -1), (-1, -1), (2, 0), (2, -1))
         )

_KICKS_CW_I = (((0, 0), (0, -2), (0, 1), (-1, -2), (2, 1)),
              ((0, 0), (0, -1), (0, 2), (2, -1), (-1, 2)),
              ((0, 0), (0, 2), (0, -1), (1, 2), (-2, -1)),
              ((0, 0), (0, 1), (0, -2), (-2, 1), (1, -2))
              )

_KICKS_CW_O = (((0, 0)),
              ((0, 0)),
              ((0, 0)),
              ((0, 0))
              )

_KICKS_CW_OTHER = (((0, 0), (0, -1), (1, -1), (-2, 0), (-2, -1)),
         ((0, 0), (0, 1), (-1, 1), (2, 0), (2, 1)),
         ((0, 0), (0, 1), (1, 1), (-2, 0), (-2, 1)),
         ((0, 0), (0, -1), (-1, -1), (2, 0), (2, -1))
         )

_KICKS_OE = (((0, 0), (1, 0), (1, 1), (1, -1), (0, 1), (0, -1)),
         ((0, 0), (-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1)),
         ((0, 0), (0, 1), (2, 1), (1, 1), (2, 0), (1, 0)),
         ((0, 0), (0, -1), (2, -1), (1, -1), (2, 0), (1, 0))
         )

#direction is -1 for ccw and 1 for cw
def _get_kick_table(shape: str, orientation: int, direction: int):
    if orientation > 3 or orientation < 0:
        raise IndexError("orientation value out of range")
    return True

#returns true if rotate was successful, false otherwise.
class SRSP(rotate.RotateTemplate):
    def __init__(self):
        self.held_keys = []

    def _counter_clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
        piece.spin_ccw()


        if collision.check_collision(grid, piece.get_blocks()):
            piece.spin_cw()
            return False
        return True
        
    
    def _clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
        piece.spin_cw()
        if collision.check_collision(grid, piece.get_blocks()):
            piece.spin_ccw()
            return False
        return True
    
    #doesn't do anything
    def _one_eighty(self, board, piece) -> bool:
        return False
    
    def update_piece(self, grid, piece, keys = []):
        if CCW in keys and CCW not in self.held_keys:
            self._counter_clockwise(grid, piece)
        if CW in keys and CW not in self.held_keys:
            self._clockwise(grid, piece)
        self.held_keys = keys.copy()
        return 0