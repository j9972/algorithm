n = int(input())

data = list(map(int, input().split()))

plus, minus, multi, div = map(int, input().split())

max_value = -10e9
min_value = 10e9


# i는 순서, now 지금 값
def dfs(i, now):
    global plus, minus, multi, div, max_value, min_value

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now+data[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now-data[i])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(i+1, now*data[i])
            multi += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1


dfs(1, data[0])

print(max_value)
print(min_value)
