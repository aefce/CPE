import sys
data = list(map(int,sys.stdin.read().split()))
for i in data:
    if i == 0:
        break  
    b = bin(i)
    c = b.count("1")
    print(f"The parity of {b[2:]} is {c} (mod 2)")