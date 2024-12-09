## Attempted
# from tqdm import tqdm
# pbar = tqdm(total=3, desc='level_1', position=0, leave=False)
# with open("input/input9.txt") as f:
with open("sample/sample9.txt") as f:
    input_lines = f.read().strip()
# print(input_lines)
# encoded_string=[]
# char=0
# flag=True
# for i in input_lines:
#     if flag:
#         encoded_string+=[(char,int(i),str(char)*int(i))]
#         flag = False
#         char+=1
#     else:
#         encoded_string+=[(".",int(i),str(".")*int(i))]
#         flag = True
# print(encoded_string)
# def replacer(s, newstring, index, nofail=False):
#     # raise an error if index is outside of the string
#     if not nofail and index not in range(len(s)):
#         raise ValueError("index outside given string")

#     # if not erroring, but the index is still not in the correct range..
#     if index < 0:  # add it to the beginning
#         return newstring + s
#     if index > len(s):  # add it to the end
#         return s + newstring

#     # insert the new string between "slices" of the original
#     return s[:index] + newstring + s[index + 1:]
# def swap(string,a,b):
#     v1,v2=list(string[a]),string[b]
#     if v1[1]>v2[1]:
#         v1[1]-=v2[1]
#         v1[2]=v1[0]*v1[1]
#         print(v1)
#         string[a]=tuple(v1)
#     elif v1[1]==v2[1]:
#         string.pop(a)    
#     string.pop(b)
#     string.insert(a,v2)
#     return string


# def find_rightmost_char(s,idx=-1):
#     upper = idx if idx != -1 else len(s)
#     for i in range(upper-1,-1,-1):
#         if s[i][0] != '.':
#             return i
#         # pbar.update()
#     return -1
# def find_leftmost_space_greater_than_charlen(s,ln,idx):
#     # print(len(s),idx,ln)
#     for i in range(idx):
#         # print(i,s[i])
#         if str(s[i][0]) == '.' and s[i][1]>=ln:
#             return i
#         # pbar.update()
#         # else:
#         #     print(f"{s[i]} failed for ln {ln}")
#     return None
        
# right=find_rightmost_char(encoded_string)
# left=find_leftmost_space_greater_than_charlen(encoded_string,encoded_string[right][1],right)
# # # encoded_string=swap_v2(encoded_string,left,right)

# print(left,right)
# print(encoded_string)
# while left==None or left<=right:
#     if left != None:
#         encoded_string=swap(encoded_string,left,right)
#         right=find_rightmost_char(encoded_string)
#     else:
#         print("No space found. moving on")
#         right=find_rightmost_char(encoded_string,idx=right)
#     left=find_leftmost_space_greater_than_charlen(encoded_string,encoded_string[right][1],right)

#     print(f"\rleft: {left},right: {right}",end="")


# # # print("\n\n Encoded: " ,''.join(map(str,encoded_string)))
# # sol=0
# # for i,val in enumerate(encoded_string):
# #     if val == ".":
# #         break
# #     sol+=i*int(val)
# # print("\n\nPart 1 Result is: ",sol)


### from online https://github.com/womogenes/AoC-2024-Solutions/blob/main/day_09/p2_day_09.py:
from tqdm import tqdm

with open("input/input9.txt") as f:
# with open("sample/sample9.txt") as f:
    input_lines = f.read().strip()

# Allocate a lot of space
size = [0] * len(input_lines)
loc = [0] * len(input_lines)

def make_filesystem(diskmap):
    global loc, size

    blocks = []

    is_file = True
    id = 0
    for x in diskmap:
        x = int(x)
        if is_file:
            loc[id] = len(blocks)
            size[id] = x
            blocks += [id] * x
            id += 1
            is_file = False
        else:
            blocks += [None] * x
            is_file = True
    
    return blocks

filesystem = make_filesystem(input_lines)

def move(arr):
    # Current file to move
    big = 0
    while size[big] > 0:
        big += 1
    big -= 1

    for to_move in tqdm(range(big, -1, -1)):
        # Find first free space that works
        free_space = 0
        first_free = 0
        while first_free < loc[to_move] and free_space < size[to_move]:
            first_free = first_free + free_space
            free_space = 0
            while arr[first_free] != None:
                first_free += 1
            while first_free + free_space < len(arr) and arr[first_free + free_space] == None:
                free_space += 1
        
        if first_free >= loc[to_move]:
            continue
        
        # Move file by swapping block values
        for idx in range(first_free, first_free + size[to_move]):
            arr[idx] = to_move
        for idx in range(loc[to_move], loc[to_move] + size[to_move]):
            arr[idx] = None
        
    return arr

def checksum(arr):
    ans = 0
    for i, x in enumerate(arr):
        if x != None:
            ans += i * x
    return ans

moved = move(filesystem)

print(checksum(moved))
