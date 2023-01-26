def rotate(arr):
    return list(zip(*arr[::-1]))


def check(new_Lock):
    n = len(new_Lock) // 3
    for x in range(n, n*2):
        for y in range(n, n*2):
            if new_Lock[x][y] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_Lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_Lock[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for i in range(n*2):
            for j in range(n*2):

                for x in range(m):
                    for y in range(m):
                        new_Lock[i+x][j+y] += key[x][y]

                if check(new_Lock):
                    return True

                for x in range(m):
                    for y in range(m):
                        new_Lock[i+x][j+y] -= key[x][y]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
