import sys

n = int(input())
arr = list(map(int,input().split()))
plus, minus, multi, divide = map(int,input().split())

max_val, min_val = -sys.maxsize, sys.maxsize

def choose(idx, cur_num):
    global min_val, max_val, plus, minus, multi, divide

    if idx == n:
        min_val = min(min_val, cur_num)
        max_val = max(max_val, cur_num)
        
    else:
        if plus > 0:
            plus -= 1
            choose(idx+1, cur_num + arr[idx])
            plus += 1
        if minus > 0:
            minus -= 1
            choose(idx+1, cur_num - arr[idx])
            minus += 1
        if multi > 0:
            multi -= 1
            choose(idx+1, cur_num * arr[idx])
            multi += 1
        if divide > 0:
            divide -= 1
            choose(idx+1, int(cur_num / arr[idx]))
            divide += 1

choose(1, arr[0])

print(max_val)
print(min_val)
