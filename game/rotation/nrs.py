import game.rotation.rotate as rotate

#returns true if rotate was successful, false otherwise.
class NRS(rotate.RotateTemplate):
    def counter_clockwise(board, piece):
        raise NotImplementedError("counterclockwise rotation not implemented")
    
    def clockwise(board, piece):
        raise NotImplementedError("clockwise rotation not implemented")
    
    #doesn't do anything
    def one_eighty(board, piece):
        return False