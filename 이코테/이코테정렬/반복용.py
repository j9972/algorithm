# 국영수
import sys
input = sys.stdin.readline

n = int(input())


data = []
for i in range(n):
    data.append(list(input().split()))

data = sorted(data, key=lambda x: (x[0], -int(x[1]), int(x[2]), -int(x[3])))

for i in data:
    print(i[0], end='\n')
