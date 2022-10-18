# 만들 수 없는 금액
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

t = 1
for i in data:
    if t < i:  # i 가 새롭게 추가된 동전이라는 의미
        break
    t += i
print(t)
