import sys
lines  = sys.stdin.read().splitlines()
for i in lines:
    if not i.strip():
        continue
    first, second =i.split()
    first = first[::-1]
    second = second[::-1]
    if (first,second) == ("0","0"):
        break
    length = max(len(first), len(second))
    oper = 0
    add = 0
    for j in range(length):
        if len(first) > j :
            f = int(first[j])
        else:
            f = 0
        if len(second) > j :
            s = int(second[j])
        else:
            s = 0
        if add + s + f >= 10:
            add = 1
            oper += 1
        else:
            add = 0
    if oper == 0:
        print("No carry operation.")
    elif oper == 1:
        print("1 carry operation.")
    else:
        print(f"{oper} carry operations.")