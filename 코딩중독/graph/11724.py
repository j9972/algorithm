from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# graph는 노드 개수의 1개 더 만큼으로 만들어 줘야 한다
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 트리 구현
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문처리
visited = [False] * (1+n)
count = 0  # 연결 개수는 간선을 돌고 나오는 dfe를 체크해서 count += 1


def dfs(start, depth):
    # 현재 노드를 방문처리
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            dfs(i, 0)
            count += 1
print(count)

# bfs 경우


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
