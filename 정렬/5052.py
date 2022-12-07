import math
import sys
input = sys.stdin.readline

for tc in range(int(input())):

    n = int(input())

    data = []
    for i in range(n):
        data.append(input().rstrip())

    data.sort()

    flag = True

    for i in range(len(data)-1):
        idx = len(data[i])
        if data[i] == data[i+1][:idx]:
            flag = False
            print('NO')
            break

    if flag == True:
        print('YES')
