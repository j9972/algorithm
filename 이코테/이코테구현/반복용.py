# 문자열 압축
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

key = []
for i in range(n):
    key.append(list(map(int, input().split())))

lock = []
for i in range(m):
    lock.append(list(map(int, input().split())))


def rotate(array):
    n = len(array)
    m = len(array[0])
    res = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = array[i][j]
    return res


def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    global n, m
    new_lock = [[0] * (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for d in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] += key[i][j]
                if check(new_lock):
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] -= key[i][j]
    return False


print(solution(key, lock))
