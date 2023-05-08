# 1051 , 살버 4
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

rect = []
for i in range(n):
    rect.append(list(map(int,input().rstrip())))

ans = []
check = min(n,m)
for i in range(n):
    for j in range(m):
        for k in range(check):
            if (i+k) < n and (j+k) < m and rect[i][j] == rect[i+k][j] and rect[i][j] == rect[i][j+k] and rect[i][j] == rect[i+k][j+k]:
                ans.append((k+1)**2)
print(max(ans))