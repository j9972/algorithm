# 실버3
import sys
input = sys.stdin.readline

n = int(input())
ans = 0
data = []
for i in range(n):
    data.append(int(input()))

data.reverse()

ans = data[0]
for i in range(1, n-1):
    ans += max(data[i], data[i+1])

print(ans)
