# 아기 상어
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = 2
count = 0


def bfs():
    global count

    x, y = 0, 0
    q = deque()
    q.append((x, y))  # 상어의 위치

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if data[x][y] < data[nx][ny]:
                    continue
                elif data[x][y] == data[nx][ny]:
                    data[nx][ny] = data[x][y]
                else:
                    count += 1
                    if count == data[x][y]:
                        data[nx][ny] = data[x][y] + 1
