# 위상 정렬 같음
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for i in range(n)]

RootTree = list(map(int, input().split()))

for i in range(n):
    tree[i] = RootTree[i]

cutNode = int(input())


def delete(cut):
    tree[cut] = -2
    for i in range(n):
        if tree[i] == cut:
            tree[i] = -2
            delete(i)


delete(cutNode)

res = 0
for i in range(n):
    if tree[i] != -2:
        err = 0
        for j in tree:
            if j == i:
                err = 1
                break
        if err == 0:
            res += 1
print(res)
