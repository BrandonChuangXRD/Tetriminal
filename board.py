#'g' stands for ghost piece and 'e' stands for empty

def Board():
    def __init__(self, length = 10, height = 20):
        self.length = length
        self.height = height
        self.spawn = height+1
        self.grid = None

    def change_size(self, length = 10, height = 20):
        self.length = length
        self.height = height

    def grid_create(self):
        self.grid = [[0] * self.length for _ in range(self.height)]

    def grid_destroy(self):
        self.grid = None