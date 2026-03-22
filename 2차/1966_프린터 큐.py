import sys
import heapq

from collections import deque

input = sys.stdin.readline

#FIFO
for _ in range(int(input())):

    n , m = map(int,input().split())
    cnt = 1

    q = list(map(int,input().split()))

    new_q = []
    for i, val in enumerate(q):
        new_q.append([val, i])

    ans = [q[m], m]

    while True:
        val, idx = new_q.pop(0)
        flag = False

        for i in new_q:
            val2, idx2 = i[0], i[1]

            if val < val2:
                flag = True
                break
    
        if flag:
            new_q.append([val, idx])
        else:
            if ans[0] == val and ans[1] == idx:
                print(cnt)
                break
            else:
                cnt += 1