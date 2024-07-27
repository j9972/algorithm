n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def possible(a,b,c):
    visited = [0] * 101

    for i in range(n):
        if arr[i] not in [arr[a], arr[b], arr[c]]:

            x,y = arr[i]
            for j in range(x,y+1):
                visited[j] += 1

    for i in visited:
        if i >= 2:
            return False
    return True

ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if possible(i,j,k):
                ans += 1
print(ans)