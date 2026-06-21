import sys
from collections import Counter
data = sys.stdin.read().splitlines()
first_case = True
for word in data:
    if not word.strip():
        continue
    if not first_case:
        print()
    first_case = False
    freq = Counter(word)
    freq = sorted(freq.items(), key = lambda x:(x[1],-ord(x[0])))
    for i in freq:
        print(ord(i[0]),i[1])