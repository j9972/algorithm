import sys
input = sys.stdin.readline

n = int(input())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
friend = [list(input()) for _ in range(n+1)]


count = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                continue

            if friend[a][b] == 'Y' or (friend[a][k] == 'Y' and friend[k][b] == 'Y'):
                friend[a][b] = 1

for i in graph:
    res = max(res, sum(i))

print(res)
