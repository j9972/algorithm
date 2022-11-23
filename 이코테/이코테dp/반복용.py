# 못생긴 수
import sys
input = sys.stdin.readline

n = int(input())

d = [0]*1000
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
d[5] = 5

arr = []


def check(i):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        return True
    else:
        return False


for i in range(6, 1001):
    if check(i) == True:
        d[i] = i
    else:
        arr.append(i)
print(d)
