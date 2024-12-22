from collections import Counter
from functools import cache
from library import timer
with open("input/input22.txt") as f:
# with open("sample/sample22.txt") as f:
    input_feed=f.read().splitlines()

mem={}


# @cache    # Caching was slower
def calculate_secret(val):
    MOD=16777216
    #ACTION 1
    secret=val*64
    secret = val^secret
    secret = secret%MOD
    # print(secret)
    #ACTION 2
    secret2 = int(secret/32)
    # print("Div",str(secret//32),"Round",secret2)
    secret = secret^secret2
    secret = secret%MOD
    # print(secret)
    #ACTION 3
    secret3 = secret*2048
    secret = secret^secret3
    secret = secret%MOD
    # print(secret,secret3)
    return secret

def calculate_iterative_secret(val,iterations):
    secret=val
    for _ in range(iterations):
        if secret in mem:
            secret = mem[secret]
        else:
            curval=secret
            secret = calculate_secret(secret)
            mem[curval] = secret
        # print(secret)
    return secret

# print(calculate_iterative_secret(2024,2000))
# print(calculate_secret(123))
def calculate_sequence_secret(val,iterations,sequences):
    secret=val
    last=secret%10
    seen=set()
    changes=[]    
    for _ in range(iterations):
        if secret in mem:
            secret = mem[secret]
        else:
            curval=secret
            secret = calculate_secret(secret)
            mem[curval] = secret
        price=secret%10
        diff = price-last
        last=price
        changes.append(diff)
        if len(changes)>=4:
            seq=tuple(changes[-4:])
            if seq not in seen:
                seen.add(seq)
                sequences[seq] += price
        # print(secret)
    return sequences
@timer
def part1():
    sol=0
    for i in input_feed:
        sol+=calculate_iterative_secret(int(i),2000)
    print("Part 1:",sol)
@timer
def part2():
    sequences = Counter()
    for i in input_feed:
        sequences = calculate_sequence_secret(int(i),2000,sequences)
    print("Part 2:",sequences.most_common(1)[0][1])

part1()
part2()