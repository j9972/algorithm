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

# 아래는 이코테


def rotate(arr):
    return list(zip(*arr[::-1]))


def check(newLock):
    n = len(newLock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if newLock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    newLock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            newLock[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)

        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        newLock[i+x][j+y] += key[i][j]

                if check(newLock):
                    return True

                for i in range(m):
                    for j in range(m):
                        newLock[i+x][j+y] -= key[i][j]

    return False
