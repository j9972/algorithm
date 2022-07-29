import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    inData = input().split()
    data.append((inData[0], int(inData[1])))

data.sort(key=lambda x: x[1])

for i in data:
    print(i[0], end=' ')
