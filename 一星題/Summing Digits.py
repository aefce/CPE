import sys
data = sys.stdin.read().split()
for i in range(len(data)):
    n = data[i]
    if n == "0":
        break
    while len(n) != 1:
        total = 0
        for j in range(len(n)):
            total += int(n[j])
        n  = str(total)
    print(n)