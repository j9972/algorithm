# 1149
import sys
input = sys.stdin.readline

data = []
n = int(input())

for i in range(n):
    r, g, b = map(int, input().split())
    data.append([r, g, b])

# 1부터 시작한 이유는 2차원의 [0] 배열에 대한 최소 값을 갖기 위함 -> dp 방식으로 쌓여가는 것중에 가장 작은값출력
for i in range(1, len(data)):
    data[i][0] += min(data[i-1][1], data[i-1][2])
    data[i][1] += min(data[i-1][0], data[i-1][2])
    data[i][2] += min(data[i-1][1], data[i-1][0])

print(min(data[n-1][0], data[n-1][1], data[n-1][2]))
