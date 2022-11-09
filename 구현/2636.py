# 치즈
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
cnt = 0
for i in range(n):
    data.append(list(map(int, input().split())))
    cnt += sum(data[i])


time = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def surround():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if data[nx][ny] == 0:  # 공기면 계속 탐색하기 위해 큐에 넣음
                    q.append((nx, ny))
                elif data[nx][ny] == 1:  # 치즈면 한 번에 녹이기 위해 melt에 넣음
                    melt.append((nx, ny))

    for x, y in melt:
        data[x][y] = 0  # 공기와 닿은 치즈를 한 번에 녹임
    return len(melt)  # 녹인 치즈 갯수 리턴


while True:
    visited = [[False] * m for _ in range(n)]
    meltCount = surround()
    cnt -= meltCount

    if cnt == 0:
        print(time, meltCount, sep='\n')
        break
    time += 1
