n,m,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

k -= 1

for i in range(n-1,-1,-1):
    flag = True
    for j in range(k, k+m):
        if arr[i][j] != 0:
            flag = False
            break
        else:
            for h in range(i-1,-1,-1):
                if arr[h][j]:
                    flag = False
                    break
            if not flag:
                break
    
    if flag:
        for j in range(k,k+m):
            arr[i][j] = 1
        break
for i in arr:
    print(*i)
        
