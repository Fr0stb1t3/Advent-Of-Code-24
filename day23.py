from library import timer
from collections import defaultdict as dd
import networkx as nx
from networkx.algorithms import find_cliques
with open("input/input23.txt") as f:
# with open("sample/sample23.txt") as f:
    input_feed=f.read().splitlines()

@timer
def part1():    
    g=dd(set)
    for l in input_feed:
        a,b=l.split("-")
        g[a].add(b)
        g[b].add(a)
    sol=0
    for a in g.keys():
        ag=a.startswith("t")
        for b in g.keys():
            if b not in g[a]:
                continue
            bg = b.startswith("t")
            if a<=b:
                continue
            cs=g[a] & g[b]
            for c in cs:
                if c>a and c>b:
                    if ag or bg or c.startswith("t"):
                        # print(a,b,c)
                        sol+=1
    print("Part 1:",sol)
    return g
@timer
def part2():
    # Using networkx for the find_cliques:
    # https://en.wikipedia.org/wiki/Clique_problem
    g2=nx.Graph()
    for l in input_feed:
        a,b=l.split("-")
        g2.add_edge(a,b)
        g2.add_edge(b,a)
    
    maxC=()
    for c  in find_cliques(g2):
        if len(c)>len(maxC):
            maxC=c
            # print(len(maxC))
    
    print("Part 2:",",".join(sorted(maxC)))
    return g2

part1()
part2()