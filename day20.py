from pprint import pprint
from library import timer
with open("input/input20.txt") as f:
# with open("sample/sample20.txt") as f:
    input_grid=f.read().splitlines()

# pprint(input_grid)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def offsets_at_dist(n):
    #This is the list of manhatten distances
    return [
        (r, c, md)
        for r in range(-n, n + 1)
        for c in range(-n, n + 1)
        if (md := abs(r) + abs(c)) <= n and (r, c) != (0, 0)
    ]

def _find_location(map: list[str], char: str) -> tuple[int, int]:
    for r, l in enumerate(map):
        for c, v in enumerate(l):
            if v == char:
                return r, c

    raise Exception("Not there dude")

def _flood_fill_maze(grid):
    end=_find_location(grid,"E")
    temp_maze=[list(line) for line in grid]
    q = [(0, end)]
    coord=[]
    while q:
        dist,(r,c) = q.pop(0)
        if isinstance(temp_maze[r][c],int):
            continue
        temp_maze[r][c]=dist
        coord.append((r,c))
        for dr,dc in DIRECTIONS:
            next_r=r+dr
            next_c=c+dc
            if temp_maze[next_r][next_c]=="." or temp_maze[next_r][next_c]=="S":
                q.append((dist+1,(next_r,next_c)))
    return temp_maze,coord

def _all_cheats(grid,r,c,offsets: list[tuple[int,int]],thresh=100):
    count=0
    val = grid[r][c]
    threshold=val-thresh
    for dr,dc,md in offsets:
        next_r=r+dr
        next_c=c+dc
        if 0<=next_r<len(grid) and 0<=next_c<len(grid[r]) and grid[next_r][next_c] != "#" and threshold-md>=grid[next_r][next_c]:
            count+=1
    return count

def get_cheat_count(input,cheat_picosecs,threshold):
    maze,coord=_flood_fill_maze(input)
    # pprint(maze)
    # pprint(coord)
    return sum(_all_cheats(maze,r,c,cheat_picosecs,threshold) for r,c in coord)
@timer
def part1():
    global input_grid
    threshold=100
    # print(offsets_at_dist(2))
    print("Part 1:",get_cheat_count(input=input_grid,cheat_picosecs=offsets_at_dist(2),threshold=threshold))
@timer
def part2():
    global input_grid
    threshold=100
    # print(offsets_at_dist(20))
    print("Part 2:",get_cheat_count(input=input_grid,cheat_picosecs=offsets_at_dist(20),threshold=threshold))

part1()
part2()