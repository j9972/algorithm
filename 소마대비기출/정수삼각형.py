# 실버 - 1932
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dp = [0] * (n+1)

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        dp[i][j] = data[i][j] + max(data[i-1][j], data[i-1][j-1])

print(dp[n-1][n-1])
