# 실버3-> 2579
import sys
input = sys.stdin.readline

n = int(input())
data = [0]
for i in range(n):
    data.append(int(input().rstrip()))

if n == 1:
    print(data[1])
else:
    dp = [0] * (n+1)
    dp[1] = data[1]
    dp[2] = data[1] + data[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + data[i] + data[i-1], dp[i-2] + data[i])
    print(dp[n])
