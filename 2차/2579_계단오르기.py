import sys
input = sys.stdin.readline

n = int(input())
n_list = [0]

for i in range(n):
    n_list.append(int(input()))

d = [0] * (n+1)
d[1] = n_list[1]
d[2] = n_list[1]  + n_list[2]

for i in range(3,n+1):
    d[i] = max(d[i-2] + n_list[i], d[i-3] + n_list[i-1] + n_list[i])

print(d[n])