import sys

n,m = map(int,input().split())

arr = [
    int(input())
    for _ in range(n)
]

def check_arr():
    
    for i in range(len(arr)-1):
        cnt = 1
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
            else:
                break
        
        if cnt >= m:
            return True
    return False

def boom():
    idx = 0
    for i in range(len(arr)-1):
        if arr[i] == 0:
            continue
        cnt = 1
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
                idx = j+1
            else:
                idx = j
                break
    
        if cnt >= m:
            for j in range(i, idx):
                arr[j] = 0

if m == 1:
    print(0)
else:
    while check_arr():
        boom()

        tmp = []
        for i in arr:
            if i != 0:
                tmp.append(i)
        
        arr = tmp[:]

    print(len(arr))
    for i in arr:
        print(i)



