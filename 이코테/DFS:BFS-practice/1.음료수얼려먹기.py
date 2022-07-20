import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

# 2차원 리스트 맵을 이런식으로 줘도 되는 이유는 후에 변수를 받지 않고 맵의 정보를 통해서만 문제를 풀기 때문
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        # 0을 1로 바꿔줘야 재귀함수를 돌릴때 무한루프에 걸리지 않는다
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False


# 2차원 배열을 돌면서 dfs 함수에서 받은 boolean값을 통해 res 값을 증진한다
res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res += 1
print(res)
