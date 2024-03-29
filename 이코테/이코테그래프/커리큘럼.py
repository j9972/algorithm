# 위상정렬 문제
from collections import deque
import copy
import sys
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
time = [0] * (n+1)  # 각 강의 시간 담을 리스트

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topo():
    res = copy.deepcopy(time)  # res는 각 강의를 수강하기까지의 최소 시간
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            res[i] = max(res[i], res[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(res[i])


topo()
