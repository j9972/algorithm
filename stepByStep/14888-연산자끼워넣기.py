import sys

n = int(input())

arr = list(map(int,input().split()))

add,minus,multi,div = map(int,input().split())

max_val = -sys.maxsize
min_val = sys.maxsize

def choose(val, cnt):
    global add,minus,multi,div, max_val, min_val

    if cnt == n:
        max_val = max(max_val ,val)
        min_val = min(min_val ,val)
    else:
        if add > 0:
            add -= 1
            choose(val + arr[cnt], cnt+1)
            add += 1
        if minus > 0:
            minus -= 1
            choose(val - arr[cnt], cnt+1)
            minus += 1
        if multi > 0:
            multi -= 1
            choose(val * arr[cnt], cnt+1)
            multi += 1
        if div > 0:
            div -= 1
            choose(val // arr[cnt], cnt+1)
            div += 1

choose(arr[0],1)
print(max_val)
print(min_val)