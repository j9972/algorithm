import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

t = int(input())


def dfs(v):
    global ans
    visited[v] = True
    cycle.append(v)
    next = arr[v]

    if visited[next] == False:
        dfs(next)
    else:
        if next in cycle:
            ans += cycle[cycle.index(next):]
        return


for i in range(t):
    ans = []
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    for i in range(1, n+1):
        if visited[i] == False:
            cycle = []
            dfs(i)

    print(n - len(ans))


# bfs인 경우
def bfs(v):
    global ans
    queue = deque[v]
    visited[v] = True
    cycle.append(v)

    while queue:
        v = queue[0]
        queue.popleft()
        next = arr[v]
        if visited[next] == False:
            visited[next] = True
            queue.append(next)
        else:
            if next in cycle:
                ans += cycle[cycle.index(next)]
            return
    return 1  # return 1이여서 ans += bfs(i) 하면됨
