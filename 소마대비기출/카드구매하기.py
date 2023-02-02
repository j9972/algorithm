# 실버 1 - 11052 - 다시
import sys
input = sys.stdin.readline

n = int(input())
data = [0] + list(map(int, input().split()))
d = [0] * (n+1)
d[0] = 0
d[1] = data[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if d[i] < d[i-j] + data[j]:
            d[i] = d[i-j] + data[j]

print(d[n])
