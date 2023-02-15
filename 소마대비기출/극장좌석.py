# 실버 1 - 2302
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if n >= 2:
    d = [i for i in range(1, n+1)]

    for i in range(m):
        data = int(input())
        d[data-1] = 0

    res = []
    cnt = 0
    for i in range(n):
        if d[i] != 0:
            cnt += 1
            if i == n-1:
                res.append(cnt)
        else:
            res.append(cnt)
            cnt = 0

    dp = [1] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    ans = 1
    for i in res:
        ans *= dp[i]
    print(ans)
else:
    for _ in range(m):
        v = int(input())
    print(1)
