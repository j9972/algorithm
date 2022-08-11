import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

# for i in m_list:
#     if i in n_list:
#         print('YES', end= '')
#     else:
#         print('NO', end= '')


def binary_search(n_list, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if n_list[mid] == target:
            return mid
        elif n_list[mid] > target:
            end = mid - 1
        elif n_list[mid] < target:
            start = mid + 1
    return None


for i in m_list:
    res = binary_search(n_list, i, 0, n-1)
    if res != None:
        print('YES', end=' ')
    else:
        print('NO', end=' ')
