import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

array = set(tuple(map(int, input().split())) for _ in range(n))

count = 0
for x, y in array:
    if((x+a, y) in array) and ((x, y+b) in array) and ((x+a, y+b) in array):
        count += 1

print(count)
