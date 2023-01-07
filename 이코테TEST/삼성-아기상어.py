from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

aquarium = []
for i in range(n):
    aquarium.append(list(map(int, input().split())))

now_x, now_y = 0, 0
size = 2
for i in range(n):
    for j in range(n):
        if aquarium[i][j] == 9:
            now_x, now_y = i, j
            aquarium[now_x][now_y] = 0


def bfs():
    # dist는 도달할 수 없음을 나타냄
    dist = [[-1] * n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and aquarium[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= aquarium[i][j] < size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


time = 0
cnt = 0

while True:
    value = find(bfs())
    if value == None:
        print(time)
        break

    else:
        now_x, now_y = value[0], value[1]
        time += value[2]

        aquarium[now_x][now_y] = 0
        cnt += 1

        if cnt >= size:
            size += 1
            cnt = 0
