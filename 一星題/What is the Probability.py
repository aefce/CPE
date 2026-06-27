import sys
lines = sys.stdin.read().splitlines()
num = int(lines[0])
for _ in range(1,num + 1):
    n, p ,i = map(float,lines[_].split())
    if p == 0:
        print("0.0000")
        continue
    r = (1-p) ** n
    a1 = (p) * ((1-p) ** (i -1 ))
    print(f"{a1/(1-r):.4f}")

