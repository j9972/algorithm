# 1010
import math
import sys
input = sys.stdin.readline


def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1


for tc in range(int(input())):
    n, m = map(int, input().split())

    # up = math.factorial(m)
    # down = math.factorial(m-n) * math.factorial(n)

    up = fact(m)
    down_first = fact(m-n)
    down_second = fact(n)

    print(up//(down_second*down_first))
