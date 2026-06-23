import sys

def bangla(n):
    
    if n == 0:
        return ""
    
    res = []

    if n >= 10000000:
        res.append(f"{bangla(n // 10000000)} kuti")
        n %= 10000000
  
    if n >= 100000:
        res.append(f"{n // 100000} lakh")
        n %= 100000
 
    if n >= 1000:
        res.append(f"{n // 1000} hajar")
        n %= 1000
   
    if n >= 100:
        res.append(f"{n // 100} shata")
        n %= 100

    if n > 0:
        res.append(str(n))
        

    return " ".join([x for x in res if x])


data = sys.stdin.read().split()

for idx, num_str in enumerate(data):
    case_num = idx + 1
    n = int(num_str)
    
 
    print(f"{case_num:4d}.", end="")
    
    if n == 0:
        print("0")
    else:
    
        print(f" {bangla(n)}")