def rotate(key):
    return list(zip(*key[::-1]))


def check(lock):
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 0:
                return True
    return False


def solution(key, lock):
    answer = True

    n = len(lock)
    m = len(key)

    newLock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            newLock[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for i in range(2*n):
            for j in range(2*n):
                for x in range(m):
                    for y in range(m):
                        newLock[i+x][j+y] += key[i][j]

                if not check(newLock):
                    return False

                for x in range(m):
                    for y in range(m):
                        newLock[i+x][j+y] -= key[i][j]

    return answer


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]])
