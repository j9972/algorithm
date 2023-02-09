# 골드4 - 1976
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
m = int(input())  # 도시 개수

parent = [i for i in range(n+1)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 1:
            union(i, j)

cities = list(map(int, input().split()))

ans = "YES"
for i in range(1, m):
    if find(cities[i] - 1) != find(cities[0] - 1):
        ans = "NO"
        break

print(ans)
