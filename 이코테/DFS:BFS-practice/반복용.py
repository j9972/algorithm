# 특정 거리의 도시 찾기
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
from collections import deque
import sys
input = sys.stdin.readline

# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
N, M, K, X = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

# BFS 부분
q = deque([X])
while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now]+1
            q.append(next)

# K값이 distance에 있다면 i값출력 없다면 -1 출력
if K in distance:
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
            check = True
else:
    print(-1)
