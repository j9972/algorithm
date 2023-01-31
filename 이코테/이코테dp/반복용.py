# 개미 전사
import sys
input = sys.stdin.readline

x = int(input())

dp = [0] * 100
data = list(map(int, input().split()))
dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, x):
    dp[i] = max(dp[i-1], dp[i-2]+data[i])
print(dp[x-1])
