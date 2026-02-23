#count of numbers without repeated digits
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

count = 0

for i in range(n1, n2 + 1):
    temp = i
    digits = []

    while temp > 0:
        d = temp % 10
        if d in digits:
            break
        digits.append(d)
        temp //= 10
    else:
        count += 1

print(count)
     