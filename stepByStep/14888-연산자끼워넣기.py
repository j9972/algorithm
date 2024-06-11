import sys

n = int(input())
A = list(map(int,input().split()))
plus, minus, multi, div = map(int,input().split())

max_val, min_val = -sys.maxsize, sys.maxsize

def choose(cnt, data):
    global plus, minus, multi, div, max_val, min_val

    if cnt == n:
        min_val = min(min_val, data)
        max_val = max(max_val, data)
        return
    else:
        if plus > 0:
            plus -= 1
            choose(cnt+1, data + A[cnt])
            plus += 1
        if minus > 0:
            minus -= 1
            choose(cnt+1, data - A[cnt])
            minus += 1
        if multi > 0:
            multi -= 1
            choose(cnt+1, data * A[cnt])
            multi += 1
        if div > 0:
            div -= 1
            choose(cnt+1, int(data / A[cnt]))
            div += 1


choose(1, A[0])
print(max_val)
print(min_val)