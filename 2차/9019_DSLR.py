import sys
input = sys.stdin.readline

from collections import deque

def D(num):
    return num * 2 % 10000

def S(num):
    if num == 0:
        return 9999
    else:
        return num - 1

def L(num):
    return (num % 1000) * 10 + num // 1000

def R(num):
    return (num % 10) * 1000 + num // 10

for _ in range(int(input())):
    a,b = map(int,input().split())

    q =deque()
    visited = [False] * 10001
    q.append([a, ''])

    while q:
        val, char = q.popleft()

        if val == b:
            print(char)
            break

        d = D(val)
        if not visited[d]:
            visited[d] = True
            q.append([d, char+'D'])

        s = S(val)
        if not visited[s]:
            visited[s] = True
            q.append([s, char+'S'])

        l = L(val)
        if not visited[l]:
            visited[l] = True
            q.append([l, char+'L'])

        r = R(val)
        if not visited[r]:
            visited[r] = True
            q.append([r, char+'R'])

