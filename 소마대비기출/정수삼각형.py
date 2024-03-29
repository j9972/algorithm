import sys
input = sys.stdin.readline

n = int(input())
d = []
for i in range(n):
    d.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = d[i-1][j-1]
        
        if j == i:
            up = 0
        else:
            up = d[i-1][j]

        d[i][j] += max(up,left_up)

print(max(d[n-1]))