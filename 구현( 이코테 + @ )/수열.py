# 2491 실버4
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

d = [1] * n
for i in range(n-1):
    if nums[i] <= nums[i+1]:
        d[i+1] += d[i]
d2 = [1] * n
for i in range(n-1):
    if nums[i] >= nums[i+1]:
        d2[i+1] += d2[i]

max1 = max(d)
max2 = max(d2)
print(max(max1, max2))