from collections import deque

n, l, r = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def process(x, y, index):
    united = []  # 연합
    united.append((x, y))

    queue = deque()
    queue.append((x, y))

    union[x][y] = index  # 연합의 번호
    summary = board[x][y]  # 인구수
    count = 1  # 연합 국가 수

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # -1이란것은 방문하지 않았다
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    summary += board[nx][ny]
                    count += 1
                    union[nx][ny] = index  # 연합의 번호
                    united.append((nx, ny))
                    queue.append((nx, ny))

    for i, j in united:  # 연합에 있어서
        board[i][j] = summary // count  # 인구수가 이동할수있는 카운트 세기
    return count


total = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:  # 연합이 아니라면
                process(i, j, index)
                index += 1  # 인덱스 증가
    if index == n*n:  # 모든 이동이 끝났다면,
        break
    total += 1

print(total)
