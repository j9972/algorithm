from collections import deque
import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = [[0] * (m) for _ in range(n)]
data = []  # 처음 입력을 받는 파트
for i in range(n):
    data.append(list(map(int, input().split())))


def virus(x, y):
    # 바이러스에 전염? x,y에 바이러스가 있을때 사용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                virus(nx, ny)


def score():
    score = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score += 1
    return score


res = 0


def dfs(count):
    # count 는 벽의 개수
    global res
    if count == 3:  # 벽 3개를 전부 세웠을때 초기화되어 있는 배열에 데이터를 옮기고 바이러스가 옮겨짊을 체크
        for i in range(n):
            for j in range(m):
                graph[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    virus(i, j)
        res = max(res, score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

    return res


print(dfs(0))
