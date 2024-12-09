from collections import Counter
col_A,col_B=[],[]
# with open('sample1.txt', 'r') as file:
with open('input1.txt', 'r') as file:
    for line in file:
        columns = line.strip().split()  # Split the line into columns
        if len(columns) >= 2:
            col1 = columns[0]
            col2 = columns[1]
            col_A.append(int(col2))
            col_B.append(int(col1))
    
    # print(col_B,"\n\n ########### \n\n",col_A)
    col_A.sort()
    col_B.sort()
    print(col_A,"\n\n ########### \n\n",col_B)
    res=[abs(x-y) for x,y in zip(col_A,col_B)]
    print(res)
    sol=sum(res)
    print(sol)

    ##PART 2
    freq=Counter(col_B)
    print(freq)
    sol2=0
    for i in col_A:
        sol2+= i*freq.get(i,0)
    print("Freqcount sum: ",sol2)

