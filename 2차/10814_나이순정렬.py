import sys
input = sys.stdin.readline

from collections import deque
import heapq

n = int(input())
arr = []

for i in range(n):
    age, name = input().split()

    arr.append([int(age), name])

for age, name in sorted(arr, key=lambda x : x[0]):
    print(age, name)