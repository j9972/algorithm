# 실버 1 - 1309
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[1] = 3
dp[2] = 7
dp[3] = 17
dp[4] = 41

for i in range(5, n+1):
    dp[i] = (dp[i-1] * 2) + dp[i-2]
print(dp[n] % 9901)
