import sys
from collections import Counter
lines = sys.stdin.read().splitlines()
for i in range(0, len(lines), 2):
    if i + 1 >= len(lines): break
    
    s1 = Counter(lines[i])
    s2 = Counter(lines[i+1])
    
    common = s1 & s2
    
    print("".join(sorted(common.elements())))