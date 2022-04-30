import sys
input = sys.stdin.readline

n = int(input())


def check(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt


print(check(n))
