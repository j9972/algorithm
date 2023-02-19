# 실버4 - 1244
import sys
input = sys.stdin.readline

n = int(input())
data = [-1] + list(map(int,input().split()))

student = int(input())

def change(n):
    if data[n] == 0:
        data[n] = 1
    else:
        data[n] = 0
    return 

for _ in range(student):
    gender , num = map(int,input().split())
    if gender == 1:
        for i in range(num,n+1,num):
           change(i)
    else:
        change(num)
        dist = min(abs(num-1), abs(len(data) - num -1))
        for i in range(1,dist+1):
            if data[num-i] == data[num+i]:
                change(num-i)
                change(num+i)
            else:
                break

for i in range(1,n+1):
    print(data[i], end=' ')
    if i % 20 == 0:
        print()

