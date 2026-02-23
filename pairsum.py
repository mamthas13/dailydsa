#Pair with the given Sum
arr = [1, -2, 1, 0, 5]
target = 0

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):   
        if arr[i] + arr[j] == target:
            found = True
            break
    if found:
        break

print(found)
    
 
