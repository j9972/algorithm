arr = [
    list(map(int,input().split()))
    for _ in range(4)
]
n = 4
direction = input()

# 오른 아래 왼 위 방향
dxs , dys = [0,1,0,-1] , [1,0,-1,0]

def rotate(tmp_arr, d):
    N = len(tmp_arr)
    ret = [[0] * n for _ in range(n)]

    if d % 4 == 1: # 90도 
        for r in range(n):
            for c in range(n):
                ret[c][n-1-r] = tmp_arr[r][c]
    elif d% 4 == 2: # 180도
        for r in range(n):
            for c in range(n):
                ret[n-1-c][n-1-r] = tmp_arr[r][c]
    elif d % 4 == 3: # 270도
        for r in range(n):
            for c in range(n):
                ret[n-1-c][r] = tmp_arr[r][c]
    else:
        for r in range(n):
            for c in range(n):
                ret[r][c] = tmp_arr[r][c]
    return ret

tmp = [
    [0] * n
    for _ in range(n)
]

def turn(direction, arr1):
    if direction == 'R':
        arr2 = rotate(arr1, 1)

    elif direction == 'U':
        arr2 = rotate(arr1, 1)
        arr2 = rotate(arr2, 1)

    elif direction == 'L':
        arr2 = rotate(arr1, 3)
    
    else:
        arr2 = arr1[:]
    
    return arr2

def move():
    global direction, tmp, arr

    new_arr = turn(direction, arr)

    # 합치기
    for i in range(n-1,-1,-1):
        for j in range(n):

            if new_arr[i][j] != 0:
                for h in range(i-1,-1,-1):
                    
                    if new_arr[h][j] == 0:
                        continue
                    
                    elif new_arr[h][j] != new_arr[i][j]:
                        break

                    elif new_arr[h][j] == new_arr[i][j]:
                        new_arr[i][j] *= 2
                        new_arr[h][j] = 0
                        break
    
    # 아래로 내림
    for i in range(n-1,-1,-1):
        for j in range(n):
            if new_arr[i][j] != 0:
                for h in range(n-1,-1,-1):
                    if tmp[h][j] == 0:
                        tmp[h][j] = new_arr[i][j]
                        break

    if direction == 'R':
        new_arr = rotate(tmp, 3)

    elif direction == 'U':
        new_arr = rotate(tmp, 1)
        new_arr = rotate(new_arr, 1)

    elif direction == 'L':
        new_arr = rotate(tmp, 1)

    else:
        new_arr = tmp[:]

    return new_arr
    
    
res = move()

for i in res:
    print(*i)