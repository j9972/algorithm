import sys
input = sys.stdin.readline

from collections import deque
import heapq

n = int(input())
arr = list()

for _ in range(n):
    arr.append(int(input()))

for i in sorted(arr):
    print(i)