def rotate(key):
    return list(zip(*key[::-1]))


def check(newLock):
    n = len(newLock) // 3
    for i in range(n):
        for j in range(n):
            if newLock[i+n][j+n] != 1:
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
                # 껴 맞춰 보기
                for i in range(m):
                    for j in range(m):
                        newLock[i+x][j+y] += key[i][j]

                if check(newLock):
                    return True

                # 껴 맞춰 본것 빼기
                for i in range(m):
                    for j in range(m):
                        newLock[i+x][j+y] -= key[i][j]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
