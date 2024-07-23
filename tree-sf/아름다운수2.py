n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.sort()


cnt = 0
for i in range(n-len(b)+1):
    arr = a[i:i + len(b)]
    arr.sort()

    if arr == b:
        cnt += 1
        

print(cnt)