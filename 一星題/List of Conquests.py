import sys
lines =  sys.stdin.read().splitlines()
num =  int(lines[0].strip())
dic = {}
for i in range(num):
    row = lines[i + 1].strip().split()[0]
    dic[row] = dic.get(row, 0) + 1
dic = sorted(dic.items(),key = lambda x:x[0])
for i in dic:
    print(i[0],i[1])
