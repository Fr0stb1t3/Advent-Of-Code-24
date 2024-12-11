
import copy
from tqdm import tqdm
from collections import Counter


with open("input/input11.txt") as f:
# with open("sample/sample11.txt") as f:
    input_lines = f.read().strip().split()
INPUT=int(input("Number of Iterations:"))
########################ATTTEMPT 1########################################
# BruteForce the hell out of it - Memory death for Iterations Above 30
# print(input_lines)
# mem={}
# starterArr=input_lines
# with tqdm(total=3, desc='level_1', position=0, leave=False) as pbar:
#     for _ in tqdm(range(INPUT)):
#         starterArr=[]
#         correction=0
#         for idx,i in enumerate(input_lines):
#             if i == '0':
#                 starterArr.append('1')
#             elif i in mem:
#                 if type(mem[i]) != str:
#                     v1,v2=mem[i]
#                     starterArr.append(v1)
#                     starterArr.append(v2) 
#                 else:   
#                     starterArr.append(str(mem[i]))
#             elif len(i)%2==0:
#                 val,val2= int(i[:len(i)//2]),int(i[len(i)//2:])
#                 # print(val,val2)
#                 if i not in mem.keys():
#                     mem[i]=(str(val),str(val2))
#                 starterArr.append(str(val))
#                 starterArr.append(str(val2))
#             else:
#                 val = int(i)*2024
#                 if i not in mem.keys():
#                     mem[i]=str(val)
#                 starterArr.append(str(val))
#             # print(idx,i)
#         # print(input_lines)
#         # print(mem)
#         input_lines=starterArr
#         pbar.update()
# print(input_lines)
# print(mem)
# print(len(input_lines))


########################ATTTEMPT 2########################################
# Time to cache

def process(stone):
    if stone == "0":
        return ["1"]
    if len(stone)%2 == 0:
        return [str(int(stone[:len(stone)//2])),str(int(stone[len(stone)//2:]))]
    return [str(int(stone)*2024)]

master=Counter(input_lines)
with tqdm(total=3, desc='level_1', position=0, leave=False) as pbar:
    for _ in tqdm(range(INPUT)):
        currentArr=Counter()
        for stone in master.keys():
            for newStone in process(stone=stone):
                currentArr[newStone]+=master[stone]
        # Updating master
        master=currentArr
        pbar.update()
print(master)
print("Solution:",sum(master.values()))