import sys
li = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
data = sys.stdin.read().split()
for i in data:
    max_value = 0
    total = 0
    check = 0
    has_found = 0
    for j in range(len(i)):
        f = li.find(i[j]) 
        if  f == -1 and i[j] != "+" and i[j] != "-" :
            check = 1
        else:
            if f!= -1:
                total += f
        if f!= -1 and ((f) + 1) > max_value:
            max_value = f + 1
    if max_value < 2:
        max_value = 2
    for j in range(max_value-1,62):
        if total % j == 0:
            max_value = j + 1 
            has_found = 1
            break
    if check or has_found == 0:
        print("such number is impossible!")
    else:
        print(max_value)