# 게임 개발
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turing():
    global d
    d -= 1
    if d == -1:
        d = 3


cnt = 1
turingPoint = 0

while True:
    turing()
    nx = x + dx[d]
    ny = y + dy[d]

    if visited[nx][ny] == 0 and data[nx][ny] == 0:  # data의 값을 변동시키지 않는 이유는 돌아갈수 있기 때문임
        visited[nx][ny] = 1  # 방문 처리
        x, y = nx, ny  # 이동
        cnt += 1
        turingPoint = 0
        continue
    else:
        turingPoint += 1

    if turingPoint == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turingPoint = 0

print(cnt)
