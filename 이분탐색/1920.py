# 수 찾기 - 부품찾기랑 비슷
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

array.sort()


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
    res = binary_search(array, i, 0, n-1)
    if res != None:
        print('1', end='\n')
    else:
        print('0', end='\n')
