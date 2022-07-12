# dfs. 대각선 체크
# done
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(x, y):
    # 너비가 w(가로), 높이가 h(세로) -> [x][y] 생각하면 이게 맞다
    if 0 <= x < h and 0 <= y < w:
        if board[x][y] == 1:
            board[x][y] = 0
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x+1, y+1)
            dfs(x+1, y)
            dfs(x+1, y-1)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False


while True:
    w, h = map(int, input().split())

    board = []
    for i in range(h):
        board.append(list(map(int, input().split())))

    # 0 0 이 입력이 되면 끝나도록 설정하는 조건이 있기 때문이다.
    if w == 0 and h == 0:
        break

    res = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                res += 1
    print(res)
