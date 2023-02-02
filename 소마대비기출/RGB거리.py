#실버1 - 1149 - 다시
import sys
input = sys.stdin.readline

n = int(input())
colors = []
for i in range(n):
    colors.append(list(map(int, input().split())))

# n 범위 조심하기 ( 1, n+1 하면 colors[n+1] 까지 구하므로 )
for i in range(1, n):
    colors[i][0] += min(colors[i-1][1], colors[i-1][2])
    colors[i][1] += min(colors[i-1][0], colors[i-1][2])
    colors[i][2] += min(colors[i-1][0], colors[i-1][1])

print(min(colors[n-1][0], colors[n-1][1], colors[n-1][2]))
