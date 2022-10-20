# 퇴사
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

t = []
p = []

for i in range(n):
    time, price = map(int, input().split())
    t.append(time)
    p.append(price)

mv = 0
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(dp[time] + p[i], mv)
        mv = dp[i]
    else:
        dp[i] = mv
print(mv)
