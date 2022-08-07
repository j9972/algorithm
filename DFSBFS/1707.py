import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

k = int(input())


for _ in range(k):
    n, m = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    res = False

    for _ in range(m):
        a, b = map(int, input().split())
        board[a].append(b)
        board[b].append(a)

    def dfs(start, group):
        global res

        if res == True:
            return

        visited[start] = group  # 같은 그룹 선정

        for i in board[start]:
            if not visited[i]:
                dfs(i, -group)  # 다른 그룹
            elif visited[start] == visited[i]:
                res = True
                return

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, 1)
            if res:
                break

    if res == True:
        print("NO")
    else:
        print("YES")
