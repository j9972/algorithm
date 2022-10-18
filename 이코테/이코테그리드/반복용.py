# 만들 수 없는 금액
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0
group = 0

for i in data:
    count += 1
    if count >= i:
        group += 1
        count = 0
print(group)
