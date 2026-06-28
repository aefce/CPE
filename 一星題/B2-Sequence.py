import sys
data = list(map(int,sys.stdin.read().split()))
point = 0
c = 1
while len(data) > point:
    check = 0
    num = data[point]
    point += 1
    li = []
    for i in range(num):
        inp = data[point]
        li.append(inp)
        point += 1
        if inp <1:
            check = 1
    if len(li) != len(set(li)):
        check = 1
    li1 = list(sorted(li))
    if li != li1:
        check = 1
    s = set()
    for i in range(len(li)):
        for j in range(i,len(li)):
            inp  = li[i] + li[j] 
            if inp in s:
                check = 1
                break
            else:
                s.add(inp)
        if check:
            break
    if check == 0:     
        print(f"Case #{c}: It is a B2-Sequence.")
    else:
        print(f"Case #{c}: It is not a B2-Sequence.")
    print()
    c += 1

    