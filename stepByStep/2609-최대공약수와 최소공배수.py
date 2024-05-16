# n,m = map(int,input().split())

# g = 0

# for i in range(min(n,m), 0, -1):
#     if n % i == 0 and m % i == 0:
#         g = i
#         break

# print(g)    
# a = n // g
# b = m // g
# print(a*b*g)

n,m = map(int,input().split())
from math import gcd

g = gcd(n,m)
print(g)
print(n*m//g)