from . import rotate
import sys
sys.path.append("..")
from game import tetrimino

#returns true if rotate was successful, false otherwise.
class NRS(rotate.RotateTemplate):
    def counter_clockwise(board: list, piece: tetrimino.Piece) -> bool:
        raise NotImplementedError("counterclockwise rotation not implemented")
    
    def clockwise(board, piece) -> bool:
        raise NotImplementedError("clockwise rotation not implemented")
    
    #doesn't do anything
    def one_eighty(board, piece) -> bool:
        return False