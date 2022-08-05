from collections import deque

n, l, r = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

res = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def process(x, y, index):
    united = []
    united.append((x, y))

    queue = deque()
    queue.append((x, y))

    summary = board[x][y]
    count = 1
    union[x][y] = index

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    summary += board[nx][ny]
                    count += 1
                    united.append((nx, ny))
                    queue.append((nx, ny))
                    union[nx][ny] = index
    for a, b in united:
        board[a][b] = summary // count
    return count


total = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if n*n == index:
        break
    total += 1
print(total)
