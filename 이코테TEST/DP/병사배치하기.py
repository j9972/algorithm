import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.reverse()

d = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            d[i] = max(d[i], d[j]+1)
print(n-max(d))
