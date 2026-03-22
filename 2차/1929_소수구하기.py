import sys
input = sys.stdin.readline

m,n = map(int,input().split())

def is_prime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(m,n+1):
    if i != 1 and is_prime(i):
        print(i)
    