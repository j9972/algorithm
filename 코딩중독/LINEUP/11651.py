import sys
n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(key=lambda x: (x[1], x[0]))

for i in data:
    print(i[0], i[1])
