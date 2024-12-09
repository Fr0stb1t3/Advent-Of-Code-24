import re
# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))_don't()_remove_this_do()_and_this_do()"

# # Pattern to match everything between 'don't()' and 'do()'
# pattern = r'don\'t\(\).*?do\(\)'

# # Find all matches
# matches = list(re.finditer(pattern, text))
# print(matches)

# if matches:
#     # Get the last match
#     last_match = matches[-1]
#     # Create a new string without the last matched section
#     result = text[:last_match.start()] + text[last_match.end():]
# else:
#     result = text  # No matches found
# print("*************************")
# print(result,"\n",text)

pattern=r'mul\((\d+),(\d+)\)'
Removal=r'don\'t\(\).*?do\(\)'
lines_of_hell=[]
# with open('sample/sample3.txt', 'r') as file:
with open('input/input3.txt', 'r') as file:
    for line in file:
        lines_of_hell.append(line.strip())

sol=0
sol2=0
n=len(lines_of_hell)
for i,line in enumerate(lines_of_hell):
    # print(line)
    # newline=re.sub(Removal,"",line)
    # print(newline)
    match=re.findall(pattern,line)
    # print(match)
    if match != None:
        for tup in match:
            sol += int(tup[0])*int(tup[1])
    
    #Part 2
       
    # matches = list(re.finditer(Removal, line))

    # if matches:
    #     # Get the last match
    #     last_match = matches[-1]
    #     # Create a new string without the last matched section
    #     newline = line[:last_match.start()] + line[last_match.end():]
    # else:
    #     newline = line  # No matches found  
    # match=re.findall(pattern,newline)
    # # print(match)
    # if match != None:
    #     for tup in match:
    #         sol2 += int(tup[0])*int(tup[1])

#Part 2
pattern=r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
match =  re.findall(pattern,lines_of_hell[0])
flag=True
for m in match:
    if m == "do()":
        flag=True
    elif m == "don't()":
        flag=False
    else:
        if flag:
            n1,n2=map(int,m[4:-1].split(","))
            sol2+=n1*n2


    
print("Solution: ",sol)
print("Solution2: ",sol2)