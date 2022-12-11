# 국영수
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(str, input().split())))

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in data:
    print(i[0], end='\n')
