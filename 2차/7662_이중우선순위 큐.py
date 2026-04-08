import sys
input = sys.stdin.readline

import heapq

def isEmpty(dic):
    for num in dic:
        if num[1] > 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())

    dic = {}
    max_heap, min_heap = [], []

    for _ in range(n):
        char, val = input().split()
        val = int(val)

        if char == 'I':
            if val in dic:
                dic[val] += 1
            else:
                heapq.heappush(max_heap, -val)
                heapq.heappush(min_heap, val)
                dic[val] = 1
        else:
            if not isEmpty(dic.items()):
                if val == 1:
                    while -max_heap[0] not in dic or dic[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in dic:
                            del(dic[temp])
                    dic[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in dic or dic[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in dic:
                            del(dic[temp])
                    dic[min_heap[0]] -= 1
        
    if isEmpty(dic.items()):
        print('EMPTY')
    else:
        while -max_heap[0] not in dic or dic[-max_heap[0]] < 1:
            -heapq.heappop(max_heap)
        while min_heap[0] not in dic or dic[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])

