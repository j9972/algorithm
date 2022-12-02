from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + \
            dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y),
                            (pos2_next_x, pos2_next_y)})

    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return next


def solution(board):
    n = len(board)
    newBoard = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newBoard[i+1][j+1] = board[i][j]

    queue = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    queue.append((pos, 0))
    visited.append(pos)

    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next in get_next_pos(pos, newBoard):
            if next not in visited:
                queue.append((next, cost + 1))
                visited.append(next)
    return 0


def next_pos_func(pos, new_one):
    next_pos = []
    pos = list(pos)
    pos1_x = pos[0][0]
    pos1_y = pos[0][1]
    pos2_x = pos[1][0]
    pos2_y = pos[1][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_next_x = pos1_x + dx[i]
        pos1_next_y = pos1_y + dy[i]
        pos2_next_x = pos2_x + dx[i]
        pos2_next_y = pos2_y + dy[i]

        if new_one[pos1_next_x][pos1_next_y] == 0 and new_one[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y),
                            (pos2_next_x, pos2_next_y)})

    if pos1_x == pos2_x:
        if i in [-1, 1]:
            if new_one[pos1_x + i][pos1_y] == 0 and new_one[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    if pos1_y == pos2_y:
        if i in [-1, 1]:
            if new_one[pos1_x][pos1_y + i] == 0 and new_one[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return next


def solution(board):
    n = len(board)
    newBoard = [[1]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            newBoard[i+1][j+1] = board[i][j]

    q = deque()
    pos = {(1, 1), (1, 2)}
    visited = []

    visited.append(pos)
    q.append((pos, 0))

    while q:
        pos, cost = q.popleft()
        for (n, n) in pos:
            return cost

        for next in next_pos_func(pos, new_one):
            if next not in visited:
                visited.append(next)
                q.append((next, cost+1))
    return 0
