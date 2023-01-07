from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def nextPos(pos, new_board):
    pos = list(pos)

    pos_x1 = pos[0][0]
    pos_y1 = pos[0][1]
    pos_x2 = pos[1][0]
    pos_y2 = pos[1][1]

    posList = []

    for i in range(4):
        next_pos_x1 = pos_x1 + dx[i]
        next_pos_y1 = pos_y1 + dy[i]
        next_pos_x2 = pos_x2 + dx[i]
        next_pos_y2 = pos_y2 + dy[i]

        if new_board[next_pos_x1][next_pos_y1] == 0 and new_board[next_pos_x2][next_pos_y2] == 0:
            posList.append({(next_pos_x1, next_pos_y1),
                           (next_pos_x2, next_pos_y2)})

    if pos_x1 == pos_x2:
        for i in [-1, 1]:
            if new_board[pos_x1+i][pos_y1] == 0 and new_board[pos_x2 + i][pos_y2] == 0:
                posList.append({(pos_x1, pos_y1), (pos_x1+i, pos_y1)})
                posList.append({(pos_x2, pos_y2), (pos_x2+i, pos_y2)})
    elif pos_y1 == pos_y2:
        for i in [-1, 1]:
            if new_board[pos_x1][pos_y1+i] == 0 and new_board[pos_x2][pos_y2 + i] == 0:
                posList.append({(pos_x1, pos_y1), (pos_x1, pos_y1+i)})
                posList.append({(pos_x2, pos_y2), (pos_x2, pos_y2+i)})
    return posList


def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    pos = {(0, 0), (0, 1)}
    q = deque([])
    visited = []

    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()

        for (n, n) in pos:
            return cost

        for next in nextPos(pos, new_board):
            if next not in visited:
                visited.append(next)
                q.append((next, cost + 1))


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
