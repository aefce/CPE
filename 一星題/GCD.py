import sys
import math
data = list(map(int,sys.stdin.read().split()))
for i in data:
    if i == 0:
        break
    else:
        g = 0
        for j in range(1, i):
            for k in range(j+1,i+1):
                g += math.gcd(j, k)
        print(g)