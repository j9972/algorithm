import sys
input = sys.stdin.readline



for _ in range(int(input())):
    n = int(input())

    d = [0] * 12

    d[1] = 1
    d[2] = 2
    d[3] = 4 
    d[4] = 7    

    if n >= 5:
        for i in range(5,n+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
    
    print(d[n])



