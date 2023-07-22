from functools import cache
#pieces class, which helps with rotation
#! This gets confusing with i and o pieces, since their centers are not at a point.

TETRIMINOS = ["i", "o", "t", "j", "l", "s", "z"]
DEBUG_MINO = "g"
class Piece():
    def __init__(self, shape = "e", orientation = "n"): #empty shape
        self.shape = shape
        self.orientation = orientation #north, south, east, west
        
    def set_shape(self, shape: str):
        self.shape = shape

    #determines the coordinates for the spawn, but on the floor.
    #this is because different games have different spawn points.
    #left justified.
    #t: 22
    #i: 21.5
    #o: 22.5
    #j: 22
    @cache
    def get_spawn(self, p, board_x = 10, board_y = 20):
        match p.shape:
            case "i":
                return (board_y+.5, (board_x//2)-.5)
            case "o":
                return (board_y+.5, (board_x//2)-.5)
            case "t":
                return (board_y+1, (board_x//2)-1)
            case "j":
                return (board_y+1, (board_x//2)-1)
            case "l":
                return (board_y+1, (board_x//2)-1)
            case "s":
                return (board_y+1, (board_x//2)-1)
            case "z":
                return (board_y+1, (board_x//2)-1)
            case "g":
                return (board_y+1, (board_x//2)-1)
            case _:
                return NotImplementedError(f"Piece {p.shape} undefined in tetrimino")

    #get the position of the 4 blocks comprising the piece, given the shape and the coordinates.
    @cache
    def get_position(self, p, y, x):
        match p.shape:
            case "i":
                return NotImplementedError("get spawn x not implemented")
            case "o":
                return NotImplementedError("get spawn x not implemented")
            case "t":
                return NotImplementedError("get spawn x not implemented")
            case "j":
                return NotImplementedError("get spawn x not implemented")
            case "l":
                return NotImplementedError("get spawn x not implemented")
            case "s":
                return NotImplementedError("get spawn x not implemented")
            case "z":
                return NotImplementedError("get spawn x not implemented")
            case "g":
                return [(y, x)]