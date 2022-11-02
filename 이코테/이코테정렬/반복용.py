# 위에서 아래로
import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

dataArr = sorted(data, reverse=True)

for i in range(len(dataArr)):
    print(dataArr[i], end=' ')
