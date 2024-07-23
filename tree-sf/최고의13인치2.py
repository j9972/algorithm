n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_cnt = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def possible(x1,y1,x2,y2):
    if not in_range(x1,y1) or not in_range(x2,y2):
        return False

    if x1 != x2:
        return True

    if abs(y1-y2) <= 2:
        return False
    
    return True

for i in range(n):
    for j in range(n):
        for a in range(n):
            for b in range(n):
                if possible(i,j,a,b):
                    max_cnt = max(max_cnt, sum(arr[i][j:j+3]) + sum(arr[a][b:b+3]))
print(max_cnt)
    