# 큰수의 법칙
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

res = 0
count = 0

while True:
    if m <= 0:
        break
    m -= 1
    count += 1
    if count <= k:
        res += data[0]
    else:
        res += data[1]
        count = 0

print(res)
