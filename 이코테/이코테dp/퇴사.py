n = int(input())

dp = [0] * (n+1)
t = []
p = []

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

mv = 0

for i in range(n-1, -1, -1):
    time = t[i] + iㅇㅌㅊ
    if time <= n:
        dp[i] = max(p[i] + dp[time], mv)
        mv = dp[i]
    else:
        dp[i] = mv

print(mv)
