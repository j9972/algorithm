n,s,m = map(int,input().split())
volumn = list(map(int,input().split()))

d = [
    [False] * (m+1)
    for _ in range(n+1)
]

d[0][s] = True

for i in range(n):
    for j in range(m+1):
        if d[i][j] == True:
            for next_vol in [j - volumn[i], j + volumn[i]]:
                if 0<=next_vol<=m:
                    d[i+1][next_vol] = True

res = -1
for i in range(m,-1,-1):
    if d[n][i] == True:
        res = i
        break
print(res)