import sys
lines = sys.stdin.read().splitlines()
point = 0
num = int(lines[point].strip())
point += 1
def base10_to_n(num, base):
    out = []
    while num >= base:
        reminder = num % base 
        num = num // base
        out.append(reminder)
    out.append(num)
    return out
for i in range(num):
    if i != 0:
        print()
    print(f"Case {i+1}:")
    li = []
    for j in range(4):
        l = list(lines[point].split())
        for k in l:
            li.append(int(k))
        point += 1
    time = int(lines[point].strip())
    point += 1
    for j in range(time):
        out = []
        n = int(lines[point].strip())
        point += 1

        if n == 0:
                all_bases = [str(b) for b in range(2, 37)]
                outlist_str = " ".join(all_bases)
                print(f"Cheapest base(s) for number 0: {outlist_str}")
                continue
        for k in range(2,37):
            total = 0
            l = base10_to_n(n,k)
            for m in l:
                total += li[m]
            out.append(total)
        min_num = min(out)
        count = out.count(min_num)
        outlist = []
        p = 0
        for k in range(count):
            p = out[p:].index(min_num) + p
            outlist.append(p+2)
            p+=1
        outlist = " ".join(outlist)
        print(f"Cheapest base(s) for number {n}: {outlist}")

