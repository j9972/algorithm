#브2 - 2979
import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

time = []
mv = 0
for i in range(3):
    i,o = map(int,input().split())
    if mv < max(i,o):
        mv = max(i,o)
    time.append((i,o))

d = [0] * (mv+1)
ans = 0
for i in range(3):
    for j in range(time[i][0], time[i][1]):
        d[j] += 1
        
for i in d:
    if i == 1:
        ans += (a*i)
    elif i == 2:
        ans += (b*i)
    else:
        ans += (c*i)
print(ans)
