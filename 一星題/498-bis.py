import sys
lines = sys.stdin.read().splitlines()
for i in range(0,len(lines),2):
    num = int(lines[i])
    li = list(map(int,lines[i+1].split()))
    li.reverse()
    total = 0
    for j in range(1,len(li)):
        total += li[j] * j * num ** (j-1)
    print(total)

