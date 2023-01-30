import sys
input = sys.stdin.readline

n = int(input().rstrip())

data = []
for i in range(n):
    rgb = list(map(int, input().rstrip().split()))
    data.append(rgb)

dp = [[] for _ in range(n)]
dp[0] = data[0]

for i in range(1, n):
    dp[i] = [
        data[i][0] + min(data[i-1][1], data[i-1][2]),
        data[i][1] + min(data[i-1][0], data[i-1][2]),
        data[i][2] + min(data[i-1][1], data[i-1][0])
    ]
print(min(dp[n-1]))
