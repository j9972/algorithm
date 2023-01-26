from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    inDegree = [0] * (n+1)

    graph = [[False] * (n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            inDegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            inDegree[b] -= 1
            inDegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            inDegree[b] += 1
            inDegree[a] -= 1

    q = deque()

    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    cycle = False
    certain = True
    res = []

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        res.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for i in res:
            print(i, end=' ')
        print()
