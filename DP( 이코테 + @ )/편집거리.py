import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

def edit(str1, str2):
    n = len(str1)
    m = len(str2)

    d = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n):
        d[i+1][0] = i
    for i in range(m):
        d[0][i+1] = i
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + 1
    
    return d[n][m]

print(edit(str1,str2))