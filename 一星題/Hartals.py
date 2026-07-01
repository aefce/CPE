import sys
data = list(map(int,sys.stdin.read().split()))
point = 0
time = data[point]
point += 1
for i in range(time):
    day = data[point]
    point += 1
    party_n = data[point]
    point += 1
    l = []
    for j in range(party_n):
        l.append(data[point])
        point += 1
    s = set()
    for j in range(1,day + 1):
        for k in l:
            if j % k == 0:
                s.add(j)
        if j % 7 == 6 or j %7 == 0:
            if j in s:
                s.remove(j)
    print(len(list(s)))