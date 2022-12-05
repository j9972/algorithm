from collections import deque

n, m, k, x = map(int, input().split())

# m개의 줄에 맞춰서 자연수가 새롭게 주워지니까 2차원 배열이 미리 만들어져 있어야 한다
# n + 1 인 이유? 0 ~ n-1 까지의 범위인데 문제에서 1 ~ n 이라는 조건이 있자나, 근데 여기서 board는 2차원 배열로 만들되, 0 ~ n의 범위로 만들어 놓고
# 아래의 for 문 에서 범위를 1 ~ n+1 로 바꿔서 1 ~ n 의 범위를 보여주는것
board = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)

print(board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([x])

# 0 부터 n까지니까 총개수는 n+1
distance = [-1] * (n+1)
distance[x] = 0

while queue:
    now = queue.popleft()
    for next in board[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

check = False
# 1부터 n번까지의 도시를 이동하기에 range 범위가 이렇게 된다.
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


# from collections import deque

# n,m,k,x = map(int,input().split())


# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)

# distacne = [-1] * (n+1)
# distacne[x] = 0

# queue = deque([x])

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# while queue:
#     now = queue.popleft()
#     while queue:
#         for next in graph[now]:
#             if distacne[next] == -1:
#                 distacne[next] = distacne[now] + 1
#                 queue.append(next)

# check = False
# for i in range(1,n+1):
#     if distacne[i] == k:
#         print(i)
#         check = True

# if check == False:
#     print(-1)
