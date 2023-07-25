import sys

def check_collision(grid: list, blocks: list) -> bool:
    for y, x in blocks:
        if y > len(grid) or y < 0 or x > len(grid[0])-1 or x < 0:
            return True
        if grid[y][x] != "e" and grid[y][x] != "x":
            return True
    return False

def check_grounded(grid: list, blocks: list) -> bool:
    for y, x in blocks:
        if y > len(grid) or y < 0 or x > len(grid[0])-1 or x < 0:
            return True
        elif y == 0:
            return True 
        elif grid[y-1][x] != "e" and grid[y-1][x] != "x":
            return True
    return False