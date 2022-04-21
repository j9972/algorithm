n = int(input())
data = list(map(int, input().split()))

for i in range(n):
    print(data[n-1-i], end=' ')
