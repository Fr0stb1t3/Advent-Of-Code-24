from collections import defaultdict as dd
from library import timer
from pprint import pprint
import numpy as np
with open("input/input25.txt") as f:
# with open("sample/sample25.txt") as f:
    lock_and_keys=f.read().split("\n\n")
    locks=[i for i in lock_and_keys if i[0]=="#"]
    keys=[i for i in lock_and_keys if i[-1]=="#"]

def convert_to_heights(entry:str):
    heights=[]
    
    workable=entry.split("\n")
    workable = [list(i) for i in workable]
    matrix=np.array(workable)
    rotated_matrix = np.rot90(matrix, k=-1)
    # pprint(rotated_matrix)
    workable = [''.join(i) for i in rotated_matrix]
    # print(workable)
    for i in workable:
        heights.append(i.count("#")-1)
    # print(heights)
    return heights

def convert_all_keys_and_locks():
    global locks,keys
    lock_heights,key_heights=[],[]
    for i in locks:
        lock_heights.append(convert_to_heights(entry=i))
    for i in keys:
        key_heights.append(convert_to_heights(entry=i))
    
    # pprint(lock_heights)
    # pprint(key_heights)
    return lock_heights,key_heights

def find_unique(height=6):
    lock_heights,key_heights=convert_all_keys_and_locks()
    unique=0
    for i in range(len(lock_heights)):
        for j in range(len(key_heights)):
            flag=True
            for h1,h2 in zip(lock_heights[i],key_heights[j]):
                if int(h1)+int(h2)>=height:
                    # print("Wrong:", lock_heights[i],key_heights[j])
                    flag=False
                    break
            if flag:
                unique+=1
    return unique
@timer
def part1():
    sol=find_unique()
    print("Part 1:",sol)

def part2():
    print("Part 2 is the Journey we went on, all stars collected :)")

part1()
part2()