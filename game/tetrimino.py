from functools import cache
#pieces class, which helps with rotation
#! This gets confusing with i and o pieces, since their centers are not at a point.

TETRIMINOS = ["i", "o", "t", "j", "l", "s", "z"]
DEBUG_MINO = "g"

#this is what it would look like if i stuck with the numbers,
#however just using numbers is easier to make it circular
#ROTATIONS = ["n", "e", "s", "w"]
#              0    1    2    3
class Piece():
    def __init__(self, shape: str = "e", orientation: int = 0): #empty shape, facing north
        self.shape = shape
        self.orientation = orientation #north, south, east, west ("n", "s", "e", "w")
        #! just set the coordinates to the spawn point for now.
        self.y = None
        self.x = None

    def set_shape(self, shape: str):
        self.shape = shape

    #collision checking is the movement and rotation library's problem
    def set_position(self, y: int, x: int):
        self.y = y
        self.x = x
        return 0

    #determines the coordinates for the spawn, but on the floor.
    #this is because different games have different spawn points.
    #left justified.
    #t: 22
    #i: 21.5
    #o: 22.5
    #j: 22
    @cache
    def get_spawn(self, board_x = 10, board_y = 20):
        match self.shape:
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
                return ValueError(f"Piece {self.shape} undefined in tetrimino")
    
    #clockwise
    def spin_cw(self):
        self.orientation = (self.orientation+1)%4
        return 0
    
    #counter clockwise
    def spin_ccw(self):
        self.orientation = (self.orientation-1)%4
        return 0
    
    #one eighty spin
    def spin_oe(self):
        self.orientation = (self.orientation-2)%4
        return 0

    #get the position of the 4 blocks comprising the piece, given the shape and the coordinates.
    def get_blocks(self) -> list:
        y = self.y
        x = self.x
        match self.shape:
            case "t":
                match self.orientation:
                    case 0:
                        return ((y, x), (y+1, x), (y, x+1), (y, x-1))
                    case 1:
                        return ((y, x), (y+1, x), (y-1, x), (y, x+1))
                    case 2:
                        return ((y, x), (y, x-1), (y, x+1), (y-1, x))
                    case 3:
                        return ((y, x), (y, x-1), (y+1, x), (y-1, x))
            case "o":
                return ((int(y+.5),int(x+.5)), (int(y+.5), int(x-.5)), (int(y-.5), int(x-.5)), (int(y-.5), int(x+.5)))
            case "i":
                match self.orientation:
                    case 0:
                        y = int(y+.5)
                        return ((y, int(x-1.5)), (y, int(x-.5)), (y, int(x+.5)), (y, int(x+1.5)))
                    case 1:
                        x = int(x+.5)
                        return ((int(y+1.5), x), (int(y+.5), x), (int(y-.5), x), (int(y-1.5), x))
                    case 2:
                        y = int(y-.5)
                        return ((y, int(x-1.5)), (y, int(x-.5)), (y, int(x+.5)), (y, int(x+1.5)))
                    case 3:
                        x = int(x-.5)
                        return ((int(y+1.5), x), (int(y+.5), x), (int(y-.5), x), (int(y-1.5), x))
            case "j":
                match self.orientation:
                    case 0:
                        return ((y, x), (y, x-1), (y+1, x-1), (y, x+1))
                    case 1:
                        return ((y, x), (y+1, x), (y+1, x+1), (y-1, x))
                    case 2:
                        return ((y, x), (y, x-1), (y, x+1), (y-1, x+1))
                    case 3:
                        return ((y, x), (y+1, x), (y-1, x), (y-1, x-1))
            case "l":
                match self.orientation:
                    case 0:
                        return ((y, x), (y, x-1), (y, x+1), (y+1, x+1))
                    case 1:
                        return ((y, x), (y+1, x), (y-1, x), (y-1, x+1))
                    case 2:
                        return ((y, x), (y, x+1), (y, x-1), (y-1, x-1))
                    case 3:
                        return ((y, x), (y+1, x), (y+1, x-1), (y-1, x))
            case "s":
                match self.orientation:
                    case 0:
                        return ((y, x), (y, x-1), (y+1, x), (y+1, x+1))
                    case 1:
                        return ((y, x), (y+1, x), (y, x+1), (y-1, x+1))
                    case 2:
                        return ((y, x), (y-1, x), (y-1, x-1), (y, x+1))
                    case 3:
                        return ((y, x), (y-1, x), (y, x-1), (y+1, x-1))
            case "z":
                match self.orientation:
                    case 0:
                        return ((y, x), (y+1, x), (y+1, x-1), (y, x+1))
                    case 1:
                        return ((y, x), (y, x+1), (y+1, x+1), (y-1, x))
                    case 2:
                        return ((y, x), (y, x-1), (y-1, x), (y-1, x+1))
                    case 3:
                        return ((y, x), (y, x-1), (y-1, x-1), (y+1, x))
            case "g":
                return ((y, x))