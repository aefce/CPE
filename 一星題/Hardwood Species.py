import sys
first = 1
data = sys.stdin.read().splitlines()
point = 0
num = int(data[point])
point += 1
for _ in range(num):
    if not first:
        print()
        first = 0
    point += 1
    dic = {}
    count = 0
    while   point < len(data) and data[point].strip() != "":
        if data[point] in dic:
            dic[data[point]] += 1
        else:
            dic[data[point]] = 1
        count += 1
        point += 1
    dic = sorted(dic.items(), key  = lambda x:(x[0]))
    for i in dic:
        print(f"{i[0]} {i[1]/count*100:.4f}")