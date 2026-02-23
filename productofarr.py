#arr = [10, 3, 5, 6, 2]
#num = []
#temp = 1
#for i in range(len(arr)):
 #   for j in range(len(arr)):
   #     temp *= arr[j]
    #num.append(temp)
#print(num)
arr = [10, 3, 5, 6, 2]
res = []

for i in range(len(arr)):
    temp = 1   # reset for every i
    for j in range(len(arr)):
        if i != j:     # skip same index
            temp *= arr[j]
    res.append(temp)

print(res)