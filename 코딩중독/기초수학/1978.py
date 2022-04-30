import math
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
count = 0


def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in data:
    if i != 1 and is_prime_num(i):
        count += 1

print(count)
