# 실버2 - 110053
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [1] * (n+1)

for i in range(n):  # 현재 위치
    for j in range(i):  # 이전을 의미
        if data[i] > data[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))
