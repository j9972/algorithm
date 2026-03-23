import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    
    zero = [0] * 41
    zero[0] = 1
    zero[1] = 0
    zero[2] = 1

    for i in range(3, n+1):
        zero[i] = zero[i-1] + zero[i-2]

    one = [0] * 41
    one[0] = 0
    one[1] = 1
    one[2] = 1

    for i in range(3, n+1):
        one[i] = one[i-1] + one[i-2]
    
    print(zero[n], one[n])