n, k = map(int,input().split())

arr = []
for i in range(1,n//2+1):
    if n % i == 0:
        arr.append(i)

arr.append(n)

if k-1 >= len(arr):
    print(0)
else:
    print(arr[k-1])