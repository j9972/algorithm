from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
alphabet = []
for i in range(r):
    alphabet.append(list(map(str, input().rstrip())))


def bfs(x, y):
    q = deque()
    q.append([alphabet])

    data = []
    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        now = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if now not in data:
                    data.append(now)
                    cnt += 1
    return cnt


print(bfs(0, 0))
