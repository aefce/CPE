import sys
lines = sys.stdin.read().splitlines()
def total(s,n):
    return(s+n) * (n-s + 1)// 2
for line in lines:
    if not line.strip():
        continue
    s,d = map(int,line.split())
    left = s
    right = 2 * 10 ** 8
    ans = s
    while left <= right :
        mid = (left + right) // 2
        if total(s,mid) >= d:
            ans = mid
            right = mid -1
        else:
            left = mid + 1
    print(ans)

