n = int(input())

data = list(map(int, input().split()))

plus, minus, multi, div = map(int, input().split())

min_val = 1e9
max_val = -1e9


def dfs(i, now):
    global plus, minus, multi, div, max_val, min_val

    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now + data[i])
            plus += 1
        elif minus > 0:
            minus -= 1
            dfs(i+1, now - data[i])
            minus += 1
        elif multi > 0:
            multi -= 1
            dfs(i+1, now * data[i])
            multi += 1
        elif div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1


dfs(1, data[0])

print(max_val)
print(min_val)
