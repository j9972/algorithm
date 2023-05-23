# 1614 실버3
import sys
input = sys.stdin.readline

finger = int(input())
n = int(input())

ans = 0

if n == 0:
    ans = finger - 1
else:
    if finger == 1:
        ans = 8 * n
    elif finger == 5:
        ans = 4 + 8 * n
    elif 2<=finger<=4:
        ans = 4 * n + 1
        if n % 2 == 0:
            ans += finger - 2
        else:
            ans += 4 - finger
    # # 짝수
    # if n % 2 == 0: 
    #     if finger == 2:
    #         print(8*(n//2-1)+9)
    #     if finger == 3:
    #         print(10+8*(n//2-1))
    #     if finger == 4:
    #         print(11+8*(n//2-1))
    #     if finger == 5:
    #         print(20+16*(n//2-1))
    # # 홀수
    # else:
    #     if finger == 2:
    #         print(7+8*(n//2))
    #     if finger == 3:
    #         print(6+8*(n//2))
    #     if finger == 4:
    #         print(5+8*(n//2))
    #     if finger == 5:
    #         print(12+16*(n//2))
print(ans)