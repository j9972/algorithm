# 실버1 - 1697
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0
while True:
    if n == k:
        break
    elif n < k:
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
