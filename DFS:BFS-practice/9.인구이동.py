from collections import deque

n, l, r = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0


def process(x, y, index):
    united = []
    united.append((x, y))

    queue = deque()
    queue.append((x, y))

    union[x][y] = index  # 연합의 번호 할당
    summary = board[x][y]  # 연합의 인구수
    count = 1  # 연합 국가 수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    queue.append((nx, ny))
                    union[nx][ny] = index
                    count += 1
                    summary += board[nx][ny]
                    united.append((nx, ny))
    for i, j in united:
        board[i][j] = summary // count
    return count


totalCount = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n:
        break
    totalCount += 1

print(totalCount)
