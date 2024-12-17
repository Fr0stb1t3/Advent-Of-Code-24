from pprint import pprint
import copy
import multiprocessing
from functools import partial

with open("input/input17.txt") as f:
# with open("sample/sample17.txt") as f:
    (initial_register,program)=f.read().split("\n\n")
    program_initial=program[9:].split(',')
def parse_input():
    global initial_register,program
    initial_register = initial_register.splitlines()
    for idx,line in enumerate(initial_register):
        key,val = line.split(": ")
        initial_register[idx] = int(val)
    program = program[9:].split(',')
    n = len(program)
    program = [(str(program[i]),int(program[i+1])) for i in range(0,n,2)]

parse_input()
registers_p2=copy.copy(initial_register)
print("Initial Register:",initial_register)
print(program)
MOD=8

def part1(seed,program):
    result=[]
    registers=[seed,0,0]

    def combo(oprand):
        if oprand<4:
            return oprand
        if oprand == 4:
            return registers[0]
        if oprand == 5:
            return registers[1]
        if oprand == 6:
            return registers[2]
        
    def adv(oprand,program_counter):
        val = combo(oprand)
        num=2**val
        result = registers[0]//num
        registers[0] = result
        return program_counter+1
    def bxl(oprand,program_counter):
        registers[1] = registers[1]^oprand
        return program_counter+1
    def bst(oprand,program_counter):
        val=combo(oprand)%MOD
        registers[1] = val
        return program_counter+1
    def jnz(oprand,program_counter):
        if registers[0] == 0:
            program_counter+=1
        else:
            #Set program counter
            program_counter=oprand
        return program_counter
    def bxc(program_counter):
        registers[1] = registers[1]^registers[2]
        return program_counter+1
    def out(operand,program_counter):
        val = str(combo(operand)%MOD).split()
        return val,program_counter+1
    def bdv(oprand,program_counter):
        val = combo(oprand)
        num=2**val
        result = registers[0]//num
        registers[1] = result
        return program_counter+1
    def cdv(oprand,program_counter):
        val = combo(oprand)
        num=2**val
        result = registers[0]//num
        registers[2] = result
        return program_counter+1

    program_counter=0
    while program_counter<len(program):
        operation,oprand=program[program_counter]
        # print(program_counter)
        if operation == '0': 
            program_counter=adv(oprand,program_counter) 
            
        elif operation == '1':
            program_counter=bxl(oprand,program_counter)
        elif operation == '2':
            program_counter=bst(oprand,program_counter)
        elif operation == '3':
            program_counter=jnz(oprand,program_counter)
        elif operation == '4':
            program_counter=bxc(program_counter)
        elif operation == '5':
            val,program_counter=out(oprand,program_counter)
            result+=val
        elif operation == '6':
            program_counter=bdv(oprand,program_counter)
        elif operation == '7':
            program_counter=cdv(oprand,program_counter)
    return result,registers

result,registers= part1(initial_register[0],program)
print("Part 1:",",".join(result))
result,registers= part1(117440,program)
print("Part 1:",",".join(result))
# registers = copy.copy(registers_p2)
# result2= part1([])
# print("Part 1:",",".join(result2))
# print(registers_p2)
# registers = copy.copy(registers_p2)
# result2= part1([])
# print("Part 1:",",".join(result2))

# ### PART 2 - Attempt 1: Bruteforce: Didnt work at ALL
# from tqdm import tqdm
# initial_A= registers_p2[0]
# print(program_initial)
# # Match_value=copy.copy(result)
# # print(Match_value)
# registers = copy.copy(registers_p2)
# print(registers)
# # with tqdm(total=3, desc='level_1', position=0, leave=False) as pbar:
# i=8**(len(program_initial)//2)
# # i=0
# while True:
#     registers = copy.copy(registers_p2)
#     registers[0] = i
#     registers_before=copy.copy(registers)
#     # print(registers)
#     value=part1([])
#     # print(result)
#     print('Iteration No:',i,'length of val: ',len(value),"result:",",".join(value),'registers_before:',registers_before,'registers:',registers,end='\r')
#     if value == program_initial:
#         print("\nPART 2:",i)
#         break
#     i+=8**(len(program_initial)//2-1)
    # pbar.update()

#### PART 2 Attempt 2 - Hints from reddit. check the pattern
# import numpy as np
initial_A= registers_p2[0]
print(program_initial)
registers = copy.copy(registers_p2)
print(registers)
seed = 8**(len(program_initial)//2)+initial_A%MOD
print(initial_A,seed)
# seed = 30106357596160 + initial_A%MOD
# after a lot of time: 240850875490665
#                       80000000212926
#                      240000002073196
#Seed No: 240000002073196 length of val:  16 result: 1,3,2,7,2,3,1,7,7,3,3,4,5,5,3,5 registers_before:
# seed = int(1E13)+2*10**13 + 4*10**12
# iteration=0
# while True:
#     seed +=1
#     value,registers=part1(seed,program)
#     print('Seed:',seed,'Iteration No:',iteration,'length of val: ',len(value),"result:",",".join(value),'registers:',registers,end='\r')
#     if value == program_initial:
#         print("\nPART 2:",seed)
#         break
#     iteration+=1

# print("Part 2: ",seed)

if result:
    print("\nPART 2:", result)