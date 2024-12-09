import pandas as pd
import numpy as np
# lines_of_hell=[]
# with open('sample4.txt', 'r') as file:
# # with open('input4.txt', 'r') as file:
#     for line in file:
#         lines_of_hell.append(line.strip().split())

from typing import Dict, Tuple, Set
import numpy as np

def parse_input() -> Dict[str, Set[Tuple[int, int]]]:
    with open("sample/sample4.txt") as f:
    # with open("input/input4.txt") as f:
        data = f.read().splitlines()

        occ = {letter: set() for letter in {"X", "M", "A", "S"}}
        for i in range(len(data)):
            for j in range(len(data[i])):
                occ[data[i][j]].add((i, j))

        return occ

def find_xmas_occurrences(occ: Dict[str, Set[Tuple[int, int]]]) -> int:
    total = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for i, j in occ["X"]:
        total += sum(
            [
                (tuple(np.add((i, j), d)) in occ["M"])
                and (tuple(np.add((i, j), np.multiply(2, d))) in occ["A"])
                and (tuple(np.add((i, j), np.multiply(3, d))) in occ["S"])
                for d in directions
            ]
        )

    return total

def find_crossed_mas_occurrences(occ: Dict[str, Set[Tuple[int, int]]]) -> int:
    total = 0
    for i, j in occ["A"]:
        b = np.array(
            [
                [(i - 1, j - 1), (i + 1, j - 1)],
                [(i - 1, j + 1), (i + 1, j + 1)]
            ]
        )

        total += sum(
            [
                set(map(tuple, rm[0])).issubset(occ["M"]) and 
                set(map(tuple, rm[1])).issubset(occ["S"])
                for rm in [np.rot90(b, k) for k in range(0, 4)]
            ]
        )
    return total

arr=parse_input()
print(arr)
p1=find_xmas_occurrences(arr)
print("Part1:",p1)
p2=find_crossed_mas_occurrences(arr)
print("Part2:",p2)
#  newlines_of_hell=np.array(lines_of_hell)
# def check_along(chars):
#     #Function to check length wise
#     strCheck="".join(chars)
#     c1=strCheck.count("XMAS")
#     c2=strCheck.count("SAMX")

#     return c1+c2

# def check_diagonal(lines,i,j):
#     #Function to check length wise
#     pass
# # pattern='XMAS|SAMX'
# n,m=len(lines_of_hell),len(lines_of_hell[0])
# x=len(newlines_of_hell)
# res=0
# # screw Regex. we go bruteforece
# for i in range(n):
#     res+=check_along(lines_of_hell[i])
#     print("Inside loop:",res)
# for i in range(x):
#     res+=check_along(newlines_of_hell[i])
# print(x)
# print(newlines_of_hell)
# print(res)
    