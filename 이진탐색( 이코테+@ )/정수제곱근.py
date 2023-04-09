import sys
input = sys.stdin.readline

n = int(input())

def convert(n):
    return n ** 2

def binary(start, end):
    while start <= end:
        mid = (start+end) // 2

        if convert(mid) >= n:
            end = mid - 1
            res = mid 
        else:
            start = mid + 1
    return res
print(binary(0, n))




