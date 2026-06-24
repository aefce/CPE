import sys
lines = sys.stdin.read().splitlines()
lines = lines[::-1]
max_len = 0
for i in lines:
    if len(i) > max_len :
        max_len  =  len(i)
for i in range(max_len):
    out  = ""
    for j in lines:
        if len(j) > i:
            out  += j[i]
        else:
            out += " "
    print(out.rstrip())

