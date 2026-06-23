import sys
data = sys.stdin.read().split()
point = 0
while len(data) > point:
    n = int(data[point])
    point += 1
    li = []
    for _ in range(n):
        li.append(int(data[point]))
        point += 1
    first = li[0]
    li2 = []
    for i in range(1, n):
        li2.append(abs(first - li[i]))
        first = li[i]
    li2.sort()
    if li2 == list(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")