import sys
input = sys.stdin.readline

x = int(input())
data = list(map(int, input().split()))

d = [0] * (x+1)

d[0] = data[0]
d[1] = max(data[0], data[1])

for i in range(2, x):
    d[i] = max(d[i-1], d[i-2] + data[i])
print(d[x-1])
