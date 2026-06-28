import sys
lines = sys.stdin.read().splitlines()
point = 0
num = int(lines[point])
point += 1
for i in range(num):
    n = lines[point].split()
    point += 1
    n = int(n[-1])
    li = []
    check = 0
    for j in range(n):
        line = lines[point].strip().split()
        for k in line:
            li.append(k)
            if "-" in k:
                check = 1
        point += 1
    if li == li[::-1] and check == 0:
        print(f"Test #{i+1}: Symmetric.")
    else:
        print(f"Test #{i+1}: Non-symmetric.")