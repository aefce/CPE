import sys
lines = sys.stdin.read().splitlines()
num = int(lines[0].strip())
for i in range(1,num + 1):
    add, sub = map(int,lines[i].split())
    if add >= sub:
        one =  (add + sub) / 2
        if one % 1 == 0:
            other = add - one
            print(int(max(one, other)), int(min(one,other)))
        else:
            print("impossible")
    else:
        print("impossible")