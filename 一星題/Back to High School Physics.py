import sys
lines = sys.stdin.read().splitlines()
for i in lines:
    v, t = map(int,i.split())
    print(int(v*t*2))