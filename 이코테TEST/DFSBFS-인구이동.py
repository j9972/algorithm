from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data = []
for i in range(n):
    data.append(list(map(int, input().split())))


def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    summary = data[x][y]
    cnt = 1
    union[x][y] = index  # 연합의 번호를 할당

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    union[nx][ny] = index
                    summary += data[nx][ny]
                    q.append((nx, ny))
                    united.append((nx, ny))
                    cnt += 1
    # 연합국가의 인구 분배 하는 부분
    for x, y in united:
        data[x][y] = summary // cnt
    return cnt


time = 0
while True:
    # 연합의 해당 국가의 번호
    union = [[-1] * (n+1) for _ in range(n+1)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:  # 방문하지 않아서 해당 국가의 번호가 초기화 값 그대로인 경우는 방문처리 가능
                index += 1  # 번호
                process(i, j, index)

    if index == n*n:
        break
    time += 1
print(time)
