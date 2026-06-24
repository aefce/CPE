import sys
lines = sys.stdin.read().splitlines()
flip = 0
for i in lines:
    out = ""
    for j in range(len(i)):
        if i[j] == '"':
            if flip :
                out += "''"
                flip = 0
            else:
                out += "``" 
                flip = 1
        else:
            out += i[j]
    print(out)