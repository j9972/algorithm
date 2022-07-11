# # DFS BFS 문제
# from collections import deque

# # dfs
# n, m, v = map(int, input().split())

# # 예제 입력을 받기 위해서 2차원 배열 형태로 밭고 n+1인 이유는 0부터 시작하니까 0인 부분을 나두고 1부터 n까지 받으려고하는것
# graph = [[] * (n+1) for _ in range(n+1)]

# # 배열의 입력을 잘 2개씩 받기 위함
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 기본적으로 false로 초기화를 시키고 false를 true로 바꾸면서 문제를 실행함
# visitied = [False] * (n+1)
# # visited를 공유하면 뒤의 함수가 실행이 잘 되지 않는다.
# visitiedS = [False] * (n+1)


# def dfs(now):
#     visitied[now] = True
#     print(now, end=' ')

#     for i in graph[now]:
#         if not visitied[i]:
#             dfs(i)


# def bfs(now):
#     queue = deque([now])
#     visitiedS[now] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if not visitiedS[i]:
#                 queue.append(i)
#                 visitiedS[i] = True


# # graph를 정렬시켜줘야 bfs문제가 통과된다. ( 이유는 우선순위가 낮은순서로 되기때문이다)
# # range 범위가 1부터 n+1인 이유는 0번째 인덱스는 시작 간선을 체크하기때문
# for i in range(1, n+1):
#     graph[i].sort()

# # print(dfs(v)) 이런식으로 하면 마지막에 None이 발생하는데 이를 조심
# dfs(v)
# print()
# bfs(v)

from collections import deque

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, v = map(int, input().split())

# 정점의 개수보다는 많은 수가 필요 하다
visited = [False] * (n+1)
visitedA = [False] * (n+1)

# 비워져 있는 것을 만들기 n or n+1
board = [[] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)


def dfs(now):
    visited[now] = True
    print(now, end=' ')

    for i in board[now]:
        if not visited[i]:
            dfs(i)


def bfs(now):
    queue = deque([now])
    visitedA[now] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in board[v]:
            if not visitedA[i]:
                queue.append(i)
                visitedA[i] = True


# for은 왜? range 범위?
for i in range(1, n+1):
    board[i].sort()

dfs(v)
print()
bfs(v)
