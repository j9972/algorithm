# dfs 문제

n = int(input())

graph = []
count = []
for i in range(n):
    graph.append(list(map(int, input())))

num = 0


def dfs(x, y):
    global num
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 1:
            # 1인 자리를 발견할때마다 1씩 올려주기
            num += 1
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
    return False


res = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count.append(num)
            res += 1
            # num 을 초기화 시켜줘야 숫자가 합쳐지는게 아니라 나눠짐
            num = 0
count.sort()
print(res)
for i in range(len(count)):
    print(count[i])
