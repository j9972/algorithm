import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())

d = [0] * 100001

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        cur_ = q.popleft()

        if cur_ == k:
            return d[k]

        for i in (cur_ + 1, cur_ - 1, cur_ * 2):
            if 0<=i<100001 and d[i] == 0:
                d[i] = d[cur_] + 1
                q.append(i)


print(bfs(n))