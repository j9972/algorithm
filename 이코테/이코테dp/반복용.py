# 금광
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    dp = []
    idx = 0
    for i in range(n):
        dp.append(data[idx:idx+m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]

            # dp[i][j] 왼쪽에서 오기전까지의 최대값
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)
    res = 0
    for i in range(n):
        res = max(res, dp[i][m-1])

    print(res)
