from collections import deque


def solution(board):
    n = len(board)
    newBoard = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newBoard[i+1][j+1] = board[i][j]
    queue = deque()
    visited = []
    pos = {(0, 0), (0, 1)}
    queue.append((pos, 0))
    visited.append(pos)

    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next in get_next(pos, newBoard):
            if next not in visited:
                queue.append((next, cost+1))
                visited.append(next)
    return 0


def get_next(pos, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):
        post1_next_x, post1_next_y = pos1_x+dx[i], pos1_y+dy[i]
        post2_next_x, post2_next_y = pos2_x+dx[i], pos2_y+dy[i]

        if board[post1_next_x][post1_next_y] == 0 and board[post2_next_x][post2_next_y] == 0:
            next_pos.append({(post1_next_x, post1_next_y),
                            (post2_next_x, post2_next_y)})

    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x + i][pos1_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})

    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos1_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    return next
