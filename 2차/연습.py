import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] or (arr[i][k] and arr[k][j]):
                arr[i][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()