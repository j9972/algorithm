# 실버 5 - 10815
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

data.sort()


def b(a, t, s, e):
    while s <= e:
        m = (s+e) // 2
        if a[m] == t:
            return m
        elif a[m] > t:
            e = m - 1
        elif a[m] < t:
            s = m+1
    return None


a = []
for i in arr:
    res = b(data, i, 0, n-1)
    if res != None:
        a.append(1)
    else:
        a.append(0)
for i in a:
    print(i, end=' ')
