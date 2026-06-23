import sys
data = sys.stdin.read().split()
for i in range(0,len(data)):
    if data[i] == "0":
        break
    if int(data[i]) % 11 == 0 :
        print(f"{data[i]} is a multiple of 11.")
    else:
        print(f"{data[i]} is not a multiple of 11.")