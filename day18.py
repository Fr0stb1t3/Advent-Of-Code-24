from collections import deque
from pprint import pprint

with open("input/input18.txt") as f:
# with open("sample/sample18.txt") as f:
    lines=f.read().splitlines()

# N,M = 7,7
byteNumber = 1024
N,M = 71,71
grid=[['.' for j in range(M)] for i in range(N)]

DIRECTIONS=[(0,1),(-1,0),(0,-1),(1,0)]

sx,sy=0,0
ex,ey=N-1,M-1
control="""...#...
..#..#.
....#..
...#..#
..#..#.
.#..#..
#.#....
"""
def simulate(grid,lines,num):
    for z in range(num):
        i,j=lines[z].strip().split(",")
        grid[int(j)][int(i)] = "#"
    return grid

def BFS(grid):
    rows, cols = len(grid), len(grid[0])
    start=(0,0)
    end=(rows-1,cols-1)
    DIRECTIONS=[(-1,0),(0,-1),(0,1),(1,0)]
    visited = set([start])
    queue = deque([(start, 0)])
    
    while queue:
        (x,y),distance = queue.popleft()
        if (x,y) == end:
            # print(visited)
            # print(queue)
            return distance
        for dx,dy in DIRECTIONS:
            nx,ny=dx+x,dy+y

            if (0<=nx<rows and 0<=ny<cols and grid[nx][ny]=='.' and(nx,ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), distance + 1))
                
    return -1


gridNew = simulate(grid,lines,byteNumber)
# pprint(gridNew)
print("\n".join("".join(gridNew[i][j] for j in range(M)) for i in range(N)))
result=BFS(grid=gridNew)
print("Part 1: ",result)
for i in range(byteNumber,len(lines)):
    gridNew = simulate(grid,lines,i)
    distance=BFS(grid=gridNew)
    print("Iteration",i,"distance:",distance,end="\r")
    if distance <0 :
        print("\nPART 2:",lines[i-1]) # i-1 because i prints the next line value
        break
