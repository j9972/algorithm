# 1이 될때까지
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0
while True:
    if n == 1:
        print(count)
        break

    if n % k == 0:
        n //= k
    else:
        n -= 1
    count += 1
