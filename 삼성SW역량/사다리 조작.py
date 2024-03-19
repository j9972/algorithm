import sys
from itertools import combinations as cb

n,m,h = map(int,input().split())

line = []
for i in range(m):
    a,b = map(int,input().split())
    line.append((b , a)) # 세로줄 : b번 -> b+1번

line.sort()

min_val = sys.maxsize

other_lines = list()

for j in range(1,h+1):
    for i in range(1,n+1):
        if (i,j) in line:
            continue
        other_lines.append((i,j))

print(line)
print(other_lines)