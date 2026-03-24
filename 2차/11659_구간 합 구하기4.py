import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_list = [0] + list(map(int,input().split()))

d = [0] * (n+1)
d[0] = 0
d[1] = n_list[1]

for i in range(2,n+1):
    d[i] = d[i-1] + n_list[i]

for _ in range(m):
    s, e = map(int,input().split())

    print(d[e] - d[s-1])

