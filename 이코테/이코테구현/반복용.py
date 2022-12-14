def rotate(arr):
    return list(zip(*arr[::-1]))


def attach(x, y, m, new_lock, key):
    for i in range(m):
        for j in range(m):
            new_lock[x+i][j+y] += key[i][j]


def detach(x, y, m, new_lock, key):
    for i in range(m):
        for j in range(m):
            new_lock[x+i][j+y] -= key[i][j]


def check(new_lock, n, m):
    for i in range(n):
        for j in range(n):
            if new_lock[i+m][j+m] != 1:
                return False
    return True


def solution(key, lock):
    n, m = len(lock), len(key)

    new_lock = [[0]*(2*m+n) for _ in range(m*2+n)]

    for i in range(n):
        for j in range(n):
            new_lock[m+i][m+j] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for x in range(1, m+n):
            for y in range(1, m+n):
                attach(x, y, m, new_lock, key)

                if check(new_lock, n, m):
                    return True

                detach(x, y, m, new_lock, key)
    return False
