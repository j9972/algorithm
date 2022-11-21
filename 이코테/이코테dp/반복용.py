# 화폐 공사
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# data[i] 는 화폐 종류
data = []
for i in range(n):
    data.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(data[i], m+1):
        if d[j-data[i]] != 10001:
            d[j] = min(d[j], d[j-data[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
