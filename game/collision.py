import sys

def check_collision(grid: list, blocks: list) -> bool:
    for y, x in blocks:
        if y > len(grid) or y < 0 or x > len(grid[0])-1 or x < 0:
            print(f"collision! {y} {x}")
            return True
        if grid[y][x] != "e" and grid[y][x] != "x":
            return True
    return False