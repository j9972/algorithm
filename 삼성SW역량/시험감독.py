import sys

n = int(input())
ClassCnt = list(map(int,input().split()))
b,c = map(int,input().split())

tot = 0

for i in ClassCnt:
    tot += 1
    i -= b

    if i > 0:
        if i <= c:
            tot += 1
        else:
            tot += i // c
            if i % c != 0:
                tot += 1
    
    #print("tot : {}".format(tot))

print(tot)