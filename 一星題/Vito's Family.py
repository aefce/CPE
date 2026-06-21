import sys
data = sys.stdin.read().split()
point = 0
num = int(data[point])
point += 1
for _ in range(num):
    number = int(data[point])
    point += 1
    li = []
    for i in range(number):
        li.append(int(data[point]))
        point += 1
    mid = number // 2
    li.sort()
    total = 0
    midnum = li[mid]
    total = sum(abs(x - midnum) for x in li)
    print(total)

