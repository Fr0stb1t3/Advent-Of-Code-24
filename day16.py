from collections import defaultdict
import heapq
import os,time
with open("input/input16.txt") as f:
# with open("sample/sample16.txt") as f:
    grid=f.read().splitlines()

n,m=len(grid),len(grid[0])
sx,sy,ex,ey=0,0,0,0

for i in range(n):
    for j in range(m):
        if grid[i][j]=="S":
            sx,sy=i,j
        elif grid[i][j]=="E":
            ex,ey=i,j
sd = 0
DIRECTIONS=[(0,1),(-1,0),(0,-1),(1,0)]

def adjacents(cur):
    cx,cy,cd= cur
    yield 1000,(cx,cy,(cd-1)%4)
    yield 1000,(cx,cy,(cd+1)%4)
    
    dx,dy = DIRECTIONS[cd]
    nx,ny=cx+dx,cy+dy
    if grid[nx][ny] != "#":
        yield 1,(nx,ny,cd)

#### Digikstras algo
pq=[]
start=(sx,sy,sd)
p1=None
heapq.heappush(pq,(0,start))
distances=defaultdict(lambda: float("inf"))
from_ = defaultdict(lambda: set())

while len(pq)>0:
    dist,cur=heapq.heappop(pq)
    (cx,cy,cd) = cur
    if (cx,cy) == (ex,ey):
        if p1 is None:
            p1=dist
            print("Part1: ",dist)
            # break
    for d,adj in adjacents(cur):
        if dist+d  < distances[adj]:
            distances[adj] = dist+d
            heapq.heappush(pq,(distances[adj],adj))
            from_[adj]={cur}
        elif dist+d <= distances[adj]:
            from_[adj].add(cur)

### PART 2 ###

for dr in range(4):
    print(dr,distances[(ex,ey,dr)])

stack=[(ex,ey,1)]
good_nodes=set(stack)
while len(stack)>0:
    s = stack.pop(-1)
    for other in from_[s]:
        if other  not in good_nodes:
            good_nodes.add(other)
            stack.append(other)
    ## Print gird trace in real time
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print("\n" * 100)
    # temp_node=set(x[:2] for x in good_nodes)
    # visual = "\n".join("".join(grid[i][j] if (i,j) not in temp_node else "\033[32m0\033[0m" for j in range(m)) for i in range(n))
    # print(visual)
    # time.sleep(0.1)
good_nodes= set(x[:2] for x in good_nodes)
print("Part 2: ",len(good_nodes))

### Visualization of Final path
visual = "\n".join("".join(grid[i][j] if (i,j) not in good_nodes else "\033[32m0\033[0m" for j in range(m)) for i in range(n))
print(visual)