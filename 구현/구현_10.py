n,m,k = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 터지고 내려오고 회전 내려오고
def rotate(tmp_arr):
    n = len(tmp_arr)

    new_arr = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            new_arr[j][n-1-i] = tmp_arr[i][j]
    
    return new_arr

dxs, dys = [-1,1,0,0],[0,0,-1,1]

def boom():
    for i in range(n):
        for j in range(n):
            cnt = 1

            if arr[i][j] == 0:
                continue

            for next_i in range(i+1,n):
                if arr[i][j] == arr[next_i][j]:
                    cnt += 1
                else:
                    break
            if cnt >= m:
                for h in range(i,i+cnt):
                    arr[h][j] = 0

def go_down():

    tmp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n-1,-1,-1):
        for j in range(n):
            if arr[i][j] != 0:
                for h in range(n-1,-1,-1):
                    if tmp[h][j] == 0:
                        tmp[h][j] = arr[i][j]
                        break  

    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp[i][j]

def check_boom():
    for i in range(n):
        for j in range(n):
            cnt = 1

            if arr[i][j] == 0:
                continue

            for next_i in range(i+1,n):
                if arr[i][j] == arr[next_i][j]:
                    cnt += 1
                else:
                    break
 
            if cnt >= m:
                return True
    return False

for _ in range(k):
    while check_boom():
        boom()
        go_down()
    arr = rotate(arr)
    go_down()

while check_boom():
    boom()
    go_down()

ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            ans += 1
print(ans)