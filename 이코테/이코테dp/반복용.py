# 못생긴 수
import sys
input = sys.stdin.readline

n = int(input())

i2 = i3 = i5 = 0
next_i2, next_i3, next_i5 = 2, 3, 5

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    dp[i] = min(next_i2, next_i3, next_i5)
    if dp[i] == next_i2:
        i2 += 1
        next_i2 = dp[i2] * 2
    if dp[i] == next_i3:
        i3 += 1
        next_i3 = dp[i3] * 3
    if dp[i] == next_i5:
        i5 += 1
        next_i5 = dp[i5] * 5

print(dp[n-1])
