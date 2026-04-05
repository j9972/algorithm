import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))

fruits = defaultdict(int)
left, ans = 0,0

for right in range(n):
    fruits[arr[right]] += 1

    while len(fruits) > 2:
        fruits[arr[left]] -= 1
    
        if fruits[arr[left]] == 0:
            del fruits[arr[left]]
    
        left += 1

    ans = max(ans, right - left + 1)

print(ans)