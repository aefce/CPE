import sys
data  = sys.stdin.read().split()
point = 0
num = int(data[point])
point += 1
dic = {}
while len(data) > point:
    word = data[point].upper()
    point += 1
    for i in word:
        if i.isalpha():
            if  i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
dic = sorted(dic.items(), key = lambda x :(-x[1],x[0]))
for i in dic:
    print(i[0], i[1])