import sys
data = sys.stdin.read().split()
num = int(data[0])
for i in range(1, num + 1):
    b1 = bin(int(data[i])).count("1")
    b2 = bin(int(data[i],16)).count("1")
    print(b1, b2)