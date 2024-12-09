def remove_one_to_sort(nums):
    """Removes one element from the list to make it sorted."""

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            # Try removing nums[i]
            temp = nums[:i] + nums[i + 1:]
            if temp == sorted(temp):
                # print(temp)
                return nums[:i] + nums[i + 1:],True

            # Try removing nums[i + 1]
            temp = nums[:i + 1] + nums[i + 2:]
            if temp == sorted(temp):
                # print(temp)
                return nums[:i + 1] + nums[i + 2:],True

    # List is already sorted
    return nums,False

# nums= [1, 3, 2,5, 4]
# print(nums)
# result,flag  = remove_one_to_sort(nums)
# print(result,flag)

allcols=[]
with open('sample/sample2.txt', 'r') as file:
# with open('input/input2.txt', 'r') as file:
    for line in file:
        # print(line)
        columns = line.strip().split()  # Split the line into columns
        # print(columns)
        allcols.append([int(x) for x in columns])

print(allcols)
safe=0
threshold=3
for i in allcols:
    # print(sorted(i))
    if (sorted(i) != i and sorted(i) != i[::-1]):
        val1,f1=remove_one_to_sort(i)
        val2,f2=remove_one_to_sort(i[::-1])
        print(val1,val2)
        if f1 == f2 == False:
            print("Unsafe one found: ",i)
            continue
        else:
            print("safe after sort ")
            flag=True
            i = val1 if f1 else val2
            print(i)
            for j in range(len(i)-1):
                if i[j] == i[j+1]:
                    # print("Unsafe, same val",i[j],i[j+1])
                    flag=False
                    continue
                elif (abs(i[j] - i[j+1])>3 ):
                    # print("Unsafe, Diff > 3: ",i[j],i[j+1])
                    flag=False
                    continue
            if flag:
                safe+=1
        
    else:
        flag=True
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                # print("Unsafe, same val",i[j],i[j+1])
                val1,f1=remove_one_to_sort(i)
                val2,f2=remove_one_to_sort(i[::-1])
                print(val1,val2)
                print(f1,f2)
                
                if f1 == f2 == False:
                    print("Unsafe one found: ",i)
                    flag=False
                    continue
                else:
                    print("safe after sort ",val1)
                    check = val1 if f1 else val2
                    print(check)
                    if (abs(check[j] - check[j+1])>3 ):
                        flag=False
                        continue

                
            elif (abs(i[j] - i[j+1])>3 ):
                # print("Unsafe, Diff > 3: ",i[j],i[j+1])
                flag=False
                continue
        if flag:
            safe+=1
print("safe number :",safe )
