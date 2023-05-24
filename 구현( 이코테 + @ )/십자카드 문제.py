# 2659 실버3
import sys
input = sys.stdin.readline

data = [True] * 10000 # 0 ~ 9999

for i in range(10000): # 0 ~ 9999
    if len(str(i)) < 4:
        data[i] = False
    if '0' in str(i):
        data[i] = False
    
n = list(map(str,input().split()))

num = int(''.join(n))
minValue = 9999

for _ in range(4):
    num = (num%1000) * 10 + num//1000
    if num < minValue:
        minValue = num

for i in range(1111,minValue+1):
    d = []

    tmp = i
    for _ in range(4):
        tmp = (tmp%1000) * 10 + tmp//1000
        d.append(tmp)
    
    for j in d:
        if j != min(d):
            data[j] = False

res = 0
for i in range(1111,minValue+1):
    if data[i] == True:
        res += 1
print(res)

