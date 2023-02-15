import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

mv = 1
for i in data:
    if mv < i:
        break
    mv += i
print(mv)
