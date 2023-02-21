#골4 - 2631
import sys
input = sys.stdin.readline

n = int(input())
line = [0]
for i in range(n):
    line.append(int(input()))

d = [1] * (n+1)

for i in range(1,n+1) :
    for j in range(1,i):
        if line[i] > line[j]:
            d[i] = max(d[i] , d[j]+1)
print(n-max(d))