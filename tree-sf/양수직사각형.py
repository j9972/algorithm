n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = -1

def possible(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if arr[i][j] <= 0:
                return False
    return True

def sum_rect(x1,y1,x2,y2):
    cnt = 0

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        for x in range(i,n):
            for y in range(j,m):
                if possible(i,j,x,y):
                    max_val = max(max_val, sum_rect(i,j,x,y))

print(max_val)