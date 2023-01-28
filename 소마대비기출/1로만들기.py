# 실버 3
import sys
input = sys.stdin.readline

x = int(input())
cnt = 0

while x == 1:
    if x % 3 == 0:
        x %= 3
        cnt += 1
    elif x % 2 == 0:
        x %= 2
        cnt += 1
    else:
        x -= 1
        cnt += 1

print(cnt)
