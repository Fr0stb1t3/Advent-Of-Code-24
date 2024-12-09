

from collections import defaultdict
from itertools import combinations

def parse_lines(filename):
    with open(filename, "r") as f:
        return f.read().strip().split("\n")
    
input = parse_lines("input/input8.txt")
# input = parse_lines("sample/sample8.txt")

n = len(input)

def in_bounds(a,b):
    return 0 <= a< n and 0<= b < n

def anti_node(a,b):
    ax,ay=a
    bx,by=b
    cx,cy=ax-(bx-ax),ay-(by-ay)
    dx,dy=bx+(bx-ax),by+(by-ay)

    if in_bounds(cx,cy):
        yield (cx,cy)
    if in_bounds(dx,dy):
        yield (dx,dy)

def anti_node_p2(a,b):
    ax,ay=a
    bx,by=b
    dx,dy = bx - ax , by - ay

    i=0
    while True:
        if in_bounds(ax-dx*i,ay-dy*i):
            yield (ax-dx*i,ay-dy*i)
        else:
            break
        i+=1
    
    i=0
    while True:
        if in_bounds(bx+dx*i,by+dy*i):
            yield (bx+dx*i,by+dy*i)
        else:
            break
        i+=1

antinodes=set()
antinodes_p2=set()
all_locs=defaultdict(list)
for i in range(n):
    for j in range(n):
        if input[i][j] != ".":
            all_locs[input[i][j]].append((i,j))
for freq in all_locs:
    locs = all_locs[freq]
    for a,b in combinations(locs,r=2):
        for anti in anti_node(a,b):
            antinodes.add(anti)
        
        for anti in anti_node_p2(a,b):
            antinodes_p2.add(anti)

print(len(antinodes))
print(len(antinodes_p2))
