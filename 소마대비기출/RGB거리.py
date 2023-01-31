#실버1 - 1149
import sys
input = sys.stdin.readline

n = int(input())
colors = []

for i in range(n):
    RGB = list(map(int, input().split()))
    colors.append(RGB)

memo = [[] for _ in range(n)]
memo[0] = colors[0]

for i in range(1, n):
    memo[i] = [
        colors[i][0] + min(memo[i-1][1], memo[i-1][2]),
        colors[i][1] + min(memo[i-1][0], memo[i-1][2]),
        colors[i][2] + min(memo[i-1][1], memo[i-1][0])
    ]

print(min(memo[n-1]))
