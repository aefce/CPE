import sys
data = sys.stdin.read().split()
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in data:
    n = int(i)
    if prime(n):
        if str(n)!=str(n)[::-1] and prime(int(str(n)[::-1])):
            print(f"{n} is emirp.")
        else:
            print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")