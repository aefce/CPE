import sys
data = sys.stdin.read().split()
point = 0
dic = {}
while len(data)> point:
    first = int(data[point])
    point += 1
    second = int(data[point])
    point += 1
    max_length = 0
    for i in range(min(first, second),max(first, second)+1):
        length =  0
        num = i
        while num != 1:
            if num in dic:
                length += dic[num]
                break
            else:
                if num %2 == 0:
                    num //= 2
                    length += 1
                else:
                    num = 3 * num + 1
                    length += 1
        dic[i] = length
        if length > max_length:
            max_length  = length
    print(first, second, max_length+1)
