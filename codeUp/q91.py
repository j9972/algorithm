n = int(input())
data = list(map(int, input().split()))

a = [0 for i in range(24)]

for i in range(n):
    a[data[i]] += 1

for i in range(1, 24):
    print(a[i], end=' ')
