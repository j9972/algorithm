# 2002 실버1
import sys
input = sys.stdin.readline

n = int(input())

terminal = []
for i in range(1,(2*n)+1):
    car = input().rstrip()
    if i <= n:
        terminal.append([car, i])
    else:
        for j in range(len(terminal)):
            if car == terminal[j][0]:
                terminal.append([car, terminal[j][1]])

left = terminal[:n]
right = terminal[n:]
# print(left)
# print(right)

cnt = 0
for i in range(n-1):
    for j in range(i+1,n):
        if right[i][1] > right[j][1]:
            cnt += 1
            break
print(cnt)

