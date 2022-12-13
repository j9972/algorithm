# 럭키
import sys
input = sys.stdin.readline

n = input().rstrip()

cnt = 0
for i in range(0, len(n)//2):
    cnt += int(n[i])
val = 0
for i in range(len(n)//2, len(n)):
    val += int(n[i])

if cnt == val:
    print('LUCKY')
else:
    print('READY')
