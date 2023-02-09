#실버2 - 1965
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [1] * n

for i in range(1, n):
    for j in range(i):  # 전 위치
        if data[i] > data[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))
