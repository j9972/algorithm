# 3780 - 플레5
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())

    parent = [i for i in range(n+1)]

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
    while True:
        data = list(map(str,input().split()))
        if data[0] == 'E':
            print(cnt)
        elif data[0] == 'I':
            union(int(data[1]),int(data[2]))
            cnt += abs(int(data[2]) - int(data[1]))
        elif data[0] == 'O':
            break
