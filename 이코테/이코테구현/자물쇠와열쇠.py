def rotate(array, d):
    n = len(array)
    res = [[0] * n for _ in range(n)]

    # 90 degree
    if d % 4 == 1:
        for r in range(n):
            for c in range(n):
                res[c][n-r-1] = array[r][c]
    # 180 degree
    elif d % 4 == 2:
        for r in range(n):
            for c in range(n):
                res[n-r-1][n-c-1] = array[r][c]
    # 270 degree
    elif d % 4 == 3:
        for r in range(n):
            for c in range(n):
                res[n-c-1][r] = array[r][c]
    # 360 degree
    else:
        for r in range(n):
            for c in range(n):
                res[r][c] = array[r][c]
    return res


def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(1, n*2):
        for j in range(1, n*2):
            new_lock[i+n][j+n] = lock[i][j]

    for i in range(1, n*2):
        for j in range(1, n*2):
            for k in range(4):
                k_key = rotate(new_lock, k)
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += k_key[x][y]

                if check(new_lock):
                    return True

                for x in range(m):
                    for y in range(n):
                        new_lock[i+x][j+y] -= k_key[x][y]
    return False
