from collections import defaultdict
from pprint import pprint
with open("input/input13.txt") as f:
# with open("sample/sample13.txt") as f:

    lines=f.read().splitlines()
    for line in lines:
        if line == '':
            lines.remove(line)

# pprint(lines)
def section(a,b,res):
    eq={}
    if "A" in a:
        a=a[10:].split(",")
        X=a[0][2:]
        Y=a[1].strip()[2:]
        # print(f"A = [{X},{Y}]")
        eq['A']=(int(X),int(Y))

    if "B" in b:
        b=b[10:].split(",")
        X=b[0][2:]
        Y=b[1].strip()[2:]
        # print(f"B = [{X},{Y}]")
        eq['B']=(int(X),int(Y))
    if "Prize:" in res:
        res=res[7:].split(",")
        X=res[0][2:]
        Y=res[1].strip()[2:]
        # print(f"Res = [{X},{Y}]")
        eq['Prize']=(int(X),int(Y))
    # print("Section:",a,b,res)
    return eq

def tokens(A,B):
    return (A*3+B)

def calculate(equation,part2=False):
    ax,ay,bx,by=equation['A'][0],equation['A'][1],equation['B'][0],equation['B'][1]
    cx,cy=equation['Prize'][0],equation['Prize'][1]
    if part2:
        cx+=10000000000000
        cy+=10000000000000
    A = abs(ax*by - bx*ay)
    C= abs(cx*by - cy*bx)
    # print("A:",A,"C:",C)
    if C%A == 0:
        # print("Divisible")
        valA=C//A
        # if valA>100:
        #     print("Value of A greater than 100, returning 0")
        #     return 0
        valB=(cx-(valA*ax))//bx
        # print("Result:",valA,valB)
        return tokens(valA,valB)
    else:
        # print("Not divisible")
        return 0
total_tokens_p1=0
total_tokens_p2=0
print("Number of Sections:",(len(lines)//3))
for i in range(0,len(lines),3):
    equation=section(lines[i],lines[i+1],lines[i+2])
    # print(equation)
    val = calculate(equation)
    total_tokens_p1+=val
    val = calculate(equation,part2=True)
    total_tokens_p2+=val

print('Total Tokens Part1:',total_tokens_p1)
print('Total Tokens Part2:',total_tokens_p2)