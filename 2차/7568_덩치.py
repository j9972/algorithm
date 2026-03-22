import sys
input = sys.stdin.readline

from collections import deque
import heapq

n = int(input())

arr = []
ans = []

for i in range(1,n+1):
    weight, height = map(int,input().split())

    arr.append([weight, height])

for i in range(n):
    ranking = 1
    for j in range(n):

        if (arr[i][0] < arr[j][0]) and (arr[i][1] < arr[j][1]) :
            ranking += 1

    ans.append(ranking)

# for i in ans:
#     print(i, end=' ')
print(*ans)
