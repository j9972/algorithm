# 실버3 - 1003
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())

    # 0 부분
    d = [0] * 41
    d[0] = 1
    d[1] = 0
    d[2] = 1

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    # 1 부분
    dp = [0] * 41
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(d[n], dp[n])
