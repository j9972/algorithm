import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

print(data)
for i in data:
    print(i, end=' ')
