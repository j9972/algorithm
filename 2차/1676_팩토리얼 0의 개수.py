import sys
input = sys.stdin.readline

from collections import deque
import heapq

def fact(n):
    if n <= 1:
        return 1
    else:
        return fact(n-1) * n

n = int(input())

val = fact(n)

cnt = 0
for v in reversed(str(val)):
    if v == '0':
        cnt += 1
    else:
        print(cnt)
        break
