# 실버 5 - 7568
import sys
input = sys.stdin.readline

n = int(input())

info = []
for i in range(n):
    w,h = map(int,input().split())
    info.append((w,h))
res = []
for i in range(len(info)):
    grade = 1
    for j in range(len(info)):
        if i != j:
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                grade += 1
    res.append(grade)
for i in res:
    print(i, end=' ')