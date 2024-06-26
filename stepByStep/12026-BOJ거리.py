import sys

n = int(input())
arr = input()

d = [sys.maxsize] * (n+1)
d[0] = 0

for i in range(1,n):
    for j in range(i):
        if arr[j] == 'B' and arr[i] != 'O':
            continue
        if arr[j] == 'O' and arr[i] != 'J':
            continue
        if arr[j] == 'J' and arr[i] != 'B':
            continue
        d[i] = min(d[i] , abs(j-i) ** 2 + d[j])

if d[n-1] == sys.maxsize:
    print(-1)
else:
    print(d[n-1])