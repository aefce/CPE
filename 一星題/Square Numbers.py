import sys
import math
lines = sys.stdin.read().splitlines()
for i in lines:
    a, b = map(int,i.split())
    if (a, b) == (0, 0):
        break
    print(math.isqrt(b)-math.isqrt(a-1))