n = int(input())
m = int(input())

# 예제 입력을 받기 위해서 2차원 배열 형태로 밭고 n+1인 이유는 0부터 시작하니까 0인 부분을 나두고 1부터 n까지 받으려고하는것
graph = [[]*n for _ in range(n+1)]

# 간선의 개수만큰을 for문 돌린다
for _ in range(m):
    # 각 노드가 다른 노드랑 연결됨을 보이기 위함
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

count = 0


def dfs(now):
    global count
    visited[now] = True

    for i in graph[now]:
        if not visited[i]:
            dfs(i)
            count += 1


dfs(1)
print(count)
