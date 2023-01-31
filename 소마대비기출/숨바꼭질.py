# 실버1 - 1697
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

while n == k:
    cnt = 0
    if n <= k:
        if n * 2 <= k:
            n *= 2
            cnt += 1
        else:
            n += 1
            cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)
