# dfs bfs 작성
from collections import deque

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, v = map(int, input().split())

# 방문처리 하지 않은걸로 처리 해놔야 한다.
visitedD = [False] * (n+1)
visitedB = [False] * (n+1)

board = [[] * (n+1) for _ in range(n+1)]

# 입력을 보면 2개의 숫자를 넣는데 그걸 보고 알수 있다.
for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)


def dfs(start):
    visitedD[start] = True
    print(start, end=' ')

    # board에 있는지 먼저 확인해야 한다
    for i in board[start]:
        if not visitedD[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visitedB[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        # board의 인덱스에 start가 아니라 v를 써야한다
        for i in board[v]:
            if not visitedB[i]:
                visitedB[i] = True
                queue.append(i)


# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문 이라는 문제 조건 떄문에 오름차순 시켜준다
for i in range(n):
    board[i].sort()

# print(dfs()) 이런식으로 하면 뒤에 None이 따라 나온다.
dfs(v)
print()
bfs(v)
