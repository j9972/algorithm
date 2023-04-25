import sys
input = sys.stdin.readline
from collections import deque

for tc in range(int(input())):
    n = int(input())

    indegree = [0] * (n+1)
    graph = [[False] * (n + 1) for _ in range(n+1)]

    data = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기 ( 이유는 등수가 뒤집히니까 )
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    res = []
    q= deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False  # 그래프 내 사이클이 존재하는지 여부

    # 정확히 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break

        while q:
            now = q.popleft()
            res.append(now)

            for j in range(1,n+1):
                if graph[now][j]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif not certain:
        print("?")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in res:
            print(i, end=' ')
        print()


