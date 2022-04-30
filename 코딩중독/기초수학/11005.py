import sys
input = sys.stdin.readline

n, b = map(int, input().split())


def convert(a, b):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(a, b)

    if q == 0:
        return tmp[r]
    else:
        return convert(q, b) + tmp[r]


print(convert(n, b))
