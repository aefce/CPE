import sys
data = list(map(int,sys.stdin.read().split()))
for n in data:
    if n == 0:
        break
    if n % 9 != 0:
        print(f"{n} is not a multiple of 9.")
    else:
        degree = 0
        nn = n
        while n % 9 == 0:
            degree += 1
            total = 0
            for i in str(n):
                total += int(i)
            n = total
        print(f"{nn} is a multiple of 9 and has 9-degree {degree}.")