import sys
from collections import deque

q = [
    deque(list(map(int,input())))
    for _ in range(4)
]

k = int(input())

def move_gear(gear, direct):
    if direct == 1:
        gear.rotate(1)
    else:
        gear.rotate(-1)

# True 면 회전 안함
def check_gear(gear1, gear2):
    return gear1[2] != gear2[6]


for i in range(k):
    which_one, direct = map(int,input().split())

    which_one -= 1
    direction = [0] * 4

    direction[which_one] = direct
    
    # 오른쪽으로 전파
    for i in range(which_one,3):
        if not check_gear(q[i], q[i+1]):
            break
        direction[i+1] = -direction[i]

    # 왼쪽으로 전파
    for i in range(which_one,0,-1):
        if not check_gear(q[i-1], q[i]):
            break
        direction[i-1] = -direction[i]
    
    # 회전시키기
    for i, val in enumerate(direction):
        if val != 0:
            move_gear(q[i], val)

ans = 0
for i, val in enumerate(q):
    if val[0] == 1:
        ans += 2**i

print(ans)

