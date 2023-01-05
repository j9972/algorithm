import copy
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 시작하는 정보를 전부 넣어줘야 한다.
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

def topo():
    res = copy.deepcopy(time)
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
    
    for i in range(1,n+1):
        print(res[i])


topo()
