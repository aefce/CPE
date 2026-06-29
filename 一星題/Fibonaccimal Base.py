import sys
data = list(map(int,sys.stdin.read().split()))
num = data[0]
l = [1,2,3,5]
s = sum(l)
for i in range(1,num + 1):
    n = data[i]
    nn = data[i]
    while n > s:
        add = l[-2]+l[-1]
        l.append(add)
        s += add
    out = ""
    l1 = l[::-1]
    for j in l1:
        if n >= j:
            out += "1"
            n -= j
        else:
            out += "0"
    if nn == 0:
        print(f'{nn} = "0" (fib)')
    else:
        print(f"{nn} = {out.lstrip("0")} (fib)")
