# 골드2 - 공항 10775
import sys
input = sys.stdin.readline

g = int(input()) # g 가 노드
p = int(input())

parent = [i for i in range(g+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

cnt = 0
for i in range(p):
    data =find(int(input()))
    if data == 0:
        break
    union(data,data-1)
    cnt +=1
print(cnt)