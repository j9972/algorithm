import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in range(n, m+1):
    if i != 1 and is_prime_num(i):
        print(i)
