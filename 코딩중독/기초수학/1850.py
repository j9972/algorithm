import sys
input = sys.stdin.readline

a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = gcd(a, b)
print('1'*g)
