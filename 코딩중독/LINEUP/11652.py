import sys
n = int(sys.stdin.readline())
data_dic = {}

for i in range(n):
    data = int(sys.stdin.readline())
    if data in data_dic:
        data_dic[data] += 1
    else:
        data_dic[data] = 1

dic = sorted(data_dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])
