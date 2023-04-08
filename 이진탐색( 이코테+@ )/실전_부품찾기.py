import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

for m_d in m_list:
    if m_d in n_list:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')