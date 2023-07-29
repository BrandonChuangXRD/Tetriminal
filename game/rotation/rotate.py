#I don't really know if there's a name for this system, but its good as a template
#its basically just NRS but with all pieces having 4 orientations rather than some having just 2
import sys
sys.path.append("..")
from game import tetrimino
from game import collision
from pynput import keyboard

CCW = keyboard.KeyCode(None, "z")
CW = keyboard.KeyCode(None, "x")
OE = keyboard.KeyCode(None, "a")



#returns true if rotate was successful, false otherwise.
#kick_dict[shape][initial_orienation][final_orientation]
class Rotate():
    def __init__(self):
        KICKS_ALL = [[(0, 0)],
                   [(0, 0)],
                   [(0, 0)],
                   [(0, 0)]
                   ]
        self.held_keys = []
        self.kick_dict = {}
        self.kick_dict["i"] = []
        self.kick_dict["o"] = []
        self.kick_dict["t"] = []
        self.kick_dict["z"] = []
        self.kick_dict["s"] = []
        self.kick_dict["l"] = []
        self.kick_dict["j"] = []
        for i in range(4):
            self.kick_dict["i"].append(KICKS_ALL)
            self.kick_dict["o"].append(KICKS_ALL)
            self.kick_dict["t"].append(KICKS_ALL)
            self.kick_dict["z"].append(KICKS_ALL)
            self.kick_dict["s"].append(KICKS_ALL)
            self.kick_dict["l"].append(KICKS_ALL)
            self.kick_dict["j"].append(KICKS_ALL)

    

    #TODO make a verify kick tables function, such that each piece, initial, final combination has at least one kick table
    def verify_kick_table(self):
        return 0

    def _counter_clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
        initial_orientation = piece.orientation
        piece.spin_ccw()
        for kick in self.kick_dict[piece.shape][initial_orientation][piece.orientation]:
            piece.y += kick[0]
            piece.x += kick[1]
            if not collision.check_collision(grid, piece.get_blocks()):
                return True
            piece.y -= kick[0]
            piece.x -= kick[1]
        piece.spin_cw()       
        print(self.kick_dict[piece.shape][initial_orientation][piece.orientation]) 
        return False
        
    
    def _clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
        initial_orientation = piece.orientation
        piece.spin_cw()
        for kick in self.kick_dict[piece.shape][initial_orientation][piece.orientation]:
            piece.y += kick[0]
            piece.x += kick[1]
            if not collision.check_collision(grid, piece.get_blocks()):
                return True
            piece.y -= kick[0]
            piece.x -= kick[1]
        piece.spin_ccw()        
        return False
    
    #doesn't do anything
    def _one_eighty(self, grid: list, piece: tetrimino.Piece) -> bool:
        initial_orientation = piece.orientation
        piece.spin_oe()
        for kick in self.kick_dict[piece.shape][initial_orientation][piece.orientation]:
            piece.y += kick[0]
            piece.x += kick[1]
            if not collision.check_collision(grid, piece.get_blocks()):
                return True
            piece.y -= kick[0]
            piece.x -= kick[1]
        piece.spin_oe()        
        return False
    
    def update_piece(self, grid, piece, keys = []):
        if CCW in keys and CCW not in self.held_keys:
            self._counter_clockwise(grid, piece)
        if CW in keys and CW not in self.held_keys:
            self._clockwise(grid, piece)
        if OE in keys and OE not in self.held_keys:
            self._one_eighty(grid, piece)
        self.held_keys = keys.copy()
        return 0