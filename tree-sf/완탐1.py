import sys

n = int(input())

arr = list(map(int,input().split()))

min_val = sys.maxsize

for i in range(n):
    dist = 0
    for j in range(n):
        if i == j:
            continue
        
        dist += abs(i - j) * (arr[j])
    
    min_val = min(min_val, dist)
print(min_val)