import sys
input = sys.stdin.readline

n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]
friend = [list(input()) for _ in range(n)]


res = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue

            if friend[a][b] == 'Y' or (friend[a][k] == 'Y' and friend[k][b] == 'Y'):
                graph[a][b] = 1

for i in graph:
    res = max(res, sum(i))

print(res)
