import sys
input = sys.stdin.readline

from collections import deque
import heapq

n = int(input())
n_list = set(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))
m_set = set(m_list)

same_ = n_list&m_set

for i in m_list:
    if i in same_:
        print(1)
    else:
        print(0)
