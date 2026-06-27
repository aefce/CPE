import sys
data = list(map(int,sys.stdin.read().split()))
num = data[0]
i = 1
for j in range(1,len(data),2):
    fp = data[j]
    sp = data[j + 1]
    total = 0
    for k in range(fp,sp+1):
        if k % 2 == 1:
            total += k
    print(f"Case {i}: {total}")
    i += 1