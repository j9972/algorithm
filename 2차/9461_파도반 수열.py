import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    d = [0] * 101
    d[0] = 1
    d[1] = 1
    d[2] = 1

    for i in range(3,n+1):
        d[i] = d[i-2] + d[i-3]

    
    print(d[n-1])