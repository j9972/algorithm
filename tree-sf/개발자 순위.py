k,n = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(k)
]

val = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            continue
        
        cnt = 0

        for t in range(k):
            if arr[t].index(i) < arr[t].index(j):
                cnt += 1
        
        if cnt == k:
            val += 1
print(val)