n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0

def possible(a,b,c):
    x1, y1 = arr[a]
    x2, y2 = arr[b]
    x3, y3 = arr[c]

    if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
        return True

    return False

def calc(a,b,c):
    x1, y1 = arr[a]
    x2, y2 = arr[b]
    x3, y3 = arr[c]

    return abs(((x2 * y1) + (x3 * y2) + (x1 * y3)) - ((x1 * y2) + (x2 * y3) + (x3 * y1)))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if possible(i,j,k):
                max_val = max(max_val, calc(i,j,k))
print(max_val)