# 2960 실버 4
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

data = [i for i in range(2,n+1)]
cnt = 0

while k != 0:
    check = 0
    for i in data:
        if i != 0:
            check = i
            break
    
    for i in range(len(data)):
        if data[i] % check == 0 and data[i] != 0:
            cnt = data[i]
            data[i] = 0
            k -= 1
        if k == 0:
            break

            
print(cnt)  



