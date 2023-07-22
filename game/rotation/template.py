#! The goal of the roatation systems is that each kick table can be applied to any piece, even fake ones. Just pick the correct ones.
import sys

class RotateTemplate():
    def counter_clockwise(board, piece):
        raise NotImplementedError("counterclockwise rotation not implemented")
    
    def clockwise(board, piece):
        raise NotImplementedError("clockwise rotation not implemented")
    
    def one_eighty(board, piece):
        raise NotImplementedError("180 rotation not implemented")