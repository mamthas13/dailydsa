arr = [2, 3, -8, 7, -1, 2, 3]

res = arr[0]   # store maximum subarray sum

for i in range(len(arr)):
    currSum = 0

    for j in range(i, len(arr)):
        currSum += arr[j]

        # Manual comparison instead of max()
        if currSum > res:
            res = currSum

print(res)