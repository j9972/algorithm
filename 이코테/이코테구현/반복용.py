# 상하좌우
import sys
input = sys.stdin.readline

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(k) + str(j):
                count += 1
print(count)
