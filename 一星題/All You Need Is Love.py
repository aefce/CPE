import sys
import math
data = sys.stdin.read().split()
point = 0
num = int(data[point])
point += 1
for i in range(num):
    f = data[point]
    point  += 1
    n1 = int(f, 2)
    s = data[point]
    point += 1
    n2 = int(s ,2)
    if math.gcd(n1, n2) == 1:
        print(f"Pair #{i + 1}: Love is not all you need!")
    else:
        print(f"Pair #{i + 1}: All you need is love!")