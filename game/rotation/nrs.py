from . import rotate
import sys
sys.path.append("..")
from game import tetrimino
from game import collision
from pynput import keyboard

CCW = keyboard.KeyCode(None, "z")
CW = keyboard.KeyCode(None, "x")
OE = keyboard.KeyCode(None, "a")

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
    
    def update_piece(self, grid, piece, keys = []):
        if CCW in keys and CCW not in self.held_keys:
            self._counter_clockwise(grid, piece)
        if CW in keys and CW not in self.held_keys:
            self._clockwise(grid, piece)
        self.held_keys = keys.copy()
        return 0
    