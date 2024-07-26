n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr.sort(key=lambda x : x[0])

cnt = 0
for i in range(n):
    flag = True
    for j in range(n):

        if i == j:
            continue

        x1,x2 = arr[i]
        x3,x4 = arr[j]

        if (x1 < x3 and x2 > x4) or (x3 < x1 and x4 > x2):
            flag = False
            break
        
        if (x1 == x3) or (x2 == x4):
            flag = False
            break
        
    if flag:
        cnt += 1
print(cnt)