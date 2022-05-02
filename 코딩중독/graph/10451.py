import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

t = int(input())


def dfs(v):
    visited[v] = True
    next = arr[v]
    if visited[next] == False:
        dfs(next)


for i in range(t):
    ans = 0
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    for i in range(1, n+1):
        if visited[i] == False:
            dfs(i)
            ans += 1

    print(ans)


# bfs인 경우
def bfs(v):
    queue = deque[v]
    visited[v] = True
    while queue:
        v = queue[0]
        queue.popleft()
        next = arr[v]
        if visited[next] == False:
            visited[next] = True
            queue.append(next)
    return 1  # return 1이여서 ans += bfs(i) 하면됨
