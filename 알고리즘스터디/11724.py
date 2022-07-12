# dfs 연결 요소 체크하는 문제 - done
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

board = [[] for _ in range(n+1)]

# 요소를 연결 하는 부분
for i in range(m):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

# dfs에서 가장 중요한 방문처리하기
visit = [False] * (n+1)
count = 0


def dfs(now):
    visit[now] = True

    # 연결된 요소중에서 찾기
    for i in board[now]:
        if visit[i] == False:
            dfs(i)


# n으로 범위를 정하면 count -1 해줘야함. 범위가 이런 이유는 board를 n+1로 해놔서
for i in range(1, n+1):
    if visit[i] == False:
        count += 1
        dfs(i)
print(count)
