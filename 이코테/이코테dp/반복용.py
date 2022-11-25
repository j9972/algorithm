# 금광
import sys
input = sys.stdin.readline

n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i):
        if i == 0:
            left = 0
        else:
            left = dp[i-1][j-1]

        if i == j:
            up = 0
        else:
            up = dp[i-1][j]

        dp[i][j] += max(left, up)

print(max(dp[n-1]))
