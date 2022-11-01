from bisect import bisect_left, bisect_right
from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

left = data[:n//2]
right = data[n//2:]

leftSum = []
rightSum = []


def count(a, find):
    return bisect_right(a, find) - bisect_left(a, find)


def getSum(arr, sumArr):
    for i in range(1, len(arr)+1):
        for j in combinations(arr, i):
            sumArr.append(sum(j))
    sumArr.sort()


getSum(left, leftSum)
getSum(right, rightSum)

ans = 0

for i in leftSum:
    find = s - i
    ans += count(rightSum, find)

ans += count(rightSum, s)
ans += count(leftSum, s)

print(ans)
