# 실버1 - 17615
import sys
input = sys.stdin.readline

n = int(input())
ball = list(map(str,input().rstrip()))


r = ball.count('R')
b = n-r
# for i in ball:
#     if i == 'R':
#         r += 1
#     else:
#         b += 1

ans = min(r,b)
cnt = 0
for i in range(n):
    if ball[0] != ball[i]:
        break
    cnt += 1

if ball[0] == 'R':
    ans = min(ans, r-cnt)
else:
    ans = min(ans, b-cnt)

cnt2 = 0
for i in range(n-1,-1,-1):
    if ball[-1] != ball[i]:
        break
    cnt2 += 1

if ball[-1] == 'R':
    ans = min(ans, r-cnt2)
else:
    ans = min(ans, b-cnt2)
print(ans)