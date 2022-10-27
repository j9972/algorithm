from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

a, b, c = map(int, input().split())

queue = deque()
queue.append((0, 0))

visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

ans = []


def check(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))


def bfs():
    while queue:
        x, y = queue.popleft()
        z = c - x - y

        if x == 0:
            ans.append(z)

        # x -> y
        water = min(x, b-y)
        check(x-water, y+water)

        # x -> z
        water = min(x, c-z)
        check(x-water, y)

        # y -> x
        water = min(y, a-x)
        check(x-water, y-water)

        # y -> z
        water = min(y, c-z)
        check(x, y-water)

        # z -> x
        water = min(z, a-x)
        check(x-water, y)

        # z -> y
        water = min(z, b-y)
        check(x, y+water)


bfs()
check.sort()

for i in ans:
    print(i, end=" ")
