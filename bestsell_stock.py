pr = [7, 10, 1, 3, 6, 9, 2]
temp = 0
for i in range(len(pr)):
    for j in range(i +1,len(pr)):
        t = pr[j]-pr[i]
        if t > temp:
            temp = t
print(temp)