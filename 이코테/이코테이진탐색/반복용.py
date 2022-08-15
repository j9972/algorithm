import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

array.sort()


def search_binary(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in m_array:
    res = search_binary(array, i, 0, n-1)
    if res != None:
        print('YES', end=' ')
    else:
        print('NO', end=' ')
