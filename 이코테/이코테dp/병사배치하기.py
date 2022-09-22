n = int(input())

dp = [1] * (n+1)
data = list(map(int, input().split()))
data.reverse()

for i in range(1, n):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
