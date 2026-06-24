import sys
import datetime
lines = sys.stdin.read().splitlines()
num = int(lines[0].strip())
for i in range(1, num+1):
    m,d = map(int,lines[i].split())
    print(datetime.date(2011,m,d).strftime("%A"))