# dfs - done
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 컴터 개수
n = int(input())
# 쌍의 개수
m = int(input())

# 쌍이므로 이렇게 생각
board = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

# 1차원 생각 ( 트리 )
visited = [False] * (n+1)

count = 0


def dfs(now):
    global count
    visited[now] = True

    # 중복을 피하기 위해서 방문체크 필수, 방문시 count 증가
    for i in board[now]:
        if visited[i] == False:
            count += 1
            dfs(i)


# 문제에서 1번 컴퓨터 부터 시작한다 했음
dfs(1)

print(count)
