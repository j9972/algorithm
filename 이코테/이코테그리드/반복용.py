# 큰 수의 법칙
import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

ans = 0
while True:
    if m == 0:
        print(ans)
        break
    for i in range(k):
        ans += first
        m -= 1
        if m <= 0:
            print(ans)
            break
    ans += second
    m -= 1
