from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())  # 팀의 수

    data = list(map(int, input().split()))

    m = int(input())  # 등수가 바뀐 수
    inDegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]

    # 방향 그래프의 간선 정보 초기화 -> 작년 팀의 순서대로 이미 정해져 있기에 i+1 ~ n 까지이다
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            inDegree[data[j]] += 1

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

    res = []
    q = deque()
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    cycle = False
    certain = False

    for i in range(n):
        if len(q) == 0:  # 사이클 있다
            cycle = True
            break

        if len(q) >= 2:  # 나올 수 있는 개수가 더 있다
            certain = True
            break

        now = q.popleft()
        res.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                inDegree[i] -= 1

                if inDegree[i] == 0:
                    q.append(i)
    # 사이클이 발생하는 경우 (일관성이 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif certain:
        print("?")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in res:
            print(i, end=' ')
        print()
