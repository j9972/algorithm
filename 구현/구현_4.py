import sys

arr = list(input())
n = len(arr)

def shift():
    tmp = arr[-1]

    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]
    
    arr[0] = tmp

ans = sys.maxsize

def press():
    compress = ""
    cnt = 1

    if n == 1 or n == 2:
        return 2
    
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            cnt += 1
        else:
            compress += arr[i] + str(cnt)
            cnt = 1

        if i == n - 2:
            compress += arr[i+1] + str(cnt)
            

    return len(compress)

for i in range(n):
    ans = min(ans, press())
    shift()

print(ans)