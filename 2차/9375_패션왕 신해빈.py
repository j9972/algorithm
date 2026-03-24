import sys
input = sys.stdin.readline

for _ in range(int(input())):

    n = int(input())

    dic = {}
    for _ in range(n):
        v,t = input().split()

        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
        
    res = 1
    for k , v in dic.items():
        res *= (v+1)
    
    print(res-1)
