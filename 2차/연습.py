import sys
input = sys.stdin.readline

n,x,y = map(int,input().split())

ans = 0

while n > 0:

    half = 2 ** (n-1)
    area = half ** 2

    # 제 1사분면
    if x < 2 ** (n-1) and y < 2 ** (n-1):
        ans += 0 * area

    # 제 2사분면
    elif x < 2 ** (n-1) and y >= 2 ** (n-1):
        ans += 1 * area
        y -= half

    # 제 3사분면
    elif x >= 2 ** (n-1) and y < 2 ** (n-1):
        ans += 2 * area
        x -= half

    # 제 4사분면
    elif x >= 2 ** (n-1) and y >= 2 ** (n-1):
        ans += 3 * area
        x -= half
        y -= half
    
    n -= 1

print(ans)