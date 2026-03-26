import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, int(n**0.5) + 1):
    if n == i**2:
        print(1)
        sys.exit()

for i in range(1, int(n**0.5) + 1):
    remain = n - i**2
    j = int(remain ** 0.5)
    
    if remain == j ** 2:
        print(2)
        sys.exit()

for i in range(1, int(n**0.5) + 1):
    for j in range(1, int((n-i**2) **0.5) + 1):
        remain = n - i ** 2 - j ** 2
        k = int(remain ** 0.5)

        if remain == k ** 2:
            print(3)
            sys.exit()
print(4)
