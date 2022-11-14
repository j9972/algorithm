# 숫자 카드 게임
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n // k
    else:
        n -= 1

    if n < k:
        break
    count += 1

count += (n-1)

print(count)
