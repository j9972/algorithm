# 실버1 - 1697 - 다시
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
length = 100001

board = [[] for _ in range(length)]
for i in range(length):
    board[i] = [i+1, i-1, i*2]

visit = [0] * length


def bfs(n):
    q = deque([n])

    if visit[n] > 0:  # 이미 방문된 곳
        return False

    visit[n] = 1  # 방문처리 된거면 1로 바꾸기 ( 처음에 )

    while q:
        now = q.popleft()

        if now == k:
            return visit[k] - 1  # 처음에 방문처리한다고 1을 올려나서 -1 필요
        for i in board[now]:
            if 0 <= i < length and visit[i] == 0:
                visit[i] = visit[now] + 1
                q.append(i)
    return True


print(bfs(n))
