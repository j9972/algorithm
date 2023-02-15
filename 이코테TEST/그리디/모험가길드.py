import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()


cnt = 0
g = 0
for i in data:
    cnt += 1
    if cnt >= i:
        g += 1
        cnt = 0
print(g)
