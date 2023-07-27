from . import rotate
import sys
sys.path.append("..")
from game import tetrimino
from game import collision
from pynput import keyboard

CCW = keyboard.KeyCode(None, "z")
CW = keyboard.KeyCode(None, "x")
OE = keyboard.KeyCode(None, "a")

_KICKS_ALL = [((0, 0)),
            ((0, 0)),
            ((0, 0)),
            ((0, 0))
            ]

#returns true if rotate was successful, false otherwise.
class NRS(rotate.RotateTemplate):
    def __init__(self):
        self.held_keys = []
        self.kick_dict = {}
        self.kick_dict["i"] = []
        self.kick_dict["o"] = []
        self.kick_dict["t"] = []
        self.kick_dict["z"] = []
        self.kick_dict["s"] = []
        self.kick_dict["l"] = []
        self.kick_dict["j"] = []
        for _ in range(4):
            self.kick_dict["i"].append(_KICKS_ALL)
            self.kick_dict["o"].append(_KICKS_ALL)
            self.kick_dict["t"].append(_KICKS_ALL)
            self.kick_dict["z"].append(_KICKS_ALL)
            self.kick_dict["s"].append(_KICKS_ALL)
            self.kick_dict["l"].append(_KICKS_ALL)
            self.kick_dict["j"].append(_KICKS_ALL)

    #TODO make a verify kick tables function, such that each piece, initial, final combination has at least one kick table,
    #execpt for when the initial orientation matches the final orientation
    def _verify_kick_table(self):
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
        return False
    
    def update_piece(self, grid, piece, keys = []):
        if CCW in keys and CCW not in self.held_keys:
            self._counter_clockwise(grid, piece)
        if CW in keys and CW not in self.held_keys:
            self._clockwise(grid, piece)
        self.held_keys = keys.copy()
        return 0
    
    # def __init__(self):
    #     self.held_keys = []

    # def _counter_clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
    #     if piece.orientation == 0 and piece.shape in ["i, s, z"]:
    #         return self._clockwise(grid, piece)
    #     piece.spin_ccw()
    #     if collision.check_collision(grid, piece.get_blocks()):
    #         piece.spin_cw()
    #         return False
    #     return True
        
    
    # def _clockwise(self, grid: list, piece: tetrimino.Piece) -> bool:
    #     if piece.orientation == 1 and piece.shape in ["i, s, z"]:
    #         return self._counter_clockwise(grid, piece)
    #     piece.spin_cw()
    #     if collision.check_collision(grid, piece.get_blocks()):
    #         piece.spin_ccw()
    #         return False
    #     return True
    
    # #doesn't do anything
    # def _one_eighty(self, board, piece) -> bool:
    #     return False
    
    # def update_piece(self, grid, piece, keys = []):
    #     if CCW in keys and CCW not in self.held_keys:
    #         self._counter_clockwise(grid, piece)
    #     if CW in keys and CW not in self.held_keys:
    #         self._clockwise(grid, piece)
    #     self.held_keys = keys.copy()
    #     return 0