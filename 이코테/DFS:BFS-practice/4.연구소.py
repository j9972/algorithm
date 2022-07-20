n, m = map(int, input().split())

# 0으로 채워지는 기본적인 2차원배열 -> 변경될 모양 생각
g = [[0] * m for _ in range(n)]

# 처음에 주워지는 바이러스 및 등에 대한 2차원 배열
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
# dfs 함수에서 이미 바이러스가 발생했기에 호출된 함수라서 주변을 체크해야함


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 아미 바이러스가 발생되서 주변을 체크하기에 바이러스가 존재하지 않는 부분이 있을떄 재귀함수
            if g[nx][ny] == 0:
                g[nx][ny] = 2
                virus(nx, ny)


def score():
    score = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global res
    if count == 3:
        # 울타리가 3개가 만들어 졌을떄 0으로 세팅해뒀던 배열에 기존 배열을 옮기기
        for i in range(n):
            for j in range(m):
                g[i][j] = data[i][j]
        # 새롭게 만들어진 배열에 바이러스가 있다면, virus 함수 호출
        for i in range(n):
            for j in range(m):
                if g[i][j] == 2:
                    virus(i, j)
        res = max(res, score())
        # ' return None === return '
        return

    # 이중 for문에서 data 베열을 보는 이유 : 새로 바뀌기전 기존에 주워졌던 배열에 울타리를 세워서 res의 최댓값을 구해보려고 하는것이다.
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                # 울타리를 다시 없애는 이유는 재귀적으로 울타리를 만들고 함수를 실행했을떄 최댓값을 구히자 못했기 뗴문이다.
                data[i][j] = 0
                count -= 1


dfs(0)
print(res)


# n, m = map(int, input().split())

# graph = [[0]*m for _ in range(n)]  # 0으로 세팅
# board = []

# for i in range(n):
#     board.append(list(map(int, input().split())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# res = 0


# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = 2
#                 virus(nx, ny)


# def getScore():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 score += 1
#     return score


# def dfs(count):
#     global res
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 graph[i][j] = board[i][j]

#         for i in range(n):
#             for j in range(m):
#                 if graph[i][j] == 2:
#                     virus(i, j)
#         res = max(res, getScore())
#         return

#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == 0:
#                 board[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 board[i][j] = 0
#                 count -= 1


# dfs(0)
# print(res)
