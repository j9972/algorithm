# 금광
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    index = 0
    dp = []
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # left up
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            # left_down
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]
            dp[i][j] += max(left_up, left_down, left)

    res = 0
    for i in dp:
        res = max(res, max(i))
    print(res)
