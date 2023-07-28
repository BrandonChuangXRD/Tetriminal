from . import rotate
import sys
sys.path.append("..")
from game import tetrimino
from game import collision
from pynput import keyboard

CCW = keyboard.KeyCode(char = "z")
CW = keyboard.KeyCode(char = "x")
OE = keyboard.KeyCode(char = "a")

#returns true if rotate was successful, false otherwise.
class NRS(rotate.Rotate):
    def _counter_clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
        if piece.orientation == 0 and piece.shape in ["i, s, z"]:
            return self._clockwise(grid, piece)
        return super()._counter_clockwise(grid, piece)
        
    
    def _clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
        if piece.orientation == 1 and piece.shape in ["i, s, z"]:
            return self._counter_clockwise(grid, piece)
        return super()._clockwise(grid, piece)
    
    #doesn't do anything
    def _one_eighty(self, grid: list, piece: tetrimino.Piece) -> bool: 
        return False
    