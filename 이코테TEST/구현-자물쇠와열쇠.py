def rotate(arr):
    return list(zip(*arr[::-1]))


def check(lock):
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    newLock = [[0] * (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            newLock[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for i in range(n*2):
            for j in range(n*2):
                for x in range(m):
                    for y in range(m):
                        newLock[i+x][j+y] += key[x][y]

                if check(newLock):
                    return True

                for x in range(m):
                    for y in range(m):
                        newLock[i+x][j+y] -= key[x][y]
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
