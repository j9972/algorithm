a,b = map(int,input().split())

arr = []

for i in range(1,1001):
    for _ in range(i):
        arr.append(i)
    if len(arr) >= 1000:
        break

cnt = 0
for i in range(a-1,b):
    cnt += arr[i]

print(cnt)