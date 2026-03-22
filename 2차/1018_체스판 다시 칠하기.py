import sys
input = sys.stdin.readline

from collections import deque
import heapq

x,y = map(int,input().split())
arr = [
    list(input().rstrip())
    for _ in range(x)
]

min_cnt = 65

even_w = [
    ['W','B','W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W','B','W']
]

odd_w = [
    ['B','W','B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B','W','B']
]

def counting(arr):
    cnt1, cnt2 = 0,0
    for i in range(8):
        for j in range(8):
            if even_w[i][j] != arr[i][j]:
                cnt1 += 1
            if odd_w[i][j] != arr[i][j]:
                cnt2 += 1            
    
    return min(cnt1,cnt2)

new_arr = [
    [[] for _ in range(8)] 
    for _ in range(8)
]

for i in range(x-7):
    for j in range(y-7):
        for a in range(8):
            for b in range(8):
                new_arr[a][b] = arr[i+a][j+b]
        
        min_cnt = min(min_cnt, counting(new_arr))
        print("counting(new_arr) : " , counting(new_arr))

print(min_cnt)
