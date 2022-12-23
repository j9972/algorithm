# 서로소 문제
import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

res = 0
for i in range(p):
    data = find(parent, int(input()))  # 받아오는 데이터가 한개일때 그거에 대해서만 parent 찾기
    if data == 0:  # 루트가 0이면 종료
        break
    union(parent, data, data - 1)  # 루트가 0이 아니면 왼쪽 집합(집합 == 탑승구)과 합치기
    res += 1
print(res)
