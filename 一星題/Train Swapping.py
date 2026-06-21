import sys
data = sys.stdin.read().split()
point  = 0
num = int(data[point])
point += 1
for _ in range(num):
    train = int(data[point])
    point += 1
    li1 = []
    for i in range(train):
        inp = int(data[point])
        li1.append(inp)
        point += 1
    times = 0
    for j in range(train):
        for i in range(1,train):
            if li1[i] < li1[i-1]:
                times += 1
                li1[i-1],li1[i] = li1[i],li1[i-1]
    print(f"Optimal train swapping takes {times} swaps.")


