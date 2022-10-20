# 못생긴수
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * n  # 1차원
dp[0] = 1

idx2 = idx3 = idx5 = 0

# 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        idx2 += 1
        next2 = dp[idx2] * 2
    if dp[i] == next3:
        idx3 += 1
        next3 = dp[idx3] * 3
    if dp[i] == next5:
        idx5 += 1
        next5 = dp[idx5] * 5

print(dp[n-1])
