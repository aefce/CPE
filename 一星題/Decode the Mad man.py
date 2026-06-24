import sys
chartrans = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
lines = sys.stdin.read().splitlines()
for i in lines:
    line = i.lower()
    out = ""
    for j in range(len(line)):
        if line[j] == " ":
            out += " "
        else:
            out += chartrans[chartrans.find(line[j])-2]
    print(out)
