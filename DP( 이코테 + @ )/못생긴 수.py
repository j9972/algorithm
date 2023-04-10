import sys
input = sys.stdin.readline

n = int(input())

i2 = i3 = i5 = 0
next2 = 2
next3 = 3
next5 = 5

d = [0] * (n+1)
d[0] = 1

for i in range(1,n+1):
    d[i] = min(next2,next3,next5)
    if d[i] == next2:
        i2 += 1
        next2 = d[i2] * 2
    if d[i] == next3:
        i3 += 1
        next3 = d[i3] * 3
    if d[i] == next5:
        i5 += 1
        next5 = d[i5] * 5
print(d[n-1])