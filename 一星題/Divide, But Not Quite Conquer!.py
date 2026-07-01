import sys
lines = sys.stdin.read().splitlines()
for i in lines:
    first, second = map(int,i.split())
    li = [first]
    if second <= 1:
        print("Boring")
        continue
    while first % second == 0:
        first //= second
        li.append(first)
    
    if first != 1:
        print("Boring")
    else:
        print(*li)