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
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] += max(left_down, left_up, left)

res = 0
for i in range(n):
    res = max(res, dp[i][m-1])

print(res)
