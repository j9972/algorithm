# 1063, 실버3
import sys
input = sys.stdin.readline

king, stone, n = input().split()

steps = {'R' : [1,0], 'L' : [-1,0], 'T' : [0,1], 'B' : [0,-1], 
            'RT' : [1,1], 'RB' : [1,-1], 'LB' : [-1,-1], 'LT' : [-1,1] }

k = list(map(int,[ord(king[0]) - ord('A') + 1, king[1]]))
s = list(map(int,[ord(stone[0]) - ord('A') + 1, stone[1]]))

for i in range(int(n)):
    step = input().rstrip()

    nx = k[0] + steps[step][0]
    ny = k[1] + steps[step][1]

    if 1<=nx<=8 and 1<=ny<=8:
        if nx == s[0] and ny == s[1]:
            sx = s[0] + steps[step][0]
            sy = s[1] + steps[step][1]
            if 1<=sx<=8 and 1<=sy<=8:
                k = [nx,ny]
                s = [sx,sy]
        else:
            k = [nx,ny]
print(chr(k[0] + 64)+str(k[1]))
print(chr(s[0] + 64)+str(s[1]))
