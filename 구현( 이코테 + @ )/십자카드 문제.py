# 2659 실버3
import sys
input = sys.stdin.readline
from itertools import permutations as pm

data = [True] * 10000

for i in range(10000):
    if '0' in str(i):
        data[i] = False
    if len(str(i)) < 4:
        data[i] = False
    
for i in range(1111,9999):
    d = []
    for num in list(pm(str(i), 4)):
        d.append(int(''.join(num)))
    
    for j in d:
        if j != min(d):
            data[j] = False
    
n = list(map(str,input().split()))
val = []
for nu in list(pm(n, 4)):
    val.append(int(''.join(nu)))

res = 0
for i in range(1111,min(val)+1):
    if data[i] == True:
        res += 1
print(res)