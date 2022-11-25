# 병사 배치
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.reverse()

# LIS
dp = [1]*n
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:  # j가 i보다 앞임
            dp[i] += max(dp[i], dp[j]+1)

print(n-max(dp))
