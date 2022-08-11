import sys
input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))
array.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return None


res = binary_search(array, x, 0, n-1)
if res != None:
    print(array.count(x))
else:
    print(-1)
