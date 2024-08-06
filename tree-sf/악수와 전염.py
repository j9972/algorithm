n,k,p,t = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(t)
]

arr.sort(key = lambda x : x[0])

handShake = [0] * (n+1) # k번 이상 악수했는지 체크용
virus = [0] * (n+1) # 감염되면 1
virus[p] = 1

for _,x,y in arr:

    if (x == p or virus[x] == 1) and (y == p or virus[y] == 1):
        handShake[x] += 1
        handShake[y] += 1
    elif (x == p or virus[x] == 1) and handShake[x] < k:
        virus[y] = 1
        handShake[x] += 1
    elif (y == p or virus[y] == 1) and handShake[y] < k:
        virus[x] = 1
        handShake[y] += 1

for i in range(1,n+1):
    print(virus[i],end='')
        