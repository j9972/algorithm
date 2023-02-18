def rotate(key):
    return list(zip(*key[::-1]))

def check(arr):
    n = len(arr)// 3
    for i in range(n,n*2):
        for j in range(n,n*2):
            if arr[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = True
    
    m = len(key)
    n = len(lock)
    newLock = [[0] * (n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            newLock[i+n][j+n] = lock[i][j]
            
    for _ in range(4):
        key = rotate(key)
        for i in range(2*n):
            for j in range(2*n):
                for x in range(m):
                    for y in range(m):
                        newLock[i+x][y+j] += key[x][y]
                        
                if check(newLock):
                    return True
                        
                for x in range(m):
                    for y in range(m):
                        newLock[i+x][y+j] -= key[x][y]
    
    return False