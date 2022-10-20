# 편집거리
import sys
input = sys.stdin.readline

str1 = input()
str2 = input()


def edit(a, b):
    n = len(a)
    m = len(b)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for i in range(1, m+1):
        dp[0][i] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

    return dp[n][m]


print(edit(str1, str2))
