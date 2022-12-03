import sys
from tkinter.tix import Tree
input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]

print(sum(a))
