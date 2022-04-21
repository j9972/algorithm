h, w = map(int, input().split())
n = int(input())

arr = [[0]*w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            arr[x-1][y+j-1] = 1
    else:
        for j in range(l):
            arr[x+j-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()
