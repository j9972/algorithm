# 실버 - 1932
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = data[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = data[i-1][j]
        data[i][j] += max(up, left_up)

print(max(data[n-1]))
