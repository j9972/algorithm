#실버1 - 1890
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

d = [[0] * n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == j == n-1:
            print(d[i][j])
            exit(0)

        dist = data[i][j]
        if dist + i < n:
            d[i+dist][j] += d[i][j]
        if dist + j < n:
            d[i][j+dist] += d[i][j]
