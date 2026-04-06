import sys
input = sys.stdin.readline

n, x, y = map(int,input().split())

# 2, 3, 1 -> 3사분면

# x < 2^(n-1)                 x < 2^(n-1)
# y < 2^(n-1)                 y >= 2^(n-1)   


# x >= 2^(n-1)                x >= 2^(n-1)
# y < 2^(n-1)                 y >= 2^(n-1)  

ans = 0 

while n > 0:

    half = 2 ** (n-1)
    area = half ** 2

    # 1사
    if x < half and y < half:
        ans += 0 * area

    # 2사
    elif x < half and y >= half:
        ans += 1 * area
        y -= half

    # 3사
    elif x >= half and y < half:
        ans += 2 * area
        x -= half

    # 4사
    elif x >= half and y >= half:
        ans += 3 * area
        x -= half
        y -= half

    n -= 1

print(ans)