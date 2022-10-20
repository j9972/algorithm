# 퇴사
import sys
input = sys.stdin.readline

# LIS 증가하는 수열로 풀기
n = int(input())
data = list(map(int, input().split()))
data.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
