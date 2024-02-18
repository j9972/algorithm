# 1차원 바람
from collections import deque
n,m,q = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

wind = list()

for _ in range(q):
    row, direct = input().split()
    row = int(row) - 1
    wind.append((row, direct))

def move(tmp_arr, row, direct):
    q = deque(tmp_arr)

    if direct == 'L': # 오른쪽으로 이동
        data = q.pop()
        q.appendleft(data)

    else:
        data = q.popleft()
        q.append(data)

    return q

def checkArr(arr1, arr2):
    for i in range(m):
        if arr1[i] == arr2[i]:
            return True
    return False

def change_wind(direct):
    if direct == 'L':
        return 'R'
    else:
        return 'L'

for i in wind:
    row, direct = i

    up, down = direct, direct

    arr[row] = move(arr[row], row , direct)
    
    for i in range(row,0,-1):

        if checkArr(arr[i], arr[i-1]):

            down = change_wind(down)
            arr[i-1] = move(arr[i-1], i-1 , down)
            continue
        else:
            break

    for i in range(row,n-1):

        if checkArr(arr[i], arr[i+1]):

            up = change_wind(up)
            arr[i+1] = move(arr[i+1], i+1 , up)
            continue
        else:
            break
                
for i in arr:
    print(*i)