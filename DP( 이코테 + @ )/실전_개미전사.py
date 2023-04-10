import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

d = [0] * (n)
d[0] = data[0]
d[1] = max(data[0], data[1])
d[2] = max(data[2]+d[0], d[1])

for i in range(3,n):
    d[i] = max(d[i-1], data[i] + d[i-2])
print(d[n-1])