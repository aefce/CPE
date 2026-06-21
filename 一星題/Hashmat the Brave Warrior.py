import sys
data = sys.stdin.read().split()
point = 0
while len(data) > point :
    first = int(data[point])
    point += 1
    second = int(data[point])
    point += 1
    print(abs(first - second))
    