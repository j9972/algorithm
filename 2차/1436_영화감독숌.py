import sys
input = sys.stdin.readline

from collections import deque
import heapq

n = int(input())

cnt = 0
target = 666

while True:

    if '666' in str(target):
        cnt += 1
    
    if n == cnt:
        print(target)
        break

    target += 1

