import sys
input = sys.stdin.readline

n = int(input())
connect = int(input())

visited = [False] * (n+1)
visited[1] = True
node = []

for i in range(connect):
    start, end = map(int,input().split())

    node.append([start, end])

for s, e in node:
    if visited[s] or visited[e]:
        visited[s] = True
        visited[e] = True

cnt = 0
for i in range(1,n+1):
    if visited[i]:
        print("i : {}, visited[i] : {}".format(i, visited[i]))
        cnt += 1
print(cnt)
