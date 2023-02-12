# 골드 5 - 2240
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

t, w = map(int, input().split())
d = [[0] * (w+1) for _ in range(t+1)]

data = [0]
for i in range(t):
    data.append(int(input()))

for i in range(t+1):
    # 이동 없음
    if data[i] == 1:
        d[i][0] = d[i-1][0] + 1
    else:
        d[i][0] = d[i-1][0]

    # 1번 이상 움직이는 경우
    for j in range(1, w+1):
        # 내가 2에 있는데 2에서 자두가 있는 경우
        if data[i] == 2 and j % 2 == 1:
            d[i][j] = max(d[i-1][j], d[i-1][j-1]) + 1
        elif data[i] == 1 and j % 2 == 0:
            d[i][j] = max(d[i-1][j], d[i-1][j-1]) + 1
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-1])

print(max(d[t]))
