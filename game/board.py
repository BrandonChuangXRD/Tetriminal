import random
from game import tetrimino
#'g': ghost piece; 'e': empty; 'x': spawnpoint warning
states = ["s", "z", "l", "j", "o", "t", "i", "e", "g", "x"]


class Board():
    def __init__(self, length=10, height=20, hidden=12):
        self.length = length
        self.height = height
        self.hidden = hidden
        self.spawn = height + 1
        self.grid = None

    def change_size(self, length=10, height=20):
        self.length = length
        self.height = height

    def grid_create(self):
        self.grid = [["e"] * self.length for _ in range(self.height + self.hidden)]

    def grid_destroy(self):
        self.grid = None

    def random_grid(self):
        self.grid = []
        for _ in range(self.height + self.hidden):
            self.grid.append([])
            for _ in range(self.length):
                self.grid[-1].append(random.choice(states))

    def add_piece(self, piece: tetrimino.Piece):
        for y, x in piece.get_blocks():
            self.grid[y][x] = piece.shape
        return 0

    def remove_piece(self, piece):
        for y, x in piece.get_blocks():
            self.grid[y][x] = "e"
        return 0

    def clear_lines(self):

        return 0