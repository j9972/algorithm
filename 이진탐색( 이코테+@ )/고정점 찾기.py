import sys
input = sys.stdin.readline

# 고정점 = 인덱스랑 값이 동일함
n = int(input())
data = list(map(int,input().split()))

start = 0
end = len(data) - 1

def binary(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        print("mid :", mid, "array[mid] :",array[mid])
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

res = binary(data,start, end)
if res == None:
    print(-1)
else:
    print(res)