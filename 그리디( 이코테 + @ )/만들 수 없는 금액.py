import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

data.sort()

t = 1

for i in data:
    if t < i:
        break
    t += i
print(t)