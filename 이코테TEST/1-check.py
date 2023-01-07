from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def nextPos(pos, board):
    pos = list(pos)

    postList = []

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
            postList.append({(next_pos_x1, next_pos_y1),
                            (next_pos_x2, next_pos_y2)})

    if pos_x1 == pos_x2:
        for i in [1, -1]:
            if board[pos_x1 + i][pos_y1] == 0 and board[pos_x2 + i][pos_y2] == 0:
                board.append({(pos_x1, pos_y1), (pos_x1+1, pos_y1)})
                board.append({(pos_x2, pos_y2), (pos_x2+1, pos_y2)})
    elif pos_y1 == pos_y2:
        for i in [1, -1]:
            if board[pos_x1][pos_y1 + i] == 0 and board[pos_x2][pos_y2 + i] == 0:
                board.append({(pos_x1, pos_y1), (pos_x1, pos_y1+1)})
                board.append({(pos_x2, pos_y2), (pos_x2, pos_y2+1)})
    return postList


def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    q = deque([])
    visited = []
    pos = {(0, 0), (0, 1)}
    visited.append(pos)
    q.append((pos, 0))

    while q:
        pos, cost = q.popleft()

        for (n, n) in pos:
            return cost

        for next in nextPos(pos, new_board):
            if next not in visited:
                visited.append(next)
                q.append((next, cost+1))
