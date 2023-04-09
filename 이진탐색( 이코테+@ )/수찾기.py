import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

a.sort()

m = int(input())
find = list(map(int,input().split()))

def binary(arr,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in find:
    res = binary(a,i,0,n-1)
    if res != None:
        print(1)
    else:
        print(0)