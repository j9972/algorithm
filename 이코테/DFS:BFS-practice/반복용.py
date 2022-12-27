from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def next_step(pos, board):
    pos = list(pos)
    posList = []

    pos_x1 = pos[0][0]
    pos_y1 = pos[0][1]
    pos_x2 = pos[1][0]
    pos_y2 = pos[1][1]

    for i in range(4):
        next_pos_x1 = pos_x1 + dx[i]
        next_pos_y1 = pos_y1 + dy[i]
        next_pos_x2 = pos_x2 + dx[i]
        next_pos_y2 = pos_y2 + dy[i]

        if board[next_pos_x1][next_pos_y1] == 0 and board[next_pos_x2][next_pos_y2] == 0:
            posList.append({(next_pos_x1, next_pos_y1),
                           (next_pos_x2, next_pos_y2)})

        if pos_x1 == pos_x2:
            for i in [-1, 1]:
                if board[pos_x1+i][pos_y1] == 0 and board[pos_x2+i][pos_y2] == 0:
                    posList.append({(pos_x1, pos_y1), (pos_x1+i, pos_y1)})
                    posList.append({(pos_x2, pos_y2), (pos_x2+i, pos_y2)})
        if pos_y1 == pos_y2:
            for i in [-1, 1]:
                if board[pos_x1][pos_y1+i] == 0 and board[pos_x2][pos_y2+i] == 0:
                    posList.append({(pos_x1, pos_y1), (pos_x1, pos_y1+i)})
                    posList.append({(pos_x2, pos_y2), (pos_x2, pos_y2+i)})
    return posList


def bfs(board):
    n = len(board)
    newBoard = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newBoard[i+1][j+1] = board[i][j]

    visited = []
    pos = {(1, 1), (1, 2)}
    visited.append(pos)
    q = deque([])
    q.append((pos, 0))

    while q:
        pos, cost = q.popleft()

        if (n, n) in pos:
            return cost

        for next in next_step(pos, newBoard):
            if next not in visited:
                visited.append(next)
                q.append((next, cost+1))
    return cost
