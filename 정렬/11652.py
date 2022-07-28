# {} - 딕셔너리 사용하는 문제

import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    data = int(input())
    if data in dic:
        dic[data] += 1
    else:
        dic[data] = 1

dicSorted = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(dicSorted[0][0])
