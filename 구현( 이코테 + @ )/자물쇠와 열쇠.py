def rotate(arr):
    return list(zip(*arr[::-1]))

def check(arr):
    n = len(arr) // 3
    for i in range(n):
        for j in range(n):
            if arr[i+n][j+n] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        for i in range(n-m,n*2):
            for j in range(n-m,n*2):
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                
                if check(new_lock):
                    return True
                        
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
    return False