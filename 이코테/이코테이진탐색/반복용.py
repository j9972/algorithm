import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

start = 0
end = max(array)
res = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for x in array:
        if x > mid:
            total += x - mid
    if total > m:
        start = mid + 1
    else:
        res = mid
        end = mid - 1
print(res)

# def search_binary(array, target, start, end):
#     while start <= end:
#         mid = (start+end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None


# for i in m_array:
#     res = search_binary(array, i, 0, n-1)
#     if res != None:
#         print('YES', end=' ')
#     else:
#         print('NO', end=' ')
